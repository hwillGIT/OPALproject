"""Unit tests for the workflow loader.

Half tests exercise the loader against tiny fake YAMLs in tmp_path
(no dependence on the in-repo workflows). The remaining half
validates that every real OPAL business workflow loads cleanly —
that catches drift between the YAML schema + the Python validator.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from orchestrator.loader import (
    BUSINESS_DIR,
    Workflow,
    WorkflowPhase,
    WorkflowValidationError,
    iter_workflows,
    list_workflows,
    load_workflow,
)


MINIMAL_YAML = """\
name: my-workflow
category: business
domain: clinical
version: "1.0"
description: a tiny test workflow
backpressure:
  - first criterion
phases:
  - id: only-phase
    lead: strategist
    questions:
      - what is the question?
    output: a written answer
emits:
  - DECISION
"""


# --------------------------------------------------------------------------
# Happy-path
# --------------------------------------------------------------------------


def _write_yaml(tmp_path: Path, body: str, name: str = "my-workflow") -> Path:
    p = tmp_path / f"{name}.yaml"
    p.write_text(body, encoding="utf-8")
    return p


class TestLoadHappyPath:
    def test_minimal_workflow_parses(self, tmp_path: Path) -> None:
        path = _write_yaml(tmp_path, MINIMAL_YAML)
        wf = load_workflow(path)
        assert isinstance(wf, Workflow)
        assert wf.name == "my-workflow"
        assert wf.category == "business"
        assert wf.domain == "clinical"
        assert wf.backpressure == ("first criterion",)
        assert wf.emits == ("DECISION",)
        assert len(wf.phases) == 1
        only = wf.phases[0]
        assert isinstance(only, WorkflowPhase)
        assert only.id == "only-phase"
        assert only.lead == "strategist"
        assert only.questions == ("what is the question?",)
        assert only.output == "a written answer"

    def test_optional_fields_default_to_empty(self, tmp_path: Path) -> None:
        path = _write_yaml(tmp_path, MINIMAL_YAML)
        wf = load_workflow(path)
        only = wf.phases[0]
        assert only.supporting == ()
        assert only.tensions == ()
        assert only.pattern is None

    def test_load_by_name_via_business_dir(self, tmp_path: Path) -> None:
        # Simulate the business-dir lookup
        biz = tmp_path / "biz"
        biz.mkdir()
        (biz / "my-workflow.yaml").write_text(MINIMAL_YAML, encoding="utf-8")
        wf = load_workflow("my-workflow", business_dir=biz)
        assert wf.name == "my-workflow"


# --------------------------------------------------------------------------
# Validation failures
# --------------------------------------------------------------------------


class TestValidationFailures:
    def test_missing_required_top_field(self, tmp_path: Path) -> None:
        # Drop the `emits` field
        body = MINIMAL_YAML.replace("emits:\n  - DECISION\n", "")
        path = _write_yaml(tmp_path, body)
        with pytest.raises(WorkflowValidationError, match="emits"):
            load_workflow(path)

    def test_name_must_match_filename(self, tmp_path: Path) -> None:
        body = MINIMAL_YAML.replace("name: my-workflow", "name: other-name")
        path = _write_yaml(tmp_path, body)
        with pytest.raises(WorkflowValidationError, match="must match filename"):
            load_workflow(path)

    def test_invalid_emit_type_rejected(self, tmp_path: Path) -> None:
        body = MINIMAL_YAML.replace("DECISION", "INVALID_TYPE")
        path = _write_yaml(tmp_path, body)
        with pytest.raises(WorkflowValidationError, match="not in vocabulary"):
            load_workflow(path)

    def test_category_must_be_business(self, tmp_path: Path) -> None:
        body = MINIMAL_YAML.replace("category: business", "category: other")
        path = _write_yaml(tmp_path, body)
        with pytest.raises(WorkflowValidationError, match="category must be"):
            load_workflow(path)

    def test_empty_phases_rejected(self, tmp_path: Path) -> None:
        body = MINIMAL_YAML.split("phases:")[0] + "phases: []\nemits:\n  - DECISION\n"
        path = _write_yaml(tmp_path, body)
        with pytest.raises(WorkflowValidationError, match="phases"):
            load_workflow(path)

    def test_duplicate_phase_ids_rejected(self, tmp_path: Path) -> None:
        body = """\
name: dup-phase
category: business
domain: clinical
version: "1.0"
description: dup phases
backpressure:
  - x
phases:
  - id: a
    lead: strategist
    questions:
      - q1
    output: o1
  - id: a
    lead: product-owner
    questions:
      - q2
    output: o2
emits:
  - DECISION
"""
        path = _write_yaml(tmp_path, body, name="dup-phase")
        with pytest.raises(WorkflowValidationError, match="duplicate phase id"):
            load_workflow(path)

    def test_phase_missing_required_field(self, tmp_path: Path) -> None:
        # Drop the `output` field from the phase
        body = MINIMAL_YAML.replace("    output: a written answer\n", "")
        path = _write_yaml(tmp_path, body)
        with pytest.raises(WorkflowValidationError, match="output"):
            load_workflow(path)

    def test_phase_empty_questions_rejected(self, tmp_path: Path) -> None:
        body = MINIMAL_YAML.replace(
            "    questions:\n      - what is the question?\n",
            "    questions: []\n",
        )
        path = _write_yaml(tmp_path, body)
        with pytest.raises(WorkflowValidationError, match="questions"):
            load_workflow(path)

    def test_missing_file_raises(self, tmp_path: Path) -> None:
        with pytest.raises(WorkflowValidationError, match="not found"):
            load_workflow(tmp_path / "does-not-exist.yaml")


# --------------------------------------------------------------------------
# Real in-repo workflows
# --------------------------------------------------------------------------


@pytest.mark.skipif(
    not BUSINESS_DIR.exists(),
    reason="business workflows dir missing — checkout incomplete?",
)
class TestRealWorkflows:
    def test_list_finds_workflows(self) -> None:
        paths = list_workflows()
        # PR #7 + #8 land 6 business workflows
        assert len(paths) >= 1
        assert all(p.suffix == ".yaml" for p in paths)

    def test_every_real_workflow_loads(self) -> None:
        loaded = list(iter_workflows())
        assert len(loaded) >= 1
        for wf in loaded:
            assert wf.category == "business"
            assert wf.phases
            assert wf.emits
            for emit in wf.emits:
                # The vocabulary check would have raised already, but
                # double-belt this:
                from orchestrator.loader import MEMORY_EVENT_TYPES
                assert emit in MEMORY_EVENT_TYPES
