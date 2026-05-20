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
├── synthesis/                     LLM synthesis layer (B-2)
│   ├── models.py                  Answer + Citation + SynthesisRequest
│   ├── prompts.py                 Strict cited-answer prompt builder
│   ├── provider.py                Pluggable LLM: anthropic / openai / gemini / stub
│   └── synthesizer.py             End-to-end: request → prompt → LLM → Answer
├── assistant/                     Voice-assistant-facing service (B-2)
│   ├── service.py                 IntelligenceAnswerService.answer(question)
│   ├── voice_router_stub.py       ContextualRouter stub (the contract the
│   │                              OPAL wearable will fulfill)
│   └── cli.py                     python -m epic_intelligence.assistant.cli
│                                  {answer | route} "..."
├── tests/                         Pytest (52 tests: 22 chunker+pipeline +
│                                  30 synthesis+assistant; all run without
│                                  API keys via the stub provider)
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

# 4. (NEW in B-2) Cited natural-language answer via the synthesis layer
python -m epic_intelligence.assistant.cli answer \
    "How does SMART on FHIR pass patient context at launch?" \
    --provider auto --top-k 5

# 5. (NEW in B-2) Route through the Contextual Router stub
#    (auto-picks EPIC vs on-call vs bedside vs out-of-domain)
python -m epic_intelligence.assistant.cli route \
    "What scope do I need for SMART on FHIR backend services?"
```

Crawler scripts available out of the box (see `scraper/package.json`):
`crawl:open-epic`, `crawl:fhir-epic`, `crawl:hl7-fhir`, `crawl:cds-hooks`,
`crawl:smart`, `crawl:all`.

## LLM synthesis layer (B-2)

`epic_intelligence/synthesis/` turns retrieved chunks into a cited
natural-language answer. Pluggable provider — pick via env or flag:

| Backend | When | Requires |
|---|---|---|
| `anthropic` | Highest quality clinician-facing answers | `ANTHROPIC_API_KEY`, `pip install anthropic` |
| `openai` | Alternative, comparable quality | `OPENAI_API_KEY`, `pip install openai` |
| `gemini` | Matches the SDK already in `memory_system/` | `GOOGLE_API_KEY`, `pip install google-generativeai` |
| `stub` | **Always available.** Deterministic echo for tests + CI | nothing |

Factory order on `--provider auto`: anthropic → openai → gemini → stub.
Override per-call with `--provider {stub\|anthropic\|openai\|gemini}` or
globally with `OPAL_SYNTHESIS_PROVIDER=anthropic` in env. Model override
via `OPAL_SYNTHESIS_MODEL=claude-sonnet-4-6` (or per-provider default).

The prompt enforces three hard rules: every claim must cite, missing
evidence must be acknowledged (not guessed), and outside Epic knowledge
must not bleed in. These are what makes the synthesizer safe for a
clinician-facing voice surface.

## Voice-assistant integration (B-2)

`epic_intelligence/assistant/` is the contract the OPAL wearable's
**Contextual Router** (Phase 3, Epic 4 — see
`hardware/opalDevice/docs/architecture/opal-system-architecture-epics.md`)
will fulfill.

  - `service.py` — `IntelligenceAnswerService.answer(question) → Answer`.
    The one public method the voice assistant calls.
  - `voice_router_stub.py` — runnable Python stub of the real device-side
    Contextual Router. Demonstrates the routing decision the real router
    must make: EPIC RAG / clinician workflow / on-call schedule /
    escalate / out-of-domain. Lets the EPIC route be exercised
    end-to-end without the real device.

```python
from epic_intelligence.assistant import IntelligenceAnswerService

service = IntelligenceAnswerService()  # constructed once
ans = service.answer("What scope do I need for medications?")
print(ans.text)
for i, c in enumerate(ans.citations, 1):
    print(f"  [{i}] {c.title}  ->  {c.source_url}")
```

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
| Live end-to-end against the full corpus | Working — **8,556 chunks indexed**, 52/52 tests pass |
| LLM synthesis layer (B-2) | Working — pluggable provider, stub always available, 22 tests |
| Voice-assistant integration stub (B-2) | Working — `ContextualRouter` stub, 8 tests, EPIC route exercised end-to-end |
| Voice-assistant on real wearable | Out of scope for this repo — `IntelligenceAnswerService` is the contract |

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
