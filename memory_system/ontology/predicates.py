"""Predicate engine — proactive pub/sub over the typed-events memory.

Predicates declare:

  - trigger:   when this fires (session_start | pre_query | post_write)
  - match:     structured filter (types, actors, tags, lookback_days, ...)
  - expand:    optional taxonomy expansion (broader/narrower depth)
  - window:    token budget + sort order applied to the result

The engine is evaluated by the briefing / orchestrator code; it does
not own any I/O of its own (events are passed in by the caller).

Predicate file format (JSON):

  [
    {
      "id": "open-actions",
      "trigger": "session_start",
      "match": {"types": ["ACTION"], "tags_any": []},
      "filter_metadata": {"status": ["open", "in-progress"]},
      "expand": null,
      "window": {"max_events": 20, "sort": "timestamp_desc"}
    },
    ...
  ]
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Literal, Mapping

Trigger = Literal["session_start", "pre_query", "post_write"]
SortOrder = Literal["timestamp_desc", "timestamp_asc", "relevance"]


@dataclass(frozen=True)
class MatchFilter:
    types: tuple[str, ...] = ()
    actors: tuple[str, ...] = ()
    workflows: tuple[str, ...] = ()
    tags_any: tuple[str, ...] = ()
    tags_all: tuple[str, ...] = ()
    lookback_days: int | None = None


@dataclass(frozen=True)
class ExpandConfig:
    broader_depth: int = 0
    narrower_depth: int = 0


@dataclass(frozen=True)
class WindowConfig:
    max_events: int = 12
    sort: SortOrder = "timestamp_desc"


@dataclass(frozen=True)
class Predicate:
    id: str
    trigger: Trigger
    match: MatchFilter = field(default_factory=MatchFilter)
    expand: ExpandConfig = field(default_factory=ExpandConfig)
    window: WindowConfig = field(default_factory=WindowConfig)
    filter_metadata: Mapping[str, tuple[str, ...]] = field(default_factory=dict)
    description: str = ""


# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------


def load_predicates(path: Path) -> list[Predicate]:
    """Parse a JSON predicates file."""
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError(
            f"predicates file at {path} must be a JSON array; "
            f"got {type(raw).__name__}",
        )
    out: list[Predicate] = []
    for entry in raw:
        if not isinstance(entry, dict):
            continue
        m = entry.get("match") or {}
        e = entry.get("expand") or {}
        w = entry.get("window") or {}
        fm = entry.get("filter_metadata") or {}
        out.append(Predicate(
            id=str(entry.get("id")),
            trigger=entry.get("trigger", "session_start"),
            description=str(entry.get("description", "")),
            match=MatchFilter(
                types=tuple(m.get("types") or ()),
                actors=tuple(m.get("actors") or ()),
                workflows=tuple(m.get("workflows") or ()),
                tags_any=tuple(m.get("tags_any") or ()),
                tags_all=tuple(m.get("tags_all") or ()),
                lookback_days=m.get("lookback_days"),
            ),
            expand=ExpandConfig(
                broader_depth=int(e.get("broader_depth", 0) or 0),
                narrower_depth=int(e.get("narrower_depth", 0) or 0),
            ),
            window=WindowConfig(
                max_events=int(w.get("max_events", 12) or 12),
                sort=w.get("sort", "timestamp_desc"),
            ),
            filter_metadata={
                k: tuple(v) if isinstance(v, list) else (str(v),)
                for k, v in fm.items()
            },
        ))
    return out


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------


def _match_event(event: dict, p: Predicate) -> bool:
    m = p.match
    if m.types and event.get("type") not in m.types:
        return False
    if m.actors and event.get("actor") not in m.actors:
        return False
    if m.workflows and event.get("workflow") not in m.workflows:
        return False
    ev_tags = set(event.get("tags") or ())
    if m.tags_any and not (ev_tags & set(m.tags_any)):
        return False
    if m.tags_all and not set(m.tags_all).issubset(ev_tags):
        return False
    if m.lookback_days is not None:
        from datetime import datetime, timedelta, timezone
        try:
            ts = datetime.fromisoformat(event.get("timestamp", ""))
        except ValueError:
            return False
        cutoff = datetime.now(timezone.utc) - timedelta(days=m.lookback_days)
        if ts < cutoff:
            return False
    if p.filter_metadata:
        md = event.get("metadata") or {}
        for key, allowed_values in p.filter_metadata.items():
            actual = md.get(key)
            if str(actual) not in allowed_values:
                return False
    return True


def _sort_events(events: list[dict], order: SortOrder) -> list[dict]:
    if order == "timestamp_desc":
        return sorted(events, key=lambda e: e.get("timestamp", ""), reverse=True)
    if order == "timestamp_asc":
        return sorted(events, key=lambda e: e.get("timestamp", ""))
    return list(events)  # relevance is computed elsewhere


def evaluate_predicate(
    predicate: Predicate,
    events: Iterable[dict],
) -> list[dict]:
    """Run one predicate over a stream of events; return matching set."""
    matched = [e for e in events if _match_event(e, predicate)]
    matched = _sort_events(matched, predicate.window.sort)
    return matched[: predicate.window.max_events]


def evaluate_trigger(
    predicates: Iterable[Predicate],
    trigger: Trigger,
    events: Iterable[dict],
) -> dict[str, list[dict]]:
    """Run every predicate matching the given trigger.

    Returns {predicate_id -> matching events}. Events are realized once
    into a list since each predicate re-scans it.
    """
    realized = list(events)
    out: dict[str, list[dict]] = {}
    for p in predicates:
        if p.trigger != trigger:
            continue
        out[p.id] = evaluate_predicate(p, realized)
    return out
