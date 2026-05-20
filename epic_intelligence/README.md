# OPAL Epic EHR Intelligence Layer

A queryable knowledge base over Epic developer documentation, used by
the OPAL voice assistant to answer clinician questions about Epic
behavior with verifiable citations back to the source page and section.

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
| Scraper (Playwright + HTTP) | Working — 147 pages across 5 sites captured |
| Chunker (entity-aware) | Working — 19 unit tests green |
| Embedder (default + Gemini) | Working — both backends wired |
| ChromaDB store + citation metadata | Working — 3 integration tests green |
| Ingestion CLI (scraper → store) | Working — `python -m epic_intelligence.ingestion.pipeline` |
| Query CLI (citation-aware) | Working — `python -m epic_intelligence.query` |
| Live end-to-end against the full corpus | Working — **8,556 chunks indexed**, 22/22 tests pass |
| Voice assistant integration | Not yet wired — separate epic |

## Indexed corpus (per site)

| Site | Files | Chunks | Source |
|---|---:|---:|---|
| `open_epic` | 31 | 358 | https://open.epic.com |
| `epic_on_fhir` | 44 | 7,343 | https://fhir.epic.com |
| `hl7_fhir_r4` | 40 | 515 | https://hl7.org/fhir/R4 |
| `cds_hooks` | 2 | 90 | https://cds-hooks.hl7.org/2.0 |
| `smart_app_launch` | 29 | 236 | SMART App Launch IG (build.fhir.org) |
| curated synthesis doc | 1 | 14 | `docs/analysis/epic-clinical-data-patient-context.md` |
| **total** | **147** | **8,556** | |

Sample queries that work today:

```
$ python -m epic_intelligence.query "SMART on FHIR launch token contents" --top-k 2
  -> hits citing build.fhir.org/ig/HL7/smart-app-launch/...

$ python -m epic_intelligence.query "CDS hooks order-sign request schema" --top-k 2
  -> hits citing cds-hooks.hl7.org/2.0

$ python -m epic_intelligence.query "Epic OAuth backend services JWT" --top-k 2
  -> hits citing fhir.epic.com/Documentation?docId=oauth2
```

## Where this plugs into OPAL

Per `hardware/opalDevice/docs/architecture/opal-system-architecture-epics.md`,
the Intelligence Layer is **Phase 3 — Epic 4: AI-Enhanced Communications**:

> Contextual Router uses multi-factor analysis with Hospital Intelligence
> Module (RAG) to determine optimal recipient.

This module is the RAG engine cited above. The Contextual Router will
call `epic_intelligence.query.query(...)` to ground voice-driven
clinical questions in the indexed Epic corpus.
