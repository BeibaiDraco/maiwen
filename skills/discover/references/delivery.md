# Write a research report a scientist can use

Write `recommendations.md` in English for a colleague who has not followed the conversation. Explain the scientific question, why an answer matters, what the data contribute and how the proposed study would work. State whether the question is supported or still conditional. If none qualifies, explain what the investigation established and which decision would be useful next. Let the research determine the length.

## Build the explanation around the question

Begin each developed question with a concrete unknown: what might differ or remain stable, in which system or population, and over what conditions or timescale? Explain why plausible answers would change an interpretation, resolve a disagreement or inform a useful decision. Introduce the closest previous study through its question, comparison and finding, then identify what remains to learn. Cite the relevant passage or check beside the claim it supports.

Describe the measurements and design that make the proposed comparison possible. Define specialized terms when they first appear. Introduce the target quantity in ordinary language before giving it a symbol. Follow the computation from eligible observations through transformations, weights, estimation and uncertainty to interpretation. Specify decisions that change the scientific meaning; use equations or pseudocode where they make the procedure clearer. The [implementation guide](implementation-handoff.md) helps identify scientific choices that are still unresolved.

Explain what positive, negative and inconclusive outcomes would mean. Keep the population, measurement, timescale and strength of inference consistent with the opening question and claimed contribution. If the calculation answers a narrower question, revise that explanation throughout the report. Put a limitation where it changes the interpretation and explain its consequence there.

Distinguish a complete calculation that awaits a collection fact from a promising question whose estimator or decision rule is still undefined. State the fact or method choice needed in each case. Justify scientific tolerances and expected precision from the intended use and available evidence; see [answerability](answerability.md).

Write connected paragraphs that develop the scientific argument. Prefer concrete statements such as “compare each participant's response in the two sessions” to labels such as “assess cross-context robustness.” Tables help compare alternatives; a diagram can clarify a design or calculation. Keep administrative details, version records and repeated review status in short linked notes. Describe performed checks and proposed analyses with the appropriate tense, and record relevant prior exposure under the [planning scope](../../dataset-card/references/generic-probes.md#default-planning-scope).

## Worked writing example

This fictional example illustrates the level of explanation. Its numbers and dataset details are invented, and its calculation describes a future analysis.

**How much does changing the measurement protocol shift the population mean?** A study plans to replace protocol A with B. For its intended population-average calibration, a mean protocol difference of 2 measurement units would matter. The question is whether the average difference stays within that tolerance. The laboratory must justify the tolerance from the intended use before examining differences. Individual agreement and preservation of group contrasts are different questions that require their own comparisons.

**Pair measurements from the same specimen.** Suppose 60 independently sampled specimens each provide an aliquot to both protocols, processing order is randomized, and measurements use the same physical unit. Each specimen supplies its own comparison, reducing the influence of differences between specimens. The sampling frame defines the population of interest. If several specimens share a source individual, the uncertainty calculation must account for that dependence.

**Calculate each paired difference, then estimate the mean and its precision.** Use `specimen_id`, `protocol`, `value`, `unit` and a documented measurement-validity flag. Resolve duplicate keys, then join one valid numeric result from each protocol to each specimen. Retain all valid pairs, including large differences, and report missing pairs and reasons for exclusion. This estimates the complete-pair mean; extending it to missing pairs requires a justified missingness model. Define aggregation first if there are repeated technical readings.

For each retained pair, set `d_i = value_B - value_A`. Give specimens equal weight and estimate the shift by `mean(d)` in the original unit. With at least two independent pairs and approximately normal differences, use the 95% interval `mean(d) ± t(0.975, n-1) * sd(d, ddof=1) / sqrt(n)`. Check those assumptions before choosing this procedure; resolve an appropriate uncertainty method otherwise. This is a direct estimate of a paired mean, with no predictive fitting or need for a train/test split. Show the paired values, difference distribution and mean interval against the tolerance band.

**Interpret the interval against the scientific tolerance.** An interval wholly inside [-2, 2] supports a mean shift within the stated population-average tolerance under the assumptions. An interval wholly above 2 or below -2 supports a consequential shift. An interval crossing a boundary leaves the decision unresolved. Opposite group-specific shifts could cancel in the overall mean while changing a between-group difference. Individual agreement, concentration-independent bias and preservation of group contrasts therefore require additional targets and comparisons.

**Next step.** Verify pairing, units, sampling, the scientific tolerance and expected precision. These checks determine whether the proposed analysis is ready. No target differences have been calculated in this illustration.

## Show how the research developed

Save evidence and decisions as the work proceeds. Link the relevant brief, data card, paper notes, candidates, checks and reviews from the report. A reader should be able to see:

- what observation, literature finding or reasoning pattern suggested an opportunity;
- which checks ran, on which data, with which assumptions, script or command, and where their compact outputs are saved;
- what changed the question, including rejected alternatives and unresolved contradictions;
- what a reviewer challenged, which revision was rechecked and what remains unsettled.

Keep these records concise and proportional to their effect on the conclusion. Save scientific rationales and evidence, rather than private deliberation or full agent transcripts. Include the input version and dependencies needed to repeat a local check. Use permitted source pointers for raw data and private papers; keep credentials and signed URLs out of shareable notes. Record access, search and budget limits where they affect the conclusion.

## Review the finished report and prepare continuation

Give the final reviewer the finished report, `NEXT.md`, plans and intended user-facing summary using the [final-document instructions](critique.md#check-the-finished-document). It checks the scientific claims, their evidence, the calculation and the clarity of the explanation across those documents. Verify consequential repairs within the existing allowance and record which revised work was actually reviewed. Unfinished rechecks stay visible.

Describe each direction according to its evidence: supported, conditional, review pending, deferred for capacity or rejected. For unresolved work, explain the specific gap and next action. If no question qualifies, report the substantive conclusions of the investigation and the most useful next decision.

Update `NEXT.md` with the stopping reason, remaining budget and repair allowance, the smallest useful continuation, necessary owner facts and links to the relevant evidence. Identify any new evidence or authorization needed. On resumption, read these records, check for changed inputs and continue the unresolved work. The final message should describe the same question and review status as the report.

## Make the full preparation accessible

The workspace index should link to the field account, pattern library and project selection, dataset card, collection report, prior uses, paper notes, questioner inputs, candidates, screening, development notes, plans and reviews. Let the reader inspect both what the questioner knew and how the questions changed. Keep all new research documents, captions, saved summaries and `NEXT.md` in English. Preserve original sources and frozen outputs; conversation may follow the user's language.
