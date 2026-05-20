"""Adversarial review for Tier-2 scope transitions.

Per ADR-001, Tier-2 transitions (active -> canonical, * -> deprecated)
are autonomous BUT gated by adversarial review. This module is that
gate.

Design contract:

  - Pure-functional prompt construction; one LLM call per review.
  - Reuses the synthesis layer's pluggable LLM provider
    (`epic_intelligence.synthesis.provider`) so we don't duplicate
    Anthropic/OpenAI/Gemini/stub plumbing.
  - Returns a structured `Verdict` (approved/rejected + reasoning),
    NEVER auto-applies anything itself. Caller (the `gating` layer
    in `lifecycle_gating.py`) decides what to do with verdicts.
  - The adversary's role is to argue AGAINST the proposal — not
    weigh both sides. A separate proposer/judge architecture would
    be a second LLM call; this PR keeps it single-call.
  - The stub provider returns a deterministic APPROVED verdict so
    tests + CI run without API keys. Tests can also inject a
    rejecting/custom reviewer.
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from typing import Iterable, Literal, Mapping, Sequence

from .lifecycle import events_for_scope
from .models import Scope, ScopeTransition
from .transitions import tier_of


Verdict = Literal["approved", "rejected"]


@dataclass(frozen=True)
class ReviewVerdict:
    """The output of one adversarial review.

    Reasoning is mandatory — a verdict without reasoning is useless
    for auditing. ``suggested_alternative`` is a short, optional
    alternative path (e.g. "deprecate instead of canonicalize",
    "wait another 30 days").
    """

    verdict: Verdict
    reasoning: str
    suggested_alternative: str | None = None
    raw_response: str = ""
    provider_name: str = "unknown"
    model_name: str = "unknown"
    metadata: Mapping[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class ReviewRequest:
    """Input to `review()`. Carries enough context for the adversary
    to argue against the transition with specifics."""

    scope: Scope
    transition: ScopeTransition
    relevant_events: tuple[dict, ...] = field(default_factory=tuple)
    extra_context: str | None = None


# ---------------------------------------------------------------------------
# Prompt construction (pure)
# ---------------------------------------------------------------------------


SYSTEM_PROMPT = """\
You are the adversarial reviewer for OPAL's scope lifecycle. The
lifecycle engine just proposed a Tier-2 transition (either
active->canonical or *->deprecated). Your job is to ARGUE AGAINST it
with specifics drawn from the provided context.

You are NOT the judge. You are the loyal opposition. Your default
posture is skeptical. You only return APPROVED when the proposal is
clearly correct AND no plausible counterargument exists.

For active->canonical, the bar is high: the canonical vocabulary is
the predicate engine's source of truth, and a wrong promotion
contaminates retrieval for everyone. Reject if:
  - Member tags are still drifting / not cohesive
  - Activity is concentrated in a single short burst (a "fad")
  - The scope's name + members look like a transient project codename
    that may not survive its sponsor leaving
  - Adjacent canonical concepts already cover this ground

For *->deprecated, the bar is moderate: deprecation is reversible
(deprecated->active is allowed), but every false deprecation costs
the operator one revert. Reject if:
  - The silence could plausibly be a measurement gap (e.g. tags
    moved to a sibling scope but the scope itself is still alive)
  - A recent CONTEXT_CHANGE event suggests the work is dormant
    rather than dead (paused pilot, regulatory wait)
  - The scope was promoted recently (a freshly active scope
    shouldn't deprecate without strong evidence)

Output STRICTLY in this format (the parser depends on it):

  VERDICT: APPROVED
  REASONING: <one to three sentences>
  ALTERNATIVE: <optional, one line; or 'none'>

OR:

  VERDICT: REJECTED
  REASONING: <one to three sentences naming the specific weakness>
  ALTERNATIVE: <one line proposing the next-best action>
"""


def _summarize_events(events: Sequence[dict], cap: int = 8) -> str:
    """Compact one-line-per-event summary for the prompt."""
    if not events:
        return "(no events touching this scope's member tags)"
    by_ts = sorted(events, key=lambda e: e.get("timestamp", ""))
    out: list[str] = []
    for e in by_ts[-cap:]:
        ts = (e.get("timestamp", "") or "")[:19]
        et = e.get("type", "?")
        ac = e.get("actor", "?")
        ti = (e.get("title", "") or "")[:80]
        out.append(f"  {ts} [{et}] {ac}: {ti}")
    if len(events) > cap:
        out.insert(
            0,
            f"  ({len(events) - cap} older event(s) elided; "
            f"showing latest {cap})",
        )
    return "\n".join(out)


def build_review_prompt(req: ReviewRequest) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for the LLM call."""
    s = req.scope
    t = req.transition
    members = ", ".join(s.member_tags) or "(none)"
    aliases = ", ".join(s.name_aliases) if s.name_aliases else "(none)"
    extra = (
        f"\n\nADDITIONAL CONTEXT FROM CALLER:\n{req.extra_context}"
        if req.extra_context else ""
    )

    user_prompt = (
        f"PROPOSED TRANSITION:\n"
        f"  scope_id     : {s.id}\n"
        f"  scope_name   : {s.name}\n"
        f"  aliases      : {aliases}\n"
        f"  current      : {t.from_status}\n"
        f"  proposed     : {t.to_status}\n"
        f"  timestamp    : {t.timestamp}\n"
        f"  reason       : {t.reason}\n\n"
        f"SCOPE STATE:\n"
        f"  first_seen   : {s.first_seen}\n"
        f"  last_seen    : {s.last_seen}\n"
        f"  member_tags  : {members}\n"
        f"  event_count  : {s.event_count}\n"
        f"  session_count: {s.session_count}\n\n"
        f"RECENT EVENTS TOUCHING THIS SCOPE:\n"
        f"{_summarize_events(req.relevant_events)}\n"
        f"{extra}\n\n"
        "Argue AGAINST this transition with specifics. Only approve "
        "if no plausible counterargument exists. Output STRICTLY in "
        "the VERDICT/REASONING/ALTERNATIVE format from the system "
        "prompt."
    )

    return SYSTEM_PROMPT, user_prompt


# ---------------------------------------------------------------------------
# Verdict parsing (pure)
# ---------------------------------------------------------------------------


_VERDICT_RE = re.compile(
    r"^\s*VERDICT\s*:\s*(APPROVED|REJECTED)\b",
    re.IGNORECASE | re.MULTILINE,
)
_REASONING_RE = re.compile(
    r"^\s*REASONING\s*:\s*(.+?)(?=^\s*ALTERNATIVE\s*:|\Z)",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
_ALT_RE = re.compile(
    r"^\s*ALTERNATIVE\s*:\s*(.+?)\s*\Z",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)


def parse_review_response(text: str) -> tuple[Verdict, str, str | None]:
    """Parse the strict VERDICT/REASONING/ALTERNATIVE block.

    Returns (verdict, reasoning, suggested_alternative_or_none).
    Falls back to 'rejected' with a parse-failure reasoning if the
    response doesn't match the expected format — the design is
    fail-safe (a malformed adversary opinion is a rejection by
    default, never an accidental approval).
    """
    m_v = _VERDICT_RE.search(text)
    if not m_v:
        return (
            "rejected",
            "parse failure: adversary response did not match the "
            "required VERDICT/REASONING/ALTERNATIVE format",
            None,
        )
    verdict_token = m_v.group(1).lower()
    verdict: Verdict = "approved" if verdict_token == "approved" else "rejected"

    m_r = _REASONING_RE.search(text)
    reasoning = m_r.group(1).strip() if m_r else "(no reasoning provided)"

    m_a = _ALT_RE.search(text)
    alternative: str | None
    if m_a:
        raw_alt = m_a.group(1).strip()
        alternative = None if raw_alt.lower() in {"none", "n/a", ""} else raw_alt
    else:
        alternative = None

    return verdict, reasoning, alternative


# ---------------------------------------------------------------------------
# Reviewers
# ---------------------------------------------------------------------------


class AdversarialReviewer:
    """The default reviewer.

    Constructed with an LLM provider (any object that satisfies
    `epic_intelligence.synthesis.LlmProvider`). For tests + CI,
    pass `StubReviewer()` from this module instead.
    """

    def __init__(self, provider) -> None:
        self._provider = provider

    @property
    def provider_name(self) -> str:
        return getattr(self._provider, "name", "unknown")

    @property
    def model_name(self) -> str:
        return getattr(self._provider, "model", "unknown")

    def review(self, request: ReviewRequest) -> ReviewVerdict:
        # Sanity: only Tier-2 transitions need adversarial review.
        try:
            t = tier_of(request.transition.from_status, request.transition.to_status)
        except ValueError as exc:
            return ReviewVerdict(
                verdict="rejected",
                reasoning=f"transition is not allowed by the table: {exc}",
                provider_name=self.provider_name,
                model_name=self.model_name,
            )
        if t < 2:
            return ReviewVerdict(
                verdict="approved",
                reasoning=(
                    f"transition is Tier {t}; adversarial review is "
                    "only required for Tier 2. Auto-approving."
                ),
                provider_name=self.provider_name,
                model_name=self.model_name,
                metadata={"tier": t, "skipped_review": True},
            )

        system_prompt, user_prompt = build_review_prompt(request)
        try:
            raw = self._provider.complete(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                max_tokens=512,
                temperature=0.1,  # tighter than synthesis — judgments
                                  # should be more reproducible
            )
        except Exception as exc:
            print(
                f"memory_system.scopes.adversarial: provider call failed "
                f"({exc}); failing safe -> rejected",
                file=sys.stderr,
            )
            return ReviewVerdict(
                verdict="rejected",
                reasoning=f"provider call failed: {exc}; failing safe",
                provider_name=self.provider_name,
                model_name=self.model_name,
            )

        verdict, reasoning, alternative = parse_review_response(raw)
        return ReviewVerdict(
            verdict=verdict,
            reasoning=reasoning,
            suggested_alternative=alternative,
            raw_response=raw,
            provider_name=self.provider_name,
            model_name=self.model_name,
            metadata={"tier": t},
        )


class StubReviewer:
    """Deterministic reviewer for tests + CI. No network.

    Default behavior: approve every Tier-2 transition with a stock
    reason. Tests that need the rejection path can pass
    ``always_reject=True`` or inject a custom ``decide`` callable.
    """

    name = "stub"
    model = "stub-reviewer"

    def __init__(
        self,
        *,
        always_reject: bool = False,
        decide=None,
    ) -> None:
        self._always_reject = always_reject
        self._decide = decide  # optional callable(req) -> (verdict, reasoning, alt)

    @property
    def provider_name(self) -> str:
        return self.name

    @property
    def model_name(self) -> str:
        return self.model

    def review(self, request: ReviewRequest) -> ReviewVerdict:
        try:
            t = tier_of(request.transition.from_status, request.transition.to_status)
        except ValueError as exc:
            return ReviewVerdict(
                verdict="rejected",
                reasoning=f"transition is not allowed by the table: {exc}",
                provider_name=self.name, model_name=self.model,
            )
        if t < 2:
            return ReviewVerdict(
                verdict="approved",
                reasoning=(
                    f"transition is Tier {t}; adversarial review is "
                    "only required for Tier 2. Auto-approving."
                ),
                provider_name=self.name, model_name=self.model,
                metadata={"tier": t, "skipped_review": True},
            )

        if self._decide is not None:
            verdict, reasoning, alternative = self._decide(request)
        elif self._always_reject:
            verdict = "rejected"
            reasoning = "stub reviewer configured to always reject"
            alternative = "approve only after a real adversary reviews this"
        else:
            verdict = "approved"
            reasoning = "stub reviewer auto-approves Tier-2 transitions"
            alternative = None

        raw = (
            f"VERDICT: {verdict.upper()}\n"
            f"REASONING: {reasoning}\n"
            f"ALTERNATIVE: {alternative or 'none'}\n"
        )
        return ReviewVerdict(
            verdict=verdict,
            reasoning=reasoning,
            suggested_alternative=alternative,
            raw_response=raw,
            provider_name=self.name, model_name=self.model,
            metadata={"tier": t},
        )
