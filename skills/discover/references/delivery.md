# Deliver research someone can act on

Write `recommendations.md` as a complete research dossier in English. A colleague who has not followed the conversation should understand the question, why it matters, what the actual data support and how to carry out the proposed study. Open with the scientific question and the opportunity it offers, making its supported or conditional status clear. If none qualifies, explain the substantive finding and next decision. Develop a readable account with enough detail to implement and assess each proposal. Let the research determine the length.

## Explain the scientific case and computation

Lead each developed question with its exact unknown and why a useful answer would change scientific understanding or a practical decision. Explain the closest primary comparison and the remaining increment, then the measurements and design that make this comparison possible. Cite deciding passages and checks beside the claims they support. Distinguish local observations, documentation, inference and unknowns. Let a reader understand the argument without reconstructing it from intermediate notes.

Write the target quantity in ordinary language before notation. Follow the proposed computation from inputs and eligible population through transformations, weights, estimation, uncertainty and interpretation. Specify choices that alter the scientific object or verdict; routine programming choices need no exhaustive prescription. Use equations or pseudocode where prose is ambiguous, and [implementation handoff](implementation-handoff.md) to expose remaining scientific decisions.

Describe positive, negative and inconclusive outcomes at the scope this computation supports. Compare those interpretations with the opening and payoff: do they imply the same measurement, time, population, mechanism and degree of generality? Repair the scientific explanation itself when they differ. A conditional heading or a distant caveat does not cure a stronger affirmative claim.

Keep scientific support separate from computational completeness. A complete algorithm may depend on an unresolved owner fact; a promising question may still lack a defined estimator or decision rule. State which is true, and what would settle it. Explain meaningful tolerances and precision evidence without inventing a default or calling a surrogate calibration complete. Use [answerability](answerability.md) when this changes the disposition.

Write in direct, connected scientific prose for a colleague new to the task. Define specialist terms, give concrete examples and use tables/diagrams where they clarify the comparison. Place consequential qualifications beside the affected claim; consolidate repeated scope and review bookkeeping into a short linked note. Avoid repetitive defensive contrasts. Detailed plans and evidence remain available, while the main account explains why the computation answers this question.

Distinguish proposed analysis from performed planning checks. Label structural/synthetic evidence and prior target exposure, and apply the [planning boundary](../../dataset-card/references/generic-probes.md#default-planning-scope) to the actual calculation. Close with the supported scope and smallest next scientific decision, preserving existing owner answers.

## Worked writing example

Use this fictional example to match the level of explanation, not as a research template. Every number and dataset detail below is invented; actual recommendations need sources and inspected support. The calculation is a proposed analysis, not a discovery-stage effect test.

**How much does changing the measurement protocol shift the population mean?** A study plans to replace protocol A with B. Its intended population-average calibration treats a mean protocol difference of 2 measurement units as consequential. The question is whether the average difference stays within that tolerance. Establish the tolerance from the intended use before examining differences. This target concerns one defined population; individual agreement and preservation of between-group contrasts require their own comparisons.

**Use paired measurements to estimate the protocol difference.** Suppose 60 independently sampled specimens each provide an aliquot to both protocols, processing order is randomized, and measurements use the same physical unit. Each specimen supplies its own comparison, reducing the influence of differences between specimens. The sampling frame defines the target population. Shared source individuals would require an uncertainty method that accounts for that dependence.

**Calculate a difference for each specimen, then the mean and its precision.** Use `specimen_id`, `protocol`, `value`, `unit` and a documented measurement-validity flag. Join one valid numeric result from each protocol to each specimen; resolve duplicate keys before joining. Retain all valid pairs, including large differences, and report missing pairs and reasons for exclusion. This estimates the complete-pair mean; extension to missing pairs needs a justified missingness model. If there are repeated technical readings, define their aggregation first.

For every retained pair set `d_i = value_B - value_A`. Give each specimen equal weight and estimate the shift by `mean(d)`, in the original unit. With at least two independent pairs and approximately normal differences, use the interval `mean(d) ± t(0.975, n-1) * sd(d, ddof=1) / sqrt(n)`. Check the support for those assumptions before treating the interval as suitable; otherwise resolve the uncertainty method. There is no predictive fitting in this comparison, so the estimand needs no train/test split. The planned output shows paired values, the difference distribution and the mean interval against the tolerance band.

**Interpret the interval relative to the scientific tolerance.** An interval wholly inside [-2, 2] supports a mean shift within the stated population-average tolerance under the assumptions. An interval wholly above 2 or below -2 supports a consequential shift. An interval crossing a boundary leaves that decision unresolved. This mean comparison does not establish individual agreement, concentration-independent bias or preservation of group contrasts. For example, opposite group-specific shifts can cancel in the overall mean while changing a between-group difference.

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

## Preserve the knowledge and development trail

Link the workspace index to the reviewed field account, pattern bank and its project selection, dataset card/source report/prior-use account, detailed paper notes, generation input, all candidates, screening, per-question development/plans/reviews and final review. Let a reader inspect what the questioner knew and how the final question changed. Explain rejected and capacity-deferred directions without inflating them into recommendations. Keep all intermediate and final artifacts in English, including figure captions, saved summaries and NEXT; conversation with the user may use their language. Preserve original sources and prior frozen outputs rather than rewriting history.
