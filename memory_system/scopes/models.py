"""Frozen value types for the scope primitive.

Pure-stdlib + dataclasses (no Pydantic dependency). Mirrors the shape
of the RTRevenue collab-memory scope models, adapted to OPAL's
existing memory_system conventions (string-typed timestamps as
ISO-8601, matching `memory_system/events/schema.py`).
"""
from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from typing import Any, Literal, Mapping

ScopeStatus = Literal["provisional", "active", "canonical", "deprecated"]
TransitionActor = Literal["autonomous", "operator", "adversary_rejected"]

_SCOPE_ID_RE = re.compile(r"^scope-[a-z0-9][a-z0-9-]{0,127}$")
_TRANSITION_ID_RE = re.compile(r"^trans-[0-9a-f]{12}$")
_ROLLBACK_ID_RE = re.compile(r"^rb-[0-9a-f]{12}$")

VALID_STATUSES: tuple[ScopeStatus, ...] = (
    "provisional", "active", "canonical", "deprecated",
)
VALID_ACTORS: tuple[TransitionActor, ...] = (
    "autonomous", "operator", "adversary_rejected",
)


class ScopeValidationError(ValueError):
    """Raised when a Scope / ScopeMember / ScopeTransition violates shape."""


def _ensure(condition: bool, msg: str) -> None:
    if not condition:
        raise ScopeValidationError(msg)


@dataclass(frozen=True)
class Scope:
    """A named cluster of related provisional tags with its own lifecycle."""

    id: str
    name: str
    status: ScopeStatus
    first_seen: str  # ISO-8601
    last_seen: str   # ISO-8601
    name_aliases: tuple[str, ...] = field(default_factory=tuple)
    member_tags: tuple[str, ...] = field(default_factory=tuple)
    session_count: int = 0
    event_count: int = 0
    promoted_from: ScopeStatus | None = None
    promoted_at: str | None = None
    rollback_id: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        _ensure(
            _SCOPE_ID_RE.match(self.id) is not None,
            f"scope.id must match {_SCOPE_ID_RE.pattern!r}, got {self.id!r}",
        )
        _ensure(1 <= len(self.name) <= 128,
                f"scope.name must be 1..128 chars; got len={len(self.name)}")
        _ensure(self.status in VALID_STATUSES,
                f"scope.status must be in {VALID_STATUSES}; got {self.status!r}")
        _ensure(self.session_count >= 0,
                f"scope.session_count must be >= 0; got {self.session_count}")
        _ensure(self.event_count >= 0,
                f"scope.event_count must be >= 0; got {self.event_count}")
        if self.rollback_id is not None:
            _ensure(_ROLLBACK_ID_RE.match(self.rollback_id) is not None,
                    f"scope.rollback_id must match "
                    f"{_ROLLBACK_ID_RE.pattern!r}; got {self.rollback_id!r}")
        if self.promoted_from is not None:
            _ensure(self.promoted_from in VALID_STATUSES,
                    f"scope.promoted_from must be in {VALID_STATUSES}; "
                    f"got {self.promoted_from!r}")

    def to_dict(self) -> dict:
        d = asdict(self)
        d["name_aliases"] = list(self.name_aliases)
        d["member_tags"] = list(self.member_tags)
        d["metadata"] = dict(self.metadata)
        return d


@dataclass(frozen=True)
class ScopeMember:
    """A provisional tag's membership in a Scope."""

    scope_id: str
    tag: str
    joined_at: str   # ISO-8601
    last_seen: str   # ISO-8601
    event_count: int = 0
    namespaced_form: str | None = None
    graduated: bool = False

    def __post_init__(self) -> None:
        _ensure(_SCOPE_ID_RE.match(self.scope_id) is not None,
                f"scope_id must match {_SCOPE_ID_RE.pattern!r}; "
                f"got {self.scope_id!r}")
        _ensure(1 <= len(self.tag) <= 128,
                f"tag must be 1..128 chars; got len={len(self.tag)}")
        _ensure(self.event_count >= 0,
                f"event_count must be >= 0; got {self.event_count}")
        if self.namespaced_form is not None:
            _ensure(len(self.namespaced_form) <= 256,
                    "namespaced_form must be <= 256 chars")

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class ScopeTransition:
    """Immutable record of a status transition for one Scope."""

    id: str
    scope_id: str
    to_status: ScopeStatus
    timestamp: str   # ISO-8601
    reason: str
    from_status: ScopeStatus | None = None
    evidence_event_ids: tuple[str, ...] = field(default_factory=tuple)
    rollback_id: str | None = None
    actor: TransitionActor = "autonomous"

    def __post_init__(self) -> None:
        _ensure(_TRANSITION_ID_RE.match(self.id) is not None,
                f"transition.id must match {_TRANSITION_ID_RE.pattern!r}; "
                f"got {self.id!r}")
        _ensure(_SCOPE_ID_RE.match(self.scope_id) is not None,
                f"scope_id must match {_SCOPE_ID_RE.pattern!r}; "
                f"got {self.scope_id!r}")
        _ensure(self.to_status in VALID_STATUSES,
                f"to_status must be in {VALID_STATUSES}; got {self.to_status!r}")
        if self.from_status is not None:
            _ensure(self.from_status in VALID_STATUSES,
                    f"from_status must be in {VALID_STATUSES}; "
                    f"got {self.from_status!r}")
        _ensure(self.actor in VALID_ACTORS,
                f"actor must be in {VALID_ACTORS}; got {self.actor!r}")
        _ensure(len(self.reason) <= 2000,
                f"reason must be <= 2000 chars; got len={len(self.reason)}")
        if self.rollback_id is not None:
            _ensure(_ROLLBACK_ID_RE.match(self.rollback_id) is not None,
                    f"rollback_id must match {_ROLLBACK_ID_RE.pattern!r}; "
                    f"got {self.rollback_id!r}")

    def to_dict(self) -> dict:
        d = asdict(self)
        d["evidence_event_ids"] = list(self.evidence_event_ids)
        return d
