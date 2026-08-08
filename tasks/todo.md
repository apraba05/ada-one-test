# Ada KB QA Tool — Execution Checklist

## Stage 0 — Setup
- [x] Resolve blockers (design file, API key, thresholds)
- [x] git init, dirs, venv, install deps (background)
- [x] NOTES.md + todo.md

## Stage 1 — Ingestion
- [x] Fetch /generative/llms.txt, filter to /docs/knowledge/ + /docs/welcome/
- [x] Fetch .md of each page → save to backend/kb/<slug>.md
- [x] Verify ≥10 usable pages (else STOP + tell user)

## Stage 2 — Index
- [x] Chunk docs (~300-500 tokens, sliding window + overlap)
- [x] Embed with all-MiniLM-L6-v2 (local)
- [x] Persist vectors+text+meta to cache/index.pkl
- [x] Manual top-k retrieval sanity check

## Stage 3 — Retrieval + Generation
- [x] embed query → cosine top-k (k=4)
- [x] Claude generation grounded ONLY in retrieved chunks, inline citations
- [x] System prompt forbids general knowledge

## Stage 4 — Confidence Gate
- [x] Retrieval score check (max cosine ≥ 0.35)
- [x] LLM judge (separate call, 0-1 groundedness + reasoning, ≥ 0.60)
- [x] Either fails → hard refuse; return full trace dict

## Stage 5 — CHECKPOINT (CLI end-to-end)
- [x] answerable Q → grounded answer + citations
- [x] out-of-scope Q → hard refusal
- [x] If shaky → STOP, tell user, stay CLI-only

## Stage 6 — API
- [x] FastAPI POST /ask, error handling (malformed/empty/API failure)

## Stage 7 — UI
- [x] Confirm refusal/badge visual treatment with user
- [x] Next.js single page per ADA-CX.md tokens
- [x] Answer / Refusal / trace panel / loading states

## Stage 8 — Eval
- [x] 6-8 CEO-framed Qs across 3 buckets, labeled
- [x] Run through UI, fix any bucket misclassification

## Stage 9 — Automated eval harness
- [x] `eval.py` — the 8 labeled Qs as data, full-pipeline run, pass/fail matrix
- [x] Non-zero exit on misclassification (usable as a regression gate)
- [x] Verify it goes RED, not just green (forced mislabel → FAIL + exit 1)
- [x] Record provider/model in the report; document the Claude-vs-local two-run diff
- [x] Regenerate eval_set.md table from a real run
- [x] Cleanups: provider-neutral rag.py docstring, answers_question in the CLI trace

## Validation strategy
- Each stage tested before next; commit per stage.
- Regression risk: cache invalidation on chunking change; threshold tuning in Stage 8.
- From Stage 9 on: `.venv/bin/python eval.py` must pass 8/8 before any commit that touches
  retrieval, prompts, or thresholds.

## Review

### What changed / was built
- Stages 1-8 all complete. 15 Ada docs ingested → local MiniLM index (375 chunks, 0 truncated)
  → cosine top-k → grounded generation → two-stage confidence gate → FastAPI → Next.js UI.
- Provider abstraction (llm.py): runs keyless on local Ollama, or Claude if a key is set.
- Confidence gate: retrieval ≥ 0.35 AND (judge ≥ 0.60 AND answers_question), else hard refuse.
- Stage 9: the eval set is now executable (`eval.py`) and gates regressions by exit code,
  closing the "no automated eval harness" scope cut.

### Validation performed
- Stage 2: retrieval sanity queries return sensible chunks above threshold.
- Stage 5: CLI end-to-end (answerable → grounded+cited; out-of-scope → refuse).
- Stage 6: API error paths (empty/malformed → 422) + happy path verified via curl.
- Stage 7: answered / refused / trace states verified in a real browser (Playwright CLI).
- Stage 8: 8-question eval matrix, all three buckets classify correctly.
- Stage 9: `eval.py` 8/8 on local llama3.1:8b in 86.3s, reproducing the Stage 8 numbers
  exactly; failure path verified by forcing a mislabel (FAIL row + exit 1); CLI re-checked
  after the trace edit.

### Key decisions / risks (see NOTES.md for full log)
- Chunk size sized to the embedding model's 256-token window (not the brief's 300-500) to
  avoid silent truncation — verified 0 chunks truncated.
- answers_question added to the judge to catch grounded-but-non-answers (Bucket B).
- RISK: local 8B judge is weaker than Claude at grounding — run with a key for production.
  Now measurable in one command: `LLM_PROVIDER=anthropic .venv/bin/python eval.py`.
  UNRUN — no key available yet.

### Follow-ups
- Hybrid search (next up, now regression-checkable), reranking, persistent vector DB,
  retry handling, multi-turn (see README).
- Roobert font is substituted (proprietary); swap in the real font file if licensed.
