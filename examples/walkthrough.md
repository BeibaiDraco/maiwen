# A small question-development walkthrough

**Fictional illustration.** All dataset details below are invented. This is a reading example, not a completed Maiwen run, a literature novelty claim or an empirical result.

## The opportunity

A laboratory is replacing measurement protocol A with B. An individual specimen is measured once with each protocol. Acquisition order is counterbalanced, both measurements share physical units, and each specimen belongs to a different donor. The immediate question is whether the mean paired shift associated with changing the measurement procedure is small enough for an intended population-average calibration.

Before inspecting paired differences, the laboratory must justify a scientifically acceptable mean shift, called delta. For example, delta might come from the maximum change in a reported population mean that would change a practical decision. A convenient fraction of the observed standard deviation would not establish that scientific tolerance.

This question combines three kinds of preparation. The field account explains what size of measurement difference matters. The pattern bank contributes a useful move: replace a vague claim of agreement with a comparison against the intended use. The dataset account establishes pairing, independent donors, order and units. Prior-use review must still determine whether this calibration has already been established in the same population and protocols.

## The precise question

**In the eligible donor population, is the average paired difference between B and A within the independently justified tolerance for the population-average calibration?**

This asks about the average protocol difference in a defined population. It does not establish individual agreement or preservation of a between-group contrast. Equal and opposite group-specific shifts could cancel in the overall mean while changing the group contrast. Those uses require their own targets and comparisons.

## Proposed computation

Let `d_i = B_i - A_i` for donor `i`, with one paired difference per independent donor. Define eligibility and missing-pair handling before using differences to select cases. Estimate the mean paired difference and its uncertainty at the donor level. If donors contribute repeated specimens, first define the donor-level target and a model or aggregation rule; treating every specimen as independent would change both the estimand and uncertainty.

An equivalence analysis at a prespecified one-sided error level of 0.05 can use two one-sided tests, or the corresponding 90% confidence interval for the mean difference under the same model. The mean shift supports the equivalence claim only if that entire interval lies inside `(-delta, +delta)`. A paired t procedure additionally needs a defensible model for the donor differences; robustness and sample size must be checked for the actual setting. Multiple calibration populations or endpoints need their own planned error control. Failure to meet equivalence is not automatically evidence of a meaningful difference.

No paired differences or target effects have been calculated in this illustration. Before analysis, the planner still needs the justified delta, adequate precision for it, a supported population/inclusion rule and an independently reviewed procedure.

## What review changes

An early proposal said “show that the protocols are interchangeable.” A reviewer observes that a small mean shift can coexist with large positive and negative individual discrepancies. The retained question becomes “average protocol difference in this defined population.” This is a change to the scientific claim, not a disclaimer appended to an unchanged conclusion.

The final disposition is conditional until the tolerance and precision are supported. If the intended use actually requires individual agreement, the planner must develop that different question and renew the relevant literature and data checks.

For the standard equivalence logic, see Schuirmann (1987), [two one-sided tests](https://doi.org/10.1007/BF01068419). The fictional use conditions above are not attributed to that paper.
