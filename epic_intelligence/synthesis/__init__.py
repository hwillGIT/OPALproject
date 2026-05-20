"""LLM synthesis layer on top of the citation-aware retrieval.

Turns a question + a set of retrieved chunks into a natural-language
answer with verifiable citations back to source URLs.

Pluggable LLM provider — Anthropic / OpenAI / Gemini / stub — selected
via environment variable. Defaults to stub when nothing is configured
so tests + CI run without API keys.
"""

from .models import Answer, Citation, SynthesisRequest
from .provider import (
    LlmProvider,
    StubProvider,
    get_provider,
)
from .prompts import build_synthesis_prompt
from .synthesizer import synthesize

__all__ = [
    "Answer",
    "Citation",
    "LlmProvider",
    "StubProvider",
    "SynthesisRequest",
    "build_synthesis_prompt",
    "get_provider",
    "synthesize",
]
