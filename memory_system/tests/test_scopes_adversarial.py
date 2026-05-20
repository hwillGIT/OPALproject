"""Unit tests for the adversarial reviewer + verdict parser."""
from __future__ import annotations

import pytest

from memory_system.scopes import (
    AdversarialReviewer,
    ReviewRequest,
    ReviewVerdict,
    Scope,
    ScopeTransition,
    StubReviewer,
    Verdict,
    build_review_prompt,
    parse_review_response,
)
from memory_system.scopes.adversarial import SYSTEM_PROMPT


def _ts(day: int = 16) -> str:
    return f"2026-05-{day:02d}T10:00:00+00:00"


def _scope(
    *,
    status="active",
    member_tags=("aurora", "north-star-metric", "pillar-deck"),
    name="aurora",
) -> Scope:
    return Scope(
        id=f"scope-{name}-2026-01",
        name=name,
        status=status,
        first_seen=_ts(day=1),
        last_seen=_ts(day=16),
        member_tags=member_tags,
    )


def _transition(
    *,
    scope_id="scope-aurora-2026-01",
    from_status="active",
    to_status="canonical",
    reason="canonicalization meets criteria",
) -> ScopeTransition:
    return ScopeTransition(
        id="trans-abcdef012345",
        scope_id=scope_id,
        from_status=from_status,
        to_status=to_status,
        timestamp=_ts(day=16),
        reason=reason,
        rollback_id="rb-abcdef012345",
    )


# --------------------------------------------------------------------------
# system prompt invariants
# --------------------------------------------------------------------------


class TestSystemPrompt:
    def test_demands_strict_output_format(self) -> None:
        assert "VERDICT:" in SYSTEM_PROMPT
        assert "REASONING:" in SYSTEM_PROMPT
        assert "ALTERNATIVE:" in SYSTEM_PROMPT

    def test_states_skeptical_posture(self) -> None:
        lowered = SYSTEM_PROMPT.lower()
        # The prompt's whole point is to argue against the proposal.
        assert "argue against" in lowered
        assert "skeptical" in lowered

    def test_distinguishes_canonical_vs_deprecation_bars(self) -> None:
        lowered = SYSTEM_PROMPT.lower()
        # Canonicalization should be called out as a high bar.
        assert "canonical" in lowered
        assert "deprecat" in lowered


# --------------------------------------------------------------------------
# build_review_prompt
# --------------------------------------------------------------------------


class TestBuildReviewPrompt:
    def test_user_prompt_contains_scope_and_transition_fields(self) -> None:
        s = _scope()
        t = _transition()
        req = ReviewRequest(scope=s, transition=t, relevant_events=())
        _, user = build_review_prompt(req)
        assert s.id in user
        assert s.name in user
        assert "active" in user
        assert "canonical" in user
        assert t.reason in user

    def test_includes_member_tags(self) -> None:
        s = _scope(member_tags=("alpha-tag", "beta-tag", "gamma-tag"))
        t = _transition(scope_id=s.id)
        req = ReviewRequest(scope=s, transition=t, relevant_events=())
        _, user = build_review_prompt(req)
        assert "alpha-tag" in user
        assert "beta-tag" in user
        assert "gamma-tag" in user

    def test_no_events_renders_placeholder(self) -> None:
        req = ReviewRequest(scope=_scope(), transition=_transition(),
                              relevant_events=())
        _, user = build_review_prompt(req)
        assert "no events touching" in user

    def test_extra_context_propagates(self) -> None:
        req = ReviewRequest(
            scope=_scope(), transition=_transition(), relevant_events=(),
            extra_context="operator flagged this scope as retained",
        )
        _, user = build_review_prompt(req)
        assert "operator flagged this scope as retained" in user
        assert "ADDITIONAL CONTEXT" in user

    def test_events_summarized_with_cap(self) -> None:
        events = [
            {
                "id": f"evt-{i:02d}xxxxxxxx",
                "timestamp": f"2026-05-{i + 1:02d}T12:00:00+00:00",
                "type": "DECISION", "actor": "operator",
                "title": f"decision {i}", "tags": ["aurora"],
            }
            for i in range(12)  # exceed the cap=8
        ]
        req = ReviewRequest(
            scope=_scope(), transition=_transition(),
            relevant_events=tuple(events),
        )
        _, user = build_review_prompt(req)
        # The summarizer emits an "older event(s) elided" note.
        assert "elided" in user
        # And shows the latest event.
        assert "decision 11" in user


# --------------------------------------------------------------------------
# parse_review_response
# --------------------------------------------------------------------------


class TestParseReviewResponse:
    def test_approved_with_alternative(self) -> None:
        text = (
            "VERDICT: APPROVED\n"
            "REASONING: scope has sustained activity over 8 sessions.\n"
            "ALTERNATIVE: none\n"
        )
        v, r, a = parse_review_response(text)
        assert v == "approved"
        assert "8 sessions" in r
        assert a is None

    def test_rejected_with_alternative(self) -> None:
        text = (
            "VERDICT: REJECTED\n"
            "REASONING: member tags look transient; pilot may not survive.\n"
            "ALTERNATIVE: wait 30 more days before re-evaluating.\n"
        )
        v, r, a = parse_review_response(text)
        assert v == "rejected"
        assert "transient" in r
        assert "wait 30" in a

    def test_case_insensitive(self) -> None:
        text = "verdict: approved\nreasoning: ok\nalternative: none"
        v, _, _ = parse_review_response(text)
        assert v == "approved"

    def test_malformed_fails_safe_to_rejected(self) -> None:
        text = "I think we should approve this because..."
        v, r, _ = parse_review_response(text)
        assert v == "rejected"
        assert "parse failure" in r

    def test_missing_alternative_returns_none(self) -> None:
        text = (
            "VERDICT: APPROVED\n"
            "REASONING: looks fine\n"
        )
        _, _, a = parse_review_response(text)
        assert a is None

    def test_alternative_none_token_returns_none(self) -> None:
        text = (
            "VERDICT: APPROVED\n"
            "REASONING: fine\n"
            "ALTERNATIVE: N/A\n"
        )
        _, _, a = parse_review_response(text)
        assert a is None


# --------------------------------------------------------------------------
# StubReviewer
# --------------------------------------------------------------------------


class TestStubReviewer:
    def test_default_approves_tier_2(self) -> None:
        r = StubReviewer()
        verdict = r.review(ReviewRequest(
            scope=_scope(), transition=_transition(),
        ))
        assert verdict.verdict == "approved"
        assert verdict.metadata["tier"] == 2

    def test_always_reject_mode(self) -> None:
        r = StubReviewer(always_reject=True)
        verdict = r.review(ReviewRequest(
            scope=_scope(), transition=_transition(),
        ))
        assert verdict.verdict == "rejected"
        assert verdict.suggested_alternative

    def test_custom_decide_callable(self) -> None:
        def custom(req):
            return ("rejected", "I just don't like it", "try again later")

        r = StubReviewer(decide=custom)
        verdict = r.review(ReviewRequest(
            scope=_scope(), transition=_transition(),
        ))
        assert verdict.verdict == "rejected"
        assert "I just don't like it" in verdict.reasoning
        assert verdict.suggested_alternative == "try again later"

    def test_skips_review_for_lower_tiers(self) -> None:
        # Tier-1 transition (provisional -> active) should be auto-approved.
        r = StubReviewer(always_reject=True)
        verdict = r.review(ReviewRequest(
            scope=_scope(status="provisional"),
            transition=_transition(from_status="provisional", to_status="active"),
        ))
        assert verdict.verdict == "approved"
        assert verdict.metadata.get("skipped_review") is True

    def test_disallowed_transition_rejected(self) -> None:
        r = StubReviewer()
        # provisional -> canonical is not in the allowed table.
        verdict = r.review(ReviewRequest(
            scope=_scope(status="provisional"),
            transition=_transition(from_status="provisional", to_status="canonical"),
        ))
        assert verdict.verdict == "rejected"
        assert "not allowed" in verdict.reasoning


# --------------------------------------------------------------------------
# AdversarialReviewer (with a fake provider, no network)
# --------------------------------------------------------------------------


class _FakeProvider:
    """Fake LLM provider that returns a canned response."""

    def __init__(self, response: str, name: str = "fake", model: str = "fake-1") -> None:
        self.response = response
        self.name = name
        self.model = model
        self.last_call: dict = {}

    def complete(self, system_prompt, user_prompt, max_tokens, temperature):
        self.last_call = {
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        return self.response


class TestAdversarialReviewer:
    def test_approved_path(self) -> None:
        provider = _FakeProvider(
            "VERDICT: APPROVED\nREASONING: ok\nALTERNATIVE: none",
        )
        reviewer = AdversarialReviewer(provider=provider)
        v = reviewer.review(ReviewRequest(
            scope=_scope(), transition=_transition(),
        ))
        assert v.verdict == "approved"
        assert v.provider_name == "fake"
        assert v.model_name == "fake-1"

    def test_rejected_path(self) -> None:
        provider = _FakeProvider(
            "VERDICT: REJECTED\nREASONING: too fresh\nALTERNATIVE: wait 30d",
        )
        reviewer = AdversarialReviewer(provider=provider)
        v = reviewer.review(ReviewRequest(
            scope=_scope(), transition=_transition(),
        ))
        assert v.verdict == "rejected"
        assert v.suggested_alternative == "wait 30d"

    def test_provider_exception_fails_safe(self) -> None:
        class BoomProvider:
            name = "boom"
            model = "boom-1"

            def complete(self, **kw):
                raise RuntimeError("network down")

        reviewer = AdversarialReviewer(provider=BoomProvider())
        v = reviewer.review(ReviewRequest(
            scope=_scope(), transition=_transition(),
        ))
        assert v.verdict == "rejected"
        assert "network down" in v.reasoning

    def test_temperature_is_low_for_reproducibility(self) -> None:
        # Judgments should be more reproducible than synthesis;
        # confirm the reviewer asks for a low temperature.
        provider = _FakeProvider(
            "VERDICT: APPROVED\nREASONING: ok\nALTERNATIVE: none",
        )
        reviewer = AdversarialReviewer(provider=provider)
        reviewer.review(ReviewRequest(
            scope=_scope(), transition=_transition(),
        ))
        assert provider.last_call["temperature"] <= 0.2
