# Planning probes

Use an initial broad pass to discover opportunities, then targeted checks to evaluate candidates. Choose representative units and design conditions before seeing response summaries. Record inputs, scope and the planning purpose alongside the result; one explanation per batch is enough.

- **Units and repeats:** Identify independent units and their nested observations using the collection documentation. Count repeats and coverage in the inspected scope.
- **Design variation:** Locate within-unit and between-unit variation, randomization, natural contrasts and variables tied to collection time. Identify separable comparisons and design confounding.
- **Joint measurements:** Check actual common observation keys, key multiplicity and simultaneous modalities. Report missing joins before choosing aggregation.
- **Timing:** Verify clocks, units and reference events. Authorized response-time distributions can establish available windows and measurement limitations; compare these with the scientific timescale under consideration.
- **Response coverage:** In authorized planning data, summarize response categories, error/no-response counts, missingness and marginal distributions with denominators. These help establish whether useful comparisons are represented.
- **Selection and missingness:** Read inclusion rules, sentinel definitions and known collection failures. Identify whether sampled coverage excludes a relevant group or condition.
- **Unusual combinations:** Look for measurements, repetitions or contrasts rarely available together; connect them to plausible scientific distinctions.

Use the existing profiler for structure. For additional summaries, write the smallest dataset-local reader after checking format and scope. Review custom serialized inputs before loading them; a filename alone establishes neither trust nor a permission requirement. Simulations can assess a proposed design under explicit assumptions when a candidate warrants them.

## Default planning scope

Use authorized data for documentation/schema inspection, bounded samples and planning diagnostics of counts, distributions, missingness, timing and valid coverage, including outcome variables. Use structural and synthetic checks to evaluate designs under stated assumptions. Record the inspected scope and exposure; leave candidate target-effect tests, significance searches, full analyses and confirmation outcomes outside discovery. A single-variable summary can be a target effect. If a later question targets an inspected summary, identify the affected scientific choices, disclose their origin and plan suitable independent evaluation. Reading raw values or authorized planning marginals does not by itself require replacing the whole dataset; match the evaluation to the actual exposure and claim.

Judge a calculation by what it establishes, not by whether its inputs are outcomes or explanatory covariates. A decoder, contrast test or absence/equivalence bound on real observations that selects the candidate's target window from observed predictive performance, effects or their absence, or supports its substantive claim, is target analysis. Keep it for a separately scoped analysis; use documentation, authorized measurement/coverage checks or synthetic alternatives for planning. If it has already been run, record the exposure and affected choices, withdraw unsupported result claims and revise the affected design's independent-evaluation plan. This does not exclude bounded covariate-overlap or collinearity checks used to assess design support.

Reuse the user's existing access and transmission permissions. These defaults define the research task, not new permission to upload private data or papers, enter reserved paths, or use another model service. When a necessary scope fact is unclear, ask about that fact and continue unaffected work. The host/environment enforces access; this guide is not a sandbox.
