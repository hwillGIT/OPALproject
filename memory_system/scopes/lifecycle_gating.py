"""Gate Tier-2 lifecycle proposals through adversarial review.

`memory_system/scopes/lifecycle.py` produces Tier-1 and Tier-2 proposals
but never gates them; the CLI used to require an explicit
`--apply-tier-2` flag to commit Tier-2 transitions blindly. This
module sits between the lifecycle and the apply step:

  proposals -> adversarial review -> (approved, rejected) -> apply only approved

The reviewer is injected (any object implementing the same shape as
`AdversarialReviewer` or `StubReviewer`), so the gating logic itself
is pure orchestration.

Output:
  - GatingResult.approved_transitions  Tier-2 transitions cleared to apply
  - GatingResult.rejected_transitions  Tier-2 transitions blocked
  - GatingResult.verdicts              full audit (transition_id -> verdict)
                                       for every transition we asked about

Caller responsibilities (see `cli.py --with-adversarial-review`):
  1. Run lifecycle.evaluate_all() to get proposals
  2. Call gate_tier_2() with those proposals + a reviewer + a way to
     fetch events for each scope (so the reviewer has context)
  3. Apply approved_transitions; record rejected_transitions + verdicts
     in the audit log so the operator can override later
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Iterable, Mapping, Sequence

from .adversarial import (
    AdversarialReviewer,
    ReviewRequest,
    ReviewVerdict,
    StubReviewer,
)
from .lifecycle import LifecycleProposals
from .models import Scope, ScopeTransition


@dataclass(frozen=True)
class GatingResult:
    """Result of running adversarial review over a Tier-2 batch."""

    approved_transitions: tuple[ScopeTransition, ...] = field(default_factory=tuple)
    rejected_transitions: tuple[ScopeTransition, ...] = field(default_factory=tuple)
    verdicts: Mapping[str, ReviewVerdict] = field(default_factory=dict)

    @property
    def total(self) -> int:
        return len(self.approved_transitions) + len(self.rejected_transitions)


def gate_tier_2(
    proposals: LifecycleProposals,
    scope_by_id: Mapping[str, Scope],
    events_for_scope_fn: Callable[[Scope], Sequence[dict]],
    reviewer: AdversarialReviewer | StubReviewer | None = None,
    *,
    extra_context_for: Callable[[ScopeTransition], str | None] | None = None,
) -> GatingResult:
    """Run adversarial review over every Tier-2 transition.

    Args:
        proposals: output of `lifecycle.evaluate_all`.
        scope_by_id: lookup so the reviewer can see the current scope
                     state for each proposal.
        events_for_scope_fn: callable that returns the events touching
                             a given scope. Caller decides how to
                             fetch (full JSONL replay, recent window,
                             prefiltered set).
        reviewer: any reviewer object; defaults to StubReviewer for
                  tests + CI.
        extra_context_for: optional callable returning a string of
                           additional context per transition (e.g.
                           "this scope was flagged for retention by
                           the operator"). Concatenated into the
                           prompt's ADDITIONAL CONTEXT block.

    Returns a GatingResult. The caller decides what to do with
    rejected transitions (skip, escalate, retain for next pass).
    """
    reviewer = reviewer or StubReviewer()

    approved: list[ScopeTransition] = []
    rejected: list[ScopeTransition] = []
    verdicts: dict[str, ReviewVerdict] = {}

    for trans in proposals.tier_2:
        scope = scope_by_id.get(trans.scope_id)
        if scope is None:
            # Defensive: if we can't see the scope we're reviewing,
            # refuse to approve. Better to keep the proposal in the
            # backlog than to apply something we can't audit.
            verdicts[trans.id] = ReviewVerdict(
                verdict="rejected",
                reasoning=(
                    f"scope {trans.scope_id!r} not found in scope_by_id "
                    "at review time; failing safe"
                ),
                provider_name=reviewer.provider_name,
                model_name=reviewer.model_name,
            )
            rejected.append(trans)
            continue

        events = tuple(events_for_scope_fn(scope))
        extra = extra_context_for(trans) if extra_context_for else None
        verdict = reviewer.review(ReviewRequest(
            scope=scope,
            transition=trans,
            relevant_events=events,
            extra_context=extra,
        ))
        verdicts[trans.id] = verdict
        if verdict.verdict == "approved":
            approved.append(trans)
        else:
            rejected.append(trans)

    return GatingResult(
        approved_transitions=tuple(approved),
        rejected_transitions=tuple(rejected),
        verdicts=verdicts,
    )


def annotate_transition_with_verdict(
    transition: ScopeTransition,
    verdict: ReviewVerdict,
) -> ScopeTransition:
    """Return a new transition whose ``reason`` field carries the
    verdict reasoning. Useful for recording approved transitions in
    the store with the adversary's reasoning attached.
    """
    new_reason = (
        f"{transition.reason} | "
        f"adversarial review ({verdict.provider_name}/{verdict.model_name}): "
        f"{verdict.verdict} -- {verdict.reasoning}"
    )
    # Re-use the dataclass replace pattern via .replace would be nicer
    # but the model is plain frozen dataclass; reconstruct.
    return ScopeTransition(
        id=transition.id,
        scope_id=transition.scope_id,
        from_status=transition.from_status,
        to_status=transition.to_status,
        timestamp=transition.timestamp,
        reason=new_reason[:2000],  # respect the max length in the model
        evidence_event_ids=transition.evidence_event_ids,
        rollback_id=transition.rollback_id,
        actor="adversary_rejected" if verdict.verdict == "rejected" else transition.actor,
    )
