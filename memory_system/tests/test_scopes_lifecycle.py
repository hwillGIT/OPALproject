"""Unit tests for the scope lifecycle engine."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from memory_system.scopes import Scope
from memory_system.scopes.lifecycle import (
    LifecycleConfig,
    LifecycleProposals,
    apply_transition,
    count_distinct_sessions,
    evaluate,
    evaluate_all,
    events_for_scope,
    last_activity,
    propose_canonicalization,
    propose_deprecation,
    propose_promotion,
)


def _utc(year: int = 2026, month: int = 1, day: int = 1, hour: int = 12) -> datetime:
    return datetime(year, month, day, hour, tzinfo=timezone.utc)


def _iso(year: int = 2026, month: int = 1, day: int = 1, hour: int = 12) -> str:
    return _utc(year, month, day, hour).isoformat()


def _event(tags, *, when: datetime, id: str = None):
    eid = id or f"evt-{when.day:02d}{when.hour:02d}xxxxxx"
    return {
        "id": eid,
        "timestamp": when.isoformat(),
        "type": "MEETING",
        "actor": "operator",
        "title": "m", "content": "c",
        "tags": list(tags),
    }


def _scope(
    *,
    status="provisional",
    member_tags=("aurora", "north-star-metric", "pillar-deck"),
    first_seen=None,
    last_seen=None,
) -> Scope:
    fs = first_seen or _iso()
    return Scope(
        id="scope-aurora-2026-01",
        name="aurora",
        status=status,
        member_tags=member_tags,
        first_seen=fs,
        last_seen=last_seen or fs,
    )


# --------------------------------------------------------------------------
# measurement helpers
# --------------------------------------------------------------------------


class TestMeasurement:
    def test_events_for_scope_filters_by_tags(self) -> None:
        scope = _scope(member_tags=("aurora", "helios"))
        events = [
            _event(["aurora"], when=_utc(day=2)),
            _event(["unrelated"], when=_utc(day=3)),
            _event(["helios", "growth"], when=_utc(day=4)),
        ]
        relevant = events_for_scope(scope, events)
        assert len(relevant) == 2

    def test_count_distinct_sessions(self) -> None:
        events = [
            _event(["x"], when=_utc(day=1, hour=10)),
            _event(["x"], when=_utc(day=1, hour=13)),  # +3h same session
            _event(["x"], when=_utc(day=2, hour=12)),  # +23h new session
        ]
        assert count_distinct_sessions(events, session_window_hours=6) == 2

    def test_count_distinct_sessions_empty(self) -> None:
        assert count_distinct_sessions([], session_window_hours=6) == 0

    def test_last_activity(self) -> None:
        events = [
            _event(["x"], when=_utc(day=1)),
            _event(["x"], when=_utc(day=5)),
            _event(["x"], when=_utc(day=3)),
        ]
        assert last_activity(events) == _utc(day=5)


# --------------------------------------------------------------------------
# promotion (Tier 1)
# --------------------------------------------------------------------------


class TestProposePromotion:
    def test_meets_criteria(self) -> None:
        scope = _scope(first_seen=_iso())
        events = [
            _event(["aurora"], when=_utc(day=2)),
            _event(["aurora"], when=_utc(day=10)),
            _event(["aurora"], when=_utc(day=20)),
        ]
        now = _utc(month=2, day=1)
        t = propose_promotion(scope, events, LifecycleConfig(), now=now)
        assert t is not None
        assert t.from_status == "provisional"
        assert t.to_status == "active"
        assert t.actor == "autonomous"
        assert t.rollback_id is not None

    def test_too_young_blocks(self) -> None:
        scope = _scope(first_seen=_iso())
        events = [
            _event(["aurora"], when=_utc(day=2, hour=8)),
            _event(["aurora"], when=_utc(day=3, hour=8)),
            _event(["aurora"], when=_utc(day=5, hour=8)),
        ]
        now = _utc(day=10)  # 9 days
        assert propose_promotion(scope, events, LifecycleConfig(), now=now) is None

    def test_too_few_sessions_blocks(self) -> None:
        scope = _scope(first_seen=_iso())
        events = [
            _event(["aurora"], when=_utc(day=2, hour=10)),
            _event(["aurora"], when=_utc(day=2, hour=11)),  # same session
        ]
        now = _utc(month=2, day=1)
        assert propose_promotion(scope, events, LifecycleConfig(), now=now) is None

    def test_wrong_status_blocks(self) -> None:
        scope = _scope(status="active", first_seen=_iso())
        events = [
            _event(["aurora"], when=_utc(day=d)) for d in (2, 10, 20)
        ]
        now = _utc(month=2, day=1)
        assert propose_promotion(scope, events, LifecycleConfig(), now=now) is None


# --------------------------------------------------------------------------
# canonicalization (Tier 2)
# --------------------------------------------------------------------------


class TestProposeCanonicalization:
    def test_meets_criteria(self) -> None:
        scope = _scope(status="active", first_seen=_iso(month=1, day=1))
        events = [
            _event(["aurora"], when=_utc(month=1, day=1) + timedelta(days=25 * i),
                    id=f"evt-sess-{i:02d}xxxx")
            for i in range(8)
        ]
        now = _utc(month=12, day=1)
        t = propose_canonicalization(scope, events, LifecycleConfig(), now=now)
        assert t is not None
        assert t.to_status == "canonical"
        assert "adversarial review" in t.reason

    def test_too_young_blocks(self) -> None:
        scope = _scope(status="active", first_seen=_iso(month=1, day=1))
        events = [
            _event(["aurora"], when=_utc(month=1, day=1) + timedelta(days=i * 3),
                    id=f"evt-{i:02d}xxxxxxxx")
            for i in range(8)
        ]
        now = _utc(month=3, day=1)
        assert propose_canonicalization(scope, events, LifecycleConfig(),
                                          now=now) is None


# --------------------------------------------------------------------------
# deprecation (Tier 2)
# --------------------------------------------------------------------------


class TestProposeDeprecation:
    def test_idle_scope_deprecates(self) -> None:
        scope = _scope(
            status="active",
            first_seen=_iso(month=1, day=1),
            last_seen=_iso(month=1, day=5),
        )
        events = [_event(["aurora"], when=_utc(month=1, day=2))]
        now = _utc(month=6, day=1)  # ~5 months later
        t = propose_deprecation(scope, events, LifecycleConfig(), now=now)
        assert t is not None
        assert t.to_status == "deprecated"

    def test_active_not_idle_no_proposal(self) -> None:
        scope = _scope(status="active", first_seen=_iso(month=1, day=1))
        events = [_event(["aurora"], when=_utc(month=1, day=29))]
        now = _utc(month=2, day=1)
        assert propose_deprecation(scope, events, LifecycleConfig(),
                                     now=now) is None

    def test_already_deprecated_returns_none(self) -> None:
        scope = _scope(status="deprecated", first_seen=_iso(month=1, day=1))
        now = _utc(year=2027, month=1, day=1)
        assert propose_deprecation(scope, [], LifecycleConfig(), now=now) is None


# --------------------------------------------------------------------------
# evaluate / evaluate_all
# --------------------------------------------------------------------------


class TestEvaluate:
    def test_deprecation_takes_precedence_over_promotion(self) -> None:
        scope = _scope(
            status="provisional",
            first_seen=_iso(month=1, day=1),
            last_seen=_iso(month=1, day=15),
        )
        events = [
            _event(["aurora"], when=_utc(month=1, day=d))
            for d in (2, 8, 15)
        ]
        now = _utc(month=6, day=1)
        result = evaluate(scope, events, LifecycleConfig(), now=now)
        assert len(result) == 1
        assert result[0].to_status == "deprecated"

    def test_no_proposal_returns_empty(self) -> None:
        scope = _scope(first_seen=_iso())
        assert evaluate(scope, [], LifecycleConfig(),
                          now=_utc(day=2)) == []


class TestEvaluateAll:
    def test_disabled_yields_empty(self) -> None:
        s = _scope()
        assert evaluate_all([s], [], LifecycleConfig(enabled=False)) == LifecycleProposals()


# --------------------------------------------------------------------------
# apply_transition
# --------------------------------------------------------------------------


class TestApplyTransition:
    def test_status_advances_and_audit_set(self) -> None:
        scope = _scope(first_seen=_iso())
        events = [_event(["aurora"], when=_utc(day=d)) for d in (2, 10, 20)]
        now = _utc(month=2, day=1)
        trans = propose_promotion(scope, events, LifecycleConfig(), now=now)
        assert trans is not None
        updated = apply_transition(scope, trans)
        assert updated.status == "active"
        assert updated.promoted_from == "provisional"
        assert updated.promoted_at == trans.timestamp
        assert updated.rollback_id == trans.rollback_id
        # original unchanged (frozen dataclass)
        assert scope.status == "provisional"

    def test_mismatched_scope_id_raises(self) -> None:
        scope = _scope()
        events = [_event(["aurora"], when=_utc(day=d)) for d in (2, 10, 20)]
        trans = propose_promotion(scope, events, LifecycleConfig(),
                                    now=_utc(month=2, day=1))
        assert trans is not None
        from dataclasses import replace
        other = Scope(
            id="scope-other-2026-01",
            name=scope.name, status=scope.status,
            first_seen=scope.first_seen, last_seen=scope.last_seen,
            member_tags=scope.member_tags,
        )
        with pytest.raises(ValueError, match="targets"):
            apply_transition(other, trans)
