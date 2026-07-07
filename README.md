# A machine-checkable Theory of Change for victim & witness support

A self-initiated, open, machine-readable demonstrator by [Tesseract Academy](https://gov.tesseract.academy). It shows how a Theory of Change (ToC) and rapid evidence assessment (REA) for victim and witness support can be built as a **typed, validated, queryable graph** — so that assumptions and evidence gaps are made explicit and machine-checkable, rather than buried in prose.

It is worked on the **National Witness Service** and **National Homicide Service** (both funded by the Ministry of Justice and delivered by Victim Support), and every outcome is anchored to one of the four **Victims' Funding Strategy** national outcomes.

> **This is an independent demonstration built entirely from public information.** It is not affiliated with, commissioned by, or endorsed by the Ministry of Justice or Victim Support, and contains no commissioned findings. Evidence grades marked *illustrative* demonstrate the structure of the method; the two entries marked **gap** are genuine — neither service has been formally evaluated for some time, which is the very reason such work is needed.

## Why this exists

A Theory of Change *is* a causal graph. Building it as one lets a validator check it the way a spell-checker checks prose:

- every pathway resolves input → activity → output → outcome → impact;
- every outcome maps to a national **Victims' Funding Strategy** outcome;
- every causal claim carries an **evidence grade** (`strong` / `moderate` / `limited` / `gap`);
- every pathway declares the **assumptions** it depends on.

The claims the service cannot yet evidence do not disappear — they are recorded as `gap` and flagged `priorityForEval: true`, becoming the prioritised questions for a future evaluation. This aligns with the [Magenta Book](https://www.gov.uk/government/publications/the-magenta-book) and with the Ministry of Justice's stated interest ([Areas of Research Interest 2025](https://www.gov.uk/government/publications/ministry-of-justice-areas-of-research-interest-2025)) in AI-assisted evidence synthesis.

## Contents

| Path | What it is |
|---|---|
| `ontology/toc.ttl` | Typed Theory-of-Change vocabulary + 7 worked pathways (4 Witness, 3 Homicide), anchored to the four Victims' Funding Strategy outcomes. |
| `shapes/toc-shapes.ttl` | SHACL shapes: completeness, outcome→VFS alignment, evidence-grade and assumption checks. |
| `evidence/evidence-map.csv` | Structured REA extraction schema (population, service model, delivery mode, outcome, effect, quality grade, provenance). |
| `scripts/validate.py` | Runs SHACL validation and prints the evidence-gap map. |

## Reproduce

```bash
pip install pyshacl rdflib
python3 scripts/validate.py
```

Expected output: `SHACL conforms: True`, followed by the evidence-gap map — **2 evidence gaps across 7 pathways** (in-court attendance effect; homicide CYP outreach).

## Method, in one line

GSR/Magenta Book bodywork, an ontology engine underneath: the deliverables a commissioner sees are the standard ToC diagram, narrative and M&E framework — the structured graph is what makes them auditable, consistent across parallel service strands, and reusable in the full evaluation that follows.

## Licence

Data and documentation: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). Built on Tesseract Academy's [open-ontologies](https://github.com/fabio-rovai/open-ontologies) validation approach.
