"""Pluggable LLM provider for the synthesis layer.

Three real backends + one stub:

  - anthropic      Claude via the `anthropic` Python SDK.
                   Requires ANTHROPIC_API_KEY in env.
  - openai         GPT-4o/mini via the `openai` SDK.
                   Requires OPENAI_API_KEY in env.
  - gemini         Google Gemini via `google.generativeai`.
                   Requires GOOGLE_API_KEY in env. Same SDK as
                   memory_system/save_session.py + embed_and_store.py.
  - stub           Deterministic, no-network echo provider for tests
                   and CI. Always available.

Factory `get_provider(prefer='auto')` picks based on env:
  - explicit OPAL_SYNTHESIS_PROVIDER env var wins if set
  - else auto: try anthropic -> openai -> gemini -> stub
  - 'stub' is always available so tests don't need API keys

Adding a new provider is one class implementing the `LlmProvider`
protocol. Keep it.
"""
from __future__ import annotations

import os
import sys
from typing import Protocol


class LlmProvider(Protocol):
    """Minimal contract every backend honours."""

    name: str
    model: str

    def complete(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int,
        temperature: float,
    ) -> str:
        """Return the assistant text. Errors raise; caller catches."""
        ...


# ---------------------------------------------------------------------------
# Stub provider — always available, deterministic, no network
# ---------------------------------------------------------------------------


class StubProvider:
    """Deterministic echo provider for tests.

    Produces a predictable answer that:
      1. Cites EVERY source (1..N) so the citation-extraction logic
         can be exercised
      2. Echoes the question so a test can grep for it
      3. Surfaces the "insufficient" path when given zero sources
    """

    name = "stub"
    model = "stub-echo"

    def complete(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int,
        temperature: float,
    ) -> str:
        # Pull the question + count the sources by counting `[N]` markers
        # in the user prompt (build_synthesis_prompt emits [1]..[N]).
        import re
        m = re.search(r"QUESTION:\s*(.+?)\n\n", user_prompt, re.DOTALL)
        question = (m.group(1).strip() if m else "(unknown)").splitlines()[0]
        source_ids = re.findall(r"^\[(\d+)\]\s+", user_prompt, re.MULTILINE)
        n = len(set(source_ids))

        if n == 0:
            return (
                "(insufficient sources) The SOURCES section is empty, so "
                f"I cannot answer the question {question!r} from grounded "
                "evidence. Re-run the retrieval with a broader query or "
                "ingest more documentation."
            )
        cites = ", ".join(f"[{i + 1}]" for i in range(n))
        return (
            f"Stub answer to: {question!r}. This deterministic test "
            f"response cites every provided source: {cites}."
        )


# ---------------------------------------------------------------------------
# Anthropic provider
# ---------------------------------------------------------------------------


class AnthropicProvider:
    name = "anthropic"

    def __init__(self, model: str | None = None) -> None:
        try:
            from anthropic import Anthropic  # type: ignore
        except ImportError as exc:  # pragma: no cover — env-dependent
            raise RuntimeError(
                "anthropic provider requested but `anthropic` Python SDK is "
                "not installed (pip install anthropic)",
            ) from exc
        key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY not set in env",
            )
        self._client = Anthropic(api_key=key)
        self.model = model or os.environ.get(
            "OPAL_SYNTHESIS_MODEL", "claude-sonnet-4-6",
        )

    def complete(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int,
        temperature: float,
    ) -> str:
        resp = self._client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
        parts: list[str] = []
        for block in resp.content:
            text = getattr(block, "text", None)
            if text:
                parts.append(text)
        return "".join(parts).strip()


# ---------------------------------------------------------------------------
# OpenAI provider
# ---------------------------------------------------------------------------


class OpenAiProvider:
    name = "openai"

    def __init__(self, model: str | None = None) -> None:
        try:
            from openai import OpenAI  # type: ignore
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError(
                "openai provider requested but `openai` Python SDK is not "
                "installed (pip install openai)",
            ) from exc
        if not os.environ.get("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY not set in env")
        self._client = OpenAI()
        self.model = model or os.environ.get(
            "OPAL_SYNTHESIS_MODEL", "gpt-4o-mini",
        )

    def complete(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int,
        temperature: float,
    ) -> str:
        resp = self._client.chat.completions.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return (resp.choices[0].message.content or "").strip()


# ---------------------------------------------------------------------------
# Gemini provider (matches the SDK already in OPAL's memory_system)
# ---------------------------------------------------------------------------


class GeminiProvider:
    name = "gemini"

    def __init__(self, model: str | None = None) -> None:
        try:
            import google.generativeai as genai  # type: ignore
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError(
                "gemini provider requested but `google-generativeai` is "
                "not installed (pip install google-generativeai)",
            ) from exc
        key = os.environ.get("GOOGLE_API_KEY")
        if not key:
            raise RuntimeError("GOOGLE_API_KEY not set in env")
        genai.configure(api_key=key)
        self._genai = genai
        self.model = model or os.environ.get(
            "OPAL_SYNTHESIS_MODEL", "gemini-1.5-flash",
        )

    def complete(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int,
        temperature: float,
    ) -> str:
        model = self._genai.GenerativeModel(
            self.model, system_instruction=system_prompt,
        )
        resp = model.generate_content(
            user_prompt,
            generation_config={
                "max_output_tokens": max_tokens,
                "temperature": temperature,
            },
        )
        return (resp.text or "").strip()


# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------


_AUTO_ORDER = ("anthropic", "openai", "gemini")


def get_provider(prefer: str = "auto", *, model: str | None = None) -> LlmProvider:
    """Pick a provider. Falls back to stub when no real backend is available.

    ``prefer`` is one of:
      - 'auto'      try anthropic, openai, gemini in order; fall back to stub
      - 'stub'      always returns the deterministic StubProvider
      - 'anthropic' force the Anthropic backend (raises if not available)
      - 'openai'    force OpenAI (raises if not available)
      - 'gemini'    force Gemini (raises if not available)

    Environment override:
      OPAL_SYNTHESIS_PROVIDER  if set, replaces ``prefer``
      OPAL_SYNTHESIS_MODEL     model name override (provider-specific default
                               otherwise — claude-sonnet-4-6 / gpt-4o-mini /
                               gemini-1.5-flash)
    """
    env_pref = os.environ.get("OPAL_SYNTHESIS_PROVIDER")
    if env_pref:
        prefer = env_pref

    if prefer == "stub":
        return StubProvider()
    if prefer == "anthropic":
        return AnthropicProvider(model=model)
    if prefer == "openai":
        return OpenAiProvider(model=model)
    if prefer == "gemini":
        return GeminiProvider(model=model)
    if prefer != "auto":
        raise ValueError(f"unknown synthesis provider: {prefer!r}")

    for cand in _AUTO_ORDER:
        try:
            return get_provider(cand, model=model)
        except Exception as exc:
            print(
                f"epic_intelligence.synthesis: {cand} unavailable ({exc}); "
                f"trying next",
                file=sys.stderr,
            )
    return StubProvider()
