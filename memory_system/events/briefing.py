"""Session-start briefing — what changed since you were last here.

A briefing answers two questions from the operator's perspective:

1. **What decisions / outcomes did the team record while I was away?**
2. **What's open right now — pending ACTIONs, in-flight PREDICTIONs
   whose timeframe has passed, recent CONTEXT_CHANGEs that may
   invalidate prior plans?**

Pure-stdlib. Reads the JSONL log. ChromaDB is *not* required for
briefings — semantic search is a later enrichment.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable

from .write import read_log

# --------------------------------------------------------------------------
# Data shapes
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class BriefingSummary:
    """The shape returned by `summarize_log`. Stable across renderers."""

    window_start: str
    window_end: str
    by_type: dict[str, list[dict]]
    open_actions: list[dict]
    overdue_predictions: list[dict]
    recent_context_changes: list[dict]
    recent_outcomes: list[dict]
    actor_activity: dict[str, int]
    total_events: int


# --------------------------------------------------------------------------
# Pure summarization
# --------------------------------------------------------------------------


def _parse_ts(ts: str) -> datetime:
    return datetime.fromisoformat(ts)


def summarize_log(
    events: Iterable[dict],
    *,
    since: datetime | None = None,
    now: datetime | None = None,
) -> BriefingSummary:
    """Build a BriefingSummary from a stream of event dicts.

    Args:
        events: dicts as produced by `read_log()`.
        since: only consider events with timestamp >= since. Default
               is now - 14 days.
        now: clock injection for tests. Default: datetime.now(UTC).
    """
    now = now or datetime.now(timezone.utc)
    since = since or (now - timedelta(days=14))

    by_type: dict[str, list[dict]] = defaultdict(list)
    open_actions: list[dict] = []
    overdue_predictions: list[dict] = []
    recent_context_changes: list[dict] = []
    recent_outcomes: list[dict] = []
    actor_activity: dict[str, int] = defaultdict(int)
    total = 0

    for ev in events:
        try:
            ts = _parse_ts(ev["timestamp"])
        except (KeyError, ValueError):
            continue
        if ts < since:
            # Out-of-window for type buckets — but still consider for
            # open actions / overdue predictions (they're forever-open
            # until something supersedes them).
            ev_type = ev.get("type")
            if ev_type == "ACTION":
                status = (ev.get("metadata") or {}).get("status")
                if status in {"open", "in-progress"}:
                    open_actions.append(ev)
            elif ev_type == "PREDICTION":
                if _prediction_is_overdue(ev, now):
                    overdue_predictions.append(ev)
            continue

        total += 1
        ev_type = ev.get("type", "UNKNOWN")
        by_type[ev_type].append(ev)
        actor_activity[ev.get("actor", "unknown")] += 1

        if ev_type == "ACTION":
            status = (ev.get("metadata") or {}).get("status")
            if status in {"open", "in-progress"}:
                open_actions.append(ev)
        elif ev_type == "PREDICTION":
            if _prediction_is_overdue(ev, now):
                overdue_predictions.append(ev)
        elif ev_type == "CONTEXT_CHANGE":
            recent_context_changes.append(ev)
        elif ev_type == "OUTCOME":
            recent_outcomes.append(ev)

    # Dedupe open_actions (could be added in both branches above).
    open_actions = _dedupe_by_id(open_actions)
    overdue_predictions = _dedupe_by_id(overdue_predictions)

    return BriefingSummary(
        window_start=since.isoformat(timespec="seconds"),
        window_end=now.isoformat(timespec="seconds"),
        by_type=dict(by_type),
        open_actions=open_actions,
        overdue_predictions=overdue_predictions,
        recent_context_changes=recent_context_changes,
        recent_outcomes=recent_outcomes,
        actor_activity=dict(actor_activity),
        total_events=total,
    )


def _prediction_is_overdue(ev: dict, now: datetime) -> bool:
    md = ev.get("metadata") or {}
    horizon = md.get("horizon")
    if not horizon:
        return False
    try:
        deadline = _parse_ts(horizon)
    except ValueError:
        return False
    return deadline <= now and not md.get("resolved")


def _dedupe_by_id(events: list[dict]) -> list[dict]:
    seen: set[str] = set()
    out: list[dict] = []
    for ev in events:
        eid = ev.get("id")
        if eid and eid not in seen:
            seen.add(eid)
            out.append(ev)
    return out


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------


def render_briefing(summary: BriefingSummary, *, max_per_bucket: int = 10) -> str:
    """Plain-text briefing for terminal / Mattermost paste."""
    lines: list[str] = []
    lines.append(
        f"# Briefing - window {summary.window_start} -> {summary.window_end}"
    )
    lines.append(
        f"  {summary.total_events} events in window; "
        f"{len(summary.actor_activity)} distinct actors"
    )
    lines.append("")

    if summary.open_actions:
        lines.append(f"## Open actions ({len(summary.open_actions)})")
        for ev in summary.open_actions[:max_per_bucket]:
            owner = (ev.get("metadata") or {}).get("owner", "unassigned")
            status = (ev.get("metadata") or {}).get("status", "?")
            lines.append(
                f"  - [{status}] {ev.get('title', '(no title)')} "
                f"(owner: {owner}; id: {ev.get('id')})"
            )
        if len(summary.open_actions) > max_per_bucket:
            lines.append(
                f"  ... and {len(summary.open_actions) - max_per_bucket} more"
            )
        lines.append("")

    if summary.overdue_predictions:
        lines.append(
            f"## Overdue predictions ({len(summary.overdue_predictions)})"
        )
        for ev in summary.overdue_predictions[:max_per_bucket]:
            md = ev.get("metadata") or {}
            lines.append(
                f"  - [conf={md.get('confidence', '?')}] "
                f"{ev.get('title', '(no title)')} "
                f"(horizon: {md.get('horizon', '?')}; id: {ev.get('id')})"
            )
        lines.append("")

    if summary.recent_context_changes:
        lines.append(
            f"## Recent CONTEXT_CHANGE ({len(summary.recent_context_changes)})"
        )
        for ev in summary.recent_context_changes[:max_per_bucket]:
            lines.append(
                f"  - {ev.get('title', '(no title)')} "
                f"(actor: {ev.get('actor', '?')}; id: {ev.get('id')})"
            )
        lines.append("")

    if summary.recent_outcomes:
        lines.append(
            f"## Recent OUTCOMEs ({len(summary.recent_outcomes)})"
        )
        for ev in summary.recent_outcomes[:max_per_bucket]:
            md = ev.get("metadata") or {}
            verifies = md.get("verifies") or ", ".join(ev.get("related") or [])
            lines.append(
                f"  - {ev.get('title', '(no title)')} "
                f"(verifies: {verifies or '?'}; id: {ev.get('id')})"
            )
        lines.append("")

    by_type = summary.by_type
    if by_type:
        lines.append("## Counts by type (in window)")
        for t in sorted(by_type):
            lines.append(f"  {t}: {len(by_type[t])}")
        lines.append("")

    if summary.actor_activity:
        lines.append("## Activity by actor (in window)")
        for actor, n in sorted(
            summary.actor_activity.items(), key=lambda kv: (-kv[1], kv[0])
        ):
            lines.append(f"  {actor}: {n}")

    return "\n".join(lines) + "\n"


def briefing_from_log(
    log_dir: Path | None = None,
    *,
    lookback_days: int = 14,
    now: datetime | None = None,
) -> str:
    """End-to-end helper: read log -> summarize -> render."""
    now = now or datetime.now(timezone.utc)
    since = now - timedelta(days=lookback_days)
    summary = summarize_log(read_log(log_dir), since=since, now=now)
    return render_briefing(summary)
