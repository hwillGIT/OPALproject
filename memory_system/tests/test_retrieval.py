"""Unit tests for the retrieval pipeline (filter / hybrid / scope / window)."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from memory_system.retrieval import (
    RetrievalConfig,
    RetrievalQuery,
    StageContext,
    compose,
    filter_only,
    hybrid_search,
    scope_expand,
    window_truncate,
)
from memory_system.retrieval.pipeline import to_result


def _utc(day: int = 16, hour: int = 12) -> str:
    return datetime(2026, 5, day, hour, tzinfo=timezone.utc).isoformat()


def _event(eid: str, **overrides) -> dict:
    base = {
        "id": eid,
        "timestamp": _utc(),
        "type": "INSIGHT",
        "actor": "strategist",
        "title": "t",
        "content": "c",
        "tags": [],
        "metadata": {},
    }
    base.update(overrides)
    return base


# --------------------------------------------------------------------------
# filter_only
# --------------------------------------------------------------------------


class TestFilterOnly:
    def test_filter_by_type(self) -> None:
        events = [
            _event("evt-a", type="DECISION"),
            _event("evt-b", type="INSIGHT"),
            _event("evt-c", type="DECISION"),
        ]
        q = RetrievalQuery(types=("DECISION",))
        ctx = StageContext(
            query=q, config=RetrievalConfig(),
            all_events=lambda: events,
        )
        out = filter_only(ctx)
        assert {h.event["id"] for h in out.hits} == {"evt-a", "evt-c"}

    def test_filter_by_tags_any(self) -> None:
        events = [
            _event("evt-a", tags=["aurora", "pitch"]),
            _event("evt-b", tags=["unrelated"]),
            _event("evt-c", tags=["pitch"]),
        ]
        q = RetrievalQuery(tags_any=("aurora", "pitch"))
        ctx = StageContext(query=q, config=RetrievalConfig(),
                            all_events=lambda: events)
        out = filter_only(ctx)
        assert {h.event["id"] for h in out.hits} == {"evt-a", "evt-c"}

    def test_filter_by_tags_all(self) -> None:
        events = [
            _event("evt-a", tags=["aurora", "pitch"]),
            _event("evt-b", tags=["aurora"]),
            _event("evt-c", tags=["aurora", "pitch", "extra"]),
        ]
        q = RetrievalQuery(tags_all=("aurora", "pitch"))
        ctx = StageContext(query=q, config=RetrievalConfig(),
                            all_events=lambda: events)
        out = filter_only(ctx)
        assert {h.event["id"] for h in out.hits} == {"evt-a", "evt-c"}

    def test_filter_by_actor(self) -> None:
        events = [
            _event("evt-a", actor="strategist"),
            _event("evt-b", actor="hardware-lead"),
        ]
        q = RetrievalQuery(actors=("strategist",))
        ctx = StageContext(query=q, config=RetrievalConfig(),
                            all_events=lambda: events)
        out = filter_only(ctx)
        assert {h.event["id"] for h in out.hits} == {"evt-a"}


# --------------------------------------------------------------------------
# hybrid_search (RRF merge)
# --------------------------------------------------------------------------


class TestHybridSearch:
    def test_merges_fts_and_vector_hits(self) -> None:
        fts_pool = [(_event("evt-fts1"), 0.9), (_event("evt-both"), 0.7)]
        vec_pool = [(_event("evt-both"), 0.85), (_event("evt-vec1"), 0.8)]

        def fts(text, k):
            return fts_pool[:k]

        def vec(text, k):
            return vec_pool[:k]

        q = RetrievalQuery(text="anything", top_k=10)
        ctx = StageContext(
            query=q, config=RetrievalConfig(),
            all_events=lambda: [],
            fts_lookup=fts, vector_lookup=vec,
        )
        out = hybrid_search(ctx)
        ids = {h.event["id"] for h in out.hits}
        assert ids == {"evt-fts1", "evt-both", "evt-vec1"}
        # evt-both should rank highest (in both pools)
        sorted_hits = sorted(out.hits, key=lambda h: h.score, reverse=True)
        assert sorted_hits[0].event["id"] == "evt-both"
        assert "+" in sorted_hits[0].source  # merged source

    def test_no_text_is_noop(self) -> None:
        q = RetrievalQuery()
        ctx = StageContext(query=q, config=RetrievalConfig(),
                            all_events=lambda: [],
                            fts_lookup=lambda t, k: [(_event("x"), 1.0)])
        out = hybrid_search(ctx)
        assert out.hits == ()


# --------------------------------------------------------------------------
# scope_expand
# --------------------------------------------------------------------------


class TestScopeExpand:
    def test_expands_via_shared_scope_membership(self) -> None:
        e_seed = _event("evt-seed", tags=["aurora"])
        e_other = _event("evt-other", tags=["pillar-deck"])
        e_unrel = _event("evt-unrel", tags=["unrelated"])

        def scope_for(tags):
            # Both 'aurora' and 'pillar-deck' belong to one scope.
            if {"aurora", "pillar-deck"} & set(tags):
                return {"scope-aurora-2026-05": frozenset(
                    {"aurora", "pillar-deck", "engaged-fleet"},
                )}
            return {}

        q = RetrievalQuery()
        ctx = StageContext(
            query=q, config=RetrievalConfig(),
            all_events=lambda: [e_seed, e_other, e_unrel],
            scope_members_for=scope_for,
            hits=(
                # Pretend a previous stage already matched the seed.
                __import__("memory_system.retrieval.pipeline",
                            fromlist=["RetrievalHit"]).RetrievalHit(
                    event=e_seed, score=1.0, source="filter",
                ),
            ),
        )
        out = scope_expand(ctx)
        ids = {h.event["id"] for h in out.hits}
        assert "evt-other" in ids
        assert "evt-unrel" not in ids


# --------------------------------------------------------------------------
# window_truncate
# --------------------------------------------------------------------------


class TestWindowTruncate:
    def test_respects_top_k(self) -> None:
        from memory_system.retrieval.pipeline import RetrievalHit
        hits = tuple(
            RetrievalHit(event=_event(f"evt-{i}"), score=float(i),
                         source="filter")
            for i in range(20)
        )
        q = RetrievalQuery(top_k=5)
        ctx = StageContext(
            query=q, config=RetrievalConfig(max_tokens=1_000_000),
            all_events=lambda: [], hits=hits,
        )
        out = window_truncate(ctx)
        assert len(out.hits) == 5
        # Highest scores kept
        assert {h.score for h in out.hits} == {15.0, 16.0, 17.0, 18.0, 19.0}

    def test_token_budget_truncates(self) -> None:
        from memory_system.retrieval.pipeline import RetrievalHit
        # Each event has ~500 chars in content => ~125 tokens at
        # chars_per_token=4. Three events => ~375 tokens.
        big_content = "x" * 500
        hits = tuple(
            RetrievalHit(
                event=_event(f"evt-{i}", content=big_content),
                score=float(i), source="filter",
            )
            for i in range(5)
        )
        q = RetrievalQuery(top_k=10)
        ctx = StageContext(
            query=q, config=RetrievalConfig(max_tokens=300),
            all_events=lambda: [], hits=hits,
        )
        out = window_truncate(ctx)
        assert out.truncated is True
        assert len(out.hits) < 5


# --------------------------------------------------------------------------
# composed pipeline
# --------------------------------------------------------------------------


def test_composed_pipeline_end_to_end() -> None:
    events = [
        _event("evt-1", type="DECISION", tags=["aurora"]),
        _event("evt-2", type="DECISION", tags=["other"]),
        _event("evt-3", type="INSIGHT", tags=["aurora"]),
        _event("evt-4", type="DECISION", tags=["aurora", "other"]),
    ]
    q = RetrievalQuery(types=("DECISION",), tags_any=("aurora",), top_k=10)
    ctx = StageContext(
        query=q, config=RetrievalConfig(),
        all_events=lambda: events,
    )
    pipeline = compose(filter_only, window_truncate)
    out = pipeline(ctx)
    result = to_result(out)
    ids = {h.event["id"] for h in result.hits}
    assert ids == {"evt-1", "evt-4"}
