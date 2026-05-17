"""CLI for the pilot-site scoring rubric.

    python -m pilot.cli score <site.yaml> [--json]
    python -m pilot.cli champions <site.yaml>
    python -m pilot.cli example
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .champion import rank_champions
from .loader import SiteLoadError, load_site
from .models import SiteAssessment
from .scoring import score_site


EXAMPLES_DIR = Path(__file__).resolve().parent / "examples"


def _cmd_score(args: argparse.Namespace) -> int:
    try:
        site = load_site(args.site)
    except SiteLoadError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    result = score_site(site)
    if args.json:
        print(json.dumps(_assessment_to_dict(result), indent=2))
    else:
        _print_pretty(result)
    return 0


def _cmd_champions(args: argparse.Namespace) -> int:
    try:
        site = load_site(args.site)
    except SiteLoadError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if not site.champion_candidates:
        print(f"# {site.name}: no champion candidates listed")
        return 0
    print(f"# Champion ranking for {site.name}")
    for i, ranking in enumerate(rank_champions(site.champion_candidates), 1):
        c = ranking.candidate
        print(f"\n{i}. {c.name} -- {c.role}  ({ranking.score:.1f}/100)")
        for r in ranking.rationale:
            print(f"   * {r}")
        if ranking.risks:
            print("   risks:")
            for r in ranking.risks:
                print(f"     - {r}")
    return 0


def _cmd_example(args: argparse.Namespace) -> int:
    examples = sorted(EXAMPLES_DIR.glob("*.yaml"))
    if not examples:
        print(f"# no examples found under {EXAMPLES_DIR}")
        return 1
    print(f"# {len(examples)} example(s) under {EXAMPLES_DIR}")
    for p in examples:
        print(f"  - {p.name}")
    return 0


def _print_pretty(a: SiteAssessment) -> None:
    print(f"# {a.site_name}: {a.verdict.value.upper()} ({a.total:.1f}/100)")
    print()
    print(a.summary)
    print()
    print("## Dimension breakdown")
    for d in a.dimensions:
        print(
            f"  [{d.dimension.value}]  raw={d.score:.0f}/100  "
            f"weighted={d.weighted:.1f}"
        )
        for r in d.rationale:
            print(f"    + {r}")
        for g in d.gaps:
            print(f"    - GAP: {g}")
        print()


def _assessment_to_dict(a: SiteAssessment) -> dict:
    return {
        "site_name": a.site_name,
        "total": a.total,
        "verdict": a.verdict.value,
        "summary": a.summary,
        "dimensions": [
            {
                "dimension": d.dimension.value,
                "score": d.score,
                "weighted": d.weighted,
                "rationale": list(d.rationale),
                "gaps": list(d.gaps),
            }
            for d in a.dimensions
        ],
    }


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="pilot-rubric")
    sub = p.add_subparsers(dest="cmd", required=True)

    ps = sub.add_parser("score", help="Score a pilot site")
    ps.add_argument("site", help="Path to a site YAML")
    ps.add_argument("--json", action="store_true", help="Emit JSON")
    ps.set_defaults(func=_cmd_score)

    pc = sub.add_parser("champions", help="Rank the champion candidates at a site")
    pc.add_argument("site", help="Path to a site YAML")
    pc.set_defaults(func=_cmd_champions)

    pe = sub.add_parser("example", help="List bundled example site YAMLs")
    pe.set_defaults(func=_cmd_example)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
