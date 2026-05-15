"""End-to-end ingestion pipeline: scraper output → chunker → ChromaDB.

The Node-based scraper writes three sibling directories per site:

    output/
      markdown/<site>/_Foo_<hash>.md     ← human-readable + agent-readable text
      structured/<site>/_Foo_<hash>.json ← URL, title, headings, links, ...
      raw/<site>/_Foo_<hash>.html        ← original HTML (not used here)

The chunker (`epic_intelligence/ingestion/chunker.py`) chunks markdown and
optionally consumes a sibling JSON for URL/title metadata. Its
`chunk_directory` only looks for that JSON next to the markdown file —
which doesn't match the scraper layout. This pipeline bridges that gap:

  1. For each markdown file, look up the matching `structured/.../*.json`
     (by basename, swapping suffix), so URL + title flow into chunks.
  2. Chunk it.
  3. Upsert chunks into the `EpicIntelligenceStore`.

It also accepts arbitrary curated markdown files outside the scraper
output (e.g., `docs/analysis/epic-clinical-data-patient-context.md`)
via `--extra-doc PATH [URL]`.

CLI:

    python -m epic_intelligence.ingestion.pipeline \\
        --scraper-output epic_intelligence/scraper/output \\
        --site open_epic \\
        --extra-doc docs/analysis/epic-clinical-data-patient-context.md \\
            https://fhir.epic.com/Documentation
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

from .chunker import EpicDocChunker
from ..index.store import EpicIntelligenceStore, DEFAULT_INDEX_DIR


@dataclass(frozen=True)
class IngestStats:
    files_processed: int
    chunks_emitted: int
    chunks_upserted: int
    skipped_files: int


def _load_structured_metadata(structured_dir: Path, md_path: Path) -> dict:
    """Find the scraper-produced JSON metadata for a markdown file, if any."""
    if not structured_dir.exists():
        return {}
    candidate = structured_dir / md_path.with_suffix(".json").name
    if not candidate.exists():
        return {}
    try:
        return json.loads(candidate.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(
            f"epic_intelligence.pipeline: bad JSON {candidate}: {exc}",
            file=sys.stderr,
        )
        return {}


def ingest_scraped_site(
    scraper_output: Path,
    site: str,
    store: EpicIntelligenceStore,
    config_name: str = "default",
) -> IngestStats:
    """Ingest one site's scraped markdown into the store.

    Looks under ``<scraper_output>/markdown/<site>/`` for `*.md` and
    pairs each with the matching JSON in ``<scraper_output>/structured/<site>/``.
    """
    chunker = EpicDocChunker(config_name=config_name)
    md_dir = scraper_output / "markdown" / site
    structured_dir = scraper_output / "structured" / site
    if not md_dir.exists():
        print(f"epic_intelligence.pipeline: no markdown at {md_dir}",
              file=sys.stderr)
        return IngestStats(0, 0, 0, 0)

    files_processed = 0
    chunks_emitted = 0
    chunks_upserted = 0
    skipped = 0

    for md_path in sorted(md_dir.glob("*.md")):
        try:
            content = md_path.read_text(encoding="utf-8", errors="ignore")
        except OSError as exc:
            print(f"epic_intelligence.pipeline: cannot read {md_path}: {exc}",
                  file=sys.stderr)
            skipped += 1
            continue

        meta = _load_structured_metadata(structured_dir, md_path)
        url = meta.get("url", "")
        title = meta.get("title", md_path.stem)

        chunks = chunker.chunk_document(
            markdown=content,
            source_file=str(md_path),
            source_url=url,
            doc_title=title,
        )
        if not chunks:
            skipped += 1
            continue
        files_processed += 1
        chunks_emitted += len(chunks)
        chunks_upserted += store.upsert_chunks([c.to_dict() for c in chunks])

    return IngestStats(
        files_processed=files_processed,
        chunks_emitted=chunks_emitted,
        chunks_upserted=chunks_upserted,
        skipped_files=skipped,
    )


def ingest_extra_doc(
    md_path: Path,
    source_url: str,
    store: EpicIntelligenceStore,
    config_name: str = "playbook",
    title: str = "",
) -> IngestStats:
    """Ingest a single curated markdown file (not from the scraper)."""
    if not md_path.exists():
        print(f"epic_intelligence.pipeline: missing extra doc {md_path}",
              file=sys.stderr)
        return IngestStats(0, 0, 0, 1)
    chunker = EpicDocChunker(config_name=config_name)
    content = md_path.read_text(encoding="utf-8", errors="ignore")
    chunks = chunker.chunk_document(
        markdown=content,
        source_file=str(md_path),
        source_url=source_url,
        doc_title=title or md_path.stem,
    )
    if not chunks:
        return IngestStats(0, 0, 0, 1)
    n = store.upsert_chunks([c.to_dict() for c in chunks])
    return IngestStats(1, len(chunks), n, 0)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Ingest scraped Epic docs into the Epic Intelligence Layer index.",
    )
    parser.add_argument(
        "--scraper-output", type=Path,
        default=Path("epic_intelligence/scraper/output"),
        help="Root of scraper output (containing markdown/, structured/, raw/).",
    )
    parser.add_argument(
        "--site", action="append", default=None,
        help="Site key under markdown/ to ingest (repeatable). "
             "Defaults to all subdirectories.",
    )
    parser.add_argument(
        "--extra-doc", action="append", nargs="+", default=[],
        metavar=("PATH", "URL"),
        help="Curated markdown to ingest. Form: 'PATH [URL] [TITLE]' (repeatable).",
    )
    parser.add_argument(
        "--config", default="default",
        choices=list(EpicDocChunker.CONFIGS.keys()),
        help="Chunker configuration to use for scraped sites.",
    )
    parser.add_argument(
        "--index-dir", type=Path, default=DEFAULT_INDEX_DIR,
        help="ChromaDB persistent directory (default: .chroma/epic_intelligence).",
    )
    parser.add_argument(
        "--collection", default="epic_intelligence",
        help="ChromaDB collection name (default: epic_intelligence).",
    )
    parser.add_argument(
        "--embedder", default="auto", choices=["auto", "default", "gemini"],
        help="Which embedder to use. Default uses Gemini iff GOOGLE_API_KEY is set.",
    )
    parser.add_argument(
        "--reset", action="store_true",
        help="Drop and recreate the collection before ingestion.",
    )
    args = parser.parse_args(argv)

    from ..index.embedder import get_embedder
    embedder, name = get_embedder(prefer=args.embedder)
    print(f"epic_intelligence: using embedder = {name}")

    store = EpicIntelligenceStore(
        embedder=embedder,
        embedder_name=name,
        index_dir=args.index_dir,
        collection_name=args.collection,
    )
    if args.reset:
        store.reset()
        print(f"epic_intelligence: reset collection '{args.collection}'")

    md_root = args.scraper_output / "markdown"
    sites = args.site
    if not sites:
        sites = (
            sorted(p.name for p in md_root.iterdir() if p.is_dir())
            if md_root.exists()
            else []
        )

    totals = IngestStats(0, 0, 0, 0)
    for site in sites:
        s = ingest_scraped_site(args.scraper_output, site, store,
                                config_name=args.config)
        print(f"  site '{site}': "
              f"{s.files_processed} files → {s.chunks_emitted} chunks "
              f"({s.chunks_upserted} upserted, {s.skipped_files} skipped)")
        totals = IngestStats(
            totals.files_processed + s.files_processed,
            totals.chunks_emitted + s.chunks_emitted,
            totals.chunks_upserted + s.chunks_upserted,
            totals.skipped_files + s.skipped_files,
        )

    for entry in args.extra_doc:
        path = Path(entry[0])
        url = entry[1] if len(entry) > 1 else ""
        title = entry[2] if len(entry) > 2 else ""
        s = ingest_extra_doc(path, url, store, title=title)
        print(f"  extra '{path.name}': "
              f"{s.files_processed} files → {s.chunks_emitted} chunks "
              f"({s.chunks_upserted} upserted, {s.skipped_files} skipped)")
        totals = IngestStats(
            totals.files_processed + s.files_processed,
            totals.chunks_emitted + s.chunks_emitted,
            totals.chunks_upserted + s.chunks_upserted,
            totals.skipped_files + s.skipped_files,
        )

    print()
    print(f"total: {totals.files_processed} files → "
          f"{totals.chunks_emitted} chunks "
          f"({totals.chunks_upserted} upserted, "
          f"{totals.skipped_files} skipped); "
          f"collection size now = {store.count()}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
