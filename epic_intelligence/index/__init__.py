"""Vector index: pluggable embedder + ChromaDB store."""

from .embedder import EmbedderFactory, get_embedder
from .store import EpicIntelligenceStore

__all__ = ["EmbedderFactory", "EpicIntelligenceStore", "get_embedder"]
