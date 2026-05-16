"""Tests for the Neo4j projection.

Pure Cypher generation tests run anywhere (no DB). The live
integration test is auto-skipped when Neo4j is unreachable —
mirroring the ChromaDB pattern in `test_pipeline_integration.py`.
"""
from __future__ import annotations

import os
from contextlib import suppress
from typing import Any

import pytest

from memory_system.events.neo4j_projection import (
    Neo4jConfig,
    Neo4jProjector,
    Neo4jUnavailable,
    SCHEMA_STATEMENTS,
    build_event_delete,
    build_event_upsert,
)


def _ev(
    eid: str = "evt-aaaaaaaaaaaa",
    type: str = "INSIGHT",
    actor: str = "strategist",
    workflow: str | None = None,
    phase: str | None = None,
    tags: tuple = (),
    related: tuple = (),
    metadata: dict | None = None,
) -> dict:
    return {
        "id": eid,
        "timestamp": "2026-05-16T10:00:00+00:00",
        "type": type,
        "actor": actor,
        "title": f"title for {eid}",
        "content": "content body",
        "workflow": workflow,
        "phase": phase,
        "tags": list(tags),
        "related": list(related),
        "metadata": metadata or {},
    }


# --------------------------------------------------------------------------
# build_event_upsert — pure Cypher builder
# --------------------------------------------------------------------------


class TestBuildEventUpsertMinimal:
    def test_event_node_always_emitted(self) -> None:
        stmts = build_event_upsert(_ev())
        assert any("MERGE (e:Event {id: $id})" in s.cypher for s in stmts)
        # First stmt = event upsert; check its params shape.
        head = stmts[0]
        assert head.params["id"] == "evt-aaaaaaaaaaaa"
        assert head.params["type"] == "INSIGHT"

    def test_actor_emits_BY_relationship(self) -> None:
        stmts = build_event_upsert(_ev(actor="hardware-lead"))
        actor_stmts = [s for s in stmts if "Actor" in s.cypher]
        assert len(actor_stmts) == 1
        assert "[:BY]" in actor_stmts[0].cypher
        assert actor_stmts[0].params["actor"] == "hardware-lead"

    def test_missing_id_returns_empty(self) -> None:
        assert build_event_upsert({}) == []
        assert build_event_upsert({"id": ""}) == []


class TestBuildEventUpsertWorkflow:
    def test_workflow_emits_IN_WORKFLOW(self) -> None:
        stmts = build_event_upsert(
            _ev(workflow="clinical-decision-loop"),
        )
        wf = [s for s in stmts if "Workflow" in s.cypher]
        assert len(wf) == 1
        assert "[:IN_WORKFLOW]" in wf[0].cypher

    def test_phase_requires_workflow_to_emit(self) -> None:
        # Phase without workflow should be skipped to avoid orphans.
        stmts = build_event_upsert(_ev(phase="bedside-reality"))
        assert not any("Phase" in s.cypher for s in stmts)

    def test_workflow_plus_phase_emits_both(self) -> None:
        stmts = build_event_upsert(_ev(
            workflow="clinical-decision-loop",
            phase="bedside-reality",
        ))
        kinds = [s.cypher for s in stmts]
        assert any("[:IN_WORKFLOW]" in c for c in kinds)
        phase_stmts = [s for s in stmts if "Phase" in s.cypher]
        assert len(phase_stmts) == 1
        assert phase_stmts[0].params["phase_key"] == (
            "clinical-decision-loop:bedside-reality"
        )


class TestBuildEventUpsertTags:
    def test_emits_one_relationship_per_tag(self) -> None:
        stmts = build_event_upsert(_ev(tags=("aurora", "pitch", "strategy")))
        tag_stmts = [s for s in stmts if "Tag" in s.cypher]
        assert len(tag_stmts) == 3
        assert {s.params["tag"] for s in tag_stmts} == {
            "aurora", "pitch", "strategy",
        }

    def test_empty_tags_skipped(self) -> None:
        stmts = build_event_upsert(_ev(tags=("", "real-tag", None)))  # type: ignore
        tag_stmts = [s for s in stmts if "Tag" in s.cypher]
        assert len(tag_stmts) == 1
        assert tag_stmts[0].params["tag"] == "real-tag"


class TestBuildEventUpsertRelationships:
    def test_related_emits_RELATED_TO(self) -> None:
        stmts = build_event_upsert(
            _ev(related=("evt-bbbbbbbbbbbb", "evt-cccccccccccc")),
        )
        rel_stmts = [s for s in stmts if "[:RELATED_TO]" in s.cypher]
        assert len(rel_stmts) == 2
        targets = {s.params["other_id"] for s in rel_stmts}
        assert targets == {"evt-bbbbbbbbbbbb", "evt-cccccccccccc"}

    def test_outcome_verifies_emits_VERIFIES(self) -> None:
        stmts = build_event_upsert(_ev(
            type="OUTCOME",
            metadata={"verifies": "evt-bbbbbbbbbbbb"},
        ))
        ver_stmts = [s for s in stmts if "[:VERIFIES]" in s.cypher]
        assert len(ver_stmts) == 1
        assert ver_stmts[0].params["other_id"] == "evt-bbbbbbbbbbbb"

    def test_metadata_supersedes_emits_SUPERSEDES(self) -> None:
        stmts = build_event_upsert(_ev(
            type="DECISION",
            metadata={"supersedes": "evt-bbbbbbbbbbbb"},
        ))
        sup_stmts = [s for s in stmts if "[:SUPERSEDES]" in s.cypher]
        assert len(sup_stmts) == 1


class TestBuildEventDelete:
    def test_delete_uses_detach(self) -> None:
        stmt = build_event_delete("evt-aaaaaaaaaaaa")
        assert "DETACH DELETE" in stmt.cypher
        assert stmt.params == {"id": "evt-aaaaaaaaaaaa"}


# --------------------------------------------------------------------------
# Schema
# --------------------------------------------------------------------------


class TestSchema:
    def test_schema_contains_unique_constraints(self) -> None:
        joined = " ".join(s.cypher for s in SCHEMA_STATEMENTS)
        assert "event_id_unique" in joined
        assert "actor_key_unique" in joined
        assert "workflow_id_unique" in joined
        assert "tag_name_unique" in joined

    def test_schema_idempotent(self) -> None:
        # Every statement uses IF NOT EXISTS so it's safe to re-run.
        for s in SCHEMA_STATEMENTS:
            assert "IF NOT EXISTS" in s.cypher


# --------------------------------------------------------------------------
# Live integration test (skipped when Neo4j unreachable)
# --------------------------------------------------------------------------


def _neo4j_reachable() -> bool:
    try:
        from neo4j import GraphDatabase  # type: ignore
    except ImportError:
        return False
    cfg = Neo4jConfig.from_env()
    try:
        driver = GraphDatabase.driver(
            cfg.uri, auth=(cfg.username, cfg.password),
        )
    except Exception:
        return False
    try:
        with driver.session(database=cfg.database) as session:
            session.run("RETURN 1").consume()
        return True
    except Exception:
        return False
    finally:
        with suppress(Exception):
            driver.close()


_NEO4J_SKIP_REASON = (
    "Neo4j not reachable (set NEO4J_URI / NEO4J_USERNAME / "
    "NEO4J_PASSWORD to enable). All pure-Cypher tests above "
    "still run; only the integration test below is gated."
)


@pytest.fixture
def projector():
    p = Neo4jProjector()
    yield p
    p.close()


@pytest.mark.skipif(not _neo4j_reachable(), reason=_NEO4J_SKIP_REASON)
class TestProjectorIntegration:
    def test_round_trip_event(self, projector: Neo4jProjector) -> None:
        ev = _ev(
            eid="evt-test12345678",
            workflow="clinical-decision-loop",
            phase="synthesis",
            tags=("aurora", "test-roundtrip"),
        )
        ok = projector.project_event(ev)
        assert ok is True

        # Query back via raw driver to confirm the node exists with
        # the expected relationships.
        driver = projector._get_driver()
        with driver.session(database=projector.config.database) as session:
            row = session.run(
                """
                MATCH (e:Event {id: $id})-[:BY]->(a:Actor)
                MATCH (e)-[:IN_WORKFLOW]->(w:Workflow)
                MATCH (e)-[:IN_PHASE]->(p:Phase)
                RETURN a.key AS actor, w.id AS workflow, p.name AS phase
                """,
                id="evt-test12345678",
            ).single()
            assert row is not None
            assert row["actor"] == "strategist"
            assert row["workflow"] == "clinical-decision-loop"
            assert row["phase"] == "synthesis"

            tags = session.run(
                """
                MATCH (e:Event {id: $id})-[:TAGGED]->(t:Tag)
                RETURN collect(t.name) AS tags
                """,
                id="evt-test12345678",
            ).single()
            assert set(tags["tags"]) == {"aurora", "test-roundtrip"}

            # Cleanup so repeat runs stay tidy.
            session.run(
                "MATCH (e:Event {id: $id}) DETACH DELETE e",
                id="evt-test12345678",
            )
