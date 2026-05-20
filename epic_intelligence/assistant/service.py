"""IntelligenceAnswerService — the public contract for the voice assistant.

One method: ``answer(question) -> Answer``.

Composes retrieval + synthesis behind a stable interface so the
voice-assistant integration doesn't have to know about ChromaDB,
embedders, or LLM providers. Swap any layer below this without
touching the caller.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ..index.embedder import get_embedder
from ..index.store import (
    DEFAULT_COLLECTION,
    DEFAULT_INDEX_DIR,
    EpicIntelligenceStore,
)
from ..synthesis import (
    Answer,
    LlmProvider,
    SynthesisRequest,
    get_provider,
    synthesize,
)
from ..synthesis.synthesizer import hits_to_citations


@dataclass(frozen=True)
class AnswerServiceConfig:
    """Tuning knobs for the service.

    Sensible defaults; the voice router can override per-call.
    """

    top_k: int = 5
    max_tokens_out: int = 1024
    temperature: float = 0.2
    instructions: str | None = None


class IntelligenceAnswerService:
    """Citation-aware answer service over the EPIC knowledge base."""

    def __init__(
        self,
        *,
        index_dir: Path = DEFAULT_INDEX_DIR,
        collection: str = DEFAULT_COLLECTION,
        embedder_pref: str = "auto",
        provider: LlmProvider | None = None,
        provider_pref: str = "auto",
        config: AnswerServiceConfig | None = None,
    ) -> None:
        embedder, embedder_name = get_embedder(prefer=embedder_pref)
        self._store = EpicIntelligenceStore(
            embedder=embedder,
            embedder_name=embedder_name,
            index_dir=index_dir,
            collection_name=collection,
        )
        self._provider = provider or get_provider(prefer=provider_pref)
        self._config = config or AnswerServiceConfig()

    @property
    def provider_name(self) -> str:
        return self._provider.name

    @property
    def model_name(self) -> str:
        return getattr(self._provider, "model", "unknown")

    def answer(
        self,
        question: str,
        *,
        top_k: int | None = None,
        max_tokens_out: int | None = None,
        temperature: float | None = None,
        instructions: str | None = None,
    ) -> Answer:
        """Retrieve + synthesize. Returns a cited Answer."""
        if not question or not question.strip():
            return Answer(
                text="(empty question; nothing to answer)",
                citations=(),
                insufficient=True,
                provider_name=self._provider.name,
                model_name=getattr(self._provider, "model", "unknown"),
            )

        hits = self._store.query(
            question, n_results=top_k or self._config.top_k,
        )
        citations = hits_to_citations(hits)
        request = SynthesisRequest(
            question=question,
            citations=citations,
            max_tokens_out=max_tokens_out or self._config.max_tokens_out,
            temperature=(
                temperature if temperature is not None
                else self._config.temperature
            ),
            instructions=instructions or self._config.instructions,
        )
        return synthesize(request, provider=self._provider)


def answer(question: str, **kwargs) -> Answer:
    """Module-level convenience: construct a default service + answer.

    Use for one-off queries; for production / repeated calls,
    instantiate `IntelligenceAnswerService` once and reuse it.
    """
    service = IntelligenceAnswerService(**kwargs)
    return service.answer(question)
