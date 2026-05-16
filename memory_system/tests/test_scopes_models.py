"""Unit tests for the scope value types + state machine + identifiers."""
from __future__ import annotations

import pytest

from memory_system.scopes import (
    ALLOWED_TRANSITIONS,
    Scope,
    ScopeMember,
    ScopeTransition,
    can_transition,
    make_rollback_id,
    make_scope_id,
    make_transition_id,
    slugify,
    tier_of,
)
from memory_system.scopes.models import ScopeValidationError


# --------------------------------------------------------------------------
# slugify
# --------------------------------------------------------------------------


class TestSlugify:
    def test_basic(self) -> None:
        assert slugify("Project Aurora") == "project-aurora"

    def test_collapses_runs(self) -> None:
        assert slugify("OPAL / LYNA — pilot 3a") == "opal-lyna-pilot-3a"

    def test_empty_input(self) -> None:
        assert slugify("___-") == ""


# --------------------------------------------------------------------------
# identifiers
# --------------------------------------------------------------------------


class TestIdentifiers:
    def test_make_scope_id_uses_yyyy_mm(self) -> None:
        sid = make_scope_id("Project Aurora", "2026-05-16T10:00:00+00:00")
        assert sid == "scope-project-aurora-2026-05"

    def test_make_scope_id_rejects_empty_slug(self) -> None:
        with pytest.raises(ValueError, match="slugifies to empty"):
            make_scope_id("___-", "2026-05-16T10:00:00+00:00")

    def test_make_scope_id_rejects_bad_timestamp(self) -> None:
        with pytest.raises(ValueError, match="YYYY-MM"):
            make_scope_id("Aurora", "last tuesday")

    def test_transition_id_deterministic(self) -> None:
        a = make_transition_id("scope-aurora-2026-05", None, "provisional",
                                "2026-05-16T10:00:00+00:00")
        b = make_transition_id("scope-aurora-2026-05", None, "provisional",
                                "2026-05-16T10:00:00+00:00")
        assert a == b
        assert a.startswith("trans-")
        assert len(a) == 18

    def test_rollback_id_deterministic(self) -> None:
        tid = "trans-abcdef012345"
        assert make_rollback_id(tid) == make_rollback_id(tid)
        assert make_rollback_id(tid).startswith("rb-")


# --------------------------------------------------------------------------
# Scope model
# --------------------------------------------------------------------------


def _ts(day: int = 16) -> str:
    return f"2026-05-{day:02d}T10:00:00+00:00"


class TestScopeValidation:
    def _build(self, **overrides):
        d = dict(
            id="scope-aurora-2026-05",
            name="Aurora",
            status="provisional",
            first_seen=_ts(),
            last_seen=_ts(),
        )
        d.update(overrides)
        return d

    def test_minimal_ok(self) -> None:
        s = Scope(**self._build())
        assert s.id == "scope-aurora-2026-05"
        assert s.status == "provisional"

    def test_bad_id_raises(self) -> None:
        with pytest.raises(ScopeValidationError, match="scope.id"):
            Scope(**self._build(id="not-a-scope-id"))

    def test_bad_status_raises(self) -> None:
        with pytest.raises(ScopeValidationError, match="status"):
            Scope(**self._build(status="something-else"))

    def test_empty_name_raises(self) -> None:
        with pytest.raises(ScopeValidationError, match="name"):
            Scope(**self._build(name=""))

    def test_negative_counts_raise(self) -> None:
        with pytest.raises(ScopeValidationError, match="session_count"):
            Scope(**self._build(session_count=-1))

    def test_frozen(self) -> None:
        s = Scope(**self._build())
        with pytest.raises(AttributeError):
            s.name = "Other"  # type: ignore[misc]

    def test_bad_rollback_id_raises(self) -> None:
        with pytest.raises(ScopeValidationError, match="rollback_id"):
            Scope(**self._build(rollback_id="not-a-rb-id"))


class TestScopeMemberValidation:
    def test_minimal_ok(self) -> None:
        m = ScopeMember(
            scope_id="scope-aurora-2026-05", tag="aurora",
            joined_at=_ts(), last_seen=_ts(),
        )
        assert m.tag == "aurora"

    def test_bad_scope_id_raises(self) -> None:
        with pytest.raises(ScopeValidationError, match="scope_id"):
            ScopeMember(
                scope_id="bad", tag="t",
                joined_at=_ts(), last_seen=_ts(),
            )


class TestScopeTransitionValidation:
    def _build(self, **overrides):
        d = dict(
            id="trans-abcdef012345",
            scope_id="scope-aurora-2026-05",
            to_status="provisional",
            timestamp=_ts(),
            reason="test",
        )
        d.update(overrides)
        return d

    def test_minimal_ok(self) -> None:
        t = ScopeTransition(**self._build())
        assert t.actor == "autonomous"

    def test_bad_id_raises(self) -> None:
        with pytest.raises(ScopeValidationError, match="transition.id"):
            ScopeTransition(**self._build(id="bad-id"))

    def test_bad_actor_raises(self) -> None:
        with pytest.raises(ScopeValidationError, match="actor"):
            ScopeTransition(**self._build(actor="impostor"))


# --------------------------------------------------------------------------
# state machine
# --------------------------------------------------------------------------


class TestStateMachine:
    def test_creation_allowed(self) -> None:
        assert can_transition(None, "provisional")
        assert tier_of(None, "provisional") == 0

    def test_promotion_is_tier_1(self) -> None:
        assert tier_of("provisional", "active") == 1

    def test_canonicalization_is_tier_2(self) -> None:
        assert tier_of("active", "canonical") == 2

    def test_deprecation_paths(self) -> None:
        assert tier_of("provisional", "deprecated") == 2
        assert tier_of("active", "deprecated") == 2
        assert tier_of("canonical", "deprecated") == 2

    def test_demotions_tier_3(self) -> None:
        assert tier_of("canonical", "active") == 3
        assert tier_of("active", "provisional") == 3

    def test_disallowed_raises(self) -> None:
        with pytest.raises(ValueError, match="not allowed"):
            tier_of("provisional", "canonical")

    def test_no_self_loops(self) -> None:
        for (from_s, to_s) in ALLOWED_TRANSITIONS:
            assert from_s != to_s
