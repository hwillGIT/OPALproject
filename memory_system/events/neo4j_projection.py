"""Project typed memory events into Neo4j as a graph.

The JSONL log is the source of truth (`memory_system/events/write.py`).
This module is one of two derived projections — the other is the
ChromaDB upsert in `write.py`. Both are best-effort: a Neo4j outage
never blocks a write to the JSONL log.

Graph schema (kept deliberately small to stay queryable):

    Nodes
        :Event       primary record per typed event
        :Actor       distinct persona / platform identifier
        :Workflow    distinct workflow id
        :Tag         distinct tag value
        :Phase       distinct workflow phase (paired with workflow)

    Relationships
        (Event)-[:BY]->(Actor)
        (Event)-[:IN_WORKFLOW]->(Workflow)
        (Event)-[:IN_PHASE]->(Phase)
        (Event)-[:TAGGED]->(Tag)
        (Event)-[:RELATED_TO]->(Event)    from event.related
        (Event)-[:VERIFIES]->(Event)      OUTCOME -> verifies metadata
        (Event)-[:SUPERSEDES]->(Event)    from metadata.supersedes if set

The Cypher builder is pure (no driver). The Neo4jProjector class
holds the live driver and runs the queries.

Env vars (reuse the pattern from save_session.py):
    NEO4J_URI         default neo4j://127.0.0.1:7687
    NEO4J_USERNAME    default neo4j
    NEO4J_PASSWORD    default architecture123
    NEO4J_DATABASE    default neo4j
"""
from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from typing import Iterable, Sequence


# ---------------------------------------------------------------------------
# Pure Cypher generation
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class CypherStatement:
    """One Cypher statement + its parameter dict."""

    cypher: str
    params: dict


# Constraints / indexes the projection relies on. Created once at
# init; safe to re-run (CREATE IF NOT EXISTS).
SCHEMA_STATEMENTS: tuple[CypherStatement, ...] = (
    CypherStatement(
        "CREATE CONSTRAINT event_id_unique IF NOT EXISTS "
        "FOR (e:Event) REQUIRE e.id IS UNIQUE",
        {},
    ),
    CypherStatement(
        "CREATE CONSTRAINT actor_key_unique IF NOT EXISTS "
        "FOR (a:Actor) REQUIRE a.key IS UNIQUE",
        {},
    ),
    CypherStatement(
        "CREATE CONSTRAINT workflow_id_unique IF NOT EXISTS "
        "FOR (w:Workflow) REQUIRE w.id IS UNIQUE",
        {},
    ),
    CypherStatement(
        "CREATE CONSTRAINT tag_name_unique IF NOT EXISTS "
        "FOR (t:Tag) REQUIRE t.name IS UNIQUE",
        {},
    ),
    CypherStatement(
        "CREATE INDEX event_type_idx IF NOT EXISTS "
        "FOR (e:Event) ON (e.type)",
        {},
    ),
    CypherStatement(
        "CREATE INDEX event_timestamp_idx IF NOT EXISTS "
        "FOR (e:Event) ON (e.timestamp)",
        {},
    ),
)


def build_event_upsert(event: dict) -> list[CypherStatement]:
    """Pure: turn one event dict into the Cypher statements that
    materialize it + its relationships in Neo4j.

    The MERGE pattern makes every statement idempotent on event id.
    Re-running against the same event is a no-op (same data) or an
    update (changed properties). The schema constraints ensure the
    uniqueness invariants.
    """
    eid = event.get("id") or ""
    if not eid:
        return []

    stmts: list[CypherStatement] = []

    # The Event node itself.
    stmts.append(CypherStatement(
        """
        MERGE (e:Event {id: $id})
        SET e.type = $type,
            e.timestamp = $timestamp,
            e.title = $title,
            e.content = $content,
            e.workflow = $workflow,
            e.phase = $phase,
            e.tag_list = $tag_list
        """,
        {
            "id": eid,
            "type": event.get("type", "UNKNOWN"),
            "timestamp": event.get("timestamp", ""),
            "title": event.get("title", ""),
            "content": event.get("content", ""),
            "workflow": event.get("workflow") or "",
            "phase": event.get("phase") or "",
            "tag_list": list(event.get("tags") or ()),
        },
    ))

    # :BY -> Actor
    actor = event.get("actor")
    if actor:
        stmts.append(CypherStatement(
            """
            MATCH (e:Event {id: $id})
            MERGE (a:Actor {key: $actor})
            MERGE (e)-[:BY]->(a)
            """,
            {"id": eid, "actor": actor},
        ))

    # :IN_WORKFLOW -> Workflow
    workflow = event.get("workflow")
    if workflow:
        stmts.append(CypherStatement(
            """
            MATCH (e:Event {id: $id})
            MERGE (w:Workflow {id: $workflow})
            MERGE (e)-[:IN_WORKFLOW]->(w)
            """,
            {"id": eid, "workflow": workflow},
        ))

        # :IN_PHASE -> Phase (only meaningful with a workflow)
        phase = event.get("phase")
        if phase:
            phase_key = f"{workflow}:{phase}"
            stmts.append(CypherStatement(
                """
                MATCH (e:Event {id: $id})
                MERGE (p:Phase {key: $phase_key})
                SET p.workflow = $workflow, p.name = $phase
                MERGE (e)-[:IN_PHASE]->(p)
                """,
                {
                    "id": eid, "phase_key": phase_key,
                    "workflow": workflow, "phase": phase,
                },
            ))

    # :TAGGED -> Tag (one per tag)
    for tag in event.get("tags") or ():
        if not tag:
            continue
        stmts.append(CypherStatement(
            """
            MATCH (e:Event {id: $id})
            MERGE (t:Tag {name: $tag})
            MERGE (e)-[:TAGGED]->(t)
            """,
            {"id": eid, "tag": tag},
        ))

    # :RELATED_TO -> Event (from `related` field)
    for rel_id in event.get("related") or ():
        if not rel_id:
            continue
        stmts.append(CypherStatement(
            """
            MATCH (e:Event {id: $id})
            MERGE (other:Event {id: $other_id})
            MERGE (e)-[:RELATED_TO]->(other)
            """,
            {"id": eid, "other_id": rel_id},
        ))

    # :VERIFIES -> Event (OUTCOME metadata)
    metadata = event.get("metadata") or {}
    verifies = metadata.get("verifies") if isinstance(metadata, dict) else None
    if verifies:
        stmts.append(CypherStatement(
            """
            MATCH (e:Event {id: $id})
            MERGE (other:Event {id: $other_id})
            MERGE (e)-[:VERIFIES]->(other)
            """,
            {"id": eid, "other_id": verifies},
        ))

    # :SUPERSEDES -> Event (generic metadata.supersedes if used)
    supersedes = metadata.get("supersedes") if isinstance(metadata, dict) else None
    if supersedes:
        stmts.append(CypherStatement(
            """
            MATCH (e:Event {id: $id})
            MERGE (other:Event {id: $other_id})
            MERGE (e)-[:SUPERSEDES]->(other)
            """,
            {"id": eid, "other_id": supersedes},
        ))

    return stmts


def build_event_delete(event_id: str) -> CypherStatement:
    """Cypher to remove an event + its outgoing relationships.

    Does not delete connected Actor / Workflow / Tag nodes — they may
    still be referenced by other events. Run a separate cleanup if
    you want to garbage-collect orphans.
    """
    return CypherStatement(
        """
        MATCH (e:Event {id: $id})
        DETACH DELETE e
        """,
        {"id": event_id},
    )


# ---------------------------------------------------------------------------
# Live projector
# ---------------------------------------------------------------------------


@dataclass
class Neo4jConfig:
    uri: str = ""
    username: str = ""
    password: str = ""
    database: str = ""

    @classmethod
    def from_env(cls) -> "Neo4jConfig":
        return cls(
            uri=(
                os.getenv("NEO4J_URI")
                or os.getenv("KNOWLEDGE_GRAPH_URI")
                or "neo4j://127.0.0.1:7687"
            ),
            username=(
                os.getenv("NEO4J_USERNAME")
                or os.getenv("KNOWLEDGE_GRAPH_USERNAME")
                or "neo4j"
            ),
            password=(
                os.getenv("NEO4J_PASSWORD")
                or os.getenv("KNOWLEDGE_GRAPH_PASSWORD")
                or "architecture123"
            ),
            database=(
                os.getenv("NEO4J_DATABASE")
                or os.getenv("KNOWLEDGE_GRAPH_DATABASE")
                or "neo4j"
            ),
        )


class Neo4jUnavailable(RuntimeError):
    """Raised when we can't reach Neo4j AT ALL (driver import fails,
    connection refused, etc.). Distinct from per-event errors which
    just get logged and skipped."""


class Neo4jProjector:
    """Thin wrapper around the neo4j Python driver for our schema.

    Reuses the env-var pattern from `save_session.py`. The driver is
    opened lazily so importing this module never touches the network.

    Best-effort by design: a single bad event logs to stderr and the
    rest of the batch keeps going.
    """

    def __init__(self, config: Neo4jConfig | None = None) -> None:
        self.config = config or Neo4jConfig.from_env()
        self._driver = None
        self._schema_initialized = False

    def _get_driver(self):
        if self._driver is not None:
            return self._driver
        try:
            from neo4j import GraphDatabase  # type: ignore
        except ImportError as exc:
            raise Neo4jUnavailable(
                f"neo4j Python driver not installed: {exc}",
            ) from exc
        try:
            self._driver = GraphDatabase.driver(
                self.config.uri,
                auth=(self.config.username, self.config.password),
            )
        except Exception as exc:  # pragma: no cover — env-dependent
            raise Neo4jUnavailable(
                f"failed to construct Neo4j driver: {exc}",
            ) from exc
        return self._driver

    def _ensure_schema(self) -> None:
        if self._schema_initialized:
            return
        driver = self._get_driver()
        try:
            with driver.session(database=self.config.database) as session:
                for stmt in SCHEMA_STATEMENTS:
                    session.run(stmt.cypher, **stmt.params)
        except Exception as exc:  # pragma: no cover
            raise Neo4jUnavailable(
                f"failed to initialize Neo4j schema: {exc}",
            ) from exc
        self._schema_initialized = True

    def project_event(self, event: dict) -> bool:
        """Upsert one event. Returns True on success, False on failure.

        Failures are logged to stderr; the JSONL log is still safe.
        """
        try:
            self._ensure_schema()
            driver = self._get_driver()
        except Neo4jUnavailable as exc:
            print(
                f"memory_system.events.neo4j_projection: unavailable "
                f"({exc}); skipping projection of {event.get('id')!r}",
                file=sys.stderr,
            )
            return False

        statements = build_event_upsert(event)
        if not statements:
            return False

        try:
            with driver.session(database=self.config.database) as session:
                def _run(tx):
                    for stmt in statements:
                        tx.run(stmt.cypher, **stmt.params)
                session.execute_write(_run)
            return True
        except Exception as exc:
            print(
                f"memory_system.events.neo4j_projection: failed for "
                f"{event.get('id')!r}: {exc}",
                file=sys.stderr,
            )
            return False

    def project_all(self, events: Iterable[dict]) -> tuple[int, int]:
        """Project a stream of events. Returns (seen, succeeded)."""
        seen = ok = 0
        for ev in events:
            seen += 1
            if self.project_event(ev):
                ok += 1
        return seen, ok

    def close(self) -> None:
        if self._driver is not None:
            try:
                self._driver.close()
            except Exception:  # pragma: no cover
                pass
            self._driver = None


# ---------------------------------------------------------------------------
# Convenience entry points (mirrors the ChromaDB shape in write.py)
# ---------------------------------------------------------------------------


def project_to_neo4j(event: dict, *, config: Neo4jConfig | None = None) -> bool:
    """One-shot best-effort projection. Opens + closes its own driver.

    For bulk replay use `Neo4jProjector(config).project_all(events)`
    to amortize the connection.
    """
    projector = Neo4jProjector(config=config)
    try:
        return projector.project_event(event)
    finally:
        projector.close()


def rebuild_neo4j_from_log(
    events: Iterable[dict],
    *,
    config: Neo4jConfig | None = None,
) -> tuple[int, int]:
    """Replay every event in the JSONL log into Neo4j. Returns
    (seen, succeeded). Idempotent per event id via MERGE.
    """
    projector = Neo4jProjector(config=config)
    try:
        return projector.project_all(events)
    finally:
        projector.close()
