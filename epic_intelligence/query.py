"""Citation-aware retrieval over the Epic Intelligence index.

Used by the OPAL voice assistant (and by humans on the CLI) to answer
"what does Epic say about X?" with verifiable cites back to the exact
Epic doc page and section. Pure retrieval — no LLM call here. The
caller (voice assistant, chat surface) feeds these hits into its own
prompt template.

CLI:

    python -m epic_intelligence.query \\
        "How does SMART on FHIR handle patient context at launch?" \\
        --top-k 5

    python -m epic_intelligence.query "OAuth scope for medications" --json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .index.embedder import get_embedder
from .index.store import EpicIntelligenceStore, QueryHit, DEFAULT_INDEX_DIR


def query(
    text: str,
    top_k: int = 5,
    index_dir: Path = DEFAULT_INDEX_DIR,
    collection: str = "epic_intelligence",
    embedder_pref: str = "auto",
) -> list[QueryHit]:
    """Run a citation-aware similarity query."""
    embedder, name = get_embedder(prefer=embedder_pref)
    store = EpicIntelligenceStore(
        embedder=embedder,
        embedder_name=name,
        index_dir=index_dir,
        collection_name=collection,
    )
    return store.query(text, n_results=top_k)


def format_hit_pretty(hit: QueryHit, idx: int) -> str:
    section = " > ".join(hit.section_path) if hit.section_path else "(top)"
    url = hit.source_url or "(no source url)"
    score = f"{hit.score:.3f}"
    return (
        f"[{idx}] {hit.title}\n"
        f"    section: {section}\n"
        f"    source : {url}\n"
        f"    score  : {score}  (cosine distance - lower = closer)\n"
        f"    chunk  : {hit.chunk_id}\n"
        f"    ---\n"
        f"    {hit.snippet}\n"
    )


def format_hit_json(hit: QueryHit) -> dict:
    return {
        "chunk_id": hit.chunk_id,
        "score": hit.score,
        "title": hit.title,
        "source_url": hit.source_url,
        "section_path": list(hit.section_path),
        "snippet": hit.snippet,
        "metadata": hit.metadata,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Query the Epic Intelligence index with citations.",
    )
    parser.add_argument("query_text", help="Natural-language question or keywords.")
    parser.add_argument("--top-k", type=int, default=5,
                        help="Number of hits to return (default: 5).")
    parser.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR,
                        help="ChromaDB persistent directory.")
    parser.add_argument("--collection", default="epic_intelligence",
                        help="Collection name.")
    parser.add_argument("--embedder", default="auto",
                        choices=["auto", "default", "gemini"],
                        help="Embedder backend.")
    parser.add_argument("--json", action="store_true",
                        help="Emit JSON instead of pretty text.")
    args = parser.parse_args(argv)

    hits = query(
        text=args.query_text,
        top_k=args.top_k,
        index_dir=args.index_dir,
        collection=args.collection,
        embedder_pref=args.embedder,
    )
    if not hits:
        print("(no results - index may be empty; run the ingestion pipeline first)",
              file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(
            {
                "query": args.query_text,
                "hits": [format_hit_json(h) for h in hits],
            },
            indent=2,
        ))
    else:
        print(f"# Query: {args.query_text!r} - top {len(hits)} hits\n")
        for i, hit in enumerate(hits, 1):
            print(format_hit_pretty(hit, i))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
