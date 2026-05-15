"""Integration test for the chunker → store → query pipeline.

Skipped automatically when the env can't support a real ChromaDB
PersistentClient (e.g. only the http-only `chromadb-client` package is
importable). The test then runs against a tiny synthetic doc — no
network, no API keys, no scraper. The bundled ChromaDB default
embedder (sentence-transformers/all-MiniLM-L6-v2 via ONNX) is used.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from epic_intelligence.ingestion.chunker import EpicDocChunker
from epic_intelligence.index import store as store_mod


pytestmark = pytest.mark.skipif(
    store_mod._detect_thin_client(),
    reason=(
        "ChromaDB http-only thin client detected; PersistentClient unavailable. "
        "See ThinClientInstalledError for fix."
    ),
)


SAMPLE_DOC = """\
# Epic SMART on FHIR

## Patient Context

When an app launches inside Hyperspace, the launch token includes a
`patient` parameter — the FHIR ID for the patient currently in
context. Apps may request patient/Observation.read,
patient/MedicationRequest.read, and patient/AllergyIntolerance.read
scopes for clinical data access. The launch token also exposes
`encounter`, `location`, `appointment`, and `loginDepartment`. SMART
v1 and SMART v2 scope formats are both supported as of August 2024.
This pattern is the canonical way to obtain patient context in any
Epic-integrated voice or clinical app.

## Backend Services Authentication

For system-to-system data exchange, use system/Patient.read with a
JWT signed by the app's private key. Population-level workflows like
nightly batch sync of new AllergyIntolerance entries or scheduled
DocumentReference pulls use this pattern. FHIR R4 is recommended;
STU3 supported for backward compatibility. USCDI v3 unlocks
outside-record variants.
"""


def test_chunk_then_index_then_query_roundtrip(tmp_path: Path) -> None:
    """Full pipeline against an in-memory-style temporary index."""
    chunker = EpicDocChunker()
    chunks = chunker.chunk_document(
        markdown=SAMPLE_DOC,
        source_file="sample.md",
        source_url="https://fhir.epic.com/Documentation?docId=oauth2",
        doc_title="Epic SMART on FHIR",
    )
    assert chunks, "sample doc should produce at least one chunk"

    s = store_mod.EpicIntelligenceStore(
        index_dir=tmp_path / "chroma",
        collection_name="epic_intelligence_test",
    )
    upserted = s.upsert_chunks([c.to_dict() for c in chunks])
    assert upserted == len(chunks)
    assert s.count() == len(chunks)

    hits = s.query("How does SMART on FHIR pass patient context?", n_results=3)
    assert hits, "expected at least one similarity hit"
    top = hits[0]
    # The most relevant chunk should come from the SMART/Patient Context
    # section — that's where every mention of `patient` parameter and
    # launch token lives in the sample.
    assert "Patient Context" in top.section_path or "Epic SMART on FHIR" in top.section_path
    assert top.source_url.startswith("https://fhir.epic.com")
    # Citation-back is intact.
    assert top.snippet
    assert top.chunk_id


def test_query_returns_empty_for_empty_string(tmp_path: Path) -> None:
    s = store_mod.EpicIntelligenceStore(
        index_dir=tmp_path / "chroma",
        collection_name="epic_intelligence_empty",
    )
    assert s.query("") == []
    assert s.query("   ") == []


def test_reset_drops_documents(tmp_path: Path) -> None:
    chunker = EpicDocChunker()
    chunks = chunker.chunk_document(
        markdown=SAMPLE_DOC, source_file="sample.md", source_url="https://x"
    )
    s = store_mod.EpicIntelligenceStore(
        index_dir=tmp_path / "chroma",
        collection_name="epic_intelligence_reset",
    )
    s.upsert_chunks([c.to_dict() for c in chunks])
    assert s.count() > 0
    s.reset()
    assert s.count() == 0
