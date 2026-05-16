"""SKOS-like ontology and proactive predicate engine.

Ports the RTRevenue collab-memory ontology layer to a JSON-first
shape (no rdflib dependency). The tag taxonomy is expressed in
``taxonomy.json`` as a SKOS-flavoured concept tree:

  {
    "concepts": {
      "clinical-workflow": {
        "prefLabel": "Clinical Workflow",
        "altLabel": ["workflow", "clinical flow"],
        "broader": ["clinical"],
        "narrower": ["bedside-workflow", "icu-workflow"]
      },
      ...
    }
  }

The predicate engine reads ``predicates.json`` — a list of
rule objects that the briefing CLI consults on each trigger
(session_start, pre_query, post_write).
"""

from .loader import (
    Concept,
    Taxonomy,
    all_tags,
    expand_tag,
    load_taxonomy,
    parent_of,
)
from .predicates import (
    Predicate,
    evaluate_predicate,
    load_predicates,
)

__all__ = [
    "Concept",
    "Predicate",
    "Taxonomy",
    "all_tags",
    "evaluate_predicate",
    "expand_tag",
    "load_predicates",
    "load_taxonomy",
    "parent_of",
]
