"""
Stage 1 — Ingestion.

Fetch Ada's docs index (llms.txt), filter to /docs/knowledge/ and /docs/welcome/,
fetch the clean .md variant of each page, and save one file per slug under kb/.

Docs already serve clean markdown, so we never scrape/parse HTML.
"""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path

import requests  # bundles certifi — avoids macOS python.org missing-CA SSL errors

INDEX_URL = "https://docs.ada.cx/generative/llms.txt"
# Only these two doc trees, per the brief.
KEEP_PREFIXES = ("https://docs.ada.cx/docs/knowledge/", "https://docs.ada.cx/docs/welcome/")
MIN_PAGES = 10  # below this, STOP rather than pad the KB

KB_DIR = Path(__file__).parent / "kb"
UA = {"User-Agent": "ada-kb-qa/1.0 (+internal eval tool)"}


def fetch(url: str, retries: int = 2) -> str:
    """GET text with a couple of naive retries (network flakiness only, not API)."""
    last = None
    for attempt in range(retries + 1):
        try:
            resp = requests.get(url, headers=UA, timeout=30)
            resp.raise_for_status()
            return resp.text
        except requests.RequestException as e:
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"failed to fetch {url}: {last}")


def parse_index(text: str) -> list[tuple[str, str]]:
    """
    Extract (title, url) pairs from the markdown link list in llms.txt,
    keeping only .md pages under the two allowed prefixes. De-duplicates by URL.
    """
    pairs: list[tuple[str, str]] = []
    seen: set[str] = set()
    # Markdown links: [Title](https://....md)
    for m in re.finditer(r"\[([^\]]+)\]\((https://docs\.ada\.cx[^)]+\.md)\)", text):
        title, url = m.group(1).strip(), m.group(2).strip()
        if url.startswith(KEEP_PREFIXES) and url not in seen:
            seen.add(url)
            pairs.append((title, url))
    return pairs


def slug_for(url: str) -> str:
    """Derive a filesystem-safe slug from the doc URL path (nested paths flattened with '--')."""
    path = url.split("docs.ada.cx/", 1)[1]
    path = path[: -len(".md")] if path.endswith(".md") else path
    # drop the leading 'docs/' tree marker, keep the meaningful tail
    parts = [p for p in path.split("/") if p and p != "docs"]
    slug = "--".join(parts)
    return re.sub(r"[^a-zA-Z0-9._-]", "-", slug)


def main() -> int:
    KB_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Fetching index: {INDEX_URL}")
    index_text = fetch(INDEX_URL)
    pages = parse_index(index_text)
    print(f"Found {len(pages)} candidate pages under {KEEP_PREFIXES}")

    if len(pages) < MIN_PAGES:
        print(
            f"\nSTOP: only {len(pages)} usable pages (< {MIN_PAGES}). "
            "Not padding the KB with unrelated sections. Investigate the index filter.",
            file=sys.stderr,
        )
        return 2

    written = []
    for title, url in pages:
        slug = slug_for(url)
        md = fetch(url)
        # Front-matter so downstream chunking keeps title + source URL with each chunk.
        header = f"---\ntitle: {title}\nsource_url: {url.removesuffix('.md')}\nslug: {slug}\n---\n\n"
        out = KB_DIR / f"{slug}.md"
        out.write_text(header + md, encoding="utf-8")
        written.append((slug, len(md)))
        print(f"  saved {slug}.md  ({len(md):,} chars)  <- {title}")
        time.sleep(0.15)  # be polite to the docs host

    print(f"\nDone. Wrote {len(written)} files to {KB_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
