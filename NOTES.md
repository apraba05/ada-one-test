# NOTES — Decision Log

Logged as I build, one line per meaningful decision. Feeds the README tradeoffs writeup.

## Pre-build clarifications (asked, not assumed)
- **Design system source**: `[ADA_DESIGN_MD_PATH]` was an unfilled placeholder → asked user → it's `~/.claude/ADA-CX.md`. Read in full before any UI work.
- **Anthropic API key**: not in env → user will add it to `backend/.env`; code reads via python-dotenv. No secret in chat/repo (.env gitignored).
- **Confidence thresholds**: user confirmed my defaults → retrieval max-cosine ≥ **0.35**, judge groundedness ≥ **0.60**. Either fails → hard refuse.

## Stage 0 — Setup
- Stack: Python backend (sentence-transformers + FastAPI required by brief), Next.js frontend. venv at `backend/.venv`.
- Committing on `main` (fresh solo greenfield repo owned by user; no default branch to protect, so no feature branch).
- Model choice: generation = `claude-sonnet-5` (strong grounded synthesis, reasonable cost); LLM judge = `claude-haiku-4-5-20251001` (fast/cheap, adequate for a 0-1 groundedness score). Both Anthropic per brief.

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
(tbd)

## Stage 7 — UI
- Roobert is proprietary (no font file available) → substituting a free geometric grotesque via `next/font`; sanctioned by ADA-CX.md §8.2 ("General Sans / Söhne / Aeonik"). FLAGGED inference.
- Confidence badge / refusal state are not in the design file → will confirm visual treatment with user at Stage 7 (per operating rule: visual choices not in design file). FLAGGED.
