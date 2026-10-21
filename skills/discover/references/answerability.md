# Establish what the proposed design could answer

Start with the exact scientific claim, target quantity or model comparison, population, independent unit, operational measurements and scope of generalization. Link each indispensable observed condition to documentation or an executed check. State inferential assumptions separately. Choose the diagnosis that could change the decision; file counts, full rank or successful code execution alone do not establish answerability.

## Match the check to the question

| Aim | Evidence to develop before recommendation |
| --- | --- |
| Describe or associate | Sampling/selection, measurement validity, nested units, missingness and uncertainty at a scientifically useful scale. Use analytic precision bounds or simulations appropriate to the design. |
| Predict or generalize | Information available at prediction time, comparison baseline, independent split units, possible leakage, target population and a credible sample/uncertainty argument. Reserve actual target-performance testing for analysis. |
| Replicate or assess robustness | Exact previous claim, the reason for revisiting it, comparable measurements/design and precision needed to inform that claim. |
| Distinguish mechanisms/models | Explicit observation and competing models, necessary identifying variation and nuisance structure; test observational equivalence before investing in recovery. |
| Estimate a causal effect | A defensible identification strategy and its assumptions, temporal order, support, selection and relevant alternative explanations. An intervention is one possible design, not the only one. |

Inspect valid joint coverage at the unit and window required by the actual comparison. Shared file keys do not establish co-measurement. Resolve special codes, event alignment, preprocessing, filtering and release corrections that can change the claim. Read [operational definitions](../../dataset-card/references/operational-definitions.md) when these issues matter.

## Use mathematical and synthetic checks purposefully

If algebra or a logical counterexample shows that distinct explanations give the same observation, record it and revise or stop that comparison. A fitted winner does not refute equivalence. In normalized, residualized or nonlinear models, derive a claimed cancellation or exclusion on the actual observation and link-function scales. Centering a covariate alone does not establish that a nuisance contribution to the response disappears. In repeated designs, test whether time, order and treatment can vary independently enough for the claim.

When recovery or precision is uncertain, simulate under explicit plausible assumptions using the inspected design scale, clustering and missingness where relevant. Before interpreting calibration, check generated observations for the claimed scale, timing, noise and sampling structure. Where a synthetic check will decide admission or rejection, first establish expected behavior in a known or noise-free case; trace consequential discrepancies through preprocessing, boundaries and the statistic before attributing them to the dataset's information limits. Run the proposed estimator against alternatives, varying signal, nuisance parameters and plausible mismatch. Include an indistinguishable or low-information case and a case where the intended scientific conclusion is false. Report confusion, uncertainty, bias or precision relevant to the aim; distinguish decisive recovery from ties, unstable rankings and simplification preference. A favorable aggregate score does not by itself establish a claim restricted to a particular time, location or subgroup.

Match precision or recovery evidence to the proposed computation from learned inputs through its reported interpretation, including any fitted direction, selected features, split, eligibility step or decision gate that affects the claim. If a check holds a learned object fixed, report the conditional quantity it validates and separately assess whether learning noise could hide the scientifically relevant difference. A narrow interval for an estimated proxy need not bound the underlying scientific object. A calculation for a simpler or different model is an illustration, not validation of the proposed analysis.

A simulation result establishes behavior under its stated assumptions and range. Connect that result back to the actual design and measurement evidence; it cannot validate unobserved real-world assumptions. Obtain noise or effect ranges from appropriate literature or already-authorized planning evidence, without searching the real candidate effect or accessing confirmation data.

## Decide on sufficient support

Identify the weakest necessary assumption and the most informative affordable check. Carry it out when the answer could reverse the recommendation. An unverified necessary measurement can block; an irrelevant verified fact need not. Describe the strength and limits of the resulting evidence, including where the dataset can give a useful inconclusive answer.

Recommend only when the value and proposed inference are supported at the stated scope and no unresolved necessary condition could overturn that support. Separate justified assumptions from unchecked facts. If the remaining gap needs a pilot, provide the exact next diagnostic and decision it would enable, without counting pilot-readiness as completed answerability or guaranteeing a publishable result.
