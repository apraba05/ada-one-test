# Ada Knowledge QA

An internal QA tool for evaluating and configuring Ada's AI-agent knowledge base.
Ask a question about setting up an Ada agent; the tool answers **only** from Ada's own
documentation with inline citations — and **hard-refuses, rather than guesses**, when it
can't answer confidently. A confidently-wrong answer is the worst failure mode for a tool
a CEO uses to evaluate a product, so the confidence gate is the core of the design.

## Architecture

```
docs.ada.cx  ──(Stage 1: ingest .md)──▶  backend/kb/*.md   (15 docs: knowledge + welcome)
                                              │
                       (Stage 2: chunk + embed, all-MiniLM-L6-v2, local)
                                              ▼
                                   backend/cache/index.pkl   (vectors + text + metadata)
                                              │
  question ─▶ FastAPI POST /ask (Stage 6) ─▶ rag.answer_query (Stages 3-4):
                                              1. embed query, cosine top-k (k=4)
                                              2. GATE 1 — max cosine ≥ 0.35 ? else refuse
                                              3. generate grounded answer (LLM, sources only)
                                              4. GATE 2 — LLM judge: groundedness ≥ 0.60
                                                 AND answers_question ? else refuse
                                              ▼
                          {answer, refused, sources, evidence, coverage,
                           retrieval_score, judge_score, answers_question,
                           judge_reasoning}
                                              │
                          Next.js UI (Stage 7) — Ada CX design system:
                          green "grounded answer" card / graphite "refusal" card
                          (+ what the KB does cover) / collapsible evidence panel /
                          collapsible confidence trace
```

### Confidence gate (Stage 4 — the core)

Two independent checks, **both must pass** or the tool hard-refuses (no hedged/partial answers):

1. **Retrieval check** — max cosine similarity across the top-k chunks must clear
   `RETRIEVAL_THRESHOLD = 0.35`. Chosen for `all-MiniLM-L6-v2`, whose "clearly relevant"
   band sits around 0.35–0.7; off-topic queries score well below (0.15–0.25 in testing).
   Short-circuits before spending a generation call.
2. **LLM judge** — a *separate* LLM call scores (0–1) whether the specific generated answer
   is actually supported by the retrieved chunks (`JUDGE_THRESHOLD = 0.60`), and separately
   whether it actually answers the question (`answers_question`). A grounded "that isn't in
   the sources" is therefore a refusal, not a green answer.

Both thresholds are exposed in the API response (`thresholds`) and rendered in the UI trace
panel so they're visible and tunable, not buried.

Because the gate is the core, it has an executable regression check: `backend/eval.py` runs
8 labeled questions (answerable / adjacent-but-not-covered / off-topic) through the full
pipeline and **exits non-zero if any of them lands in the wrong bucket**. Run it before and
after any change to retrieval, prompts, or thresholds — see `backend/eval_set.md`.

### LLM provider

`backend/llm.py` abstracts the two LLM operations (generation, judge) behind a provider
interface with two backends:

- **`anthropic`** — Claude (`claude-opus-4-8`) via the official SDK. The brief's default.
- **`ollama`** — a local model (`llama3.2:3b` by default), no API key required.

Selection: `LLM_PROVIDER` env var forces one; otherwise **auto** — Anthropic if
`ANTHROPIC_API_KEY` is set, else Ollama. The tool runs keyless on local Ollama today and
switches to Claude with zero code changes the moment a key is present.

> **Quality note:** a small local model is measurably weaker at strict grounding and at acting
> as a reliable groundedness judge — the exact core of this tool. For production evaluation,
> run with a Claude key. See NOTES.md.

### Latency

A local model generates at roughly 30 tokens/second, so answer length *is* response time.
Three changes took a question from ~20s to ~6s: defaulting to a 3B model (verified to still
pass all 8 eval cases), capping answers at ~120 words, and warming both the LLM and the
embedding model at startup so the first question doesn't pay the load cost.

`OLLAMA_MODEL=llama3.1:latest` trades ~2x latency for a more discriminating judge.

Note that the answer is **not** streamed, deliberately: the judge can still refuse after
generation, so showing tokens as they arrive would leak an answer the gate is about to reject.
The UI shows real pipeline progress instead.

## Running it

**Prereqs:** Python 3.12, Node 20+. For the keyless path: Ollama running with a model pulled
(`ollama pull llama3.1`). For Claude: put `ANTHROPIC_API_KEY=...` in `backend/.env`.

```bash
# Backend
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python ingest.py          # Stage 1 — fetch docs to kb/ (one-time)
.venv/bin/python index.py           # Stage 2 — build the embedding index (cached)
.venv/bin/python cli.py "Can I connect my Zendesk help center?"   # Stage 5 — CLI
.venv/bin/python eval.py            # eval harness — 8 labeled Qs, non-zero exit on regression
.venv/bin/uvicorn app:app --port 8000                             # Stage 6 — API

# Frontend (separate terminal)
cd frontend
npm install
npm run dev                          # http://localhost:3000
```

The CLI (`cli.py`) is a full standalone path — it works even without the UI.

## Explicit scope cuts

Deliberately **not** built (and not gold-plated around):

- No persistent vector DB — in-memory + a local `cache/index.pkl` file only.
- No hybrid search / reranking — pure vector cosine similarity.
- No multi-turn conversation — single question in, single answer out.
- No streaming — incompatible with a gate that can refuse after generation (see Latency).
- No retry/backoff on LLM calls.
- No CI — `backend/eval.py` is run by hand, and it asserts bucket classification
  (answer vs. refuse) only, not answer-quality scoring.
- No auth, no multi-user, no deployment/hosting.
- No responsive / mobile design.

## What I'd add next

- **Hybrid search** — add BM25 keyword scoring alongside vectors; would catch exact-term
  queries (product names, API fields) where pure embeddings underperform. `eval.py` is the
  guardrail for this: it changes retrieval, which is what the first gate keys off.
- **Reranking** — a cross-encoder reranker over the top-k to sharpen chunk ordering before
  generation, improving both answer quality and the retrieval-gate signal.
- **Persistent vector DB** — move vectors to e.g. pgvector/Qdrant so the index survives
  restarts, scales past in-memory, and supports incremental doc updates.
- **Retry handling** — exponential backoff on LLM calls (the SDK already retries 429/5xx;
  add app-level handling for the Ollama backend and surface transient failures gracefully).
- **Multi-turn** — conversation memory so follow-ups ("what about for Salesforce?") resolve
  against prior context, with the confidence gate applied per turn.
