"""
Stage 6 — API layer.

Thin FastAPI wrapper around the Stage 3-4 pipeline. One POST /ask endpoint.
Runs locally, no deployment. Basic production-shaped error handling:
malformed requests, empty queries, and LLM/backend failures.

Run: uvicorn app:app --reload --port 8000
"""
from __future__ import annotations

import logging
import threading

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator

from index import Index
from llm import get_llm
from rag import answer_query, RETRIEVAL_THRESHOLD, JUDGE_THRESHOLD

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ada-kb-qa")

app = FastAPI(title="Ada KB QA", version="1.0.0")

# Local Next.js dev server talks to this API from the browser.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

# Build/load the index once at startup (cheap on cache hit).
_index: Index | None = None


@app.on_event("startup")
def _startup() -> None:
    global _index
    _index = Index.load()
    llm = get_llm()
    logger.info("Index loaded (%d chunks); LLM provider=%s model=%s", len(_index.chunks), llm.provider, llm.model)

    # Warm in the background so the server accepts requests immediately; a question that
    # arrives mid-warm just waits for the same load it would have triggered itself.
    def _warm() -> None:
        try:
            # The SentenceTransformer is lazy-loaded on first search, so without this the
            # embedding model load also lands on the first question.
            _index.search("warm", k=1)
            llm.warm()
            logger.info("LLM + embedder warm (%s)", llm.model)
        except Exception:
            logger.warning("LLM warmup failed; first question will pay the load cost", exc_info=True)

    threading.Thread(target=_warm, daemon=True).start()


class AskRequest(BaseModel):
    question: str = Field(..., description="The user's question about configuring Ada.")

    @field_validator("question")
    @classmethod
    def _non_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("question must not be empty")
        if len(v) > 2000:
            raise ValueError("question is too long (max 2000 characters)")
        return v.strip()


class Source(BaseModel):
    title: str
    url: str
    score: float


class Evidence(Source):
    """A retrieved chunk excerpt — lets a reader audit the answer (or the refusal) directly."""
    text: str


class AskResponse(BaseModel):
    answer: str
    refused: bool
    sources: list[Source]
    evidence: list[Evidence]
    coverage: list[str]
    retrieval_score: float
    judge_score: float | None
    answers_question: bool | None
    judge_reasoning: str
    thresholds: dict[str, float]


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "provider": get_llm().provider, "model": get_llm().model}


@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest) -> AskResponse:
    if _index is None:  # defensive; startup should have set it
        raise HTTPException(status_code=503, detail="Index not ready.")
    try:
        result = answer_query(req.question, _index)
    except Exception as exc:  # LLM/backend failure — surface a clean 502, log the detail
        logger.exception("answer_query failed")
        raise HTTPException(
            status_code=502,
            detail=f"The answering service failed ({type(exc).__name__}). Check that the LLM backend is reachable.",
        ) from exc

    return AskResponse(
        **result,
        thresholds={"retrieval": RETRIEVAL_THRESHOLD, "judge": JUDGE_THRESHOLD},
    )
