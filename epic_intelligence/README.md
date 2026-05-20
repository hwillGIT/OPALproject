# OPAL Epic EHR Intelligence Layer

A queryable knowledge base over Epic developer documentation, used by
the OPAL voice assistant to answer clinician questions about Epic
behavior with verifiable citations back to the source page and section.

> **End-user context:** This module is the backbone of every LYNA
> clinical-staff journey. See [`INTELLIGENCE_LAYER.md`](../INTELLIGENCE_LAYER.md)
> for the ten user stories that exercise it — bedside med lookup
> (§4.1), float-nurse onboarding (§4.2), charge-nurse handoff in the
> resource-offline window (§4.3), coming-on-shift sign-on (§4.4),
> new-grad policy lookup (§4.5), surfacing a hospital AI tool the
> nurse didn't know existed (§4.6), cardiac step-down rapid response
> (§4.7), isolation-room broadcast (§4.8), a clean handoff to the
> phone for a pressure-injury photo (§4.9), and an ad-hoc bedside
> interpreter session at 03:00 (§4.10). Every story is anchored to
> the I-Corps customer-discovery research (H1–H18). The query router,
> citation strategy, FHIR fan-out, and per-site AI registry described
> below are what make those stories work. UI specifications for each
> journey live in `hardware/opalDevice/docs/ux/`.

## What this answers

> "How does SMART on FHIR pass patient context at launch?"
> "What scope do I need to read MedicationRequest as a backend service?"
> "Which CDS Hooks fire at order-sign?"
> "Does USCDI v3 expose outside-record AllergyIntolerance?"

The layer ingests Epic's public documentation (Open Epic, fhir.epic.com,
HL7 FHIR R4 resource pages, CDS Hooks IG, SMART App Launch IG) plus
curated synthesis docs (`docs/analysis/epic-clinical-data-patient-context.md`),
chunks them with Epic-aware entity extraction, embeds each chunk, and
serves them via a citation-aware similarity-search API.

## Module layout

```
epic_intelligence/
├── scraper/                       Node — Playwright + cheerio crawlers
│   ├── playwright_crawler.js
│   ├── http_crawler.js
│   └── output/
│       ├── markdown/<site>/       Cleaned text per page (input to chunker)
│       ├── structured/<site>/     URL, title, headings, links per page (metadata)
│       └── raw/<site>/            Raw HTML (kept for replay)
├── ingestion/
│   ├── chunker.py                 Section-aware chunker w/ Epic entity extraction
│   └── pipeline.py                scraper output → chunker → ChromaDB
├── index/
│   ├── embedder.py                Pluggable: ChromaDB default OR Gemini
│   └── store.py                   PersistentClient wrapper, citation metadata
├── query.py                       Citation-aware retrieval API + CLI
├── tests/                         Pytest (19 unit + 3 integration)
└── README.md                      This file
```

## End-to-end workflow

```bash
# 1. Crawl one Epic doc site (32 pages already scraped from open.epic.com)
cd epic_intelligence/scraper
npm install
node http_crawler.js --site open_epic --max-pages 60

# 2. Ingest the scraped output + the curated EPIC analysis doc
cd ../..
python -m epic_intelligence.ingestion.pipeline \
    --site open_epic \
    --extra-doc docs/analysis/epic-clinical-data-patient-context.md \
        https://fhir.epic.com/Documentation \
        "Epic Developer Guide Synthesis"

# 3. Query the index
python -m epic_intelligence.query \
    "How does SMART on FHIR pass patient context at launch?" --top-k 5

python -m epic_intelligence.query "OAuth scope for medications" --json
```

Crawler scripts available out of the box (see `scraper/package.json`):
`crawl:open-epic`, `crawl:fhir-epic`, `crawl:hl7-fhir`, `crawl:cds-hooks`,
`crawl:smart`, `crawl:all`.

## Embedder choice

| Backend | When | Quality | Network/key required |
|---|---|---|---|
| `chromadb-default` | Always available | Good | None (sentence-transformers/all-MiniLM-L6-v2 via ONNX) |
| `gemini` | If `GOOGLE_API_KEY` set in env | Higher | Yes — Google Generative AI |

The factory in `index/embedder.py` picks `gemini` when the key is present
and falls back to `chromadb-default` otherwise. Override with
`--embedder default` or `--embedder gemini` on the pipeline/query CLIs.

## Citation contract

Every `QueryHit` from `epic_intelligence.query.query()` exposes:

```python
hit.title           # doc title (from scraped <title> or extra-doc title)
hit.source_url      # canonical URL — what the voice assistant cites
hit.section_path    # ("Patient Context", "SMART on FHIR", ...) — header trail
hit.snippet         # first 400 chars of the matched chunk, ellipsized at word
hit.score           # cosine distance (lower = closer)
hit.metadata        # full ChromaDB metadata: entities, chunk_index, etc.
```

This is the contract the voice assistant (and any future chat surface)
relies on to attribute every answer back to a verifiable Epic source.

## Tests

```bash
python -m pytest epic_intelligence/tests/ -v
```

19 unit tests cover the chunker (entity extraction, section parsing,
code-block preservation, end-to-end chunking, determinism). 3
integration tests exercise the chunker → store → query roundtrip with
ChromaDB's bundled offline embedder; they skip automatically when
ChromaDB's `PersistentClient` isn't usable in the env.

## Known: ChromaDB thin-client conflict

If ingestion or queries fail with:

> `Chroma is running in http-only client mode...`

…the `chromadb-client` (thin) package is shadowing `chromadb` (full).
Both install to the same import path. Fix:

```bash
pip uninstall -y chromadb-client chromadb
pip install chromadb
```

`store.py` detects this case and raises `ThinClientInstalledError` with
the same message rather than failing inside ChromaDB internals.

## Status

| Phase | State |
|---|---|
| Scraper (Playwright + HTTP) | Working — 32 pages of open.epic.com captured |
| Chunker (entity-aware) | Working — 19 unit tests green |
| Embedder (default + Gemini) | Working — both backends wired |
| ChromaDB store + citation metadata | Working — 3 integration tests, env-gated |
| Ingestion CLI (scraper → store) | Working — `python -m epic_intelligence.ingestion.pipeline` |
| Query CLI (citation-aware) | Working — `python -m epic_intelligence.query` |
| Live end-to-end smoke against the 32 scraped pages | **Pending** — ChromaDB env conflict above |
| Voice assistant integration | Not yet wired — separate epic |

## Where this plugs into OPAL

Per `hardware/opalDevice/docs/architecture/opal-system-architecture-epics.md`,
the Intelligence Layer is **Phase 3 — Epic 4: AI-Enhanced Communications**:

> Contextual Router uses multi-factor analysis with Hospital Intelligence
> Module (RAG) to determine optimal recipient.

This module is the RAG engine cited above. The Contextual Router will
call `epic_intelligence.query.query(...)` to ground voice-driven
clinical questions in the indexed Epic corpus.
