"""Burst-detection engine for the scope primitive.

Pure functions over typed events (`memory_system/events/schema.py`).
Given a stream of events, a set of known tags (canonical ontology +
tags already attached to existing scopes), and a configuration,
returns zero or more ScopeCandidate proposals.

Two triggers (preserved from RTRevenue ADR-001):

  1. Single-event burst — one event introduces ≥N new provisional tags
  2. Windowed co-occurrence — a new tag co-occurs with ≥M other
     unattached provisionals inside a tight time window

Materialization is deterministic: scope id, transition id, and
rollback id all derive from content. Replaying the event log
produces identical scope identities.
"""
from __future__ import annotations

from collections import OrderedDict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import AbstractSet, Iterable, Sequence

from .identifiers import (
    make_rollback_id,
    make_scope_id,
    make_transition_id,
    slugify,
)
from .models import Scope, ScopeMember, ScopeTransition
from .transitions import tier_of


@dataclass(frozen=True)
class BurstDetectionConfig:
    """Tunable thresholds. Defaults from RTRevenue ADR-001."""

    enabled: bool = True
    min_new_tags_in_event: int = 3
    window_hours: int = 24
    min_co_occurrence: int = 2


@dataclass(frozen=True)
class ScopeCandidate:
    """An immutable proposal for a (None -> provisional) Tier-0 transition."""

    proposed_name: str
    member_tags: tuple[str, ...]
    evidence_event_ids: tuple[str, ...]
    first_seen: str  # ISO-8601
    last_seen: str   # ISO-8601
    reason: str


@dataclass(frozen=True)
class ScopeMaterialization:
    """The persistable shape: Scope + ScopeMember[] + ScopeTransition."""

    scope: Scope
    members: tuple[ScopeMember, ...]
    transition: ScopeTransition


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _event_tags(event: dict) -> tuple[str, ...]:
    return tuple(event.get("tags") or ())


def _event_id(event: dict) -> str:
    return event.get("id") or ""


def _event_timestamp(event: dict) -> str:
    return event.get("timestamp") or ""


def _parse_ts(iso: str) -> datetime:
    return datetime.fromisoformat(iso)


def _provisional_in(event: dict, known: AbstractSet[str]) -> tuple[str, ...]:
    return tuple(t for t in _event_tags(event) if t and t not in known)


def propose_name_from_tags(tags: Sequence[str]) -> str:
    """Pick a display name for a candidate scope from its provisional tags.

    Heuristic, in order:
      1. First single-token slug of length >= 4 (codename like 'aurora').
      2. Longest tag by character count.
      3. ``cluster-{slugified_first_tag}`` (degenerate fallback).

    Stable under input order — replay determinism depends on it.
    """
    if not tags:
        raise ValueError("cannot name an empty cluster")
    for t in tags:
        slug = slugify(t)
        if not slug:
            continue
        if "-" not in slug and len(slug) >= 4:
            return t
    longest = max(tags, key=lambda x: (len(x), x))
    if slugify(longest):
        return longest
    fallback = slugify(tags[0]) or "unnamed"
    return f"cluster-{fallback}"


# ---------------------------------------------------------------------------
# Detection (pure)
# ---------------------------------------------------------------------------


def detect_event_burst(
    event: dict,
    known_tags: AbstractSet[str],
    config: BurstDetectionConfig,
) -> ScopeCandidate | None:
    """Single-event burst: N or more new provisional tags in one event."""
    if not config.enabled:
        return None
    new_tags = _provisional_in(event, known_tags)
    if len(new_tags) < config.min_new_tags_in_event:
        return None
    name = propose_name_from_tags(new_tags)
    ts = _event_timestamp(event)
    return ScopeCandidate(
        proposed_name=name,
        member_tags=tuple(sorted(set(new_tags))),
        evidence_event_ids=(_event_id(event),),
        first_seen=ts,
        last_seen=ts,
        reason=(
            f"single-event burst: {len(new_tags)} new provisional tags "
            f"introduced in event {_event_id(event)}"
        ),
    )


def detect_window_burst(
    event: dict,
    recent_events: Sequence[dict],
    known_tags: AbstractSet[str],
    config: BurstDetectionConfig,
) -> ScopeCandidate | None:
    """Cross-event burst over a recent time window."""
    if not config.enabled:
        return None
    try:
        now_ts = _parse_ts(_event_timestamp(event))
    except ValueError:
        return None
    cutoff = now_ts - timedelta(hours=config.window_hours)

    in_window: list[dict] = [event]
    for prior in recent_events:
        if _event_id(prior) == _event_id(event):
            continue
        try:
            ts = _parse_ts(_event_timestamp(prior))
        except ValueError:
            continue
        if ts < cutoff or ts > now_ts:
            continue
        in_window.append(prior)

    contributors: list[dict] = []
    union_tags: list[str] = []
    seen: set[str] = set()
    for ev in in_window:
        new = _provisional_in(ev, known_tags)
        if not new:
            continue
        contributors.append(ev)
        for t in new:
            if t not in seen:
                seen.add(t)
                union_tags.append(t)

    if not _provisional_in(event, known_tags):
        return None
    if len(contributors) < config.min_co_occurrence:
        return None
    if len(union_tags) < config.min_new_tags_in_event:
        return None

    ordered = sorted(contributors, key=lambda e: _event_timestamp(e))
    first_ts = _event_timestamp(ordered[0])
    last_ts = _event_timestamp(ordered[-1])
    name = propose_name_from_tags(union_tags)
    return ScopeCandidate(
        proposed_name=name,
        member_tags=tuple(sorted(set(union_tags))),
        evidence_event_ids=tuple(_event_id(e) for e in ordered),
        first_seen=first_ts,
        last_seen=last_ts,
        reason=(
            f"windowed co-occurrence burst: {len(union_tags)} provisional tags "
            f"across {len(contributors)} events within "
            f"{config.window_hours}h of {_event_id(event)}"
        ),
    )


def detect(
    event: dict,
    recent_events: Sequence[dict],
    known_tags: AbstractSet[str],
    config: BurstDetectionConfig,
) -> list[ScopeCandidate]:
    """Run all detectors. Returns 0 or 1 candidates.

    Single-event is preferred over windowed when both fire — smaller
    evidence set, cleaner naming, more deterministic under reorder.
    """
    single = detect_event_burst(event, known_tags, config)
    if single is not None:
        return [single]
    windowed = detect_window_burst(event, recent_events, known_tags, config)
    if windowed is not None:
        return [windowed]
    return []


# ---------------------------------------------------------------------------
# Materialization
# ---------------------------------------------------------------------------


def materialize(
    candidate: ScopeCandidate,
    actor: str = "autonomous",
    metadata: dict | None = None,
) -> ScopeMaterialization:
    """Turn a candidate into the (Scope, members, transition) triple."""
    scope_id = make_scope_id(candidate.proposed_name, candidate.first_seen)
    transition_id = make_transition_id(
        scope_id=scope_id,
        from_status=None,
        to_status="provisional",
        timestamp_iso=candidate.first_seen,
    )
    rollback_id = make_rollback_id(transition_id)

    # Sanity check that the transition table allows this move.
    tier_of(None, "provisional")  # raises if not allowed

    scope = Scope(
        id=scope_id,
        name=candidate.proposed_name,
        status="provisional",
        first_seen=candidate.first_seen,
        last_seen=candidate.last_seen,
        member_tags=candidate.member_tags,
        session_count=1,
        event_count=len(candidate.evidence_event_ids),
        rollback_id=rollback_id,
        metadata=dict(metadata or {}),
    )
    members = tuple(
        ScopeMember(
            scope_id=scope_id,
            tag=tag,
            joined_at=candidate.first_seen,
            last_seen=candidate.last_seen,
            event_count=1,
        )
        for tag in candidate.member_tags
    )
    transition = ScopeTransition(
        id=transition_id,
        scope_id=scope_id,
        from_status=None,
        to_status="provisional",
        timestamp=candidate.first_seen,
        reason=candidate.reason,
        evidence_event_ids=candidate.evidence_event_ids,
        rollback_id=rollback_id,
        actor=actor,  # type: ignore[arg-type]
    )
    return ScopeMaterialization(
        scope=scope, members=members, transition=transition,
    )


# ---------------------------------------------------------------------------
# Stream replay (for rebuild-from-JSONL)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ReplayState:
    known_tags: frozenset[str]
    scope_index: dict[str, str] = field(default_factory=dict)
    materialized: tuple[ScopeMaterialization, ...] = field(default_factory=tuple)


def absorb(state: ReplayState, mat: ScopeMaterialization) -> ReplayState:
    new_index = dict(state.scope_index)
    for member in mat.members:
        new_index[member.tag] = mat.scope.id
    return ReplayState(
        known_tags=state.known_tags | frozenset(mat.scope.member_tags),
        scope_index=new_index,
        materialized=(*state.materialized, mat),
    )


def replay(
    events: Iterable[dict],
    canonical_tags: AbstractSet[str],
    config: BurstDetectionConfig,
    window_size: int = 200,
) -> ReplayState:
    """Replay typed events through the detector, growing known_tags as scopes
    are created. Used by rebuild to reconstruct scope state from JSONL."""
    state = ReplayState(known_tags=frozenset(canonical_tags))
    recent: list[dict] = []
    for event in events:
        cands = detect(event, recent, state.known_tags, config)
        for cand in cands:
            mat = materialize(cand)
            state = absorb(state, mat)
        recent.append(event)
        if len(recent) > window_size:
            del recent[0 : len(recent) - window_size]
    return state
