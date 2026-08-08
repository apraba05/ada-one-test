"""
Stage 5 — CLI checkpoint / fallback.

Runs the full pipeline end-to-end from the terminal, no UI. Also the permanent
fallback deliverable.

Usage:
  python cli.py "How do I connect my Zendesk help center?"
  python cli.py            # runs the two built-in checkpoint questions
"""
from __future__ import annotations

import sys

from index import Index
from rag import answer_query, RETRIEVAL_THRESHOLD, JUDGE_THRESHOLD


def _print_result(query: str, r: dict) -> None:
    print("=" * 72)
    print(f"Q: {query}\n")
    status = "REFUSED" if r["refused"] else "ANSWERED"
    print(f"[{status}]\n{r['answer']}\n")
    if not r["refused"] and r["sources"]:
        print("Sources:")
        for s in r["sources"]:
            print(f"  - {s['title']}  ({s['url']})")
        print()
    js = r["judge_score"]
    print(
        f"trace: retrieval_score={r['retrieval_score']:.3f} (>= {RETRIEVAL_THRESHOLD}) | "
        f"judge_score={'n/a' if js is None else f'{js:.2f}'} (>= {JUDGE_THRESHOLD})"
    )
    print(f"judge_reasoning: {r['judge_reasoning']}")
    print("=" * 72 + "\n")


def main() -> int:
    index = Index.load()
    if len(sys.argv) > 1:
        queries = [" ".join(sys.argv[1:])]
    else:
        # Stage 5 checkpoint: one clearly-answerable, one clearly out-of-scope.
        queries = [
            "How do I connect my Zendesk help center to Ada?",
            "What is the airspeed velocity of an unladen swallow?",
        ]
    for q in queries:
        _print_result(q, answer_query(q, index))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
