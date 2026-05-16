"""Write helpers for the Memory-First Protocol.

Two write surfaces:

1. Append-only JSONL log on disk (always succeeds, fast, no network):
   ``memory_system/events/log/YYYY-MM-DD.jsonl``. This is the source
   of truth for the protocol; everything else is an index over it.

2. Optional projection into the existing ChromaDB instance (the same
   instance ``save_session.py`` already talks to). Lets the briefing
   layer issue semantic queries.

Both writes are idempotent on event id — re-appending the same Event
to the JSONL is a no-op (line dedupe at append time). The ChromaDB
upsert is naturally idempotent.

The ChromaDB projection is best-effort: if ChromaDB is unreachable,
the JSONL write still succeeds and the projection can be replayed
later via ``rebuild_index()``.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Iterable

from .schema import Event, validate_event

DEFAULT_LOG_DIR = Path(__file__).resolve().parent / "log"
DEFAULT_CHROMA_COLLECTION = "opal_memory_events"


def append_event(event: Event, log_dir: Path | None = None) -> Path:
    """Append one event to the daily JSONL log.

    Returns the path written. Idempotent on event id: if the same id
    already exists in today's file, the write is skipped.
    """
    validate_event(event)
    log_dir = log_dir or DEFAULT_LOG_DIR
    log_dir.mkdir(parents=True, exist_ok=True)
    date = event.timestamp[:10]  # YYYY-MM-DD
    path = log_dir / f"{date}.jsonl"

    if path.exists() and _id_exists_in_file(event.id, path):
        return path

    with path.open("a", encoding="utf-8") as f:
        f.write(event.to_json())
        f.write("\n")
    return path


def _id_exists_in_file(event_id: str, path: Path) -> bool:
    needle = f'"id":"{event_id}"'
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if needle in line:
                return True
    return False


def read_log(log_dir: Path | None = None) -> Iterable[dict]:
    """Yield every event dict from the JSONL log in chronological
    order (by filename, then by append order within a file).
    """
    log_dir = log_dir or DEFAULT_LOG_DIR
    if not log_dir.exists():
        return
    for f in sorted(log_dir.glob("*.jsonl")):
        with f.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except json.JSONDecodeError as exc:
                    print(
                        f"memory_system.events.read_log: skipping "
                        f"malformed line in {f}: {exc}",
                        file=sys.stderr,
                    )


# ---------------------------------------------------------------------------
# Optional ChromaDB projection
# ---------------------------------------------------------------------------


def project_to_chroma(
    event: Event,
    *,
    collection_name: str = DEFAULT_CHROMA_COLLECTION,
    chroma_path: Path | None = None,
) -> bool:
    """Best-effort upsert of one event into ChromaDB.

    Returns True on success, False on any failure (logged to stderr).
    Caller decides whether to retry.
    """
    try:
        import chromadb  # type: ignore
    except ImportError:
        print(
            "memory_system.events: chromadb not installed; "
            "skipping projection",
            file=sys.stderr,
        )
        return False
    path = chroma_path or (
        Path(os.environ.get("OPAL_MEMORY_CHROMA_PATH",
                            ".chroma/opal_memory_events"))
    )
    try:
        path.mkdir(parents=True, exist_ok=True)
        client = chromadb.PersistentClient(path=str(path))
        coll = client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"},
        )
        # Flatten the schema into ChromaDB-safe scalar metadata.
        md = {
            "type": event.type,
            "actor": event.actor,
            "timestamp": event.timestamp,
            "workflow": event.workflow or "",
            "phase": event.phase or "",
            "tags": ",".join(event.tags),
            "title": event.title,
        }
        for k, v in (event.metadata or {}).items():
            # Coerce nested values to strings to satisfy ChromaDB.
            if isinstance(v, (str, int, float, bool)):
                md[f"meta_{k}"] = v
            else:
                md[f"meta_{k}"] = json.dumps(v, sort_keys=True)
        coll.upsert(
            ids=[event.id],
            documents=[f"{event.title}\n\n{event.content}"],
            metadatas=[md],
        )
        return True
    except Exception as exc:
        print(
            f"memory_system.events: chroma projection failed for "
            f"{event.id}: {exc}",
            file=sys.stderr,
        )
        return False


def rebuild_index(
    log_dir: Path | None = None,
    *,
    collection_name: str = DEFAULT_CHROMA_COLLECTION,
    chroma_path: Path | None = None,
) -> tuple[int, int]:
    """Replay every event in the JSONL log into ChromaDB.

    Useful after a ChromaDB outage, schema change, or fresh clone.
    Returns (total_events_seen, successfully_projected).
    """
    from .schema import Event as _Event  # local import; avoid cycles
    seen = 0
    ok = 0
    for d in read_log(log_dir):
        seen += 1
        try:
            ev = _Event(
                id=d["id"],
                timestamp=d["timestamp"],
                type=d["type"],
                actor=d["actor"],
                title=d["title"],
                content=d["content"],
                workflow=d.get("workflow"),
                phase=d.get("phase"),
                tags=tuple(d.get("tags", [])),
                related=tuple(d.get("related", [])),
                metadata=d.get("metadata", {}),
            )
        except (KeyError, TypeError) as exc:
            print(
                f"memory_system.events.rebuild_index: skip malformed "
                f"event: {exc}",
                file=sys.stderr,
            )
            continue
        if project_to_chroma(
            ev, collection_name=collection_name, chroma_path=chroma_path,
        ):
            ok += 1
    return seen, ok
