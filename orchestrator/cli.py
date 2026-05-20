"""CLI for the workflow orchestrator.

    python -m orchestrator.cli list
    python -m orchestrator.cli show <workflow-name>
    python -m orchestrator.cli run <workflow-name> [--provider stub|auto|...]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .loader import (
    BUSINESS_DIR,
    Workflow,
    WorkflowValidationError,
    iter_workflows,
    list_workflows,
    load_workflow,
)
from .persona import PERSONAS_DIR, PersonaNotFound, load_persona
from .runner import RunnerConfig, WorkflowResult, WorkflowRunner


def _cmd_list(args: argparse.Namespace) -> int:
    paths = list_workflows(args.business_dir)
    if not paths:
        print("# no business workflows found")
        return 0
    print(f"# {len(paths)} business workflow(s) under {args.business_dir}")
    for path in paths:
        try:
            wf = load_workflow(path)
            print(f"  - {wf.name}  ({wf.domain})  {len(wf.phases)} phases  emits {','.join(wf.emits)}")
        except WorkflowValidationError as exc:
            print(f"  - {path.name}  FAILED VALIDATION: {exc}")
    return 0


def _cmd_show(args: argparse.Namespace) -> int:
    try:
        wf = load_workflow(args.name, args.business_dir)
    except WorkflowValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"# Workflow: {wf.name}")
    print(f"  category    : {wf.category}")
    print(f"  domain      : {wf.domain}")
    print(f"  version     : {wf.version}")
    print(f"  emits       : {', '.join(wf.emits)}")
    print(f"  source      : {wf.source_path}")
    print("\n  backpressure:")
    for b in wf.backpressure:
        print(f"    - {b}")
    print("\n  phases:")
    for phase in wf.phases:
        print(f"    [{phase.id}] lead={phase.lead}"
              f"  supporting={list(phase.supporting) or '-'}")
        if phase.tensions:
            print(f"      tensions: {', '.join(phase.tensions)}")
        if phase.pattern:
            print(f"      pattern: {phase.pattern}")
        print(f"      output: {phase.output}")
    return 0


def _cmd_run(args: argparse.Namespace) -> int:
    try:
        wf = load_workflow(args.name, args.business_dir)
    except WorkflowValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    # Build provider per the --provider flag, defaulting to stub so
    # this command runs without API keys in CI / new envs.
    from .provider import get_provider
    provider = get_provider(args.provider)

    # Build the event sink — by default append to the JSONL log; in
    # --dry-run mode just count them, never write.
    from memory_system.events.write import append_event
    if args.dry_run:
        emitted_events: list = []

        def sink(ev):
            emitted_events.append(ev)
    else:
        emitted_events = None  # not tracked separately in real mode

        def sink(ev):
            append_event(ev)

    config = RunnerConfig(
        max_tokens_per_phase=args.max_tokens,
        temperature=args.temperature,
        initial_context=args.context or "",
    )

    try:
        runner = WorkflowRunner(
            provider=provider,
            event_sink=sink,
            config=config,
        )
        result = runner.run(wf)
    except PersonaNotFound as exc:
        print(f"error: {exc}", file=sys.stderr)
        print(
            "(personas live under bots/shared/personas/gtm/; "
            "see bots/shared/personas/DEPARTMENTS.md for the roster)",
            file=sys.stderr,
        )
        return 2

    if args.json:
        _print_run_json(result, dry_run=args.dry_run)
    else:
        _print_run_pretty(result, dry_run=args.dry_run)
    return 0


def _print_run_pretty(result: WorkflowResult, *, dry_run: bool) -> None:
    print(f"# Run: {result.workflow.name}")
    print(f"  provider={result.provider_name} model={result.model_name}")
    print(f"  phases={len(result.phase_results)}  "
          f"backpressure={result.backpressure_status}")
    if dry_run:
        print("  (dry-run: events NOT appended to the JSONL log)")
    print()
    for pr in result.phase_results:
        print(f"## phase {pr.phase.id}  (lead: {pr.persona.name} / {pr.persona.label})")
        print(f"   emitted: {', '.join(pr.emitted_event_ids) or '(none — persona judged nothing memory-worthy)'}")
        if pr.triggered_predicates:
            tp_lines = ", ".join(
                f"{pid}({len(ids)})" for pid, ids in pr.triggered_predicates.items()
            )
            print(f"   tripped predicates: {tp_lines}")
        print()
        # First ~30 lines of the (clean, emit-stripped) response
        for line in pr.response_text.splitlines()[:30]:
            print(f"    {line}")
        if len(pr.response_text.splitlines()) > 30:
            print(f"    ... ({len(pr.response_text.splitlines()) - 30} more lines)")
        print()


def _print_run_json(result: WorkflowResult, *, dry_run: bool) -> None:
    out = {
        "workflow": result.workflow.name,
        "provider": result.provider_name,
        "model": result.model_name,
        "backpressure_status": result.backpressure_status,
        "dry_run": dry_run,
        "phases": [
            {
                "id": pr.phase.id,
                "lead_persona": {
                    "key": pr.persona.key,
                    "name": pr.persona.name,
                    "label": pr.persona.label,
                },
                "response": pr.response_text,
                "emitted_event_ids": list(pr.emitted_event_ids),
                "triggered_predicates": {
                    pid: list(ids) for pid, ids in pr.triggered_predicates.items()
                },
            }
            for pr in result.phase_results
        ],
    }
    print(json.dumps(out, indent=2))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="workflow-orchestrator")
    sub = p.add_subparsers(dest="cmd", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--business-dir", type=Path, default=BUSINESS_DIR,
        help="Directory holding business workflow YAMLs "
             "(default: %(default)s)",
    )

    pl = sub.add_parser("list", parents=[common],
                         help="List known business workflows")
    pl.set_defaults(func=_cmd_list)

    ps = sub.add_parser("show", parents=[common],
                         help="Print one workflow's structure")
    ps.add_argument("name", help="Workflow name (filename stem) or path")
    ps.set_defaults(func=_cmd_show)

    pr = sub.add_parser("run", parents=[common],
                         help="Execute a workflow end-to-end")
    pr.add_argument("name", help="Workflow name (filename stem) or path")
    pr.add_argument(
        "--provider", default="stub",
        choices=["auto", "stub", "anthropic", "openai", "gemini"],
        help="LLM provider for persona calls. Default: stub (no API key needed). "
             "'auto' tries anthropic -> openai -> gemini -> stub.",
    )
    pr.add_argument("--max-tokens", type=int, default=1024,
                    help="Max tokens per phase response")
    pr.add_argument("--temperature", type=float, default=0.3,
                    help="LLM temperature (per phase)")
    pr.add_argument("--context",
                    help="Operator context to prepend to every phase prompt")
    pr.add_argument("--dry-run", action="store_true",
                    help="Run phases + build prompts but do NOT append events "
                         "to the JSONL log")
    pr.add_argument("--json", action="store_true",
                    help="Emit JSON instead of pretty text")
    pr.set_defaults(func=_cmd_run)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
