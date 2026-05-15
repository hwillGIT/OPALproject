"""ChromaDB-backed store for the Epic Intelligence Layer.

Wraps a `PersistentClient` so the index is a directory on disk — no
ChromaDB server needed (the repo-root `embed_and_store.py` uses an HTTP
client; we deliberately diverge here so this layer is self-contained
and works offline).

Collection name is `epic_intelligence`. Each document is one chunk
produced by `epic_intelligence/ingestion/chunker.py`. The chunk's
`source_url`, `section_path`, `chunk_index`, and entity sets are
preserved as ChromaDB metadata so query results can cite back to the
exact Epic doc page and section that produced them.

Metadata keys (all flat — ChromaDB requires scalar metadata values):
  - source_file: str
  - source_url: str
  - title: str
  - section_path: str (joined " > ")
  - section_title: str
  - section_level: int
  - chunk_index: int
  - total_chunks: int
  - token_estimate: int
  - has_code: bool
  - word_count: int
  - entities_<type>: str (CSV) — one key per entity type detected
"""
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import chromadb

from .embedder import Embedder, get_embedder

DEFAULT_COLLECTION = "epic_intelligence"
DEFAULT_INDEX_DIR = Path(".chroma") / "epic_intelligence"


class ThinClientInstalledError(RuntimeError):
    """Raised when only the http-only `chromadb-client` package is importable.

    The full ``chromadb`` package and the thin ``chromadb-client`` install to
    the *same* import name. When both are installed, whichever was installed
    most recently wins, and `PersistentClient` only works with the full
    package. Suggest the simple fix.
    """

    MESSAGE = (
        "epic_intelligence requires the full `chromadb` package, but the\n"
        "thin `chromadb-client` package is currently shadowing it. Run:\n"
        "    pip uninstall -y chromadb-client chromadb\n"
        "    pip install chromadb\n"
        "and re-run the pipeline."
    )

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


def _detect_thin_client() -> bool:
    """Return True iff the installed `chromadb` is the http-only thin variant."""
    try:
        from chromadb import config as _cfg  # type: ignore
    except Exception:
        return False
    return bool(getattr(_cfg, "is_thin_client", False))


@dataclass(frozen=True)
class QueryHit:
    """One result from a similarity query, with everything needed to cite."""

    chunk_id: str
    score: float  # cosine distance (lower = closer); ChromaDB convention
    title: str
    source_url: str
    section_path: tuple[str, ...]
    snippet: str
    metadata: dict[str, object]


def _flatten_chunk_metadata(chunk_dict: dict) -> dict[str, object]:
    """Convert a Chunk's nested metadata into ChromaDB-safe scalars."""
    md = {
        "source_file": chunk_dict.get("source_file", ""),
        "source_url": chunk_dict.get("source_url", ""),
        "title": chunk_dict.get("title", ""),
        "section_path": " > ".join(chunk_dict.get("section_path", []) or []),
        "chunk_index": chunk_dict.get("chunk_index", 0),
        "total_chunks": chunk_dict.get("total_chunks", 0),
        "token_estimate": chunk_dict.get("token_estimate", 0),
    }
    inner = chunk_dict.get("metadata", {}) or {}
    md["section_title"] = inner.get("section_title", "")
    md["section_level"] = int(inner.get("section_level", 0) or 0)
    md["has_code"] = bool(inner.get("has_code", False))
    md["word_count"] = int(inner.get("word_count", 0) or 0)
    for ent_type, values in (inner.get("entities") or {}).items():
        if isinstance(values, list) and values:
            md[f"entities_{ent_type}"] = ",".join(sorted(set(map(str, values))))
    return md


class EpicIntelligenceStore:
    """Thin wrapper around a ChromaDB collection for chunked Epic docs.

    Uses cosine distance. `get_or_create_collection` is idempotent — repeat
    runs of the ingestion pipeline upsert chunks (Chunk.id is deterministic
    from source filename + chunk_index, so an unchanged document re-ingests
    to the same row).
    """

    def __init__(
        self,
        embedder: Embedder | None = None,
        embedder_name: str = "",
        index_dir: Path = DEFAULT_INDEX_DIR,
        collection_name: str = DEFAULT_COLLECTION,
    ) -> None:
        if embedder is None:
            embedder, embedder_name = get_embedder()
        self.embedder = embedder
        self.embedder_name = embedder_name or "unknown"
        self.index_dir = Path(index_dir)
        self.collection_name = collection_name
        self.index_dir.mkdir(parents=True, exist_ok=True)
        if _detect_thin_client():
            raise ThinClientInstalledError()
        self._client = chromadb.PersistentClient(path=str(self.index_dir))
        self._collection = self._client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedder,
            metadata={"hnsw:space": "cosine"},
        )

    @property
    def collection(self):  # noqa: D401 — exposing the raw handle is useful in tests
        return self._collection

    def count(self) -> int:
        return self._collection.count()

    def upsert_chunks(self, chunks: Sequence[dict]) -> int:
        """Upsert a batch of chunks (each as a `Chunk.to_dict()` payload).

        Returns the number of chunks written.
        """
        if not chunks:
            return 0
        ids: list[str] = []
        documents: list[str] = []
        metadatas: list[dict[str, object]] = []
        for c in chunks:
            chunk_id = c.get("id")
            content = c.get("content")
            if not chunk_id or not content:
                print(
                    f"epic_intelligence.store: skipping malformed chunk "
                    f"(id={chunk_id!r})",
                    file=sys.stderr,
                )
                continue
            ids.append(chunk_id)
            documents.append(content)
            metadatas.append(_flatten_chunk_metadata(c))
        if not ids:
            return 0
        self._collection.upsert(ids=ids, documents=documents, metadatas=metadatas)
        return len(ids)

    def query(self, text: str, n_results: int = 5) -> list[QueryHit]:
        """Run a similarity query, return citation-ready hits."""
        if not text.strip():
            return []
        result = self._collection.query(query_texts=[text], n_results=n_results)
        ids = (result.get("ids") or [[]])[0]
        docs = (result.get("documents") or [[]])[0]
        mds = (result.get("metadatas") or [[]])[0]
        dists = (result.get("distances") or [[]])[0]

        hits: list[QueryHit] = []
        for i, chunk_id in enumerate(ids):
            md = mds[i] if i < len(mds) else {}
            doc = docs[i] if i < len(docs) else ""
            score = float(dists[i]) if i < len(dists) else 0.0
            section_path = tuple(
                s for s in str(md.get("section_path", "")).split(" > ") if s
            )
            snippet = _make_snippet(doc, max_chars=400)
            hits.append(
                QueryHit(
                    chunk_id=chunk_id,
                    score=score,
                    title=str(md.get("title", "")),
                    source_url=str(md.get("source_url", "")),
                    section_path=section_path,
                    snippet=snippet,
                    metadata=dict(md),
                )
            )
        return hits

    def reset(self) -> None:
        """Drop and recreate the collection — for clean re-ingestion."""
        self._client.delete_collection(self.collection_name)
        self._collection = self._client.get_or_create_collection(
            name=self.collection_name,
            embedding_function=self.embedder,
            metadata={"hnsw:space": "cosine"},
        )


def _make_snippet(text: str, max_chars: int) -> str:
    """First N chars of the chunk, with a trailing ellipsis if truncated."""
    text = text.strip().replace("\r\n", "\n")
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars]
    last_space = cut.rfind(" ")
    if last_space > max_chars * 0.6:
        cut = cut[:last_space]
    return cut.rstrip() + "..."
