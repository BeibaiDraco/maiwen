# Deliver research someone can act on

Write `recommendations.md` as a complete research dossier in the user's preferred language. A colleague who has not followed the conversation should understand the question, why it matters, what the actual data support and how to carry out the proposed study. Open with the scientific question and the opportunity it offers, making its supported or conditional status clear. If none qualifies, explain the substantive finding and next decision. Develop a readable account with enough detail to implement and assess each proposal. Let the research determine the length.

## Explain the scientific case

Write as a scientist explaining an interesting problem to a colleague. Develop what happens, what is unknown, why the comparison is informative and what different answers would teach us. Use concrete examples before technical notation and choose headings that name the science. State each consequential condition where it affects the interpretation or computation, with its practical implication or next check. Consolidate repeated scope, authorization and review bookkeeping in a short status note with evidence links. Edit out generic disclaimers, repeated negative contrasts and precautionary lists that add no decision; retain the substantive limits and precision of the claim. Apply this style to the readable field map and research notes as well as the final dossier.

Build a coherent account for each developed question. The following are content needs, not a form to fill or a required set of headings; combine them where that improves the explanation.

- **Exact question and stakes.** Describe the concrete setting, population, comparison, target quantity and intended claim in ordinary language before introducing notation. Explain the knowledge or practical decision at stake and what a useful answer would change. Define specialist terms when first needed.
- **Closest evidence and remaining contribution.** Explain what the closest primary work actually established, with paper/section/figure or code locators, and how the proposal differs. Connect same-data precedents and relevant work from other systems to this exact question. State unresolved close leads and search limitations; do not turn an incomplete search into a novelty claim. If paper reasoning generated or changed the proposal, link the actual source-to-target mapping.
- **Actual dataset support.** Identify the data release and authorized scope, measurement meanings, sampling and independent units, relevant timing and coverage. Report the decisive inspected counts or diagnostics at the units the claim requires, including exclusions or conflicts that change the usable comparison. Link the supporting script/output or documentation beside the fact. Separate observed facts, documentation, owner reports, code inference, design choices and unknowns. A file count or a general data card cannot substitute for evidence about the final design.
- **Why this design can answer this question.** Connect identifying variation, assumptions and precision/recovery evidence to the proposed claim. Explain the weakest necessary condition and any important alternative explanation. State whether support is direct, bounded by justified assumptions, or still conditional. Put a decisive limitation next to the claim it limits, even when further details live later in the report.

Do not make the reader reconstruct the main scientific argument from intermediate notes. Use tables or diagrams when they clarify the comparison, data flow or competing interpretations, without turning every decision into a table. Explain the reasoning behind the final design at a level a scientific colleague can inspect; omit private deliberation and repetitive work logs.

## Specify the proposed computation

Give an implementable chain from inputs to interpretable outputs. Write equations or pseudocode where prose leaves consequential ambiguity. Name the following where relevant to the design, and explain consequential items that do not apply:

1. Inputs, variable meanings and units, eligibility and exclusion rules; keys and join cardinalities; special codes, windows and alignment; duplicate and invalid-record treatment. State the resulting target population and unit of analysis.
2. Transformations and aggregation, including nested/repeated units, weighting, missingness and sparse-condition handling. Distinguish prespecified choices from choices that still need justification; link the evidence for recoding and measurement definitions.
3. The target quantity, estimator or model, comparisons/baselines, controls and relevant assumptions. Specify enough of the formula, predictors or algorithm that an implementer does not have to invent the scientific comparison. Give any meaningful tolerance or decision threshold its scientific basis rather than choosing it from the observed target result.
4. Training, tuning and evaluation separation when needed, with independent split units, information available at prediction time and leakage prevention. For a non-predictive estimand, explain why a split is unnecessary or what independent evaluation is planned.
5. Uncertainty at the correct dependence level, relevant multiple-comparison handling and targeted sensitivity checks. Connect the proposed precision or recovery diagnostic to this estimator and scale; a successful simpler calculation is only an illustration.
6. Expected output tables, figures and quantities, followed by the interpretation each would permit. Cover plausible positive, negative and inconclusive outcomes without inventing results. Distinguish a meaningful absence from inadequate precision, prediction from explanation and association from a causal claim as appropriate.

Keep the proposed analysis distinct from checks already performed. Label diagnostic numbers as planning evidence, and report prior outcome exposure when it affects later independent evaluation. The [default planning scope](../../dataset-card/references/generic-probes.md#default-planning-scope) still applies: describing an analysis or writing a skeleton does not authorize running candidate target effects. Use [answerability](answerability.md) if an unresolved choice or new evidence changes the question's disposition.

Close each developed proposal with its supported scope, limitations and practical next action. State necessary access, dependencies or resource constraints when they affect feasibility. Explain which unresolved facts or scientific choices prevent implementation or recommendation, who can resolve them when known, and what the answer would change. Preserve already-reported unknowns rather than repeatedly asking the owner the same question.

## Worked writing example

Use this fictional example to match the level of explanation, not as a research template. Every number and dataset detail below is invented; actual recommendations need sources and inspected support. The calculation is a proposed analysis, not a discovery-stage effect test.

**Will changing the measurement protocol shift the group comparison?** A study plans to replace protocol A with B. Its scientific contrast is small enough that a mean shift of 2 measurement units would affect interpretation. The question is whether the average change stays within that tolerance. Establish the tolerance from the intended scientific use before examining differences. The answer will guide pooling for this mean comparison; specimen-level agreement is a separate question.

**Use paired measurements to isolate the change.** Suppose 60 independently sampled specimens each provide an aliquot to both protocols, processing order is randomized, and measurements use the same physical unit. Each specimen supplies its own comparison, reducing the influence of differences between specimens. The sampling frame defines the target population. Shared source individuals would require an uncertainty method that accounts for that dependence.

**Calculate a difference for each specimen, then the mean and its precision.** Use `specimen_id`, `protocol`, `value`, `unit` and a documented measurement-validity flag. Join one valid numeric result from each protocol to each specimen; resolve duplicate keys before joining. Retain all valid pairs, including large differences, and report missing pairs and reasons for exclusion. This estimates the complete-pair mean; extension to missing pairs needs a justified missingness model. If there are repeated technical readings, define their aggregation first.

For every retained pair set `d_i = value_B - value_A`. Give each specimen equal weight and estimate the shift by `mean(d)`, in the original unit. With at least two independent pairs and approximately normal differences, use the interval `mean(d) ± t(0.975, n-1) * sd(d, ddof=1) / sqrt(n)`. Check the support for those assumptions before treating the interval as suitable; otherwise resolve the uncertainty method. There is no predictive fitting in this comparison, so the estimand needs no train/test split. The planned output shows paired values, the difference distribution and the mean interval against the tolerance band.

**Interpret the interval relative to the scientific tolerance.** An interval wholly inside [-2, 2] supports a mean shift small enough for the intended pooling decision under the stated assumptions. An interval wholly above 2 or below -2 supports a consequential shift. An interval crossing a boundary leaves that decision unresolved. This mean comparison says little about individual errors or concentration-dependent bias, which would need their own comparisons.

**Next step.** Verify pairing, units, sampling, the scientific tolerance and expected precision. Those checks determine whether the proposed analysis is ready. The quantities above describe a fictional future study; no target differences have been calculated.

## Keep the research path visible

Save useful intermediate records as the work proceeds, not only a retrospective success story. Use the existing brief, card, prior-use, candidate, check and review notes; add a focused note only when it makes evidence easier to inspect. Link the relevant records from the dossier so a reader can follow:

- which data observations, literature findings or paper transfers opened an opportunity;
- which checks were run, on what input scope, with which script/command and assumptions, and where their compact outputs can be found;
- which findings changed a decision, including material reframes, alternatives considered, rejected directions and unresolved contradictions;
- what independent reviewers challenged, which actual repaired revision was verified against which evidence, and what remains unsettled.

These are concise records of evidence, decisions and their scientific rationale, not hidden chain-of-thought, full agent transcripts or a new state protocol. Keep detail proportional to its effect on the conclusion. Store reusable scripts and compact diagnostics with enough input/version and dependency information to repeat the check. Do not copy raw data, private PDFs, credentials or signed URLs into shareable notes; use permitted source pointers. Record budget, access and search limits where they constrain the conclusion.

## Check the finished dossier and enable continuation

Prepare the report, `NEXT.md` and intended user-facing summary for the [final-document check](critique.md#check-the-finished-document) of their exact versions: evidence and claims, readability, implementation handoff and agreement about supported scope. Use the bounded repair/verification cycle there for consequential defects, including reviewer-proposed fixes. Record which revised work was actually checked and retain pending checks when the allowance or task budget ends. A review of an earlier candidate does not cover a new method, and a later correction does not retroactively validate the original delivery.

Group other work by actual disposition: worth a decisive pilot, unresolved, or rejected with evidence. Explain the specific gap and next action. A recommendation to continue designing is distinct from a supported research question; neither completed templates nor counts of gaps decide acceptance. If no question qualifies, deliver the substantive negative findings and most useful next decision rather than padding the recommendation list.

Update `NEXT.md` with the smallest useful continuation, the current stopping reason, owner-only facts needed and links to the relevant evidence and review. State any necessary new evidence or authorization before further work; do not offer another repair cycle as though its recorded allowance were unused. On resumption, read the brief, recommendations, pending actions and their evidence, check for changed inputs and continue from the unresolved decision. Update affected work after user interventions instead of automatically restarting. The final user message must retain the report's limits and review status rather than upgrading a conditional proposal to a supported recommendation.
