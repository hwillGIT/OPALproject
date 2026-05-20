"""Value types for the synthesis layer.

Pure-stdlib, frozen dataclasses. Mirrors the shape of
``epic_intelligence.index.store.QueryHit`` on the input side and
emits a clean ``Answer`` shape the voice-assistant + UI surfaces can
both consume.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping


@dataclass(frozen=True)
class Citation:
    """One source citation in a synthesized answer.

    The voice assistant reads ``source_url`` aloud as the provenance;
    the UI surfaces render ``title`` + ``section_path`` as the link
    text and ``snippet`` as the hover preview.
    """

    chunk_id: str
    title: str
    source_url: str
    section_path: tuple[str, ...]
    snippet: str
    score: float


@dataclass(frozen=True)
class Answer:
    """The output of synthesize().

    ``text`` is the natural-language answer, suitable for TTS or
    direct display. ``citations`` carry the provenance — the
    answer text MUST reference them by 1-indexed bracketed numerals
    (``[1]``, ``[2]``, ...) that map to ``citations[i-1]``.
    ``insufficient`` is True when the retrieval set was too thin to
    answer confidently; in that case ``text`` explains what's missing
    rather than guessing.
    """

    text: str
    citations: tuple[Citation, ...]
    insufficient: bool = False
    provider_name: str = "unknown"
    model_name: str = "unknown"
    metadata: Mapping[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class SynthesisRequest:
    """Input passed to synthesize().

    Kept separate from ``RetrievalQuery`` so the synthesis layer
    doesn't depend on how the chunks were retrieved (FTS, vector,
    hybrid, or even a hand-picked set during testing).
    """

    question: str
    citations: tuple[Citation, ...]
    max_tokens_out: int = 1024
    temperature: float = 0.2
    instructions: str | None = None
