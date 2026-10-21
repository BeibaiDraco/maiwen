# Check whether the dossier can be implemented

Use this to test whether a colleague could implement the proposed computation, during final-document review or earlier when a key inference needs an implementation check. Use an independent host-native context when available and authorized. Provide the current proposed computation or completed dossier, linked authorized evidence, accessible data locations or necessary samples/documentation, and the planning boundary. For the initial assessment, withhold the author's conversation, intended answers to unresolved choices and earlier reviewer verdicts; a repair check receives the specific finding and changed work as described below. Record what the implementer actually received; inaccessible links are delivery gaps, not permission to seek unauthorized access.

## Attempt the handoff

Ask the implementer to translate the proposed analysis into an ordered computation and identify where the document stops being sufficient. For a substantial or technically ambiguous plan, a small code skeleton with synthetic fixtures can make this concrete. For a simpler plan, annotated pseudocode and a decision-gap report can be enough. Reuse existing tools and libraries; do not build a framework or require a new API/provider call.

Follow the document from input records through eligibility, joins, transformations, units and weighting to the target quantity, estimator, uncertainty and output interpretation. Link each consequential implementation decision back to the dossier or evidence. Routine choices such as function organization, file naming and equivalent library implementations can be made and recorded briefly. Distinguish them from choices that alter the population, measurement, comparison, estimand, assumptions or evaluation: do not silently invent the latter, copy a convenient default, or infer them from the result the author seems to want.

For a missing scientific choice, report the precise gap, the affected computation or claim, plausible alternatives when helpful, and the evidence or decision needed to proceed. Keep unresolved branches explicit. If producing code, leave those branches unimplemented or fail with an explanatory error rather than supplying a scientifically consequential default. Treat an implementer's proposed method as an unverified suggestion, and check its assumptions and scientific consequences before adopting it. Preserve already-answered owner questions, including answers that a fact is unknown.

## Keep the check within planning

A skeleton is a proposed implementation, not an executed study. Use only authorized structure checks and synthetic fixtures to exercise joins, aggregation, split isolation, uncertainty formulas or output shapes where useful. Label synthetic data and diagnostic numbers clearly. Do not fit or test candidate target effects on real data, measure target predictive performance, search significance or access confirmation outcomes. The [default planning scope](../../dataset-card/references/generic-probes.md#default-planning-scope) governs any actual data inspection. Do not run a complete target analysis merely to demonstrate that the skeleton works.

Report what was written, what was run, on which permitted inputs and proposed procedure revision, and what remains untested. If a check is used to validate a new rule, exercise that actual rule with a relevant failure case as well as its intended behavior; a simpler surrogate does not validate the complete procedure. Passing synthetic checks establishes only those implementation properties under the stated fixture; it does not establish real-data identification, precision, scientific value or correctness of unverified measurement assumptions.

## Return an actionable result

Return the proposed computation or skeleton, any checks and their outputs, and a concise report of:

- scientific decisions or missing evidence that block faithful implementation;
- document ambiguities or missing links that the author can repair;
- routine implementation choices made without changing the scientific design;
- the portion that could be implemented faithfully and the limits of the check.

Put these results in `review.md` and link any code or longer report. Use the [bounded repair and verification cycle](critique.md#repair-verify-and-stop): the author repairs the dossier or supports a scientific choice with evidence, then the reviewer checks the actual changed computation and its affected claims. A promise to implement or calibrate later leaves that part pending. Retain a conditional disposition when the gap remains; do not turn implementer convenience into scientific authority. A successful handoff establishes that the plan can be translated, while substantive evidence and review determine whether the question is worth recommending.

## Make continuation easy

Prepare a ready-to-use next request in `NEXT.md` alongside the dossier so the [final check](critique.md#check-the-finished-document) covers both. Fill it from the actual files and existing authorization, naming the dossier's exact path and revision (version, dated revision or hash), the requested action and unresolved scientific decisions. For example:

> Continue from [dossier path and revision], [brief path], [NEXT path] and the linked evidence. Next, [specific planning action or implementation-preparation task]. The unresolved scientific decisions are [decisions and source locations]; preserve recorded owner answers, including unknowns. Existing authorization is [source and permitted scope]. Prepare [requested output] within that scope. This planning handoff does not authorize candidate target-effect execution on real data.
