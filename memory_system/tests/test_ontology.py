"""Unit tests for the SKOS-like ontology loader + predicate engine."""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from memory_system.ontology import (
    Concept,
    Taxonomy,
    all_tags,
    evaluate_predicate,
    expand_tag,
    load_predicates,
    load_taxonomy,
    parent_of,
)
from memory_system.ontology.predicates import (
    MatchFilter,
    Predicate,
    WindowConfig,
    evaluate_trigger,
)


# --------------------------------------------------------------------------
# taxonomy loader
# --------------------------------------------------------------------------


SAMPLE_TAXONOMY = {
    "concepts": {
        "clinical": {
            "prefLabel": "Clinical",
            "altLabel": ["bedside"],
            "broader": [],
            "narrower": ["clinical-workflow"],
        },
        "clinical-workflow": {
            "prefLabel": "Clinical Workflow",
            "altLabel": ["workflow"],
            "broader": ["clinical"],
            "narrower": [],
        },
        "regulatory": {
            "prefLabel": "Regulatory",
            "altLabel": [],
            "broader": [],
            "narrower": ["fda"],
        },
        "fda": {
            "prefLabel": "FDA",
            "altLabel": ["510k"],
            "broader": ["regulatory"],
            "narrower": [],
        },
    },
}


class TestLoadTaxonomy:
    def test_load_from_file(self, tmp_path: Path) -> None:
        p = tmp_path / "tax.json"
        p.write_text(json.dumps(SAMPLE_TAXONOMY))
        tx = load_taxonomy(p)
        assert isinstance(tx, Taxonomy)
        assert "clinical" in tx.concepts
        assert tx.concepts["clinical"].pref_label == "Clinical"
        assert tx.concepts["fda"].broader == ("regulatory",)

    def test_all_tags(self, tmp_path: Path) -> None:
        p = tmp_path / "tax.json"
        p.write_text(json.dumps(SAMPLE_TAXONOMY))
        tx = load_taxonomy(p)
        tags = all_tags(tx)
        assert "clinical" in tags
        assert "Clinical" in tags
        assert "bedside" in tags
        assert "510k" in tags


class TestExpand:
    def test_parent_of_key(self, tmp_path: Path) -> None:
        p = tmp_path / "tax.json"
        p.write_text(json.dumps(SAMPLE_TAXONOMY))
        tx = load_taxonomy(p)
        assert parent_of(tx, "clinical-workflow") == {"clinical"}

    def test_parent_of_alt_label(self, tmp_path: Path) -> None:
        # 'workflow' is an altLabel of 'clinical-workflow'
        p = tmp_path / "tax.json"
        p.write_text(json.dumps(SAMPLE_TAXONOMY))
        tx = load_taxonomy(p)
        assert parent_of(tx, "workflow") == {"clinical"}

    def test_expand_broader_depth_1(self, tmp_path: Path) -> None:
        p = tmp_path / "tax.json"
        p.write_text(json.dumps(SAMPLE_TAXONOMY))
        tx = load_taxonomy(p)
        result = expand_tag(tx, "fda", depth=1, direction="broader")
        assert result == {"fda", "regulatory"}

    def test_expand_narrower_depth_1(self, tmp_path: Path) -> None:
        p = tmp_path / "tax.json"
        p.write_text(json.dumps(SAMPLE_TAXONOMY))
        tx = load_taxonomy(p)
        result = expand_tag(tx, "regulatory", depth=1, direction="narrower")
        assert "regulatory" in result
        assert "fda" in result


# --------------------------------------------------------------------------
# bundled OPAL taxonomy + predicates load
# --------------------------------------------------------------------------


def test_bundled_taxonomy_loads() -> None:
    here = Path(__file__).resolve().parent.parent
    tx = load_taxonomy(here / "ontology" / "taxonomy.json")
    assert "clinical" in tx.concepts
    assert "fda" in tx.concepts
    assert "fundraising" in tx.concepts


def test_bundled_predicates_load() -> None:
    here = Path(__file__).resolve().parent.parent
    preds = load_predicates(here / "ontology" / "predicates.json")
    assert len(preds) >= 1
    assert any(p.id == "open-actions" for p in preds)


# --------------------------------------------------------------------------
# predicate evaluation
# --------------------------------------------------------------------------


def _utc(day: int = 16, hour: int = 12) -> str:
    return datetime(2026, 5, day, hour, tzinfo=timezone.utc).isoformat()


def _event(eid: str, **overrides):
    base = {
        "id": eid, "timestamp": _utc(),
        "type": "INSIGHT", "actor": "strategist",
        "title": "t", "content": "c",
        "tags": [], "metadata": {},
    }
    base.update(overrides)
    return base


class TestEvaluatePredicate:
    def test_type_match(self) -> None:
        p = Predicate(
            id="x", trigger="session_start",
            match=MatchFilter(types=("DECISION",)),
            window=WindowConfig(max_events=10),
        )
        events = [
            _event("evt-a", type="DECISION"),
            _event("evt-b", type="INSIGHT"),
        ]
        out = evaluate_predicate(p, events)
        assert {e["id"] for e in out} == {"evt-a"}

    def test_filter_metadata(self) -> None:
        p = Predicate(
            id="open-actions", trigger="session_start",
            match=MatchFilter(types=("ACTION",)),
            filter_metadata={"status": ("open", "in-progress")},
        )
        events = [
            _event("evt-a", type="ACTION", metadata={"status": "open"}),
            _event("evt-b", type="ACTION", metadata={"status": "completed"}),
            _event("evt-c", type="ACTION", metadata={"status": "in-progress"}),
        ]
        out = evaluate_predicate(p, events)
        assert {e["id"] for e in out} == {"evt-a", "evt-c"}

    def test_tags_any(self) -> None:
        p = Predicate(
            id="x", trigger="session_start",
            match=MatchFilter(tags_any=("aurora", "pitch")),
        )
        events = [
            _event("evt-a", tags=["aurora"]),
            _event("evt-b", tags=["unrelated"]),
            _event("evt-c", tags=["pitch", "x"]),
        ]
        out = evaluate_predicate(p, events)
        assert {e["id"] for e in out} == {"evt-a", "evt-c"}


class TestEvaluateTrigger:
    def test_groups_by_predicate_id(self) -> None:
        p1 = Predicate(
            id="a", trigger="session_start",
            match=MatchFilter(types=("DECISION",)),
        )
        p2 = Predicate(
            id="b", trigger="session_start",
            match=MatchFilter(types=("INSIGHT",)),
        )
        p3 = Predicate(
            id="c", trigger="pre_query",
            match=MatchFilter(types=("DECISION",)),
        )
        events = [
            _event("evt-a", type="DECISION"),
            _event("evt-b", type="INSIGHT"),
        ]
        out = evaluate_trigger([p1, p2, p3], "session_start", events)
        assert set(out.keys()) == {"a", "b"}
        assert {e["id"] for e in out["a"]} == {"evt-a"}
        assert {e["id"] for e in out["b"]} == {"evt-b"}
