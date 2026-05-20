"""Unit + integration tests for burst detection and replay."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from memory_system.scopes.detect import (
    BurstDetectionConfig,
    absorb,
    detect,
    detect_event_burst,
    detect_window_burst,
    materialize,
    propose_name_from_tags,
    replay,
)


def _ts(year: int = 2026, month: int = 5, day: int = 16, hour: int = 12) -> str:
    return datetime(year, month, day, hour, tzinfo=timezone.utc).isoformat()


def _event(tags, *, day: int = 16, hour: int = 12, id: str = None):
    eid = id or f"evt-{''.join(tags)[:12].ljust(12, 'x')}"
    return {
        "id": eid,
        "timestamp": _ts(day=day, hour=hour),
        "type": "MEETING",
        "actor": "operator",
        "title": "meeting",
        "content": "content",
        "tags": list(tags),
    }


# --------------------------------------------------------------------------
# propose_name_from_tags
# --------------------------------------------------------------------------


class TestProposeName:
    def test_picks_codename_first(self) -> None:
        assert propose_name_from_tags(
            ["pillar-deck", "aurora", "engaged-fleet"],
        ) == "aurora"

    def test_first_codename_wins(self) -> None:
        # Stable under input order: first qualifying single-token wins.
        assert propose_name_from_tags(
            ["aurora", "helios", "north-star"],
        ) == "aurora"

    def test_falls_back_to_longest(self) -> None:
        assert propose_name_from_tags(
            ["a-b", "x-y-z-q-w", "c-d-e"],
        ) == "x-y-z-q-w"

    def test_empty_raises(self) -> None:
        with pytest.raises(ValueError):
            propose_name_from_tags([])


# --------------------------------------------------------------------------
# detect_event_burst
# --------------------------------------------------------------------------


class TestEventBurst:
    def test_three_new_tags_triggers(self) -> None:
        ev = _event(["aurora", "north-star-metric", "pillar-deck"])
        cand = detect_event_burst(ev, set(), BurstDetectionConfig())
        assert cand is not None
        assert cand.proposed_name == "aurora"
        assert set(cand.member_tags) == {"aurora", "north-star-metric", "pillar-deck"}
        assert cand.evidence_event_ids == (ev["id"],)

    def test_two_new_tags_below_threshold(self) -> None:
        ev = _event(["aurora", "north-star-metric"])
        assert detect_event_burst(ev, set(), BurstDetectionConfig()) is None

    def test_canonical_tags_dont_count(self) -> None:
        ev = _event(["strategy", "growth", "aurora"])
        cand = detect_event_burst(ev, {"strategy", "growth"},
                                   BurstDetectionConfig())
        assert cand is None

    def test_disabled_returns_none(self) -> None:
        ev = _event(["a-tag", "b-tag", "c-tag"])
        assert detect_event_burst(
            ev, set(), BurstDetectionConfig(enabled=False),
        ) is None


# --------------------------------------------------------------------------
# detect_window_burst
# --------------------------------------------------------------------------


class TestWindowBurst:
    def test_three_tags_across_two_events_in_window(self) -> None:
        e1 = _event(["aurora", "pillar-deck"], hour=10, id="evt-aaa1")
        e2 = _event(["engaged-fleet"], hour=11, id="evt-bbb2")
        cand = detect_window_burst(e2, [e1], set(), BurstDetectionConfig())
        assert cand is not None
        assert set(cand.member_tags) == {"aurora", "pillar-deck", "engaged-fleet"}
        assert e1["id"] in cand.evidence_event_ids
        assert e2["id"] in cand.evidence_event_ids

    def test_event_outside_window_excluded(self) -> None:
        # 48h gap
        e1 = _event(["aurora", "pillar-deck"], day=14, id="evt-aaa1")
        e2 = _event(["engaged-fleet"], day=16, id="evt-bbb2")
        cand = detect_window_burst(e2, [e1], set(), BurstDetectionConfig())
        assert cand is None

    def test_current_event_must_contribute(self) -> None:
        e1 = _event(["aurora", "pillar-deck", "engaged-fleet"], hour=10,
                     id="evt-aaa1")
        e2 = _event(["strategy"], hour=11, id="evt-bbb2")
        cand = detect_window_burst(e2, [e1], {"strategy"},
                                    BurstDetectionConfig())
        assert cand is None


# --------------------------------------------------------------------------
# combined detect
# --------------------------------------------------------------------------


class TestDetect:
    def test_single_event_preferred_when_both_fire(self) -> None:
        prior = _event(["a-tag", "b-tag"], hour=10, id="evt-prior")
        cur = _event(["c-tag", "d-tag", "e-tag"], hour=11, id="evt-cur")
        cands = detect(cur, [prior], set(), BurstDetectionConfig())
        assert len(cands) == 1
        assert cands[0].evidence_event_ids == (cur["id"],)

    def test_no_burst_returns_empty(self) -> None:
        ev = _event(["just-one"])
        assert detect(ev, [], set(), BurstDetectionConfig()) == []


# --------------------------------------------------------------------------
# materialize
# --------------------------------------------------------------------------


class TestMaterialize:
    def test_produces_provisional_scope(self) -> None:
        from memory_system.scopes.detect import ScopeCandidate
        cand = ScopeCandidate(
            proposed_name="Aurora",
            member_tags=("aurora", "pillar-deck", "engaged-fleet"),
            evidence_event_ids=("evt-aaa1",),
            first_seen=_ts(),
            last_seen=_ts(),
            reason="test",
        )
        mat = materialize(cand)
        assert mat.scope.status == "provisional"
        assert mat.scope.id == "scope-aurora-2026-05"
        assert mat.transition.from_status is None
        assert mat.transition.to_status == "provisional"
        assert mat.transition.actor == "autonomous"
        assert mat.scope.rollback_id == mat.transition.rollback_id

    def test_deterministic_under_replay(self) -> None:
        from memory_system.scopes.detect import ScopeCandidate
        c = ScopeCandidate(
            proposed_name="Aurora",
            member_tags=("aurora",),
            evidence_event_ids=("evt-aaa1",),
            first_seen=_ts(), last_seen=_ts(), reason="t",
        )
        a = materialize(c)
        b = materialize(c)
        assert a.scope.id == b.scope.id
        assert a.transition.id == b.transition.id


# --------------------------------------------------------------------------
# replay
# --------------------------------------------------------------------------


class TestReplay:
    def test_empty_stream_yields_empty(self) -> None:
        state = replay([], set(), BurstDetectionConfig())
        assert state.materialized == ()

    def test_single_burst_creates_one_scope(self) -> None:
        e = _event(["aurora", "pillar-deck", "engaged-fleet"])
        state = replay([e], set(), BurstDetectionConfig())
        assert len(state.materialized) == 1
        assert state.materialized[0].scope.name == "aurora"

    def test_subsequent_known_tags_dont_recreate(self) -> None:
        e1 = _event(["aurora", "pillar-deck", "engaged-fleet"], day=16,
                     id="evt-e1xx")
        e2 = _event(["aurora", "pillar-deck"], day=17, id="evt-e2xx")
        state = replay([e1, e2], set(), BurstDetectionConfig())
        assert len(state.materialized) == 1

    def test_two_independent_bursts_create_two(self) -> None:
        e1 = _event(["aurora", "alpha-tag", "beta-tag"], day=16, id="evt-e1xx")
        e2 = _event(["helios", "gamma-tag", "delta-tag"], day=24, id="evt-e2xx")
        state = replay([e1, e2], set(), BurstDetectionConfig())
        names = sorted(m.scope.name for m in state.materialized)
        assert names == ["aurora", "helios"]

    def test_canonical_tags_suppress_burst(self) -> None:
        e = _event(["strategy", "growth", "compliance"])
        state = replay([e], {"strategy", "growth", "compliance"},
                        BurstDetectionConfig())
        assert state.materialized == ()
