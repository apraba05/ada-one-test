"""
LLM provider abstraction.

The brief specifies Claude (Anthropic API) for both generation and the judge.
To allow a keyless local demo, this module abstracts the two LLM operations
behind a provider interface with two backends:

  - "anthropic": Claude via the official SDK (the brief's default).
  - "ollama":    a local model via the Ollama HTTP API (no API key required).

Selection (see get_llm):
  LLM_PROVIDER env var forces a provider; otherwise auto — Anthropic if
  ANTHROPIC_API_KEY is set, else Ollama.

Quality caveat (logged in NOTES.md): a small local model (llama3.1:8b) is
materially weaker at strict grounding and at acting as a reliable groundedness
judge — the exact core of this tool. Prefer Claude when a key is available.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Type, TypeVar

import requests
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv(Path(__file__).parent / ".env")

ANTHROPIC_MODEL = "claude-opus-4-8"
# 3B by default: ~2x faster than llama3.1:8b (≈6s vs ≈12s per answered question) and it still
# passes all 8 eval cases, so the gate's behaviour is unchanged — verified, not assumed. Its
# judge scores are less discriminating though (0.90 flat where the 8B spreads 0.80-1.00), so
# use OLLAMA_MODEL=llama3.1:latest, or a Claude key, when judging fidelity matters more than speed.
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

T = TypeVar("T", bound=BaseModel)


class LLM:
    """Common interface: free-text generation + schema-constrained JSON."""

    provider: str
    model: str

    def generate(self, system: str, user: str, max_tokens: int) -> str:
        raise NotImplementedError

    def generate_json(self, user: str, schema: Type[T], max_tokens: int) -> T:
        raise NotImplementedError

    def warm(self) -> None:
        """Pay the model load cost up front instead of on the user's first question."""


class AnthropicLLM(LLM):
    provider = "anthropic"
    model = ANTHROPIC_MODEL

    def __init__(self) -> None:
        import anthropic
        self._client = anthropic.Anthropic()

    def generate(self, system: str, user: str, max_tokens: int) -> str:
        resp = self._client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return "".join(b.text for b in resp.content if b.type == "text").strip()

    def generate_json(self, user: str, schema: Type[T], max_tokens: int) -> T:
        resp = self._client.messages.parse(
            model=self.model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": user}],
            output_format=schema,
        )
        return resp.parsed_output


class OllamaLLM(LLM):
    provider = "ollama"

    def __init__(self) -> None:
        self.model = OLLAMA_MODEL

    def _chat(self, messages: list[dict], max_tokens: int, fmt: dict | None = None) -> str:
        payload = {
            "model": self.model,
            "stream": False,
            "messages": messages,
            # Keep the model resident: a query makes two back-to-back calls, and the default
            # idle unload costs a reload (~2s) between them and on the next question.
            "keep_alive": -1,
            # 4096 comfortably fits the largest prompt we build (4 chunks + answer + judge
            # instructions ~= 1.6k tokens); the 8192 default just allocates KV cache we never use.
            "options": {"temperature": 0, "num_ctx": 4096, "num_predict": max_tokens},
        }
        if fmt is not None:
            payload["format"] = fmt
        r = requests.post(f"{OLLAMA_URL}/api/chat", json=payload, timeout=300)
        r.raise_for_status()
        return r.json()["message"]["content"]

    def generate(self, system: str, user: str, max_tokens: int) -> str:
        return self._chat(
            [{"role": "system", "content": system}, {"role": "user", "content": user}],
            max_tokens,
        ).strip()

    def generate_json(self, user: str, schema: Type[T], max_tokens: int) -> T:
        content = self._chat(
            [{"role": "user", "content": user}],
            max_tokens,
            fmt=schema.model_json_schema(),
        )
        return schema.model_validate_json(content)

    def warm(self) -> None:
        """Loading a cold model costs ~20s — the single worst moment in a live demo, and it
        would otherwise land on the first question someone asks."""
        self._chat([{"role": "user", "content": "ok"}], max_tokens=1)


_llm: LLM | None = None


def get_llm() -> LLM:
    global _llm
    if _llm is None:
        provider = os.getenv("LLM_PROVIDER", "").strip().lower()
        if not provider:
            provider = "anthropic" if os.getenv("ANTHROPIC_API_KEY") else "ollama"
        _llm = AnthropicLLM() if provider == "anthropic" else OllamaLLM()
    return _llm
