"""Tests for the Tier-2 adversarial-review gating layer."""
from __future__ import annotations

import pytest

from memory_system.scopes import (
    Scope,
    ScopeTransition,
    StubReviewer,
    annotate_transition_with_verdict,
    gate_tier_2,
)
from memory_system.scopes.lifecycle import LifecycleProposals


def _ts(day: int = 16) -> str:
    return f"2026-05-{day:02d}T10:00:00+00:00"


def _scope(name: str = "aurora", status="active") -> Scope:
    return Scope(
        id=f"scope-{name}-2026-01",
        name=name,
        status=status,
        first_seen=_ts(day=1),
        last_seen=_ts(day=16),
        member_tags=(f"{name}-tag-a", f"{name}-tag-b"),
    )


def _t(scope_id: str, *, from_status="active", to_status="canonical",
        tid="trans-aaaaaaaaaaaa") -> ScopeTransition:
    return ScopeTransition(
        id=tid,
        scope_id=scope_id,
        from_status=from_status,
        to_status=to_status,
        timestamp=_ts(day=16),
        reason="canon criteria met",
        rollback_id="rb-aaaaaaaaaaaa",
    )


def _no_events(_scope: Scope) -> list[dict]:
    return []


class TestGateTier2:
    def test_empty_proposals(self) -> None:
        result = gate_tier_2(
            proposals=LifecycleProposals(),
            scope_by_id={},
            events_for_scope_fn=_no_events,
            reviewer=StubReviewer(),
        )
        assert result.total == 0
        assert result.verdicts == {}

    def test_all_approved_with_stub(self) -> None:
        s = _scope()
        proposals = LifecycleProposals(tier_2=(_t(s.id),))
        result = gate_tier_2(
            proposals=proposals,
            scope_by_id={s.id: s},
            events_for_scope_fn=_no_events,
            reviewer=StubReviewer(),
        )
        assert len(result.approved_transitions) == 1
        assert len(result.rejected_transitions) == 0
        v = result.verdicts["trans-aaaaaaaaaaaa"]
        assert v.verdict == "approved"

    def test_all_rejected_in_reject_mode(self) -> None:
        s = _scope()
        proposals = LifecycleProposals(tier_2=(_t(s.id),))
        result = gate_tier_2(
            proposals=proposals,
            scope_by_id={s.id: s},
            events_for_scope_fn=_no_events,
            reviewer=StubReviewer(always_reject=True),
        )
        assert len(result.approved_transitions) == 0
        assert len(result.rejected_transitions) == 1
        v = result.verdicts["trans-aaaaaaaaaaaa"]
        assert v.verdict == "rejected"
        assert v.suggested_alternative

    def test_missing_scope_fails_safe(self) -> None:
        # Transition targets a scope not in scope_by_id.
        s = _scope()
        proposals = LifecycleProposals(
            tier_2=(_t("scope-disappeared-2026-01"),),
        )
        result = gate_tier_2(
            proposals=proposals,
            scope_by_id={s.id: s},  # different id
            events_for_scope_fn=_no_events,
            reviewer=StubReviewer(),
        )
        assert len(result.approved_transitions) == 0
        assert len(result.rejected_transitions) == 1
        v = result.verdicts["trans-aaaaaaaaaaaa"]
        assert v.verdict == "rejected"
        assert "not found" in v.reasoning

    def test_extra_context_callable_is_invoked(self) -> None:
        s = _scope()
        proposals = LifecycleProposals(tier_2=(_t(s.id),))
        seen: list = []

        def context_for(trans):
            seen.append(trans.id)
            return "operator retained this scope"

        def decide(req):
            assert "operator retained" in (req.extra_context or "")
            return ("approved", "context confirmed", None)

        result = gate_tier_2(
            proposals=proposals,
            scope_by_id={s.id: s},
            events_for_scope_fn=_no_events,
            reviewer=StubReviewer(decide=decide),
            extra_context_for=context_for,
        )
        assert seen == ["trans-aaaaaaaaaaaa"]
        assert len(result.approved_transitions) == 1

    def test_mixed_outcomes(self) -> None:
        s1 = _scope("alpha")
        s2 = _scope("beta")
        t1 = _t(s1.id, tid="trans-aaaaaaaaaaa1")
        t2 = _t(s2.id, tid="trans-aaaaaaaaaaa2")
        proposals = LifecycleProposals(tier_2=(t1, t2))

        # Reject only beta.
        def decide(req):
            if "beta" in req.scope.id:
                return ("rejected", "beta has no momentum", "wait")
            return ("approved", "alpha is solid", None)

        result = gate_tier_2(
            proposals=proposals,
            scope_by_id={s1.id: s1, s2.id: s2},
            events_for_scope_fn=_no_events,
            reviewer=StubReviewer(decide=decide),
        )
        assert {t.scope_id for t in result.approved_transitions} == {s1.id}
        assert {t.scope_id for t in result.rejected_transitions} == {s2.id}


class TestAnnotateTransition:
    def test_reason_carries_verdict_metadata(self) -> None:
        s = _scope()
        t = _t(s.id)
        from memory_system.scopes import ReviewVerdict
        verdict = ReviewVerdict(
            verdict="approved",
            reasoning="scope has sustained activity",
            provider_name="stub", model_name="stub-1",
        )
        annotated = annotate_transition_with_verdict(t, verdict)
        assert annotated.id == t.id  # identity preserved
        assert "adversarial review" in annotated.reason
        assert "approved" in annotated.reason
        assert "sustained activity" in annotated.reason
        assert annotated.actor == "autonomous"  # approved -> actor unchanged

    def test_rejected_verdict_changes_actor(self) -> None:
        s = _scope()
        t = _t(s.id)
        from memory_system.scopes import ReviewVerdict
        verdict = ReviewVerdict(
            verdict="rejected",
            reasoning="member tags drifting",
            provider_name="stub", model_name="stub-1",
        )
        annotated = annotate_transition_with_verdict(t, verdict)
        assert annotated.actor == "adversary_rejected"

    def test_reason_truncated_to_model_max(self) -> None:
        s = _scope()
        # Use a long reason that will be combined with the verdict.
        long_t = ScopeTransition(
            id="trans-aaaaaaaaaaa3",
            scope_id=s.id,
            from_status="active",
            to_status="canonical",
            timestamp=_ts(),
            reason="x" * 1900,  # below 2000 alone
            rollback_id="rb-aaaaaaaaaaa3",
        )
        from memory_system.scopes import ReviewVerdict
        verdict = ReviewVerdict(
            verdict="approved",
            reasoning="y" * 500,  # the combined > 2000 should be truncated
            provider_name="stub", model_name="stub-1",
        )
        annotated = annotate_transition_with_verdict(long_t, verdict)
        assert len(annotated.reason) <= 2000
