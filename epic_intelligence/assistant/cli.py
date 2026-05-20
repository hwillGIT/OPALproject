"""CLI surface for the assistant.

Two entry points:

    python -m epic_intelligence.assistant.cli answer "How does ... ?"
        -> just call IntelligenceAnswerService.answer; print Answer

    python -m epic_intelligence.assistant.cli route "How does ... ?"
        -> classify via the ContextualRouter stub; if it routes to
           EPIC, also print the cited Answer.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ..index.store import DEFAULT_COLLECTION, DEFAULT_INDEX_DIR
from .service import AnswerServiceConfig, IntelligenceAnswerService
from .voice_router_stub import ContextualRouter


def _print_answer_pretty(ans, *, question: str) -> None:
    print(f"# Q: {question!r}")
    print(f"# provider={ans.provider_name}  model={ans.model_name}")
    if ans.insufficient:
        print("# (flagged INSUFFICIENT by synthesizer)")
    print()
    print(ans.text)
    if ans.citations:
        print("\n## Sources")
        for i, c in enumerate(ans.citations, start=1):
            section = " > ".join(c.section_path) if c.section_path else "(top)"
            print(f"  [{i}] {c.title}")
            print(f"      section: {section}")
            print(f"      source : {c.source_url}")
            print(f"      score  : {c.score:.3f}")


def _print_answer_json(ans, *, question: str) -> None:
    print(json.dumps({
        "question": question,
        "text": ans.text,
        "insufficient": ans.insufficient,
        "provider": ans.provider_name,
        "model": ans.model_name,
        "citations": [
            {
                "chunk_id": c.chunk_id,
                "title": c.title,
                "source_url": c.source_url,
                "section_path": list(c.section_path),
                "snippet": c.snippet,
                "score": c.score,
            }
            for c in ans.citations
        ],
        "metadata": dict(ans.metadata),
    }, indent=2))


def _cmd_answer(args: argparse.Namespace) -> int:
    service = IntelligenceAnswerService(
        index_dir=args.index_dir,
        collection=args.collection,
        embedder_pref=args.embedder,
        provider_pref=args.provider,
        config=AnswerServiceConfig(
            top_k=args.top_k,
            max_tokens_out=args.max_tokens_out,
            temperature=args.temperature,
        ),
    )
    ans = service.answer(args.question)
    if args.json:
        _print_answer_json(ans, question=args.question)
    else:
        _print_answer_pretty(ans, question=args.question)
    return 0 if not ans.insufficient or args.allow_insufficient else 1


def _cmd_route(args: argparse.Namespace) -> int:
    router = ContextualRouter()
    decision = router.route(args.question)
    if args.json:
        out = {
            "question": args.question,
            "target": decision.target,
            "confidence": decision.confidence,
            "reason": decision.reason,
            "metadata": dict(decision.metadata),
        }
        if decision.answer is not None:
            out["answer"] = {
                "text": decision.answer.text,
                "insufficient": decision.answer.insufficient,
                "provider": decision.answer.provider_name,
                "model": decision.answer.model_name,
                "citations": [
                    {
                        "chunk_id": c.chunk_id,
                        "title": c.title,
                        "source_url": c.source_url,
                        "section_path": list(c.section_path),
                        "snippet": c.snippet,
                        "score": c.score,
                    }
                    for c in decision.answer.citations
                ],
            }
        print(json.dumps(out, indent=2))
        return 0

    print(f"# Q: {args.question!r}")
    print(f"  route       : {decision.target}")
    print(f"  confidence  : {decision.confidence:.2f}")
    print(f"  reason      : {decision.reason}")
    if decision.metadata.get("matched_keywords"):
        kws = ", ".join(decision.metadata["matched_keywords"])
        print(f"  matched     : {kws}")
    if decision.answer is not None:
        print()
        _print_answer_pretty(decision.answer, question=args.question)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="epic-intel-assistant")
    sub = p.add_subparsers(dest="cmd", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR,
                        help="ChromaDB persistent directory")
    common.add_argument("--collection", default=DEFAULT_COLLECTION,
                        help="Collection name")
    common.add_argument("--embedder", default="auto",
                        choices=["auto", "default", "gemini"],
                        help="Embedder backend")
    common.add_argument(
        "--provider", default="auto",
        choices=["auto", "stub", "anthropic", "openai", "gemini"],
        help="LLM synthesis provider. 'auto' = first available real "
             "provider; 'stub' = deterministic local fallback (no API "
             "key needed)",
    )
    common.add_argument("--top-k", type=int, default=5)
    common.add_argument("--max-tokens-out", type=int, default=1024)
    common.add_argument("--temperature", type=float, default=0.2)
    common.add_argument("--json", action="store_true",
                        help="Emit JSON instead of pretty text")

    pa = sub.add_parser("answer", parents=[common],
                         help="Retrieve + synthesize an answer (skips router)")
    pa.add_argument("question")
    pa.add_argument("--allow-insufficient", action="store_true",
                    help="Exit 0 even when the synthesizer flagged "
                         "INSUFFICIENT (default: exit 1)")
    pa.set_defaults(func=_cmd_answer)

    pr = sub.add_parser("route", parents=[common],
                         help="Run the Contextual Router stub")
    pr.add_argument("question")
    pr.set_defaults(func=_cmd_route)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
