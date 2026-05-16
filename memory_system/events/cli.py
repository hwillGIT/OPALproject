"""CLI for the Memory-First Protocol.

Subcommands:

    memory event write       Append a typed event to the JSONL log
    memory event briefing    Render a session-start briefing
    memory event rebuild     Replay JSONL log into ChromaDB

Designed for ad-hoc human use AND for the bot orchestrator to shell
out to. Both surfaces are stable.

Usage examples:

    python -m memory_system.events.cli write \\
        --type DECISION --actor strategist \\
        --workflow investor-pitch-review --phase strategic-logic \\
        --title "Lead with the platform thesis" \\
        --content "We chose the platform thesis over the device thesis because..." \\
        --tags pitch,strategy

    python -m memory_system.events.cli briefing --lookback-days 7

    python -m memory_system.events.cli rebuild
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .briefing import briefing_from_log
from .schema import EVENT_TYPES, EventValidationError, new_event
from .write import (
    DEFAULT_CHROMA_COLLECTION,
    DEFAULT_LOG_DIR,
    append_event,
    project_to_chroma,
    rebuild_index,
)


def _cmd_write(args: argparse.Namespace) -> int:
    tags = [t.strip() for t in (args.tags or "").split(",") if t.strip()]
    related = [r.strip() for r in (args.related or "").split(",") if r.strip()]
    metadata = json.loads(args.metadata) if args.metadata else {}
    try:
        ev = new_event(
            type=args.type,
            actor=args.actor,
            title=args.title,
            content=args.content,
            workflow=args.workflow,
            phase=args.phase,
            tags=tags,
            related=related,
            metadata=metadata,
        )
    except EventValidationError as exc:
        print(f"event validation failed: {exc}", file=sys.stderr)
        return 1

    path = append_event(ev, log_dir=args.log_dir)
    print(f"appended {ev.id} -> {path}")
    if args.project:
        ok = project_to_chroma(
            ev,
            collection_name=args.collection,
            chroma_path=args.chroma_path,
        )
        print(f"chroma upsert: {'OK' if ok else 'FAILED (see stderr)'}")
    return 0


def _cmd_briefing(args: argparse.Namespace) -> int:
    text = briefing_from_log(
        log_dir=args.log_dir,
        lookback_days=args.lookback_days,
    )
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"briefing -> {args.out}")
    else:
        sys.stdout.write(text)
    return 0


def _cmd_rebuild(args: argparse.Namespace) -> int:
    seen, ok = rebuild_index(
        log_dir=args.log_dir,
        collection_name=args.collection,
        chroma_path=args.chroma_path,
    )
    print(f"rebuild: saw {seen} events; projected {ok} into ChromaDB")
    return 0 if seen == ok else 1


def _add_log_dir(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--log-dir", type=Path, default=DEFAULT_LOG_DIR,
        help="Directory for the JSONL event log (default: %(default)s)",
    )


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="memory-events")
    sub = p.add_subparsers(dest="cmd", required=True)

    pw = sub.add_parser("write", help="Append a typed event")
    _add_log_dir(pw)
    pw.add_argument("--type", required=True, choices=sorted(EVENT_TYPES))
    pw.add_argument("--actor", required=True,
                    help="Persona key or platform identifier (kebab-case)")
    pw.add_argument("--title", required=True)
    pw.add_argument("--content", required=True)
    pw.add_argument("--workflow", help="Workflow id (e.g. clinical-decision-loop)")
    pw.add_argument("--phase", help="Phase id within the workflow")
    pw.add_argument("--tags", help="Comma-separated tags")
    pw.add_argument("--related", help="Comma-separated related event ids")
    pw.add_argument("--metadata", help="JSON object (type-specific fields)")
    pw.add_argument("--project", action="store_true",
                    help="Also upsert into ChromaDB after the JSONL append")
    pw.add_argument("--collection", default=DEFAULT_CHROMA_COLLECTION)
    pw.add_argument("--chroma-path", type=Path,
                    help="Override ChromaDB persistent directory")
    pw.set_defaults(func=_cmd_write)

    pb = sub.add_parser("briefing", help="Render a session-start briefing")
    _add_log_dir(pb)
    pb.add_argument("--lookback-days", type=int, default=14)
    pb.add_argument("--out", help="Write briefing to file instead of stdout")
    pb.set_defaults(func=_cmd_briefing)

    pr = sub.add_parser("rebuild", help="Replay JSONL log into ChromaDB")
    _add_log_dir(pr)
    pr.add_argument("--collection", default=DEFAULT_CHROMA_COLLECTION)
    pr.add_argument("--chroma-path", type=Path,
                    help="Override ChromaDB persistent directory")
    pr.set_defaults(func=_cmd_rebuild)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
