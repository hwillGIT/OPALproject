"""Typed event schema for the Memory-First Protocol.

Pure stdlib — no Pydantic, no ChromaDB, no Neo4j dependencies. The
schema is enforced by ``validate_event`` and ``new_event`` so any
caller (CLI, bot, test) gets the same validation rules.

Event vocabulary (must match ``bots/shared/workflows/validate.js``
MEMORY_EVENT_TYPES — keep in sync):

- DECISION       — a choice was made; the chooser, options, rationale
- ACTION         — a task was taken or assigned; owner + status
- INSIGHT        — a pattern, finding, or non-obvious fact worth retaining
- PREDICTION     — a falsifiable forecast with confidence + timeframe
- OUTCOME        — observed reality against a prior PREDICTION or ACTION
- DEBATE         — multi-position discussion captured for future reference
- CONTEXT_CHANGE — a meaningful shift in environment (market, regulatory,
                   org, scope) that may invalidate prior decisions
- ARTIFACT       — a concrete deliverable produced (spec, deck, model,
                   diagram, etc.) with a pointer to where it lives

Per-actor write helpers live in ``write.py``; the briefing CLI lives
in ``briefing.py`` and ``cli.py``.
"""
from __future__ import annotations

import json
import re
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable, Mapping

EVENT_TYPES = frozenset({
    "DECISION", "ACTION", "INSIGHT", "PREDICTION",
    "OUTCOME", "DEBATE", "CONTEXT_CHANGE", "ARTIFACT",
})

# Actors include OPAL persona keys plus a few platform identifiers.
# We don't import persona-metadata.js (Python <-> Node boundary); the
# actor field is validated for shape (kebab-case slug) only. Higher
# layers can cross-check against the JS metadata if they wish.
_ACTOR_RE = re.compile(r"^[a-z][a-z0-9-]{1,63}$")
_ID_RE = re.compile(r"^evt-[0-9a-f]{12}$")


class EventValidationError(ValueError):
    """Raised when an event payload fails schema checks."""


@dataclass(frozen=True)
class Event:
    """An immutable typed memory event.

    Fields:
        id:         "evt-" + 12 hex chars (deterministic or random).
        timestamp:  ISO-8601 UTC, e.g. "2026-05-16T13:45:00+00:00".
        type:       One of EVENT_TYPES.
        actor:      Persona key OR platform identifier (e.g.
                    "strategist", "operator", "system").
        workflow:   Optional workflow id this event belongs to
                    (e.g. "clinical-decision-loop"). May be None
                    for free-form events.
        phase:      Optional phase id within the workflow (e.g.
                    "bedside-reality"). May be None.
        title:      Human-readable summary (≤200 chars).
        content:    Full body (≤8000 chars). Markdown allowed.
        tags:       Free-form labels for retrieval (sorted, deduped).
        related:    Tuple of related Event ids (cause/effect, follow-up).
        metadata:   Free-form structured payload — type-specific fields
                    live here (e.g. confidence for PREDICTION, status
                    for ACTION).
    """

    id: str
    timestamp: str
    type: str
    actor: str
    title: str
    content: str
    workflow: str | None = None
    phase: str | None = None
    tags: tuple[str, ...] = field(default_factory=tuple)
    related: tuple[str, ...] = field(default_factory=tuple)
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        d = asdict(self)
        d["tags"] = list(self.tags)
        d["related"] = list(self.related)
        d["metadata"] = dict(self.metadata)
        return d

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), sort_keys=True, separators=(",", ":"))


# ---------------------------------------------------------------------------
# Construction + validation
# ---------------------------------------------------------------------------


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _mint_id() -> str:
    return "evt-" + uuid.uuid4().hex[:12]


def new_event(
    *,
    type: str,
    actor: str,
    title: str,
    content: str,
    workflow: str | None = None,
    phase: str | None = None,
    tags: Iterable[str] = (),
    related: Iterable[str] = (),
    metadata: Mapping[str, Any] | None = None,
    timestamp: str | None = None,
    id: str | None = None,
) -> Event:
    """Construct a validated Event.

    Raises EventValidationError on bad input. Optional ``id`` and
    ``timestamp`` are filled in if not provided.
    """
    ev = Event(
        id=id or _mint_id(),
        timestamp=timestamp or _now_iso(),
        type=type,
        actor=actor,
        title=title,
        content=content,
        workflow=workflow,
        phase=phase,
        tags=tuple(sorted(set(t.strip() for t in tags if t.strip()))),
        related=tuple(related),
        metadata=dict(metadata or {}),
    )
    validate_event(ev)
    return ev


def validate_event(ev: Event) -> None:
    """Raise EventValidationError if ev violates the schema."""
    if not _ID_RE.match(ev.id):
        raise EventValidationError(
            f"id must match {_ID_RE.pattern!r}, got {ev.id!r}",
        )
    if ev.type not in EVENT_TYPES:
        raise EventValidationError(
            f"type {ev.type!r} not in {sorted(EVENT_TYPES)}",
        )
    if not _ACTOR_RE.match(ev.actor):
        raise EventValidationError(
            f"actor {ev.actor!r} must match {_ACTOR_RE.pattern!r}",
        )
    if not ev.title or len(ev.title) > 200:
        raise EventValidationError(
            f"title must be non-empty and ≤200 chars; got len={len(ev.title)}",
        )
    if not ev.content or len(ev.content) > 8000:
        raise EventValidationError(
            f"content must be non-empty and ≤8000 chars; got len={len(ev.content)}",
        )
    try:
        datetime.fromisoformat(ev.timestamp)
    except ValueError as exc:
        raise EventValidationError(
            f"timestamp must be ISO-8601, got {ev.timestamp!r}: {exc}",
        ) from exc
    for r in ev.related:
        if not _ID_RE.match(r):
            raise EventValidationError(
                f"related id {r!r} must match {_ID_RE.pattern!r}",
            )
    # Type-specific metadata requirements:
    if ev.type == "PREDICTION":
        conf = ev.metadata.get("confidence")
        if conf is None:
            raise EventValidationError(
                "PREDICTION events require metadata.confidence in [0.0, 1.0]",
            )
        try:
            cf = float(conf)
        except (TypeError, ValueError) as exc:
            raise EventValidationError(
                f"PREDICTION metadata.confidence must be a number, got {conf!r}",
            ) from exc
        if not 0.0 <= cf <= 1.0:
            raise EventValidationError(
                f"PREDICTION metadata.confidence must be in [0.0, 1.0]; got {cf}",
            )
    if ev.type == "ACTION":
        status = ev.metadata.get("status")
        if status not in {"open", "in-progress", "completed", "cancelled"}:
            raise EventValidationError(
                "ACTION events require metadata.status in "
                "{open, in-progress, completed, cancelled}",
            )
    if ev.type == "OUTCOME":
        if "verifies" not in ev.metadata and not ev.related:
            raise EventValidationError(
                "OUTCOME events require either metadata.verifies (a "
                "prior event id) OR at least one related event id",
            )
