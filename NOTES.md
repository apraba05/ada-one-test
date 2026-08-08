# NOTES — Decision Log

Logged as I build, one line per meaningful decision. Feeds the README tradeoffs writeup.

## Pre-build clarifications (asked, not assumed)
- **Design system source**: `[ADA_DESIGN_MD_PATH]` was an unfilled placeholder → asked user → it's `~/.claude/ADA-CX.md`. Read in full before any UI work.
- **Anthropic API key**: not in env → user will add it to `backend/.env`; code reads via python-dotenv. No secret in chat/repo (.env gitignored).
- **Confidence thresholds**: user confirmed my defaults → retrieval max-cosine ≥ **0.35**, judge groundedness ≥ **0.60**. Either fails → hard refuse.

## Stage 0 — Setup
- Stack: Python backend (sentence-transformers + FastAPI required by brief), Next.js frontend. venv at `backend/.venv`.
- Committing on `main` (fresh solo greenfield repo owned by user; no default branch to protect, so no feature branch).
- Model choice: **claude-opus-4-8 for BOTH generation and the LLM judge.** (Revised from an earlier Sonnet/Haiku plan.) Rationale: the claude-api skill mandates Opus 4.8 as the default unless the user names another model and says not to downgrade for cost — that's the user's decision. Trustworthy grounding is this tool's entire purpose, and the user raised no cost constraint. Note: two Opus calls per query (generate + judge) — acceptable for an interactive single-question demo.
- Judge uses `client.messages.parse()` + a Pydantic schema (guaranteed structured `{judge_score, reasoning, supported}`); structured outputs are supported on Opus 4.8.
- Generation runs WITHOUT extended thinking: grounded synthesis from 4 short chunks is a simple extraction task, and skipping thinking keeps the interactive latency low. The separate LLM judge is the correctness safety net. (Skill defaults to adaptive thinking "for anything remotely complicated"; this isn't.)

## Stage 1 — Ingestion
- llms.txt is a small pointer index → real page list is in `/generative/llms.txt` (524 lines). Filtered strictly to `/docs/knowledge/` and `/docs/welcome/` prefixes.
- Result: 15 pages (8 knowledge + 7 welcome) — within the ~12-15 target, no padding needed.
- Fetch `.md` variant of each page URL (docs serve clean markdown; no HTML scraping).

## Stage 2 — Index
- **Chunk size deviation (deliberate)**: brief says ~300-500 tokens, but all-MiniLM-L6-v2 hard-caps at 256 word-pieces and *silently truncates* beyond. Targeting 300-500 truncated 23% of chunks (verified: 64/275 over 256, one at 6050). Sized to model window instead: TARGET=210 tokens, OVERLAP=40, packed on paragraph boundaries. Correctness > literal number (brief's own "no silent regressions" principle).
- Robust decomposition for oversized blocks (tables/long lists with no sentence boundaries): paragraph → newlines → sentences → hard token-window. Guarantees 0 chunks truncated (verified: 375 chunks, max 250 tokens, 0 over 256).
- Embeddings L2-normalized → cosine == dot product. Persisted to cache/index.pkl with a fingerprint (model + params + kb content hash) so re-runs skip re-embed; stale KB auto-rebuilds.
- Sanity check passed: "Zendesk import" → Knowledge integration chunks (0.66-0.69); "create an article" → Article creation chunks (0.76-0.81). Good matches sit well above the 0.35 floor.

## Stage 3-4 — Retrieval + Generation + Confidence Gate
- Two-stage gate: retrieval max-cosine >= 0.35 AND LLM judge groundedness >= 0.60; either fails => hard refuse (no hedged/partial answers). Retrieval-fail short-circuits before spending a generation call.
- Judge is a SEPARATE call scoring whether the *specific* answer is grounded in the retrieved chunks (not just topic relevance), returning score + reasoning via structured output.

## Provider change — local model (user-requested, mid-build)
- User asked to run a local model instead of an Anthropic API key. This overrides the brief's "Call Claude" mandate (a direct user instruction supersedes the written spec).
- Built `llm.py`: provider abstraction with two backends — `anthropic` (Claude, brief default) and `ollama` (local, keyless). Auto-selects: Anthropic if ANTHROPIC_API_KEY set, else Ollama. Force with `LLM_PROVIDER`. Runs keyless now AND on Claude if a key is added later — no code change.
- Local default: `llama3.1:latest` (8B) via Ollama HTTP (already on machine). Judge uses Ollama's JSON-schema `format` for structured output (parity with Claude's messages.parse).
- **FLAGGED QUALITY CAVEAT**: an 8B local model is weaker at strict grounding and reliable groundedness judging — the core of this tool. Watching at Stage 5/8; will surface honestly if the gate misclassifies buckets. Thresholds may need retuning for the local judge's score distribution.

## Stage 7 — UI
- Refusal/badge visual treatment CONFIRMED by user: answered = white-fr card + green left-border; refused = graphite/pewter card, no green, "not enough information" heading; confidence trace collapsible below both.

- Roobert is proprietary (no font file available) → substituting a free geometric grotesque via `next/font`; sanctioned by ADA-CX.md §8.2 ("General Sans / Söhne / Aeonik"). FLAGGED inference.

## Stage 8 — Eval set (8 CEO-framed questions, 3 buckets)
- Bucket A (answerable): Zendesk connect, create article, website import, best practices → all ANSWERED (judge 0.8-1.0). ✓
- Bucket B (adjacent/not covered): "How much does Ada cost?", "Deploy on WhatsApp?" → all REFUSED. ✓
- Bucket C (off-topic/nonsense): "Capital of France?", prompt-injection "ignore instructions…" → all REFUSED at retrieval gate. ✓
- **Bug found & fixed (the Bucket-B case Stage 8 exists to catch):** initially B was ANSWERED. Root cause: I conflated "grounded" with "actually answers". The model honestly said "there is no information about X in the sources" (correctly grounded, judge=1.0) but it was shown as a green "Grounded answer". Fix: judge now ALSO returns `answers_question` (bool); gate refuses when `judge_score < 0.60 OR not answers_question`. Not a threshold hack — a grounded non-answer is a refusal by definition here. Surfaced in the UI trace as "Answer addresses the question ✓/✗".
- Thresholds held at retrieval>=0.35 / judge>=0.60 across all 8 — no retuning needed for the local judge after the answers_question fix.

## Stage 9 — Automated eval harness (`eval.py`)
- Promoted the eval set from a hand-written table to executable data: `eval.py` holds the 8 questions + expected bucket, runs the full pipeline, prints a pass/fail matrix, and **exits non-zero on any misclassification**. Rationale: the gate is this tool's whole value, and it was only ever verified by hand — so there was no way to prove a change hadn't broken it, and no way to measure the flagged local-judge risk.
- Chose this BEFORE the other roadmap items (hybrid search, reranking) deliberately: both mutate retrieval, which is exactly what gate 1 keys off. A Bucket C question drifting above RETRIEVAL_THRESHOLD becomes a confidently-wrong answer — the failure mode the README calls the worst possible one. Harness first makes the rest of the roadmap safe to land.
- Verified the harness can go RED, not just green: forced a deliberate mislabel and confirmed the FAIL row, the MISCLASSIFIED diagnostics block, and exit code 1. A regression gate that can't fail is decoration.
- Baseline run (local `llama3.1:8b`): **8/8 in 86.3s**, and the scores reproduced the hand-recorded Stage 8 table exactly (0.72/0.88/0.66/0.69 retrieval on bucket A, 0.20/0.24 on C). Confirms the pipeline is deterministic at temperature 0 and that the original manual table was accurate.
- Report header records `provider=... model=...`, and `eval_set.md` documents the `LLM_PROVIDER=ollama|anthropic` two-run diff. This converts the flagged "8B judge is weaker than Claude" risk from prose into a one-command measurement — still UNRUN, no key available (user opted to stay keyless for now).
- Bucket C cases return in ~0.1s vs ~12-24s for A/B, which visibly confirms the retrieval gate short-circuits before spending a generation call.
- Cleanups found while reading: `rag.py` module docstring still said "Claude" post-provider-abstraction (now provider-neutral, and documents `answers_question`); `cli.py` trace omitted `answers_question` — the field that fixed the Bucket B bug — while the API and UI both surfaced it. Now printed.
