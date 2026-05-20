"""Workflow YAML loader.

Pure-stdlib + pyyaml. Reads the business workflow files in
``bots/shared/workflows/business/`` and validates the same fields
the Node validator (``bots/shared/workflows/validate.js``) checks.
The two validators MUST stay in sync — both consult the same source
of truth.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator, Mapping

try:
    import yaml  # type: ignore
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "orchestrator requires pyyaml. Install with: pip install pyyaml",
    ) from exc


REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS_DIR = REPO_ROOT / "bots" / "shared" / "workflows"
BUSINESS_DIR = WORKFLOWS_DIR / "business"

MEMORY_EVENT_TYPES = frozenset({
    "DECISION", "ACTION", "INSIGHT", "PREDICTION",
    "OUTCOME", "DEBATE", "CONTEXT_CHANGE", "ARTIFACT",
})


class WorkflowValidationError(ValueError):
    """Raised when a workflow YAML violates the schema."""


@dataclass(frozen=True)
class WorkflowPhase:
    """One phase within a business workflow.

    Mirrors the YAML schema:
        id, lead, supporting, tensions, pattern, questions, output
    """

    id: str
    lead: str
    questions: tuple[str, ...]
    output: str
    supporting: tuple[str, ...] = field(default_factory=tuple)
    tensions: tuple[str, ...] = field(default_factory=tuple)
    pattern: str | None = None


@dataclass(frozen=True)
class Workflow:
    """A loaded + validated workflow definition.

    Mirrors the YAML schema:
        name, category, domain, version, description,
        backpressure, phases, emits
    """

    name: str
    category: str
    domain: str
    version: str
    description: str
    backpressure: tuple[str, ...]
    phases: tuple[WorkflowPhase, ...]
    emits: tuple[str, ...]
    source_path: Path | None = None


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------


def list_workflows(business_dir: Path | None = None) -> list[Path]:
    """List the business workflow YAML files in the configured dir."""
    d = business_dir or BUSINESS_DIR
    if not d.exists():
        return []
    return sorted(d.glob("*.yaml"))


def load_workflow(
    name_or_path: str | Path,
    business_dir: Path | None = None,
) -> Workflow:
    """Load + validate a workflow.

    Accepts either:
      - A workflow name (e.g. "clinical-decision-loop"), resolved
        against ``business_dir`` (default: bots/shared/workflows/business/)
      - An explicit Path to a YAML file

    Raises ``WorkflowValidationError`` on missing required fields or
    invalid emit types.
    """
    if isinstance(name_or_path, Path) or "/" in str(name_or_path) or str(name_or_path).endswith(".yaml"):
        path = Path(name_or_path)
        if not path.exists() and business_dir:
            path = business_dir / path
    else:
        d = business_dir or BUSINESS_DIR
        path = d / f"{name_or_path}.yaml"
        if not path.exists():
            path = d / f"{name_or_path}"

    if not path.exists():
        raise WorkflowValidationError(f"workflow file not found: {path}")

    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise WorkflowValidationError(
            f"failed to parse {path}: {exc}",
        ) from exc

    return _validate_and_build(raw, source_path=path)


def _validate_and_build(raw: Mapping, source_path: Path) -> Workflow:
    """Translate the parsed YAML dict into a Workflow + raise on bad input."""
    required_top = ("name", "category", "domain", "version", "description",
                    "backpressure", "phases", "emits")
    for key in required_top:
        if key not in raw:
            raise WorkflowValidationError(
                f"{source_path.name}: missing top-level field '{key}'",
            )

    name = str(raw["name"])
    expected_name = source_path.stem
    if name != expected_name:
        raise WorkflowValidationError(
            f"{source_path.name}: name {name!r} must match filename stem "
            f"{expected_name!r}",
        )

    category = str(raw["category"])
    if category != "business":
        raise WorkflowValidationError(
            f"{source_path.name}: category must be 'business', got {category!r}",
        )

    backpressure = raw["backpressure"]
    if not isinstance(backpressure, list) or len(backpressure) == 0:
        raise WorkflowValidationError(
            f"{source_path.name}: backpressure must be a non-empty list",
        )

    emits_raw = raw["emits"]
    if not isinstance(emits_raw, list) or len(emits_raw) == 0:
        raise WorkflowValidationError(
            f"{source_path.name}: emits must be a non-empty list",
        )
    for e in emits_raw:
        if e not in MEMORY_EVENT_TYPES:
            raise WorkflowValidationError(
                f"{source_path.name}: emit {e!r} not in vocabulary "
                f"({sorted(MEMORY_EVENT_TYPES)})",
            )
    emits = tuple(str(e) for e in emits_raw)

    phases_raw = raw["phases"]
    if not isinstance(phases_raw, list) or len(phases_raw) == 0:
        raise WorkflowValidationError(
            f"{source_path.name}: phases must be a non-empty list",
        )

    phases: list[WorkflowPhase] = []
    seen_phase_ids: set[str] = set()
    required_phase = ("id", "lead", "questions", "output")
    for i, phase in enumerate(phases_raw):
        if not isinstance(phase, dict):
            raise WorkflowValidationError(
                f"{source_path.name}: phase #{i} must be an object",
            )
        for key in required_phase:
            if key not in phase:
                raise WorkflowValidationError(
                    f"{source_path.name}: phase #{i} missing required field "
                    f"{key!r}",
                )
        pid = str(phase["id"])
        if pid in seen_phase_ids:
            raise WorkflowValidationError(
                f"{source_path.name}: duplicate phase id {pid!r}",
            )
        seen_phase_ids.add(pid)
        questions = phase["questions"]
        if not isinstance(questions, list) or not questions:
            raise WorkflowValidationError(
                f"{source_path.name}: phase {pid!r} must have a non-empty "
                "questions list",
            )
        phases.append(WorkflowPhase(
            id=pid,
            lead=str(phase["lead"]),
            supporting=tuple(str(s) for s in (phase.get("supporting") or ())),
            tensions=tuple(str(t) for t in (phase.get("tensions") or ())),
            pattern=(str(phase["pattern"]) if phase.get("pattern") else None),
            questions=tuple(str(q) for q in questions),
            output=str(phase["output"]),
        ))

    return Workflow(
        name=name,
        category=category,
        domain=str(raw["domain"]),
        version=str(raw["version"]),
        description=str(raw["description"]),
        backpressure=tuple(str(b) for b in backpressure),
        phases=tuple(phases),
        emits=emits,
        source_path=source_path,
    )


def iter_workflows(business_dir: Path | None = None) -> Iterator[Workflow]:
    """Yield every loaded workflow under the business directory."""
    for path in list_workflows(business_dir):
        yield load_workflow(path)
