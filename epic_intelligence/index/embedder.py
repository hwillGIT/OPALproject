"""Pluggable embedding functions for the Epic Intelligence Layer.

Two backends:

  * default (no API key)  — ChromaDB's bundled `DefaultEmbeddingFunction`,
                            backed by sentence-transformers/all-MiniLM-L6-v2
                            via ONNX runtime. Runs fully offline. ~384-dim.
                            Good enough for development and tests.
  * gemini (GOOGLE_API_KEY) — Google's `models/embedding-001` via
                              `google.generativeai.embed_content`. Higher
                              quality. Matches the embedder used by the
                              repo-root `embed_and_store.py` so collections
                              can be reasoned about consistently.

The factory picks gemini iff `GOOGLE_API_KEY` is set in the environment AND
`google-generativeai` imports cleanly. Otherwise it falls back to default.
The choice is logged so the operator can confirm what produced the index.

Both backends conform to ChromaDB's `EmbeddingFunction` protocol:
``__call__(input: list[str]) -> list[list[float]]``. That makes them
drop-in for any ChromaDB collection.
"""
from __future__ import annotations

import os
import sys
from typing import Protocol

from chromadb.utils import embedding_functions


class Embedder(Protocol):
    """Minimal protocol for ChromaDB-compatible embedders."""

    def __call__(self, input: list[str]) -> list[list[float]]: ...


class EmbedderFactory:
    """Selects an embedder based on the runtime environment.

    Pure decision logic; no caching. Callers typically construct one and
    pass it to `EpicIntelligenceStore`.
    """

    DEFAULT_GEMINI_MODEL = "models/embedding-001"

    @staticmethod
    def has_gemini_key() -> bool:
        return bool(os.environ.get("GOOGLE_API_KEY"))

    @classmethod
    def make_default(cls) -> tuple[Embedder, str]:
        """ChromaDB's bundled offline embedder. Returns (embedder, name)."""
        ef = embedding_functions.DefaultEmbeddingFunction()
        return ef, "chromadb-default (all-MiniLM-L6-v2)"

    @classmethod
    def make_gemini(cls, model: str | None = None) -> tuple[Embedder, str]:
        """Google Gemini embedder. Requires GOOGLE_API_KEY."""
        if not cls.has_gemini_key():
            raise RuntimeError(
                "GOOGLE_API_KEY not set; cannot build the Gemini embedder.",
            )
        try:
            ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
                api_key=os.environ["GOOGLE_API_KEY"],
                model_name=model or cls.DEFAULT_GEMINI_MODEL,
            )
        except Exception as exc:  # pragma: no cover — env-dependent
            raise RuntimeError(
                f"failed to construct Gemini embedder: {exc}",
            ) from exc
        return ef, f"gemini ({model or cls.DEFAULT_GEMINI_MODEL})"

    @classmethod
    def select(cls, prefer: str = "auto") -> tuple[Embedder, str]:
        """Pick an embedder.

        Args:
            prefer: 'auto' (gemini if key, else default), 'default', or 'gemini'.
        """
        if prefer == "default":
            return cls.make_default()
        if prefer == "gemini":
            return cls.make_gemini()
        if prefer != "auto":
            raise ValueError(f"unknown embedder preference: {prefer!r}")
        if cls.has_gemini_key():
            try:
                return cls.make_gemini()
            except Exception as exc:
                print(
                    f"epic_intelligence: gemini embedder failed ({exc}); "
                    "falling back to default",
                    file=sys.stderr,
                )
        return cls.make_default()


def get_embedder(prefer: str = "auto") -> tuple[Embedder, str]:
    """Convenience wrapper around `EmbedderFactory.select`."""
    return EmbedderFactory.select(prefer=prefer)
