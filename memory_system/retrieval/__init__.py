"""Hybrid retrieval pipeline over typed memory events.

Composable pipeline (each stage is a pure function):

    filter_only      -> structured filter by type/actor/workflow/tags/date
    hybrid_search    -> RRF merge of FTS5 results + ChromaDB vector results
    scope_expand     -> expand member-tag hits to all events tagged with
                        the same scope's other member tags
    window_truncate  -> enforce a token budget on the returned set

Each stage takes a ``StageContext`` and returns a (potentially new)
``StageContext``. The full pipeline is ``compose(*stages)``.

Adapted from RTRevenue's collab-memory retrieval pipeline, simplified
to:
  - Use OPAL's existing ChromaDB (no new sqlite-vec dep)
  - Drop the Kuzu graph dependency (graph-hop expansion is handled
    via scope membership instead, since OPAL's scope-aware retrieval
    is the same idea expressed through SQLite scope tables)
  - Stay in pure-stdlib for everything except the optional ChromaDB
    backend
"""

from .pipeline import (
    RetrievalConfig,
    RetrievalHit,
    RetrievalQuery,
    RetrievalResult,
    StageContext,
    compose,
    filter_only,
    hybrid_search,
    scope_expand,
    window_truncate,
)

__all__ = [
    "RetrievalConfig",
    "RetrievalHit",
    "RetrievalQuery",
    "RetrievalResult",
    "StageContext",
    "compose",
    "filter_only",
    "hybrid_search",
    "scope_expand",
    "window_truncate",
]
