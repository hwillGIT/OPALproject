"""OPAL Epic EHR Intelligence Layer.

Builds a queryable knowledge base over Epic developer documentation
(Open Epic, fhir.epic.com, HL7 FHIR R4, CDS Hooks, SMART App Launch IG)
so OPAL's voice assistant can answer clinician questions grounded in
authoritative Epic source material.

Pipeline (left → right):

    scraper/ ──→ ingestion/chunker.py ──→ ingestion/pipeline.py
                                                  │
                                                  ▼
                                         index/embedder.py
                                                  │
                                                  ▼
                                          index/store.py
                                          (ChromaDB collection
                                           "epic_intelligence")
                                                  │
                                                  ▼
                                            query.py
                                          (citation-aware
                                           retrieval API + CLI)
"""
