"""Scope lifecycle engine.

Pure functions that observe a Scope and the events that mention its
member tags, and *propose* the next status transition:

    provisional -> active      (Tier 1, autonomous w/ rollback window)
    active      -> canonical   (Tier 2, autonomous + adversarial review)
    *           -> deprecated  (Tier 2, autonomous + adversarial review)

Adversarial review is NOT implemented here — Tier-2 proposals are
returned for the caller (CLI / cron / scheduled task) to either
auto-apply or queue for operator confirmation.

Caller responsibility:
  - Tier-1 proposals are safe to auto-commit; the rollback ledger
    (`memory_system/scopes/store.py` transitions table) gives a
    7-day window to revert.
  - Tier-2 proposals SHOULD pass adversarial review before commit.
    Without that gate, treat them as suggestions for the operator.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Iterable, Sequence

from .identifiers import make_rollback_id, make_transition_id
from .models import Scope, ScopeStatus, ScopeTransition
from .transitions import tier_of


@dataclass(frozen=True)
class LifecycleConfig:
    """Tunable thresholds. Defaults from RTRevenue ADR-001."""

    enabled: bool = True

    # provisional -> active (Tier 1)
    promotion_min_sessions: int = 3
    promotion_min_age_days: int = 14

    # active -> canonical (Tier 2)
    canonicalization_min_age_days: int = 180
    canonicalization_min_sessions: int = 8

    # * -> deprecated (Tier 2)
    deprecation_idle_days: int = 90

    # Session boundary
    session_window_hours: int = 6


@dataclass(frozen=True)
class LifecycleProposals:
    tier_1: tuple[ScopeTransition, ...] = field(default_factory=tuple)
    tier_2: tuple[ScopeTransition, ...] = field(default_factory=tuple)

    @property
    def total(self) -> int:
        return len(self.tier_1) + len(self.tier_2)


# ---------------------------------------------------------------------------
# Measurement helpers (pure)
# ---------------------------------------------------------------------------


def _parse_ts(iso: str) -> datetime:
    return datetime.fromisoformat(iso)


def events_for_scope(scope: Scope, events: Iterable[dict]) -> list[dict]:
    """Events whose tag set intersects the scope's member tags."""
    members = set(scope.member_tags)
    if not members:
        return []
    return [e for e in events if members.intersection(e.get("tags") or ())]


def count_distinct_sessions(
    events: Sequence[dict],
    session_window_hours: int,
) -> int:
    """Group events into sessions and return the count."""
    if not events:
        return 0
    parsed: list[tuple[datetime, dict]] = []
    for e in events:
        try:
            parsed.append((_parse_ts(e.get("timestamp", "")), e))
        except ValueError:
            continue
    if not parsed:
        return 0
    parsed.sort(key=lambda kv: kv[0])
    boundary = timedelta(hours=session_window_hours)
    sessions = 1
    last_ts = parsed[0][0]
    for ts, _ in parsed[1:]:
        if ts - last_ts > boundary:
            sessions += 1
        last_ts = ts
    return sessions


def last_activity(events: Sequence[dict]) -> datetime | None:
    if not events:
        return None
    out: datetime | None = None
    for e in events:
        try:
            ts = _parse_ts(e.get("timestamp", ""))
        except ValueError:
            continue
        if out is None or ts > out:
            out = ts
    return out


def _now_utc() -> datetime:
    return datetime.now(timezone.utc)


# ---------------------------------------------------------------------------
# Proposal builders
# ---------------------------------------------------------------------------


def _build_transition(
    scope: Scope,
    to_status: ScopeStatus,
    timestamp: datetime,
    reason: str,
    evidence_event_ids: tuple[str, ...],
) -> ScopeTransition:
    ts_iso = timestamp.isoformat(timespec="seconds")
    transition_id = make_transition_id(
        scope_id=scope.id,
        from_status=scope.status,
        to_status=to_status,
        timestamp_iso=ts_iso,
    )
    rollback_id = make_rollback_id(transition_id)
    tier_of(scope.status, to_status)  # raises if disallowed
    return ScopeTransition(
        id=transition_id,
        scope_id=scope.id,
        from_status=scope.status,
        to_status=to_status,
        timestamp=ts_iso,
        reason=reason,
        evidence_event_ids=evidence_event_ids,
        rollback_id=rollback_id,
        actor="autonomous",
    )


def propose_promotion(
    scope: Scope,
    events: Sequence[dict],
    config: LifecycleConfig,
    now: datetime | None = None,
) -> ScopeTransition | None:
    """Propose provisional -> active when the scope has matured enough."""
    if not config.enabled or scope.status != "provisional":
        return None
    now = now or _now_utc()
    age = now - _parse_ts(scope.first_seen)
    if age < timedelta(days=config.promotion_min_age_days):
        return None
    relevant = events_for_scope(scope, events)
    sessions = count_distinct_sessions(relevant, config.session_window_hours)
    if sessions < config.promotion_min_sessions:
        return None
    evidence = tuple(sorted({e.get("id", "") for e in relevant if e.get("id")}))
    reason = (
        f"promotion: {sessions} sessions over {age.days}d met "
        f"provisional->active criteria "
        f"(>= {config.promotion_min_sessions} sessions, "
        f">= {config.promotion_min_age_days}d age)"
    )
    return _build_transition(scope, "active", now, reason, evidence)


def propose_canonicalization(
    scope: Scope,
    events: Sequence[dict],
    config: LifecycleConfig,
    now: datetime | None = None,
) -> ScopeTransition | None:
    """Propose active -> canonical when the scope has stood the test of time."""
    if not config.enabled or scope.status != "active":
        return None
    now = now or _now_utc()
    age = now - _parse_ts(scope.first_seen)
    if age < timedelta(days=config.canonicalization_min_age_days):
        return None
    relevant = events_for_scope(scope, events)
    sessions = count_distinct_sessions(relevant, config.session_window_hours)
    if sessions < config.canonicalization_min_sessions:
        return None
    evidence = tuple(sorted({e.get("id", "") for e in relevant if e.get("id")}))
    reason = (
        f"canonicalization: {sessions} sessions over {age.days}d met "
        f"active->canonical criteria "
        f"(>= {config.canonicalization_min_sessions} sessions, "
        f">= {config.canonicalization_min_age_days}d age) "
        "-- pending adversarial review"
    )
    return _build_transition(scope, "canonical", now, reason, evidence)


def propose_deprecation(
    scope: Scope,
    events: Sequence[dict],
    config: LifecycleConfig,
    now: datetime | None = None,
) -> ScopeTransition | None:
    """Propose * -> deprecated when the scope has gone idle."""
    if not config.enabled or scope.status == "deprecated":
        return None
    now = now or _now_utc()
    relevant = events_for_scope(scope, events)
    activity = last_activity(relevant)
    if activity is None:
        try:
            activity = _parse_ts(scope.last_seen)
        except ValueError:
            activity = _parse_ts(scope.first_seen)
    idle = now - activity
    if idle < timedelta(days=config.deprecation_idle_days):
        return None
    reason = (
        f"deprecation: scope idle for {idle.days}d "
        f"(threshold {config.deprecation_idle_days}d) -- "
        "no event touched any member tag"
    )
    evidence = tuple(
        e.get("id", "") for e in sorted(
            relevant, key=lambda e: e.get("timestamp", ""), reverse=True,
        )[:5] if e.get("id")
    )
    return _build_transition(scope, "deprecated", now, reason, evidence)


# ---------------------------------------------------------------------------
# Aggregation
# ---------------------------------------------------------------------------


def evaluate(
    scope: Scope,
    events: Sequence[dict],
    config: LifecycleConfig,
    now: datetime | None = None,
) -> list[ScopeTransition]:
    """Run all proposers for one scope. Returns 0 or 1 transitions.

    Deprecation is checked first so an idle scope isn't promoted on
    the same pass.
    """
    for proposer in (propose_deprecation, propose_canonicalization, propose_promotion):
        proposed = proposer(scope, events, config, now=now)
        if proposed is not None:
            return [proposed]
    return []


def evaluate_all(
    scopes: Sequence[Scope],
    events: Sequence[dict],
    config: LifecycleConfig,
    now: datetime | None = None,
) -> LifecycleProposals:
    """Run the engine across many scopes. Splits proposals by tier."""
    if not config.enabled:
        return LifecycleProposals()
    tier_1: list[ScopeTransition] = []
    tier_2: list[ScopeTransition] = []
    for scope in scopes:
        for trans in evaluate(scope, events, config, now=now):
            tier = tier_of(trans.from_status, trans.to_status)
            if tier <= 1:
                tier_1.append(trans)
            else:
                tier_2.append(trans)
    return LifecycleProposals(tier_1=tuple(tier_1), tier_2=tuple(tier_2))


# ---------------------------------------------------------------------------
# Apply
# ---------------------------------------------------------------------------


def apply_transition(scope: Scope, transition: ScopeTransition) -> Scope:
    """Pure: return a new Scope with the transition applied."""
    if transition.scope_id != scope.id:
        raise ValueError(
            f"transition {transition.id} targets {transition.scope_id!r} "
            f"but scope is {scope.id!r}",
        )
    if transition.from_status != scope.status:
        raise ValueError(
            f"transition expects from_status={transition.from_status!r} "
            f"but scope is currently {scope.status!r}",
        )
    new_last = max(scope.last_seen, transition.timestamp)
    return Scope(
        id=scope.id,
        name=scope.name,
        name_aliases=scope.name_aliases,
        status=transition.to_status,
        first_seen=scope.first_seen,
        last_seen=new_last,
        member_tags=scope.member_tags,
        session_count=scope.session_count,
        event_count=scope.event_count,
        promoted_from=scope.status,
        promoted_at=transition.timestamp,
        rollback_id=transition.rollback_id,
        metadata=scope.metadata,
    )
