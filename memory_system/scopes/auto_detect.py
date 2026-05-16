"""Auto-detect scopes on every accepted event.

Bridges the typed-events write path (``memory_system/events/write.py``)
into the scope subsystem. Called as a hook from the events CLI / API
AFTER a successful JSONL append.

Best-effort by design:
  - If the scopes DB or ontology can't be opened, the function logs to
    stderr and returns an empty list. The event itself still landed in
    the JSONL log; the source-of-truth invariant is preserved.
  - Detection is idempotent on scope id (deterministic from name +
    first_seen month), so re-running this for the same event is a no-op.
"""
from __future__ import annotations

import sys
from collections.abc import Iterable
from pathlib import Path

from ..ontology.loader import all_tags as ontology_tags
from ..ontology.loader import load_taxonomy
from .detect import (
    BurstDetectionConfig,
    ScopeMaterialization,
    detect,
    materialize,
)
from .store import (
    DEFAULT_DB_PATH,
    append_transition,
    list_scopes,
    open_db,
    upsert_member,
    upsert_scope,
)


DEFAULT_TAXONOMY_PATH = Path(__file__).resolve().parent.parent / "ontology" / "taxonomy.json"


def autodetect_for_event(
    event: dict,
    *,
    recent_events: Iterable[dict] = (),
    db_path: Path | None = None,
    taxonomy_path: Path | None = None,
    config: BurstDetectionConfig | None = None,
) -> list[ScopeMaterialization]:
    """Run burst detection for one freshly-appended event and persist.

    Args:
        event: the dict form of the freshly-appended Event.
        recent_events: prior events for window-burst context. Caller
                       passes whatever is cheaply available (e.g. the
                       last 24h from the JSONL log).
        db_path: scopes SQLite path. Defaults to DEFAULT_DB_PATH.
        taxonomy_path: ontology JSON path. Defaults to the bundled file.
        config: burst-detection config. Defaults to ADR-001 values.

    Returns the materializations that were persisted (could be empty).
    """
    cfg = config or BurstDetectionConfig()
    if not cfg.enabled:
        return []

    canonical: set[str] = set()
    try:
        tx = load_taxonomy(taxonomy_path or DEFAULT_TAXONOMY_PATH)
        canonical = ontology_tags(tx)
    except Exception as exc:
        print(
            f"memory_system.scopes.auto_detect: taxonomy unavailable "
            f"({exc}); treating all tags as provisional",
            file=sys.stderr,
        )

    known_member_tags: set[str] = set()
    try:
        conn = open_db(db_path)
        for s in list_scopes(conn):
            known_member_tags.update(s.member_tags)
    except Exception as exc:
        print(
            f"memory_system.scopes.auto_detect: scopes DB unavailable "
            f"({exc}); cannot persist new scopes",
            file=sys.stderr,
        )
        return []

    known_tags = canonical | known_member_tags

    try:
        candidates = detect(event, list(recent_events), known_tags, cfg)
    except Exception as exc:
        print(
            f"memory_system.scopes.auto_detect: detect() raised ({exc}); "
            "skipping",
            file=sys.stderr,
        )
        conn.close()
        return []

    persisted: list[ScopeMaterialization] = []
    try:
        for cand in candidates:
            mat = materialize(cand)
            upsert_scope(conn, mat.scope)
            for member in mat.members:
                upsert_member(conn, member)
            append_transition(conn, mat.transition)
            persisted.append(mat)
        if persisted:
            conn.commit()
    finally:
        conn.close()
    return persisted
