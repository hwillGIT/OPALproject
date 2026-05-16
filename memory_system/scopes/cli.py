"""CLI for the scope subsystem.

Subcommands:

    python -m memory_system.scopes.cli list [--status ...] [--format pretty|json]
    python -m memory_system.scopes.cli lifecycle [--apply] [--apply-tier-2]
    python -m memory_system.scopes.cli revert <rollback_id>
    python -m memory_system.scopes.cli rebuild [--log-dir DIR]
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from ..events.write import DEFAULT_LOG_DIR, read_log
from .detect import BurstDetectionConfig, replay
from .lifecycle import (
    LifecycleConfig,
    apply_transition,
    evaluate_all,
)
from .models import ScopeTransition, VALID_STATUSES
from .store import (
    DEFAULT_DB_PATH,
    append_transition,
    find_transition_by_rollback,
    get_scope,
    index_all,
    list_scopes,
    list_transitions,
    open_db,
    upsert_scope,
)


def _format_scope_pretty(s) -> str:
    return (
        f"- **{s.id}** [{s.status}] {s.name} -- "
        f"{len(s.member_tags)} member(s), {s.event_count} event(s), "
        f"first_seen={s.first_seen[:10]}"
    )


def _format_transition_pretty(t: ScopeTransition) -> str:
    rb = f" rollback={t.rollback_id}" if t.rollback_id else ""
    return (
        f"- **{t.scope_id}** {t.from_status or '(none)'} -> {t.to_status} "
        f"@ {t.timestamp[:10]} -- {t.reason}{rb}"
    )


def _cmd_list(args: argparse.Namespace) -> int:
    conn = open_db(args.db_path)
    try:
        statuses = tuple(args.status or ())
        scopes = list_scopes(conn, statuses=statuses, limit=args.limit)
    finally:
        conn.close()

    if args.format == "json":
        print(json.dumps(
            [
                {
                    "id": s.id, "name": s.name, "status": s.status,
                    "member_tags": list(s.member_tags),
                    "first_seen": s.first_seen, "last_seen": s.last_seen,
                    "event_count": s.event_count,
                    "session_count": s.session_count,
                    "rollback_id": s.rollback_id,
                }
                for s in scopes
            ],
            indent=2,
        ))
        return 0

    if not scopes:
        print("# no scopes found")
        return 0
    print(f"# {len(scopes)} scope(s)")
    for s in scopes:
        print(_format_scope_pretty(s))
        if args.verbose:
            for tag in s.member_tags:
                print(f"    - {tag}")
    return 0


def _cmd_lifecycle(args: argparse.Namespace) -> int:
    cfg = LifecycleConfig()
    if not cfg.enabled:
        print("# lifecycle: disabled in config")
        return 0
    conn = open_db(args.db_path)
    try:
        scopes = list_scopes(conn)
        events = list(read_log(args.log_dir))
        proposals = evaluate_all(scopes, events, cfg)

        if proposals.total == 0:
            print("# lifecycle: no transitions proposed")
            return 0

        print(f"# lifecycle: {proposals.total} proposal(s)")
        if proposals.tier_1:
            print(f"\n## Tier 1 ({len(proposals.tier_1)}) -- "
                  "autonomous, rollback window")
            for t in proposals.tier_1:
                print(_format_transition_pretty(t))
        if proposals.tier_2:
            print(f"\n## Tier 2 ({len(proposals.tier_2)}) -- "
                  "pending adversarial review")
            for t in proposals.tier_2:
                print(_format_transition_pretty(t))

        if not args.apply and not args.apply_tier_2:
            print("\n# dry-run -- pass --apply to commit Tier 1, "
                  "--apply-tier-2 to also commit Tier 2")
            return 0

        scope_by_id = {s.id: s for s in scopes}
        applied = 0
        to_apply: list[ScopeTransition] = []
        if args.apply:
            to_apply.extend(proposals.tier_1)
        if args.apply_tier_2:
            to_apply.extend(proposals.tier_2)

        for trans in to_apply:
            scope = scope_by_id.get(trans.scope_id)
            if scope is None:
                print(
                    f"warn: scope {trans.scope_id!r} disappeared; skipping",
                    file=sys.stderr,
                )
                continue
            updated = apply_transition(scope, trans)
            upsert_scope(conn, updated)
            append_transition(conn, trans)
            scope_by_id[scope.id] = updated
            applied += 1
        conn.commit()
        print(f"\n# applied {applied} transition(s)")
    finally:
        conn.close()
    return 0


def _cmd_revert(args: argparse.Namespace) -> int:
    """Reverse a Tier-1 transition within its rollback window.

    Appends a new compensating transition (not destructive). The
    rolled-back scope status returns to its prior value.
    """
    conn = open_db(args.db_path)
    try:
        t = find_transition_by_rollback(conn, args.rollback_id)
        if t is None:
            print(
                f"revert: no transition found for rollback_id={args.rollback_id!r}",
                file=sys.stderr,
            )
            return 1
        if t.from_status is None:
            print(
                "revert: cannot revert a (None -> provisional) creation "
                "transition this way; use 'deprecate' instead",
                file=sys.stderr,
            )
            return 1
        scope = get_scope(conn, t.scope_id)
        if scope is None:
            print(f"revert: scope {t.scope_id!r} no longer exists",
                  file=sys.stderr)
            return 1
        if scope.status != t.to_status:
            print(
                f"revert: scope is in status {scope.status!r}, but the "
                f"target transition moved it to {t.to_status!r}. Cannot "
                "safely revert -- newer transition(s) intervened.",
                file=sys.stderr,
            )
            return 1

        from .identifiers import make_rollback_id, make_transition_id
        now_iso = datetime.now(timezone.utc).isoformat(timespec="seconds")
        compensating = ScopeTransition(
            id=make_transition_id(
                scope_id=t.scope_id,
                from_status=t.to_status,
                to_status=t.from_status,
                timestamp_iso=now_iso,
            ),
            scope_id=t.scope_id,
            from_status=t.to_status,
            to_status=t.from_status,  # type: ignore[arg-type]
            timestamp=now_iso,
            reason=f"revert of transition {t.id} (rollback_id={t.rollback_id})",
            evidence_event_ids=t.evidence_event_ids,
            rollback_id=make_rollback_id(
                make_transition_id(
                    scope_id=t.scope_id,
                    from_status=t.to_status,
                    to_status=t.from_status,
                    timestamp_iso=now_iso,
                ),
            ),
            actor="operator",
        )
        updated = apply_transition(scope, compensating)
        upsert_scope(conn, updated)
        append_transition(conn, compensating)
        conn.commit()
        print(
            f"reverted: {scope.id} {t.to_status} -> {t.from_status} "
            f"(new transition {compensating.id})",
        )
    finally:
        conn.close()
    return 0


def _cmd_rebuild(args: argparse.Namespace) -> int:
    """Rebuild scope state from the JSONL log."""
    cfg = BurstDetectionConfig()
    canonical: set[str] = set()
    try:
        from ..ontology.loader import all_tags as ontology_tags
        from ..ontology.loader import load_taxonomy
        from .auto_detect import DEFAULT_TAXONOMY_PATH
        tx = load_taxonomy(args.taxonomy_path or DEFAULT_TAXONOMY_PATH)
        canonical = ontology_tags(tx)
    except Exception as exc:
        print(
            f"rebuild: taxonomy unavailable ({exc}); treating all tags "
            "as provisional",
            file=sys.stderr,
        )

    events = list(read_log(args.log_dir))
    state = replay(events, canonical_tags=canonical, config=cfg)

    if not args.write:
        print(
            f"# rebuild dry-run: would create {len(state.materialized)} "
            f"scope(s) from {len(events)} events",
        )
        return 0

    conn = open_db(args.db_path)
    try:
        s_n, m_n, t_n = index_all(
            conn,
            scopes=[m.scope for m in state.materialized],
            members=[mem for mat in state.materialized for mem in mat.members],
            transitions=[m.transition for m in state.materialized],
        )
        conn.commit()
        print(f"# rebuild: scopes={s_n} members={m_n} transitions={t_n}")
    finally:
        conn.close()
    return 0


def _add_db_path(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--db-path", type=Path, default=DEFAULT_DB_PATH,
                        help="Scopes SQLite path (default: %(default)s)")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="memory-scopes")
    sub = p.add_subparsers(dest="cmd", required=True)

    pl = sub.add_parser("list", help="List inferred scopes")
    _add_db_path(pl)
    pl.add_argument("--status", nargs="*",
                    choices=list(VALID_STATUSES),
                    help="Filter by status (any of)")
    pl.add_argument("--limit", type=int, default=100)
    pl.add_argument("--format", choices=["pretty", "json"], default="pretty")
    pl.add_argument("--verbose", "-v", action="store_true")
    pl.set_defaults(func=_cmd_list)

    pc = sub.add_parser("lifecycle", help="Evaluate lifecycle transitions")
    _add_db_path(pc)
    pc.add_argument("--log-dir", type=Path, default=DEFAULT_LOG_DIR,
                    help="Events JSONL log directory")
    pc.add_argument("--apply", action="store_true",
                    help="Auto-apply Tier-1 promotions")
    pc.add_argument("--apply-tier-2", action="store_true",
                    help="Also auto-apply Tier-2 (canonicalization, deprecation)")
    pc.set_defaults(func=_cmd_lifecycle)

    pr = sub.add_parser("revert", help="Reverse a Tier-1 transition")
    _add_db_path(pr)
    pr.add_argument("rollback_id", help="The rollback_id of the transition to undo")
    pr.set_defaults(func=_cmd_revert)

    pb = sub.add_parser("rebuild", help="Rebuild scopes from the JSONL event log")
    _add_db_path(pb)
    pb.add_argument("--log-dir", type=Path, default=DEFAULT_LOG_DIR)
    pb.add_argument("--taxonomy-path", type=Path,
                    help="Override ontology taxonomy JSON")
    pb.add_argument("--write", action="store_true",
                    help="Actually write to the scopes DB (default: dry-run)")
    pb.set_defaults(func=_cmd_rebuild)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
