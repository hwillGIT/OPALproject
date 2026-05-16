"""Tests for the Memory-First Protocol event layer.

No network, no ChromaDB, no Neo4j required. Schema + JSONL write +
briefing summarization only.
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from memory_system.events import (
    EVENT_TYPES,
    Event,
    EventValidationError,
    new_event,
    validate_event,
)
from memory_system.events.briefing import (
    BriefingSummary,
    render_briefing,
    summarize_log,
)
from memory_system.events.write import append_event, read_log


# --------------------------------------------------------------------------
# Schema
# --------------------------------------------------------------------------


class TestEventConstruction:
    def test_minimal_happy_path(self) -> None:
        ev = new_event(
            type="INSIGHT",
            actor="strategist",
            title="Platform thesis resonates with healthcare buyers",
            content="Three of four CMO conversations validated the framing.",
        )
        assert ev.id.startswith("evt-")
        assert len(ev.id) == 16
        assert ev.timestamp
        assert ev.type == "INSIGHT"
        assert ev.actor == "strategist"
        assert ev.workflow is None
        assert ev.phase is None
        assert ev.tags == ()

    def test_tags_are_sorted_and_deduped(self) -> None:
        ev = new_event(
            type="INSIGHT", actor="strategist",
            title="t", content="c",
            tags=["pitch", "strategy", "pitch", ""],
        )
        assert ev.tags == ("pitch", "strategy")

    def test_explicit_id_and_timestamp_preserved(self) -> None:
        ts = "2026-05-15T12:00:00+00:00"
        ev = new_event(
            id="evt-abcdef012345",
            timestamp=ts,
            type="DECISION", actor="product-owner",
            title="t", content="c",
        )
        assert ev.id == "evt-abcdef012345"
        assert ev.timestamp == ts


class TestSchemaValidation:
    def _base(self, **overrides) -> dict:
        d = dict(
            id="evt-aaaaaaaaaaaa",
            timestamp="2026-05-15T12:00:00+00:00",
            type="INSIGHT",
            actor="strategist",
            title="t",
            content="c",
        )
        d.update(overrides)
        return d

    def test_bad_id_rejected(self) -> None:
        ev = Event(**self._base(id="not-an-evt-id"))
        with pytest.raises(EventValidationError, match="id"):
            validate_event(ev)

    def test_bad_type_rejected(self) -> None:
        ev = Event(**self._base(type="SOMETHING_ELSE"))
        with pytest.raises(EventValidationError, match="type"):
            validate_event(ev)

    def test_bad_actor_rejected(self) -> None:
        ev = Event(**self._base(actor="Bad Actor"))  # space + caps
        with pytest.raises(EventValidationError, match="actor"):
            validate_event(ev)

    def test_empty_title_rejected(self) -> None:
        ev = Event(**self._base(title=""))
        with pytest.raises(EventValidationError, match="title"):
            validate_event(ev)

    def test_oversize_title_rejected(self) -> None:
        ev = Event(**self._base(title="x" * 201))
        with pytest.raises(EventValidationError, match="title"):
            validate_event(ev)

    def test_bad_timestamp_rejected(self) -> None:
        ev = Event(**self._base(timestamp="last tuesday"))
        with pytest.raises(EventValidationError, match="timestamp"):
            validate_event(ev)

    def test_bad_related_id_rejected(self) -> None:
        ev = Event(**self._base(related=("not-an-id",)))
        with pytest.raises(EventValidationError, match="related"):
            validate_event(ev)

    def test_all_event_types_accepted(self) -> None:
        """Smoke: every type in EVENT_TYPES should validate when
        accompanied by its required metadata."""
        for t in EVENT_TYPES:
            meta = _required_metadata_for(t)
            kwargs = dict(
                type=t, actor="strategist",
                title=f"t for {t}", content="c",
            )
            if t == "OUTCOME":
                kwargs["related"] = ("evt-abcdef012345",)
            kwargs["metadata"] = meta
            ev = new_event(**kwargs)
            assert ev.type == t


def _required_metadata_for(t: str) -> dict:
    if t == "PREDICTION":
        return {"confidence": 0.7, "horizon": "2026-12-31T00:00:00+00:00"}
    if t == "ACTION":
        return {"status": "open", "owner": "hardware-lead"}
    if t == "OUTCOME":
        return {"verifies": "evt-abcdef012345"}
    return {}


class TestTypeSpecificMetadata:
    def test_prediction_requires_confidence(self) -> None:
        with pytest.raises(EventValidationError, match="confidence"):
            new_event(
                type="PREDICTION", actor="strategist",
                title="t", content="c",
                metadata={"horizon": "2026-12-31T00:00:00+00:00"},
            )

    def test_prediction_confidence_must_be_in_range(self) -> None:
        with pytest.raises(EventValidationError, match="confidence"):
            new_event(
                type="PREDICTION", actor="strategist",
                title="t", content="c",
                metadata={"confidence": 1.5},
            )
        with pytest.raises(EventValidationError, match="confidence"):
            new_event(
                type="PREDICTION", actor="strategist",
                title="t", content="c",
                metadata={"confidence": -0.1},
            )

    def test_action_requires_valid_status(self) -> None:
        with pytest.raises(EventValidationError, match="status"):
            new_event(
                type="ACTION", actor="product-owner",
                title="t", content="c",
                metadata={"status": "todo"},  # not in vocabulary
            )

    def test_outcome_requires_verifies_or_related(self) -> None:
        with pytest.raises(EventValidationError, match="verifies"):
            new_event(
                type="OUTCOME", actor="reliability-engineer",
                title="t", content="c",
            )

    def test_outcome_with_related_passes(self) -> None:
        ev = new_event(
            type="OUTCOME", actor="reliability-engineer",
            title="t", content="c",
            related=["evt-abcdef012345"],
        )
        assert ev.related == ("evt-abcdef012345",)


# --------------------------------------------------------------------------
# JSONL append
# --------------------------------------------------------------------------


class TestAppendEvent:
    def test_writes_to_dated_file(self, tmp_path: Path) -> None:
        ev = new_event(
            type="INSIGHT", actor="strategist",
            title="t", content="c",
            timestamp="2026-05-15T12:00:00+00:00",
        )
        path = append_event(ev, log_dir=tmp_path)
        assert path.name == "2026-05-15.jsonl"
        assert path.exists()
        line = path.read_text(encoding="utf-8").strip()
        parsed = json.loads(line)
        assert parsed["id"] == ev.id

    def test_idempotent_on_id(self, tmp_path: Path) -> None:
        ev = new_event(
            type="INSIGHT", actor="strategist",
            title="t", content="c",
            timestamp="2026-05-15T12:00:00+00:00",
        )
        append_event(ev, log_dir=tmp_path)
        append_event(ev, log_dir=tmp_path)  # second write should no-op
        path = tmp_path / "2026-05-15.jsonl"
        assert len(path.read_text(encoding="utf-8").strip().split("\n")) == 1

    def test_different_ids_both_written(self, tmp_path: Path) -> None:
        ev1 = new_event(
            type="INSIGHT", actor="strategist",
            title="a", content="c",
            timestamp="2026-05-15T12:00:00+00:00",
        )
        ev2 = new_event(
            type="INSIGHT", actor="strategist",
            title="b", content="c",
            timestamp="2026-05-15T12:00:00+00:00",
        )
        append_event(ev1, log_dir=tmp_path)
        append_event(ev2, log_dir=tmp_path)
        path = tmp_path / "2026-05-15.jsonl"
        assert len(path.read_text(encoding="utf-8").strip().split("\n")) == 2

    def test_read_log_yields_in_order(self, tmp_path: Path) -> None:
        ev1 = new_event(
            type="INSIGHT", actor="strategist",
            title="first", content="c",
            timestamp="2026-05-14T12:00:00+00:00",
        )
        ev2 = new_event(
            type="INSIGHT", actor="strategist",
            title="second", content="c",
            timestamp="2026-05-15T12:00:00+00:00",
        )
        append_event(ev2, log_dir=tmp_path)
        append_event(ev1, log_dir=tmp_path)
        titles = [d["title"] for d in read_log(tmp_path)]
        assert titles == ["first", "second"]  # files sorted by name


# --------------------------------------------------------------------------
# Briefing
# --------------------------------------------------------------------------


def _utc(year, month, day, hour=12) -> datetime:
    return datetime(year, month, day, hour, tzinfo=timezone.utc)


def _event_dict(**overrides) -> dict:
    base = {
        "id": "evt-" + ("a" * 12),
        "timestamp": "2026-05-15T12:00:00+00:00",
        "type": "INSIGHT",
        "actor": "strategist",
        "title": "default",
        "content": "c",
        "workflow": None,
        "phase": None,
        "tags": [],
        "related": [],
        "metadata": {},
    }
    base.update(overrides)
    return base


class TestSummarizeLog:
    def test_empty_log(self) -> None:
        s = summarize_log([], now=_utc(2026, 5, 15))
        assert s.total_events == 0
        assert s.open_actions == []
        assert s.overdue_predictions == []

    def test_in_window_events_counted_by_type(self) -> None:
        now = _utc(2026, 5, 15)
        events = [
            _event_dict(id="evt-aaaaaaaaaaaa", type="DECISION",
                        timestamp="2026-05-14T12:00:00+00:00"),
            _event_dict(id="evt-bbbbbbbbbbbb", type="INSIGHT",
                        timestamp="2026-05-13T12:00:00+00:00"),
            _event_dict(id="evt-cccccccccccc", type="DECISION",
                        timestamp="2026-05-12T12:00:00+00:00"),
        ]
        s = summarize_log(events, now=now)
        assert s.total_events == 3
        assert len(s.by_type["DECISION"]) == 2
        assert len(s.by_type["INSIGHT"]) == 1

    def test_out_of_window_events_excluded_from_totals(self) -> None:
        now = _utc(2026, 5, 15)
        events = [
            _event_dict(id="evt-aaaaaaaaaaaa", type="INSIGHT",
                        timestamp="2026-04-01T12:00:00+00:00"),
        ]
        s = summarize_log(events, now=now)
        assert s.total_events == 0

    def test_open_actions_surfaced_even_when_old(self) -> None:
        now = _utc(2026, 5, 15)
        events = [
            _event_dict(
                id="evt-aaaaaaaaaaaa", type="ACTION",
                timestamp="2026-01-01T12:00:00+00:00",  # >14d window
                metadata={"status": "open", "owner": "hardware-lead"},
            ),
        ]
        s = summarize_log(events, now=now)
        assert len(s.open_actions) == 1
        assert s.total_events == 0  # not counted in window

    def test_overdue_predictions_surfaced(self) -> None:
        now = _utc(2026, 5, 15)
        events = [
            _event_dict(
                id="evt-aaaaaaaaaaaa", type="PREDICTION",
                timestamp="2026-05-10T12:00:00+00:00",
                metadata={"confidence": 0.7,
                          "horizon": "2026-05-14T00:00:00+00:00"},
            ),
        ]
        s = summarize_log(events, now=now)
        assert len(s.overdue_predictions) == 1

    def test_resolved_predictions_not_overdue(self) -> None:
        now = _utc(2026, 5, 15)
        events = [
            _event_dict(
                id="evt-aaaaaaaaaaaa", type="PREDICTION",
                timestamp="2026-05-10T12:00:00+00:00",
                metadata={"confidence": 0.7,
                          "horizon": "2026-05-14T00:00:00+00:00",
                          "resolved": True},
            ),
        ]
        s = summarize_log(events, now=now)
        assert s.overdue_predictions == []

    def test_recent_context_changes(self) -> None:
        now = _utc(2026, 5, 15)
        events = [
            _event_dict(id="evt-aaaaaaaaaaaa", type="CONTEXT_CHANGE",
                        timestamp="2026-05-14T12:00:00+00:00",
                        title="EPIC announced new App Orchard policy"),
        ]
        s = summarize_log(events, now=now)
        assert len(s.recent_context_changes) == 1

    def test_actor_activity_counted(self) -> None:
        now = _utc(2026, 5, 15)
        events = [
            _event_dict(id="evt-aaaaaaaaaaaa", actor="strategist",
                        timestamp="2026-05-14T12:00:00+00:00"),
            _event_dict(id="evt-bbbbbbbbbbbb", actor="strategist",
                        timestamp="2026-05-13T12:00:00+00:00"),
            _event_dict(id="evt-cccccccccccc", actor="hardware-lead",
                        timestamp="2026-05-12T12:00:00+00:00"),
        ]
        s = summarize_log(events, now=now)
        assert s.actor_activity == {"strategist": 2, "hardware-lead": 1}


class TestRenderBriefing:
    def test_empty_renders_clean(self) -> None:
        s = BriefingSummary(
            window_start="2026-05-01T00:00:00",
            window_end="2026-05-15T00:00:00",
            by_type={}, open_actions=[],
            overdue_predictions=[], recent_context_changes=[],
            recent_outcomes=[], actor_activity={}, total_events=0,
        )
        text = render_briefing(s)
        assert "0 events in window" in text

    def test_open_actions_rendered(self) -> None:
        s = BriefingSummary(
            window_start="2026-05-01T00:00:00",
            window_end="2026-05-15T00:00:00",
            by_type={},
            open_actions=[
                {
                    "id": "evt-aaaaaaaaaaaa",
                    "title": "Build wake-word fallback",
                    "metadata": {"owner": "hardware-lead", "status": "open"},
                }
            ],
            overdue_predictions=[], recent_context_changes=[],
            recent_outcomes=[],
            actor_activity={"strategist": 3}, total_events=5,
        )
        text = render_briefing(s)
        assert "Open actions (1)" in text
        assert "Build wake-word fallback" in text
        assert "hardware-lead" in text
