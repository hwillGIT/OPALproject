"""SQLite store for scopes / members / transitions.

Three tables, idempotent schema (CREATE IF NOT EXISTS), rebuildable
from the typed-events JSONL log (`memory_system/events/log/`).

Default DB path: `.opal-memory/scopes.sqlite` (gitignored).

Why SQLite and not the existing ChromaDB / Neo4j:
- Scopes are structured, low-cardinality, transactional data —
  SQLite is the right fit, not a vector store
- Keeps the scope store independent of ChromaDB and Neo4j outages
- Mirrors RTRevenue's collab-memory pattern where scope metadata
  lives next to FTS5 in the same SQLite file
- Stdlib-only: no new pip dependency
"""
from __future__ import annotations

import json
import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterable, Iterator

from .models import (
    Scope,
    ScopeMember,
    ScopeStatus,
    ScopeTransition,
)

DEFAULT_DB_PATH = Path(
    os.environ.get("OPAL_MEMORY_SCOPES_DB", ".opal-memory/scopes.sqlite"),
)


SCHEMA = """
CREATE TABLE IF NOT EXISTS scopes (
    id              TEXT PRIMARY KEY,
    name            TEXT NOT NULL,
    name_aliases    TEXT NOT NULL DEFAULT '[]',
    status          TEXT NOT NULL CHECK (
                       status IN ('provisional','active','canonical','deprecated')
                    ),
    first_seen      TEXT NOT NULL,
    last_seen       TEXT NOT NULL,
    session_count   INTEGER NOT NULL DEFAULT 0,
    event_count     INTEGER NOT NULL DEFAULT 0,
    promoted_from   TEXT,
    promoted_at     TEXT,
    rollback_id     TEXT,
    metadata        TEXT NOT NULL DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS idx_scopes_status ON scopes(status);
CREATE INDEX IF NOT EXISTS idx_scopes_last_seen ON scopes(last_seen);

CREATE TABLE IF NOT EXISTS scope_members (
    scope_id        TEXT NOT NULL,
    tag             TEXT NOT NULL,
    joined_at       TEXT NOT NULL,
    last_seen       TEXT NOT NULL,
    event_count     INTEGER NOT NULL DEFAULT 0,
    namespaced_form TEXT,
    graduated       INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (scope_id, tag),
    FOREIGN KEY (scope_id) REFERENCES scopes(id)
);
CREATE INDEX IF NOT EXISTS idx_scope_members_tag ON scope_members(tag);

CREATE TABLE IF NOT EXISTS scope_transitions (
    id                  TEXT PRIMARY KEY,
    scope_id            TEXT NOT NULL,
    from_status         TEXT,
    to_status           TEXT NOT NULL,
    timestamp           TEXT NOT NULL,
    reason              TEXT NOT NULL,
    evidence_event_ids  TEXT NOT NULL DEFAULT '[]',
    rollback_id         TEXT,
    actor               TEXT NOT NULL CHECK (
                           actor IN ('autonomous','operator','adversary_rejected')
                        ),
    FOREIGN KEY (scope_id) REFERENCES scopes(id)
);
CREATE INDEX IF NOT EXISTS idx_scope_transitions_scope ON scope_transitions(scope_id);
CREATE INDEX IF NOT EXISTS idx_scope_transitions_ts ON scope_transitions(timestamp);
CREATE INDEX IF NOT EXISTS idx_scope_transitions_rb ON scope_transitions(rollback_id);
"""


def open_db(path: Path | str | None = None) -> sqlite3.Connection:
    """Open (or create) the scopes SQLite file.

    Safe to call repeatedly — schema is CREATE-IF-NOT-EXISTS.
    """
    p = Path(path) if path is not None else DEFAULT_DB_PATH
    p.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(p))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.executescript(SCHEMA)
    return conn


@contextmanager
def connect(path: Path | str | None = None) -> Iterator[sqlite3.Connection]:
    """Context-managed connection. Commits on exit, rollbacks on error."""
    conn = open_db(path)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


# --------------------------------------------------------------------------
# Scope CRUD
# --------------------------------------------------------------------------


def upsert_scope(conn: sqlite3.Connection, scope: Scope) -> None:
    conn.execute("DELETE FROM scopes WHERE id = ?", (scope.id,))
    conn.execute(
        """
        INSERT INTO scopes (
            id, name, name_aliases, status,
            first_seen, last_seen, session_count, event_count,
            promoted_from, promoted_at, rollback_id, metadata
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            scope.id,
            scope.name,
            json.dumps(list(scope.name_aliases)),
            scope.status,
            scope.first_seen,
            scope.last_seen,
            scope.session_count,
            scope.event_count,
            scope.promoted_from,
            scope.promoted_at,
            scope.rollback_id,
            json.dumps(dict(scope.metadata)),
        ),
    )


def _row_to_scope(row) -> Scope:
    return Scope(
        id=row[0],
        name=row[1],
        name_aliases=tuple(json.loads(row[2])),
        status=row[3],
        first_seen=row[4],
        last_seen=row[5],
        session_count=row[6],
        event_count=row[7],
        promoted_from=row[8],
        promoted_at=row[9],
        rollback_id=row[10],
        metadata=json.loads(row[11]),
    )


_SCOPE_COLS = (
    "id, name, name_aliases, status, first_seen, last_seen, "
    "session_count, event_count, promoted_from, promoted_at, "
    "rollback_id, metadata"
)


def get_scope(conn: sqlite3.Connection, scope_id: str) -> Scope | None:
    row = conn.execute(
        f"SELECT {_SCOPE_COLS} FROM scopes WHERE id = ?",
        (scope_id,),
    ).fetchone()
    if not row:
        return None
    scope = _row_to_scope(row)
    members = list_members(conn, scope_id)
    return Scope(**{**scope.to_dict(),
                    "member_tags": tuple(m.tag for m in members)})


def list_scopes(
    conn: sqlite3.Connection,
    statuses: tuple[ScopeStatus, ...] = (),
    limit: int = 500,
) -> list[Scope]:
    """List scopes, optionally filtered by status. Most recently active first."""
    if statuses:
        placeholders = ",".join("?" * len(statuses))
        rows = conn.execute(
            f"SELECT {_SCOPE_COLS} FROM scopes "
            f"WHERE status IN ({placeholders}) "
            f"ORDER BY last_seen DESC LIMIT ?",
            [*statuses, limit],
        ).fetchall()
    else:
        rows = conn.execute(
            f"SELECT {_SCOPE_COLS} FROM scopes ORDER BY last_seen DESC LIMIT ?",
            (limit,),
        ).fetchall()
    out: list[Scope] = []
    for r in rows:
        scope = _row_to_scope(r)
        members = list_members(conn, scope.id)
        out.append(Scope(**{**scope.to_dict(),
                            "member_tags": tuple(m.tag for m in members)}))
    return out


# --------------------------------------------------------------------------
# Member CRUD
# --------------------------------------------------------------------------


def upsert_member(conn: sqlite3.Connection, member: ScopeMember) -> None:
    conn.execute(
        "DELETE FROM scope_members WHERE scope_id = ? AND tag = ?",
        (member.scope_id, member.tag),
    )
    conn.execute(
        """
        INSERT INTO scope_members (
            scope_id, tag, joined_at, last_seen,
            event_count, namespaced_form, graduated
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            member.scope_id, member.tag,
            member.joined_at, member.last_seen,
            member.event_count, member.namespaced_form,
            1 if member.graduated else 0,
        ),
    )


def list_members(conn: sqlite3.Connection, scope_id: str) -> list[ScopeMember]:
    rows = conn.execute(
        "SELECT scope_id, tag, joined_at, last_seen, "
        "event_count, namespaced_form, graduated "
        "FROM scope_members WHERE scope_id = ? ORDER BY joined_at ASC",
        (scope_id,),
    ).fetchall()
    return [
        ScopeMember(
            scope_id=r[0], tag=r[1], joined_at=r[2], last_seen=r[3],
            event_count=r[4], namespaced_form=r[5], graduated=bool(r[6]),
        )
        for r in rows
    ]


def find_scopes_for_tag(conn: sqlite3.Connection, tag: str) -> list[str]:
    """Scope ids that include the given tag."""
    rows = conn.execute(
        "SELECT scope_id FROM scope_members WHERE tag = ?", (tag,),
    ).fetchall()
    return [r[0] for r in rows]


# --------------------------------------------------------------------------
# Transition CRUD
# --------------------------------------------------------------------------


def append_transition(conn: sqlite3.Connection, t: ScopeTransition) -> None:
    conn.execute("DELETE FROM scope_transitions WHERE id = ?", (t.id,))
    conn.execute(
        """
        INSERT INTO scope_transitions (
            id, scope_id, from_status, to_status, timestamp, reason,
            evidence_event_ids, rollback_id, actor
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            t.id, t.scope_id, t.from_status, t.to_status,
            t.timestamp, t.reason,
            json.dumps(list(t.evidence_event_ids)),
            t.rollback_id, t.actor,
        ),
    )


def list_transitions(
    conn: sqlite3.Connection,
    scope_id: str | None = None,
    limit: int = 500,
) -> list[ScopeTransition]:
    cols = ("id, scope_id, from_status, to_status, timestamp, reason, "
            "evidence_event_ids, rollback_id, actor")
    if scope_id:
        rows = conn.execute(
            f"SELECT {cols} FROM scope_transitions WHERE scope_id = ? "
            f"ORDER BY timestamp DESC LIMIT ?",
            (scope_id, limit),
        ).fetchall()
    else:
        rows = conn.execute(
            f"SELECT {cols} FROM scope_transitions "
            f"ORDER BY timestamp DESC LIMIT ?",
            (limit,),
        ).fetchall()
    return [
        ScopeTransition(
            id=r[0], scope_id=r[1], from_status=r[2], to_status=r[3],
            timestamp=r[4], reason=r[5],
            evidence_event_ids=tuple(json.loads(r[6])),
            rollback_id=r[7], actor=r[8],
        )
        for r in rows
    ]


def find_transition_by_rollback(
    conn: sqlite3.Connection, rollback_id: str,
) -> ScopeTransition | None:
    cols = ("id, scope_id, from_status, to_status, timestamp, reason, "
            "evidence_event_ids, rollback_id, actor")
    row = conn.execute(
        f"SELECT {cols} FROM scope_transitions WHERE rollback_id = ?",
        (rollback_id,),
    ).fetchone()
    if not row:
        return None
    return ScopeTransition(
        id=row[0], scope_id=row[1], from_status=row[2], to_status=row[3],
        timestamp=row[4], reason=row[5],
        evidence_event_ids=tuple(json.loads(row[6])),
        rollback_id=row[7], actor=row[8],
    )


# --------------------------------------------------------------------------
# Bulk load (used by rebuild from JSONL)
# --------------------------------------------------------------------------


def index_all(
    conn: sqlite3.Connection,
    scopes: Iterable[Scope] = (),
    members: Iterable[ScopeMember] = (),
    transitions: Iterable[ScopeTransition] = (),
) -> tuple[int, int, int]:
    s_count = m_count = t_count = 0
    for s in scopes:
        upsert_scope(conn, s)
        s_count += 1
    for m in members:
        upsert_member(conn, m)
        m_count += 1
    for t in transitions:
        append_transition(conn, t)
        t_count += 1
    return s_count, m_count, t_count
