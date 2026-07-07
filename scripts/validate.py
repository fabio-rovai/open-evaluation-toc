#!/usr/bin/env python3
"""Validate the Theory-of-Change graph against the SHACL shapes, and
report the evidence-gap map (the honest output of a rapid evidence
assessment: which causal claims are not yet supported).

Usage:
    python3 scripts/validate.py

Requires: pyshacl, rdflib  (pip install pyshacl rdflib)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "ontology" / "toc.ttl"
SHAPES = ROOT / "shapes" / "toc-shapes.ttl"

try:
    from pyshacl import validate
    from rdflib import Graph
except ImportError:
    sys.exit("Install dependencies first:  pip install pyshacl rdflib")

def main() -> int:
    conforms, _, text = validate(
        data_graph=str(DATA),
        shacl_graph=str(SHAPES),
        data_graph_format="turtle",
        shacl_graph_format="turtle",
        inference="rdfs",
        advanced=True,
    )
    print(f"SHACL conforms: {conforms}")
    if not conforms:
        print(text)
        return 1

    # Structure is sound -> report the evidence-gap map by query.
    g = Graph().parse(str(DATA), format="turtle")
    q = """
    PREFIX toc: <https://gov.tesseract.academy/ns/toc#>
    SELECT ?service ?label ?grade ?priority WHERE {
        ?p a toc:Pathway ;
           toc:service ?service ;
           rdfs:label ?label ;
           toc:evidenceGrade ?grade ;
           toc:priorityForEval ?priority .
    } ORDER BY ?service ?grade
    """
    print("\nEvidence-gap map (priority-for-evaluation pathways first):")
    rows = sorted(g.query(q), key=lambda r: (str(r.grade) != "gap", str(r.service)))
    for r in rows:
        flag = "  <-- PRIORITY FOR EVALUATION" if str(r.priority).lower() == "true" else ""
        print(f"  [{str(r.grade):8}] {r.service} :: {r.label}{flag}")
    gaps = sum(1 for r in rows if str(r.grade) == "gap")
    print(f"\n{gaps} evidence gap(s) identified across {len(rows)} pathways.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
