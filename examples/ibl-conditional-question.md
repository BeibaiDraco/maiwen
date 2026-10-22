# IBL: does temporal persistence carry from spontaneous activity into behavior?

**Historical conditional direction, not an analysis-ready recommendation.** This is an edited account of a Codex discovery using Maiwen `0.2.0-alpha.3`. It preserves the scientific stopping point. The original run inspected a bounded 36-session IBL planning view, not the whole release. The beta candidate did not regenerate or validate this question.

## Why ask it?

Temporal persistence describes how a neuron's activity covaries over time. An atlas measured during spontaneous activity is attractive as a compact description of neural dynamics. To use it when interpreting behavior, one needs to know what carries between recording contexts: the relative ordering of units, their absolute values, or neither.

The question was: **do the same sorted unit identities retain their relative long-lag persistence from the final task period to the subsequent spontaneous period, and is any change consistent with common rescaling or does it differ among units?** Reliable reordering would limit use of a spontaneous atlas for those units during behavior. Stable ordering could support relative portability in this recorded setting; it would not mean individual values are unchanged.

## Existing work narrows the contribution

[Shi and colleagues' BWM study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12407892/) estimates spontaneous persistence, including mixtures of decay components, and relates it to task selectivity. [Fontanier and colleagues](https://elifesciences.org/articles/63795) already examine engagement and pause timescales in the same neurons using a different spike-pair statistic. Thus, a generic claim that timescales differ between rest and task would be insufficient.

The possible contribution is the matched measurement and portability comparison in this IBL setting. The original run also checked adjacent timescale literature and a recent IBL micropublication; exact code overlap remained unaudited. This short example is not an exhaustive novelty review. Any new continuation must reopen the closest work and its current code before asserting a remaining gap.

## What was actually available?

In the authorized view, 27 sessions had explicit spontaneous-interval labels. Twenty-four had at least 600 seconds of marked spontaneous time, spanning 36 insertions and 3,977 potential sorted-unit identities. These are structural availability counts. They do not certify continuous acquisition, stable biological cells or reliable timescale estimates.

The proposed comparison used the final 600 seconds of task and the first 600 seconds of the marked spontaneous block, split into two 300-second records per context. Task always preceded spontaneous recording. Time, satiety and recording drift therefore remained alternative explanations for a context difference. This was a descriptive portability question, not an identified effect of engagement on intrinsic dynamics.

## The calculation and the decisive difficulty

The plan specified count covariance at matched binning and lag support, normalized by the record's count variance. For each unit it would estimate a persistence curve in the four records, evaluate repetition within context, then compare cross-context relative and absolute agreement while respecting mouse/session dependence.

Choosing a scalar summary was consequential. A short-lag area was proposed as an easier substitute for a long-timescale mixture fit. Executed synthetic counterexamples showed that shortening the lag range could reverse unit ordering even without noise. Added task drive could also reverse raw ordering without changing latent persistence. A separate counterexample showed that perfect repeat agreement could coexist with wrong estimates when errors were shared.

These checks blocked the argument that an easy scalar plus high repeat correlation would establish portability. They did not demonstrate that the dataset was useless. They established that the measurement, reliability model and scientific interpretation had to be chosen together.

## The retained handoff

The next planning step was to define one common scalar, fit/eligibility procedure, comparison functional and scientifically useful tolerance, then test the complete procedure on synthetic spikes with mixtures, variable rates, drive, drift and fit failures. The plan also needed acquisition and unit-stability evidence. No local persistence target effect was estimated.

The useful output was a precise conditional question and the evidence deciding whether it could become an executable study. It did not yet satisfy the standard for a supported final recommendation. That distinction is part of the example's scientific meaning.

**Provenance:** curated from the frozen alpha.3 Codex `recommendations.md`, the persistence plan/development record and its independent review in the private development archive. Those originals remain unchanged. Public readers can inspect the source literature above, but this condensed example is not a public reproducibility bundle for the private trial's checks or counts.
