---
name: dataset-card
description: Discover research opportunities by building a broad, source-backed data card from an authorized dataset, with or without a seed question; deepen the card as candidates emerge.
---

# Discover what the data make possible

Write all saved notes, check explanations and summaries in English. Use the coordinator's assigned location; for new work, default to `research/<dataset>/knowledge/dataset/card.md` with checks in the adjacent `checks/` directory. When continuing older work, link the existing card from the current workspace index rather than silently creating a competing version or rewriting frozen records. Read [the card guide](references/card-template.md) and retain scripts, inputs and outputs so another researcher can inspect the evidence.

## First pass: build breadth before choosing questions

1. Locate the data, dictionary, collection papers and processing code. Apply the [default planning scope](references/generic-probes.md#default-planning-scope), recording existing authorization and exclusions rather than asking again.
2. Map the collection purpose, measured variables, independent and repeated units, assigned conditions, timing, modalities and joint measurements. Open a small representative sample of the needed format before relying on it. Use `scripts/profile.py` for supported formats and reviewed dataset-local readers for other authorized summaries; resolve dependencies only for the modalities currently needed.
3. Inspect representative coverage across design conditions, units and modalities. Within authorized planning data, summarize counts, missingness, ranges and distributions, including behavioral responses. Record the denominator and inspected scope for each summary.
4. Build a table showing which scientific distinctions the collection design could resolve: what is being compared, what separates the alternatives, which observations are available and which explanations remain confounded. Start from the design and measurements even when there is no candidate; use [the probe guide](references/generic-probes.md) to choose useful checks.
5. Describe unusual research opportunities: rare combinations of measurements, repeated observations, natural contrasts, timing or coverage. Explain what kinds of questions each could support and the evidence still needed. Record early ideas separately; formal generation receives this broad account alongside reviewed field knowledge and question patterns.
6. Resolve remaining owner-only facts with a few [targeted questions](references/owner-interview.md). Save the broad card before committing to one direction.

## Second pass: deepen around candidates

For each promising candidate, read [operational definitions](references/operational-definitions.md) and inspect the meaning of the recorded measurements, special values, denominators, filters, release corrections and valid joint windows needed for its comparison. Test a defensible alternative definition if the first one may misrepresent the scientific object. Update the card with findings that could preserve, reframe or reject the question. Separate documentation, code inference, observation and owner reports. Revisit affected facts when the dataset changes.

## Profiler use

```bash
python3 <skill-dir>/scripts/profile.py /absolute/path/to/table.csv
python3 <skill-dir>/scripts/profile.py /absolute/path/to/table.csv \
  --sample-rows 100 --columns subject_id,response
```

The helper exports structure and selected-column missingness/types. Write a small local check for additional authorized distributions or design coverage; use existing tools or a focused script suited to the data. Use a reviewed reader for custom formats and preserve sampling limits in the card.
