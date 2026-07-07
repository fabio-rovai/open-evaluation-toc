# When a Theory of Change has to hold up

A self-initiated, open method demonstrator by [Tesseract Academy](https://gov.tesseract.academy). It shows how a **Theory of Change** — the workhorse of non-experimental evaluation — can be built as a **typed, evidence-graded, machine-validated graph** rather than a prose diagram, so that its weak links are named rather than buried.

The method is worked openly on **victim and witness support** (court-based support for witnesses; support for families bereaved by homicide), with every outcome anchored to the four published **[Victims' Funding Strategy](https://www.gov.uk/government/publications/victims-funding-strategy/victims-funding-strategy)** national outcomes.

> **Independent, self-initiated reflection on method.** Built entirely from public information and open standards. It uses no confidential or commissioned data and represents no organisation's findings but our own. Evidence grades marked *illustrative* demonstrate the structure of the method; the entries marked **gap** reflect a real state of the field — widely-assumed links that are not yet robustly evidenced.

## Why this exists

The centre of government is raising the evidential bar behind spending. The [Evaluation Task Force](https://www.gov.uk/government/publications/evaluation-task-force-strategy-2026-2029) (Cabinet Office / HM Treasury) is shifting from checking that evaluation happens to ensuring evidence shapes decisions; the [Victims and Prisoners Act 2024](https://www.legislation.gov.uk/ukpga/2024/21/contents) and the Victims' Funding Strategy push victim services towards outcome-based, accountable, proportionately-evidenced commissioning. Most of that evaluation rests on a Theory of Change — and theory-based evaluation has long carried a known flaw (Weiss): the programme theory gets drawn and then not used, because on the page a link with no evidence looks identical to a link with strong evidence.

Treating the Theory of Change as data fixes that:

- every pathway resolves input → activity → output → outcome → impact;
- every outcome maps to a **published** national outcome, not a bespoke one;
- every causal claim carries an **evidence grade** (`strong` / `moderate` / `limited` / `gap`);
- every pathway declares the **assumptions** it depends on;
- a SHACL validator checks the whole graph for completeness, and the gaps are surfaced by query.

The claims a service cannot yet evidence are recorded as `gap` and flagged `priorityForEval: true`, becoming the prioritised questions for a future evaluation. This aligns with the [Magenta Book](https://www.gov.uk/government/publications/the-magenta-book) and with the Ministry of Justice's [Areas of Research Interest 2025](https://www.gov.uk/government/publications/ministry-of-justice-areas-of-research-interest-2025) interest in AI-assisted evidence synthesis.

## Contents

| Path | What it is |
|---|---|
| `ontology/toc.ttl` | Typed Theory-of-Change vocabulary + 7 worked pathways, anchored to the four Victims' Funding Strategy outcomes. |
| `shapes/toc-shapes.ttl` | SHACL shapes: completeness, outcome anchoring, evidence-grade and assumption checks. |
| `evidence/evidence-map.csv` | Structured evidence-extraction schema (population, service model, delivery mode, outcome, effect, quality grade, provenance). |
| `scripts/validate.py` | Runs SHACL validation and prints the evidence-gap map. |

## Reproduce

```bash
pip install pyshacl rdflib
python3 scripts/validate.py
```

Expected output: `SHACL conforms: True`, followed by the evidence-gap map — **2 evidence gaps across 7 pathways**.

## Method, in one line

The products a commissioner sees are the familiar ones — the diagram, the narrative, the monitoring-and-evaluation framework; the structured graph underneath is what makes them auditable, internally consistent, and reusable in the full evaluation that follows.

## Licence

Data and documentation: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). Built on Tesseract Academy's [open-ontologies](https://github.com/fabio-rovai/open-ontologies) validation approach.
