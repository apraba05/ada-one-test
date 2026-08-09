"""
Stages 3 + 4 — Retrieval, grounded generation, and the two-stage confidence gate.

Pipeline for a query:
  1. Embed query, cosine top-k (k=4) over the local index.
  2. Generate an answer (via the configured LLM provider, see llm.py), grounded
     ONLY in the retrieved chunks.
  3. Gate:
       (a) retrieval check — max cosine similarity must clear RETRIEVAL_THRESHOLD
       (b) LLM judge — a SEPARATE LLM call scores how well the *specific* answer
           is supported by the retrieved context (must clear JUDGE_THRESHOLD) and
           whether it actually answers the question (answers_question)
     If EITHER check fails -> hard refuse. No hedged/partial answers.

Returns the full trace: {answer, refused, sources, retrieval_score, judge_score,
answers_question, judge_reasoning}.
"""
from __future__ import annotations

from dataclasses import dataclass

from pydantic import BaseModel, Field

from index import Index
from llm import get_llm

TOP_K = 4

# --- Confidence-gate thresholds (user-confirmed defaults; see NOTES.md) ---
RETRIEVAL_THRESHOLD = 0.35  # max cosine over retrieved chunks (all-MiniLM-L6-v2 "clearly relevant" band)
JUDGE_THRESHOLD = 0.60      # groundedness score (0-1) from the LLM judge

# Latency is dominated by tokens generated (~30 tok/s on a local 8B), and these are caps on
# runaway output, not targets — a typical answer lands near 160 and the judge near 80.
GEN_MAX_TOKENS = 400
JUDGE_MAX_TOKENS = 256

EVIDENCE_CHARS = 400  # per-chunk excerpt shown in the UI evidence panel

REFUSAL_TEXT = (
    "I don't have enough information in the knowledge base to answer that confidently."
)

GEN_SYSTEM = """You are a QA assistant for Ada (an AI customer-service platform). \
You answer questions about setting up and configuring an Ada AI agent's knowledge base, \
for a non-technical CEO evaluating the product.

STRICT GROUNDING RULES — these override everything else:
- Answer ONLY using the numbered SOURCES provided in the user message.
- Do NOT use any general knowledge about Ada, customer-service platforms, or anything \
not present in the SOURCES. If the SOURCES do not contain the answer, say so plainly.
- Cite the source doc title inline in square brackets after each claim, e.g. [Knowledge integration].
- Be direct and concise. Do not hedge, speculate, or pad. No preamble like "Based on the sources".
- Keep the answer under 120 words. Lead with the direct answer. Use short numbered steps only \
if the SOURCES actually describe steps. Every generated token is latency, so do not restate \
the question or add a closing summary.
- If the SOURCES only partially cover the question, answer only the covered part and state \
what is not covered."""


class JudgeResult(BaseModel):
    """Structured output for the groundedness judge."""
    judge_score: float = Field(description="0.0-1.0: how well the specific answer is supported by the SOURCES")
    answers_question: bool = Field(
        description="True only if the ANSWER actually provides the information the QUESTION asks for, "
        "drawn from the SOURCES. False if the answer says the information is not in the sources, "
        "punts, or only gives adjacent/general info without answering the question."
    )
    reasoning: str = Field(description="ONE short sentence explaining the score and the answers_question decision")


@dataclass
class Source:
    title: str
    url: str
    score: float


def _format_sources(chunks: list[dict]) -> str:
    blocks = []
    for c in chunks:
        blocks.append(f"### {c['title']}\n{c['text']}")
    return "\n\n".join(blocks)


def _source_titles(chunks: list[dict]) -> str:
    seen = []
    for c in chunks:
        if c["title"] not in seen:
            seen.append(c["title"])
    return ", ".join(f"[{t}]" for t in seen)


def generate_answer(query: str, chunks: list[dict]) -> str:
    user_msg = (
        f"SOURCES (each begins with a '### Title' header):\n\n{_format_sources(chunks)}\n\n"
        f"QUESTION: {query}\n\n"
        "Write a clean, direct answer for the CEO using only the SOURCES above. Cite the "
        f"relevant source title inline in square brackets, e.g. {_source_titles(chunks)}. "
        "Do NOT reproduce the '###' headers or the raw source text, and do NOT repeat these "
        "instructions — write the answer in your own words with inline [Title] citations."
    )
    return get_llm().generate(GEN_SYSTEM, user_msg, max_tokens=GEN_MAX_TOKENS)


def judge_answer(query: str, answer: str, chunks: list[dict]) -> JudgeResult:
    """SEPARATE LLM call: is THIS answer actually supported by THESE chunks?"""
    user_msg = (
        "You are a grounding auditor. Given a QUESTION, a candidate ANSWER, and the SOURCES "
        "that answer was drawn from, judge whether the substantive claims in the ANSWER are "
        "supported by the SOURCES.\n\n"
        "Judge SUBSTANCE, not wording. Reasonable paraphrase, summarization, reformatting into "
        "steps, and synonyms of the source content ARE grounded — do not penalize the answer "
        "for using different words than the sources (e.g. 'articles' vs 'website content', "
        "'connect' vs 'add source'). Score based on whether a reader could verify each claim "
        "against the SOURCES.\n\n"
        "Score 0.8-1.0 when the claims are supported by the sources (even if paraphrased). "
        "Score below 0.6 only when the answer introduces specific facts absent from the SOURCES, "
        "contradicts them, or the SOURCES are genuinely off-topic for the QUESTION. An answer "
        "that correctly says the information isn't available scores high (it makes no unsupported "
        "claim). Do not nitpick minor omissions or formatting differences.\n\n"
        "SEPARATELY, set answers_question: true ONLY if the ANSWER actually provides the specific "
        "information the QUESTION asks for, using the SOURCES. Set it FALSE if the answer says the "
        "information is not in the sources, declines, punts to 'contact the Ada team', or only gives "
        "adjacent/general information without answering the question. (So a grounded 'there is no "
        "information about X in the sources' has a HIGH judge_score but answers_question=false.)\n\n"
        f"QUESTION: {query}\n\n"
        f"ANSWER: {answer}\n\n"
        f"SOURCES:\n\n{_format_sources(chunks)}"
    )
    return get_llm().generate_json(user_msg, JudgeResult, max_tokens=JUDGE_MAX_TOKENS)


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

    # What the retriever actually looked at, so a refusal can be audited rather than trusted.
    evidence = [
        {
            "title": c["title"],
            "url": c["source_url"],
            "score": c["score"],
            "text": c["text"][:EVIDENCE_CHARS] + ("…" if len(c["text"]) > EVIDENCE_CHARS else ""),
        }
        for c in chunks[:3]
    ]

    # Gate stage 1: retrieval. If nothing is relevant, refuse without spending a generation call.
    if retrieval_score < RETRIEVAL_THRESHOLD:
        return {
            "answer": REFUSAL_TEXT,
            "refused": True,
            "sources": source_list,
            "evidence": evidence,
            # Deliberately empty: nothing cleared the relevance floor, so naming the
            # nearest docs would imply a connection the scores don't support.
            "coverage": [],
            "retrieval_score": retrieval_score,
            "judge_score": None,
            "answers_question": None,
            "judge_reasoning": "Retrieval score below threshold — no sufficiently relevant documents.",
        }

    answer = generate_answer(query, chunks)
    judge = judge_answer(query, answer, chunks)

    # Gate stage 2: LLM judge. Refuse if the answer is weakly grounded OR it doesn't actually
    # answer the question (a grounded "not covered in the sources" is a refusal, not an answer).
    refused = judge.judge_score < JUDGE_THRESHOLD or not judge.answers_question

    # A judge-gate refusal means the retrieved docs WERE topically close but didn't contain the
    # answer — so naming them is a real coverage signal ("pricing isn't here, but X and Y are"),
    # not a guess. Retrieval-gate refusals above deliberately get no such hint.
    coverage = [s["title"] for s in source_list[:3]] if refused else []

    return {
        "answer": REFUSAL_TEXT if refused else answer,
        "refused": refused,
        "sources": source_list,
        "evidence": evidence,
        "coverage": coverage,
        "retrieval_score": retrieval_score,
        "judge_score": judge.judge_score,
        "answers_question": judge.answers_question,
        "judge_reasoning": judge.reasoning,
    }
