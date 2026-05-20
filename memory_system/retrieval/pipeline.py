"""Composable retrieval pipeline.

Pure functions; the only I/O happens via callbacks passed into the
stage context (FTS lookups, vector lookups, scope membership). This
lets the same stages run in tests with in-memory fakes AND in
production with the real ChromaDB / SQLite backends.

Pipeline stages:

  filter_only(ctx)      structured filter by type/actor/workflow/tags/dates
  hybrid_search(ctx)    RRF-merge FTS5 hits + vector hits
  scope_expand(ctx)     pull events that share a scope membership with a hit
  window_truncate(ctx)  enforce token budget (oldest hits dropped first
                        when sort='timestamp_desc', lowest-score-first
                        when sort='relevance')

Compose them in any order via ``compose(*stages)``.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Iterable, Literal, Mapping, Sequence

SortOrder = Literal["timestamp_desc", "timestamp_asc", "relevance"]


# ---------------------------------------------------------------------------
# Query + result value types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class RetrievalConfig:
    """Pipeline tuning knobs."""

    rrf_constant: int = 60
    default_top_k: int = 12
    max_tokens: int = 1500
    chars_per_token: int = 4


@dataclass(frozen=True)
class RetrievalQuery:
    """A user-facing query into the typed-events memory.

    Fields:
        text         optional free-text query (drives hybrid_search)
        types        restrict to these event types (DECISION, INSIGHT, ...)
        actors       restrict to these actor keys
        workflows    restrict to these workflow ids
        tags_any     match events with ANY of these tags
        tags_all     match events with ALL of these tags
        scopes       expand hits to share these scope ids' member tags
        lookback_days  only consider events within this many days
        top_k        max distinct hits to return
        sort         ordering applied at window_truncate
    """

    text: str | None = None
    types: tuple[str, ...] = ()
    actors: tuple[str, ...] = ()
    workflows: tuple[str, ...] = ()
    tags_any: tuple[str, ...] = ()
    tags_all: tuple[str, ...] = ()
    scopes: tuple[str, ...] = ()
    lookback_days: int | None = None
    top_k: int = 12
    sort: SortOrder = "relevance"


@dataclass(frozen=True)
class RetrievalHit:
    """A scored event in the result set."""

    event: dict
    score: float
    source: str  # 'fts' | 'vector' | 'filter' | 'scope' | 'merged'


@dataclass(frozen=True)
class RetrievalResult:
    hits: tuple[RetrievalHit, ...]
    total_tokens: int
    truncated: bool
    reasoning: str = ""


# ---------------------------------------------------------------------------
# Stage context
# ---------------------------------------------------------------------------


FtsLookup = Callable[[str, int], Sequence[tuple[dict, float]]]
VectorLookup = Callable[[str, int], Sequence[tuple[dict, float]]]
EventIter = Callable[[], Iterable[dict]]
ScopeMembersFor = Callable[[Iterable[str]], dict[str, frozenset[str]]]


@dataclass(frozen=True)
class StageContext:
    """The data + callbacks that flow through every pipeline stage.

    ``hits`` is the cumulative scored list. Stages add to it; the
    final ``window_truncate`` enforces the budget.
    """

    query: RetrievalQuery
    config: RetrievalConfig
    all_events: EventIter
    fts_lookup: FtsLookup | None = None
    vector_lookup: VectorLookup | None = None
    scope_members_for: ScopeMembersFor | None = None
    hits: tuple[RetrievalHit, ...] = field(default_factory=tuple)
    reasoning: str = ""
    truncated: bool = False

    def replace(self, **overrides) -> "StageContext":
        return StageContext(
            query=overrides.get("query", self.query),
            config=overrides.get("config", self.config),
            all_events=overrides.get("all_events", self.all_events),
            fts_lookup=overrides.get("fts_lookup", self.fts_lookup),
            vector_lookup=overrides.get("vector_lookup", self.vector_lookup),
            scope_members_for=overrides.get(
                "scope_members_for", self.scope_members_for,
            ),
            hits=overrides.get("hits", self.hits),
            reasoning=overrides.get("reasoning", self.reasoning),
            truncated=overrides.get("truncated", self.truncated),
        )


def compose(*stages):
    """Compose stages into one callable: ctx -> ctx."""
    def composed(ctx: StageContext) -> StageContext:
        out = ctx
        for stage in stages:
            out = stage(out)
        return out
    return composed


# ---------------------------------------------------------------------------
# Stage: filter_only
# ---------------------------------------------------------------------------


def _passes_filter(event: dict, q: RetrievalQuery) -> bool:
    if q.types and event.get("type") not in q.types:
        return False
    if q.actors and event.get("actor") not in q.actors:
        return False
    if q.workflows and event.get("workflow") not in q.workflows:
        return False
    ev_tags = set(event.get("tags") or ())
    if q.tags_any and not (ev_tags & set(q.tags_any)):
        return False
    if q.tags_all and not set(q.tags_all).issubset(ev_tags):
        return False
    if q.lookback_days is not None:
        from datetime import datetime, timedelta, timezone
        try:
            ts = datetime.fromisoformat(event.get("timestamp", ""))
        except ValueError:
            return False
        cutoff = datetime.now(timezone.utc) - timedelta(days=q.lookback_days)
        if ts < cutoff:
            return False
    return True


def filter_only(ctx: StageContext) -> StageContext:
    """Structured filter pass. Adds all matching events at score=1.0."""
    matched = [
        RetrievalHit(event=e, score=1.0, source="filter")
        for e in ctx.all_events()
        if _passes_filter(e, ctx.query)
    ]
    return ctx.replace(
        hits=tuple(_merge_hits(ctx.hits, matched)),
        reasoning=_append(ctx.reasoning, f"filter_only matched {len(matched)}"),
    )


# ---------------------------------------------------------------------------
# Stage: hybrid_search (RRF merge of FTS + vector)
# ---------------------------------------------------------------------------


def hybrid_search(ctx: StageContext) -> StageContext:
    """RRF-merge FTS5 hits and vector hits for the query text.

    No-op if no text is provided or both lookup callbacks are None.
    """
    q = ctx.query
    if not q.text:
        return ctx
    top_k = max(q.top_k, ctx.config.default_top_k)
    fts_hits: list[tuple[dict, float]] = []
    vec_hits: list[tuple[dict, float]] = []
    if ctx.fts_lookup is not None:
        try:
            fts_hits = list(ctx.fts_lookup(q.text, top_k))
        except Exception:
            fts_hits = []
    if ctx.vector_lookup is not None:
        try:
            vec_hits = list(ctx.vector_lookup(q.text, top_k))
        except Exception:
            vec_hits = []

    rrf_scores: dict[str, float] = {}
    rrf_events: dict[str, dict] = {}
    sources: dict[str, set[str]] = {}
    k = ctx.config.rrf_constant

    for rank, (ev, _) in enumerate(fts_hits, start=1):
        eid = ev.get("id", "")
        if not eid:
            continue
        rrf_scores[eid] = rrf_scores.get(eid, 0.0) + 1.0 / (k + rank)
        rrf_events[eid] = ev
        sources.setdefault(eid, set()).add("fts")

    for rank, (ev, _) in enumerate(vec_hits, start=1):
        eid = ev.get("id", "")
        if not eid:
            continue
        rrf_scores[eid] = rrf_scores.get(eid, 0.0) + 1.0 / (k + rank)
        rrf_events[eid] = ev
        sources.setdefault(eid, set()).add("vector")

    merged = [
        RetrievalHit(
            event=rrf_events[eid],
            score=score,
            source="+".join(sorted(sources[eid])),
        )
        for eid, score in sorted(
            rrf_scores.items(), key=lambda kv: kv[1], reverse=True,
        )
    ]
    return ctx.replace(
        hits=tuple(_merge_hits(ctx.hits, merged)),
        reasoning=_append(
            ctx.reasoning,
            f"hybrid_search merged {len(fts_hits)} fts + {len(vec_hits)} vec",
        ),
    )


# ---------------------------------------------------------------------------
# Stage: scope_expand
# ---------------------------------------------------------------------------


def scope_expand(ctx: StageContext) -> StageContext:
    """For every current hit, expand to events that share a scope membership.

    Looks at each hit's tags, finds the scope ids those tags belong to,
    then includes any event tagged with any of those scopes' other
    member tags.
    """
    if ctx.scope_members_for is None:
        return ctx
    tag_set: set[str] = set()
    for hit in ctx.hits:
        tag_set.update(hit.event.get("tags") or ())
    if ctx.query.scopes:
        scope_map = ctx.scope_members_for(ctx.query.scopes)
    elif tag_set:
        scope_map = ctx.scope_members_for(tag_set)
    else:
        return ctx
    all_member_tags: set[str] = set()
    for tags in scope_map.values():
        all_member_tags.update(tags)
    if not all_member_tags:
        return ctx
    already_have = {h.event.get("id") for h in ctx.hits}
    expanded: list[RetrievalHit] = []
    for ev in ctx.all_events():
        if ev.get("id") in already_have:
            continue
        ev_tags = set(ev.get("tags") or ())
        if ev_tags & all_member_tags:
            expanded.append(RetrievalHit(event=ev, score=0.5, source="scope"))
    return ctx.replace(
        hits=tuple(_merge_hits(ctx.hits, expanded)),
        reasoning=_append(
            ctx.reasoning,
            f"scope_expand added {len(expanded)} via shared scope membership",
        ),
    )


# ---------------------------------------------------------------------------
# Stage: window_truncate
# ---------------------------------------------------------------------------


def window_truncate(ctx: StageContext) -> StageContext:
    """Enforce token budget. Drops oldest / lowest-score hits as needed."""
    q = ctx.query
    sorted_hits = _sort_hits(ctx.hits, q.sort)
    top_k_hits = sorted_hits[: q.top_k]
    chars_per_token = ctx.config.chars_per_token
    max_tokens = ctx.config.max_tokens
    out: list[RetrievalHit] = []
    used = 0
    for hit in top_k_hits:
        cost = (
            len(hit.event.get("title", ""))
            + len(hit.event.get("content", ""))
        ) // chars_per_token
        if used + cost > max_tokens and out:
            return ctx.replace(
                hits=tuple(out),
                truncated=True,
                reasoning=_append(
                    ctx.reasoning,
                    f"window_truncate kept {len(out)}/{len(top_k_hits)} "
                    f"(budget={max_tokens} tokens, used~{used})",
                ),
            )
        out.append(hit)
        used += cost
    return ctx.replace(
        hits=tuple(out),
        truncated=False,
        reasoning=_append(
            ctx.reasoning,
            f"window_truncate kept {len(out)}/{len(top_k_hits)} "
            f"(used~{used} tokens)",
        ),
    )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _merge_hits(
    existing: Sequence[RetrievalHit],
    new: Sequence[RetrievalHit],
) -> list[RetrievalHit]:
    """Merge two lists deduping by event id; keep the higher-scoring entry."""
    out: dict[str, RetrievalHit] = {}
    for hit in existing:
        eid = hit.event.get("id", "")
        if eid:
            out[eid] = hit
    for hit in new:
        eid = hit.event.get("id", "")
        if not eid:
            continue
        prior = out.get(eid)
        if prior is None or hit.score > prior.score:
            out[eid] = hit
    return list(out.values())


def _sort_hits(
    hits: Sequence[RetrievalHit],
    order: SortOrder,
) -> list[RetrievalHit]:
    if order == "timestamp_desc":
        return sorted(
            hits, key=lambda h: h.event.get("timestamp", ""), reverse=True,
        )
    if order == "timestamp_asc":
        return sorted(hits, key=lambda h: h.event.get("timestamp", ""))
    return sorted(hits, key=lambda h: h.score, reverse=True)


def _append(prev: str, line: str) -> str:
    if not prev:
        return line
    return f"{prev}; {line}"


def to_result(ctx: StageContext) -> RetrievalResult:
    """Finalize a StageContext into a RetrievalResult."""
    used = sum(
        (len(h.event.get("title", "")) + len(h.event.get("content", "")))
        // ctx.config.chars_per_token
        for h in ctx.hits
    )
    return RetrievalResult(
        hits=ctx.hits,
        total_tokens=used,
        truncated=ctx.truncated,
        reasoning=ctx.reasoning,
    )
