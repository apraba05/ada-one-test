"""
Stages 3 + 4 — Retrieval, grounded generation, and the two-stage confidence gate.

Pipeline for a query:
  1. Embed query, cosine top-k (k=4) over the local index.
  2. Generate an answer with Claude, grounded ONLY in the retrieved chunks.
  3. Gate:
       (a) retrieval check — max cosine similarity must clear RETRIEVAL_THRESHOLD
       (b) LLM judge — a SEPARATE Claude call scores how well the *specific* answer
           is supported by the retrieved context; must clear JUDGE_THRESHOLD
     If EITHER check fails -> hard refuse. No hedged/partial answers.

Returns the full trace: {answer, refused, sources, retrieval_score, judge_score,
judge_reasoning}.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import anthropic
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from index import Index

load_dotenv(Path(__file__).parent / ".env")

MODEL = "claude-opus-4-8"  # both generation and judge; see NOTES.md
TOP_K = 4

# --- Confidence-gate thresholds (user-confirmed defaults; see NOTES.md) ---
RETRIEVAL_THRESHOLD = 0.35  # max cosine over retrieved chunks (all-MiniLM-L6-v2 "clearly relevant" band)
JUDGE_THRESHOLD = 0.60      # groundedness score (0-1) from the LLM judge

REFUSAL_TEXT = (
    "I don't have enough information in the knowledge base to answer that confidently."
)

_client: anthropic.Anthropic | None = None


def get_client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        # Resolves ANTHROPIC_API_KEY from env / backend/.env
        _client = anthropic.Anthropic()
    return _client


GEN_SYSTEM = """You are a QA assistant for Ada (an AI customer-service platform). \
You answer questions about setting up and configuring an Ada AI agent's knowledge base, \
for a non-technical CEO evaluating the product.

STRICT GROUNDING RULES — these override everything else:
- Answer ONLY using the numbered SOURCES provided in the user message.
- Do NOT use any general knowledge about Ada, customer-service platforms, or anything \
not present in the SOURCES. If the SOURCES do not contain the answer, say so plainly.
- Cite the source doc title inline in square brackets after each claim, e.g. [Knowledge integration].
- Be direct and concise. Do not hedge, speculate, or pad. No preamble like "Based on the sources".
- If the SOURCES only partially cover the question, answer only the covered part and state \
what is not covered."""


class JudgeResult(BaseModel):
    """Structured output for the groundedness judge."""
    judge_score: float = Field(description="0.0-1.0: how well the specific answer is supported by the SOURCES")
    supported: bool = Field(description="True only if every substantive claim is directly grounded in the SOURCES")
    reasoning: str = Field(description="One or two sentences explaining the score")


@dataclass
class Source:
    title: str
    url: str
    score: float


def _format_sources(chunks: list[dict]) -> str:
    blocks = []
    for i, c in enumerate(chunks, 1):
        blocks.append(f"[Source {i}] Title: {c['title']}\n{c['text']}")
    return "\n\n---\n\n".join(blocks)


def generate_answer(query: str, chunks: list[dict]) -> str:
    client = get_client()
    user_msg = (
        f"SOURCES:\n\n{_format_sources(chunks)}\n\n"
        f"QUESTION: {query}\n\n"
        "Answer using only the SOURCES above, with inline [Title] citations."
    )
    resp = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=GEN_SYSTEM,
        messages=[{"role": "user", "content": user_msg}],
    )
    return "".join(b.text for b in resp.content if b.type == "text").strip()


def judge_answer(query: str, answer: str, chunks: list[dict]) -> JudgeResult:
    """SEPARATE Claude call: is THIS answer actually supported by THESE chunks?"""
    client = get_client()
    user_msg = (
        "You are a strict grounding auditor. Given a QUESTION, a candidate ANSWER, and the "
        "SOURCES that answer was supposed to be drawn from, judge whether the specific claims "
        "in the ANSWER are directly supported by the SOURCES.\n\n"
        "Score 1.0 only if every substantive claim is explicitly supported. Score low if the "
        "answer adds facts not in the SOURCES, generalizes beyond them, or the SOURCES are "
        "off-topic for the QUESTION. An answer that correctly says the information isn't "
        "available should score high (it is grounded — it makes no unsupported claim).\n\n"
        f"QUESTION: {query}\n\n"
        f"ANSWER: {answer}\n\n"
        f"SOURCES:\n\n{_format_sources(chunks)}"
    )
    resp = client.messages.parse(
        model=MODEL,
        max_tokens=512,
        messages=[{"role": "user", "content": user_msg}],
        output_format=JudgeResult,
    )
    return resp.parsed_output


def answer_query(query: str, index: Index, k: int = TOP_K) -> dict:
    """Full Stage 3+4 pipeline. Returns the trace dict."""
    chunks = index.search(query, k=k)
    retrieval_score = max((c["score"] for c in chunks), default=0.0)

    # De-duplicate sources by doc title for display (keep best score per doc).
    sources: dict[str, Source] = {}
    for c in chunks:
        s = sources.get(c["title"])
        if s is None or c["score"] > s.score:
            sources[c["title"]] = Source(title=c["title"], url=c["source_url"], score=c["score"])
    source_list = [s.__dict__ for s in sorted(sources.values(), key=lambda s: -s.score)]

    # Gate stage 1: retrieval. If nothing is relevant, refuse without spending a generation call.
    if retrieval_score < RETRIEVAL_THRESHOLD:
        return {
            "answer": REFUSAL_TEXT,
            "refused": True,
            "sources": source_list,
            "retrieval_score": retrieval_score,
            "judge_score": None,
            "judge_reasoning": "Retrieval score below threshold — no sufficiently relevant documents.",
        }

    answer = generate_answer(query, chunks)
    judge = judge_answer(query, answer, chunks)

    # Gate stage 2: LLM judge. Either check failing -> hard refuse.
    refused = judge.judge_score < JUDGE_THRESHOLD
    return {
        "answer": REFUSAL_TEXT if refused else answer,
        "refused": refused,
        "sources": source_list,
        "retrieval_score": retrieval_score,
        "judge_score": judge.judge_score,
        "judge_reasoning": judge.reasoning,
    }
