"""LLM provider abstraction for the orchestrator.

A "provider" is any object with a ``.complete(system_prompt,
user_prompt, max_tokens, temperature) -> str`` method, plus optional
``.name`` and ``.model`` attributes.

This module ships a deterministic ``StubProvider`` so the runner +
CLI work end-to-end with zero external dependencies and no API keys.
When the user asks for ``--provider anthropic|openai|gemini|auto`` we
delegate to ``epic_intelligence.synthesis.get_provider`` — that
package is the canonical home for real provider wiring.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class StubProvider:
    """Deterministic provider that echoes its prompt — for tests + CI.

    Returns a short, structured response so downstream phases get
    something to summarize and emit events about. Never opens a
    network connection, never reads an API key.
    """

    name: str = "stub"
    model: str = "stub-deterministic"

    def complete(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int = 1024,
        temperature: float = 0.3,
    ) -> str:
        # Pull a one-line "what is the phase asking" hint out of the
        # user prompt for readability.
        phase_line = next(
            (l for l in user_prompt.splitlines() if l.startswith("PHASE:")),
            "PHASE: (unknown)",
        )
        return (
            f"[stub-response] {phase_line}\n"
            f"This is a deterministic stub answer. Replace the provider "
            f"with --provider anthropic|openai|gemini|auto for real LLM "
            f"output.\n"
            f"(system prompt was {len(system_prompt)} chars; "
            f"user prompt was {len(user_prompt)} chars; "
            f"max_tokens={max_tokens}, temperature={temperature})"
        )


def get_provider(name: str = "stub"):
    """Resolve a provider by name.

    ``stub`` → built-in ``StubProvider`` (no external deps).
    Anything else (``auto``, ``anthropic``, ``openai``, ``gemini``)
    is delegated to ``epic_intelligence.synthesis.get_provider``.
    ImportError on that package is surfaced with a helpful hint.
    """
    if name == "stub":
        return StubProvider()
    try:
        from epic_intelligence.synthesis import get_provider as _real_get
    except ImportError as exc:
        raise RuntimeError(
            f"provider {name!r} requires the epic_intelligence.synthesis "
            "package, which isn't installed on this branch. Use "
            "'--provider stub' or merge the synthesis PR.",
        ) from exc
    return _real_get(name)
