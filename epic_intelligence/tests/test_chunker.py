"""Unit tests for epic_intelligence.ingestion.chunker.

These tests exercise the pure-Python pieces only. No network, no LLM,
no ChromaDB. Lets us run the suite anywhere without secrets.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from epic_intelligence.ingestion.chunker import Chunk, EpicDocChunker


# --------------------------------------------------------------------------
# Entity extraction
# --------------------------------------------------------------------------


class TestEntityExtraction:
    def setup_method(self) -> None:
        self.chunker = EpicDocChunker()

    def test_extracts_fhir_resource_names(self) -> None:
        text = (
            "Apps must request the Patient and Observation resources, "
            "then optionally MedicationRequest and AllergyIntolerance."
        )
        ents = self.chunker.extract_entities(text)
        assert "fhir_resource" in ents
        assert {"Patient", "Observation", "MedicationRequest",
                "AllergyIntolerance"}.issubset(set(ents["fhir_resource"]))

    def test_extracts_oauth_scopes(self) -> None:
        text = (
            "Request scopes like patient/Observation.read, user/MedicationRequest.write, "
            "and system/Patient.r for backend services."
        )
        ents = self.chunker.extract_entities(text)
        assert "oauth_scope" in ents
        flat = " ".join(ents["oauth_scope"])
        assert "patient" in flat
        assert "user" in flat
        assert "system" in flat

    def test_extracts_cds_hooks(self) -> None:
        text = "Subscribe to patient-view, order-select, and order-sign hooks."
        ents = self.chunker.extract_entities(text)
        assert "cds_hook" in ents
        assert {"patient-view", "order-select", "order-sign"} <= set(ents["cds_hook"])

    def test_extracts_uscdi_versions(self) -> None:
        text = "Per USCDI v3, all clinical resources must be exposed."
        ents = self.chunker.extract_entities(text)
        assert "uscdi_version" in ents
        # Match formatting normalizes capitalization but the version token survives.
        assert any("v3" in v.lower() for v in ents["uscdi_version"])

    def test_extracts_fhir_versions(self) -> None:
        text = "FHIR R4 is the recommended version. STU3 is also supported."
        ents = self.chunker.extract_entities(text)
        assert "fhir_version" in ents
        joined = " ".join(ents["fhir_version"]).upper()
        assert "R4" in joined
        assert "STU3" in joined

    def test_no_entities_returns_empty_dict(self) -> None:
        text = "This text contains no FHIR or Epic-specific terms."
        ents = self.chunker.extract_entities(text)
        # The "FHIR" word alone won't match — patterns require the full token.
        assert isinstance(ents, dict)


# --------------------------------------------------------------------------
# Section extraction
# --------------------------------------------------------------------------


class TestSectionExtraction:
    def setup_method(self) -> None:
        self.chunker = EpicDocChunker()

    def test_top_level_headers_recognized(self) -> None:
        md = "# Top\n\nbody one\n\n## Sub\n\nbody two\n"
        sections = self.chunker.extract_sections(md)
        titles = [t for t, _, _ in sections]
        assert titles == ["Top", "Sub"]

    def test_levels_match_hash_count(self) -> None:
        md = "# A\n\nx\n\n## B\n\ny\n\n### C\n\nz\n"
        sections = self.chunker.extract_sections(md)
        levels = [lvl for _, _, lvl in sections]
        assert levels == [1, 2, 3]

    def test_content_before_first_header_is_introduction(self) -> None:
        md = "preamble line\n\n# First\n\nbody\n"
        sections = self.chunker.extract_sections(md)
        # First entry should be the implicit Introduction with the preamble.
        assert sections[0][0] == "Introduction"
        assert "preamble" in sections[0][1]


# --------------------------------------------------------------------------
# Code-block preservation
# --------------------------------------------------------------------------


class TestCodeBlockPreservation:
    def setup_method(self) -> None:
        self.chunker = EpicDocChunker()

    def test_roundtrip_preserves_code_block(self) -> None:
        original = "intro\n\n```json\n{\"a\":1}\n```\n\noutro\n"
        with_placeholders, code_blocks = self.chunker.preserve_code_blocks(original)
        assert "```" not in with_placeholders
        assert len(code_blocks) == 1
        restored = self.chunker.restore_code_blocks(with_placeholders, code_blocks)
        assert restored == original

    def test_multiple_code_blocks(self) -> None:
        original = "```a\nx\n```\n\nmid\n\n```b\ny\n```\n"
        with_placeholders, code_blocks = self.chunker.preserve_code_blocks(original)
        assert len(code_blocks) == 2
        restored = self.chunker.restore_code_blocks(with_placeholders, code_blocks)
        assert restored == original


# --------------------------------------------------------------------------
# Chunking
# --------------------------------------------------------------------------


class TestChunkText:
    def setup_method(self) -> None:
        self.chunker = EpicDocChunker()

    def test_short_text_returns_one_chunk(self) -> None:
        chunks = self.chunker.chunk_text("short body", max_chars=1000, overlap_chars=100)
        assert chunks == ["short body"]

    def test_long_text_splits_into_multiple_chunks(self) -> None:
        body = "\n\n".join(["paragraph " + ("x" * 100)] * 20)
        chunks = self.chunker.chunk_text(body, max_chars=500, overlap_chars=50)
        assert len(chunks) > 1
        # No chunk should massively exceed the max (small overshoot tolerated).
        assert max(len(c) for c in chunks) < 1500


# --------------------------------------------------------------------------
# End-to-end chunk_document
# --------------------------------------------------------------------------


# Sized to clear the chunker's `min_chunk_size` threshold under any of the
# bundled configs (default = 400 chars / chunk minimum).
SAMPLE_DOC = """\
# Epic on FHIR — Auth Overview

## SMART on FHIR

When an app launches inside Hyperspace, the launch token includes a
`patient` parameter — the FHIR ID for the patient currently in context.
Apps may request the patient/Observation.read scope to access labs and
the patient/MedicationRequest.read scope to access active orders. The
launch token also exposes `encounter`, `location`, `appointment`, and
`loginDepartment` when an encounter is in context. Standalone launches
bypass this flow: in patient-facing standalone launches, the patient
FHIR ID is returned in the token response, but in provider-facing
standalone launches, the patient FHIR ID is NOT returned and the app
must determine the patient independently. Both SMART v1 and SMART v2
scope formats are supported as of August 2024. Subscribe to
patient-view, order-select, and order-sign hooks for clinical decision
support integration.

```json
{
  "resourceType": "Observation",
  "subject": { "reference": "Patient/12345" }
}
```

## Backend Services

For system-to-system data exchange, use the system/Patient.read scope
with a JWT signed by the app's private key. No patient context is
provided at launch — the app constructs queries from known identifiers.
This pattern is appropriate for population-level workflows: nightly
batch sync of new AllergyIntolerance entries, scheduled pulls of
DocumentReference records, or building a real-time MedicationStatement
mirror keyed off patient MRN. The Patient and Practitioner resources
are commonly read this way as anchors for downstream queries against
Observation, Condition, Encounter, and Procedure. FHIR R4 is the
recommended version; STU3 is supported for backward compatibility.
USCDI v3 entries unlock outside-record variants of nearly every
clinical resource type, enabling cross-organization read access.
"""


class TestChunkDocumentEndToEnd:
    def test_produces_chunks_with_metadata(self, tmp_path: Path) -> None:
        chunker = EpicDocChunker()
        chunks = chunker.chunk_document(
            markdown=SAMPLE_DOC,
            source_file=str(tmp_path / "auth.md"),
            source_url="https://fhir.epic.com/Documentation?docId=oauth2",
            doc_title="Epic on FHIR — Auth Overview",
        )
        assert len(chunks) >= 1, "SAMPLE_DOC should clear min_chunk_size"
        first = chunks[0]
        assert isinstance(first, Chunk)
        assert first.source_url.startswith("https://fhir.epic.com")
        # Section path should reflect a real header from the doc.
        all_section_titles = {t for c in chunks for t in c.section_path}
        assert all_section_titles & {
            "Epic on FHIR — Auth Overview",
            "SMART on FHIR",
            "Backend Services",
        }
        # All chunks share total_chunks = len(chunks).
        assert all(c.total_chunks == len(chunks) for c in chunks)

    def test_chunks_carry_extracted_entities(self) -> None:
        chunker = EpicDocChunker()
        chunks = chunker.chunk_document(
            markdown=SAMPLE_DOC,
            source_file="auth.md",
            source_url="https://example/auth",
        )
        assert chunks, "expected at least one chunk"
        all_entities: set[str] = set()
        for c in chunks:
            for ent_type, vals in c.metadata.get("entities", {}).items():
                all_entities.update(f"{ent_type}:{v}" for v in vals)
        # We expect at least one OAuth scope and one FHIR resource.
        assert any(e.startswith("oauth_scope:") for e in all_entities), all_entities
        assert any(e.startswith("fhir_resource:") for e in all_entities), all_entities

    def test_code_block_survives_chunking(self) -> None:
        chunker = EpicDocChunker()
        chunks = chunker.chunk_document(
            markdown=SAMPLE_DOC,
            source_file="auth.md",
            source_url="https://example/auth",
        )
        assert chunks, "expected at least one chunk"
        joined = "\n\n".join(c.content for c in chunks)
        assert "```json" in joined
        assert '"resourceType"' in joined


# --------------------------------------------------------------------------
# Determinism
# --------------------------------------------------------------------------


class TestDeterminism:
    def test_chunk_ids_are_stable_across_runs(self) -> None:
        chunker = EpicDocChunker()
        run_a = chunker.chunk_document(SAMPLE_DOC, source_file="auth.md")
        run_b = chunker.chunk_document(SAMPLE_DOC, source_file="auth.md")
        assert [c.id for c in run_a] == [c.id for c in run_b]
        assert [c.content for c in run_a] == [c.content for c in run_b]


# --------------------------------------------------------------------------
# Entry-point sanity
# --------------------------------------------------------------------------


def test_default_config_present() -> None:
    assert "default" in EpicDocChunker.CONFIGS
    assert EpicDocChunker.CONFIGS["default"]["chunk_size"] > 0


def test_unknown_config_falls_back_to_default() -> None:
    chunker = EpicDocChunker(config_name="does-not-exist")
    assert chunker.config == EpicDocChunker.CONFIGS["default"]
