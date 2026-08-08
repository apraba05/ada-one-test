"""
Stage 2 — Index.

Chunk each kb/*.md doc into overlapping windows sized to the embedding model's
context, embed locally with all-MiniLM-L6-v2, and persist vectors + text +
source metadata to a single cache file so re-runs don't re-embed.

NOTE on chunk size: the brief suggests ~300-500 tokens, but all-MiniLM-L6-v2
has a hard 256 word-piece limit and *silently truncates* longer inputs. We
therefore target ~240 tokens (packed on paragraph boundaries, ~40-token
overlap) so no chunk content is dropped. See NOTES.md.
"""
from __future__ import annotations

import hashlib
import pickle
import re
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"
TARGET_TOKENS = 210      # under the model's 256 cap w/ headroom for join + tokenizer round-trip drift
OVERLAP_TOKENS = 40      # sliding-window overlap between adjacent chunks
MAX_TOKENS = 256         # all-MiniLM-L6-v2 hard word-piece limit (truncates beyond this)

BACKEND = Path(__file__).parent
KB_DIR = BACKEND / "kb"
CACHE_FILE = BACKEND / "cache" / "index.pkl"

_model = None  # lazily-loaded SentenceTransformer (heavy import)


def get_model():
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer(MODEL_NAME)
    return _model


@dataclass
class Chunk:
    text: str
    title: str
    source_url: str
    slug: str
    chunk_id: int


def _parse_front_matter(raw: str) -> tuple[dict, str]:
    """Split the '--- ... ---' YAML-ish front-matter we wrote in ingest.py from the body."""
    m = re.match(r"^---\n(.*?)\n---\n\n?(.*)$", raw, re.DOTALL)
    if not m:
        return {}, raw
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2)


def _split_blocks(body: str) -> list[str]:
    """Split into paragraph/heading blocks on blank lines; keep markdown structure intact."""
    blocks = [b.strip() for b in re.split(r"\n\s*\n", body) if b.strip()]
    return blocks


def _tok_len(tokenizer, text: str) -> int:
    return len(tokenizer.encode(text, add_special_tokens=False))


def _hard_token_split(tokenizer, text: str) -> list[str]:
    """Last-resort split of a unit with no usable text boundary (e.g. a big table) into
    <=TARGET_TOKENS windows by decoding token slices. Guarantees no truncation downstream."""
    ids = tokenizer.encode(text, add_special_tokens=False)
    out = []
    for i in range(0, len(ids), TARGET_TOKENS):
        out.append(tokenizer.decode(ids[i : i + TARGET_TOKENS]).strip())
    return [o for o in out if o]


def _atomize(tokenizer, block: str) -> list[str]:
    """Decompose one block into units each <= TARGET_TOKENS.
    Try progressively finer boundaries: whole block -> lines (table rows / list items)
    -> sentences -> hard token window."""
    if _tok_len(tokenizer, block) <= TARGET_TOKENS:
        return [block]

    def pack(pieces: list[str], joiner: str) -> list[str]:
        units, buf = [], ""
        for p in pieces:
            cand = f"{buf}{joiner}{p}".strip() if buf else p
            if buf and _tok_len(tokenizer, cand) > TARGET_TOKENS:
                units.append(buf)
                buf = p
            else:
                buf = cand
        if buf:
            units.append(buf)
        return units

    # 1) split on newlines (table rows, list items)
    result: list[str] = []
    for u in pack(block.split("\n"), "\n"):
        if _tok_len(tokenizer, u) <= TARGET_TOKENS:
            result.append(u)
            continue
        # 2) split on sentences
        for s in pack(re.split(r"(?<=[.!?])\s+", u), " "):
            if _tok_len(tokenizer, s) <= TARGET_TOKENS:
                result.append(s)
            else:
                # 3) hard token-window split
                result.extend(_hard_token_split(tokenizer, s))
    return result


def chunk_document(meta: dict, body: str, tokenizer) -> list[Chunk]:
    """
    Greedily pack blocks into ~TARGET_TOKENS chunks on paragraph boundaries,
    carrying ~OVERLAP_TOKENS of trailing content into the next chunk.
    A single block longer than the target is hard-split by sentence.
    """
    title = meta.get("title", meta.get("slug", "Untitled"))
    source_url = meta.get("source_url", "")
    slug = meta.get("slug", "")

    # Pre-split every block into units that each fit the model's window (no truncation).
    units: list[str] = []
    for block in _split_blocks(body):
        units.extend(_atomize(tokenizer, block))

    chunks: list[Chunk] = []
    cur: list[str] = []
    cur_tokens = 0
    cid = 0

    def flush():
        nonlocal cur, cur_tokens, cid
        if not cur:
            return
        text = "\n\n".join(cur).strip()
        chunks.append(Chunk(text=text, title=title, source_url=source_url, slug=slug, chunk_id=cid))
        cid += 1
        # Build overlap tail: keep trailing units up to ~OVERLAP_TOKENS for the next chunk.
        tail: list[str] = []
        tail_tokens = 0
        for u in reversed(cur):
            t = _tok_len(tokenizer, u)
            if tail_tokens + t > OVERLAP_TOKENS:
                break
            tail.insert(0, u)
            tail_tokens += t
        cur = tail
        cur_tokens = tail_tokens

    for u in units:
        t = _tok_len(tokenizer, u)
        if cur_tokens + t > TARGET_TOKENS and cur:
            flush()
        cur.append(u)
        cur_tokens += t
    flush()
    return chunks


def _kb_fingerprint() -> str:
    """Hash of all kb file contents + chunking params, so we skip re-embedding unchanged KBs."""
    h = hashlib.sha256()
    h.update(f"{MODEL_NAME}|{TARGET_TOKENS}|{OVERLAP_TOKENS}".encode())
    for p in sorted(KB_DIR.glob("*.md")):
        h.update(p.name.encode())
        h.update(p.read_bytes())
    return h.hexdigest()


def build_index(force: bool = False) -> "Index":
    fp = _kb_fingerprint()
    if not force and CACHE_FILE.exists():
        cached = pickle.loads(CACHE_FILE.read_bytes())
        if cached.get("fingerprint") == fp:
            print(f"[index] cache hit ({len(cached['chunks'])} chunks) — skipping re-embed")
            return Index.from_cache(cached)

    model = get_model()
    tokenizer = model.tokenizer
    all_chunks: list[Chunk] = []
    for p in sorted(KB_DIR.glob("*.md")):
        meta, body = _parse_front_matter(p.read_text(encoding="utf-8"))
        meta.setdefault("slug", p.stem)
        all_chunks.extend(chunk_document(meta, body, tokenizer))

    print(f"[index] embedding {len(all_chunks)} chunks from {len(list(KB_DIR.glob('*.md')))} docs ...")
    texts = [c.text for c in all_chunks]
    embeddings = model.encode(
        texts, normalize_embeddings=True, show_progress_bar=False, batch_size=64
    ).astype(np.float32)

    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "fingerprint": fp,
        "model": MODEL_NAME,
        "chunks": [asdict(c) for c in all_chunks],
        "embeddings": embeddings,
    }
    CACHE_FILE.write_bytes(pickle.dumps(payload))
    print(f"[index] persisted {len(all_chunks)} chunks -> {CACHE_FILE}")
    return Index.from_cache(payload)


class Index:
    def __init__(self, chunks: list[dict], embeddings: np.ndarray):
        self.chunks = chunks
        self.embeddings = embeddings

    @classmethod
    def from_cache(cls, payload: dict) -> "Index":
        return cls(payload["chunks"], payload["embeddings"])

    @classmethod
    def load(cls) -> "Index":
        """Load persisted index, building it if missing/stale."""
        return build_index(force=False)

    def search(self, query: str, k: int = 4) -> list[dict]:
        """Cosine top-k. Embeddings are L2-normalized, so cosine == dot product."""
        model = get_model()
        qv = model.encode([query], normalize_embeddings=True).astype(np.float32)[0]
        scores = self.embeddings @ qv
        top = np.argsort(-scores)[:k]
        results = []
        for i in top:
            r = dict(self.chunks[i])
            r["score"] = float(scores[i])
            results.append(r)
        return results


if __name__ == "__main__":
    import sys
    idx = build_index(force="--force" in sys.argv)
    # Manual sanity check (Stage 2 gate): a clearly in-scope query should return sensible chunks.
    for q in ["Can I import my Zendesk knowledge base?", "How do I create an article in Ada?"]:
        print(f"\n=== QUERY: {q} ===")
        for r in idx.search(q, k=4):
            print(f"  {r['score']:.3f}  [{r['title']}]  {r['text'][:90].replace(chr(10),' ')}...")
