# Ada KB QA Tool — Execution Checklist

## Stage 0 — Setup
- [x] Resolve blockers (design file, API key, thresholds)
- [x] git init, dirs, venv, install deps (background)
- [x] NOTES.md + todo.md

## Stage 1 — Ingestion
- [ ] Fetch /generative/llms.txt, filter to /docs/knowledge/ + /docs/welcome/
- [ ] Fetch .md of each page → save to backend/kb/<slug>.md
- [ ] Verify ≥10 usable pages (else STOP + tell user)

## Stage 2 — Index
- [ ] Chunk docs (~300-500 tokens, sliding window + overlap)
- [ ] Embed with all-MiniLM-L6-v2 (local)
- [ ] Persist vectors+text+meta to cache/index.pkl
- [ ] Manual top-k retrieval sanity check

## Stage 3 — Retrieval + Generation
- [ ] embed query → cosine top-k (k=4)
- [ ] Claude generation grounded ONLY in retrieved chunks, inline citations
- [ ] System prompt forbids general knowledge

## Stage 4 — Confidence Gate
- [ ] Retrieval score check (max cosine ≥ 0.35)
- [ ] LLM judge (separate call, 0-1 groundedness + reasoning, ≥ 0.60)
- [ ] Either fails → hard refuse; return full trace dict

## Stage 5 — CHECKPOINT (CLI end-to-end)
- [ ] answerable Q → grounded answer + citations
- [ ] out-of-scope Q → hard refusal
- [ ] If shaky → STOP, tell user, stay CLI-only

## Stage 6 — API
- [ ] FastAPI POST /ask, error handling (malformed/empty/API failure)

## Stage 7 — UI
- [ ] Confirm refusal/badge visual treatment with user
- [ ] Next.js single page per ADA-CX.md tokens
- [ ] Answer / Refusal / trace panel / loading states

## Stage 8 — Eval
- [ ] 6-8 CEO-framed Qs across 3 buckets, labeled
- [ ] Run through UI, fix any bucket misclassification

## Validation strategy
- Each stage tested before next; commit per stage.
- Regression risk: cache invalidation on chunking change; threshold tuning in Stage 8.

## Review (filled at end)
