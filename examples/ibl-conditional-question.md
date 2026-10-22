# IBL: does temporal persistence carry from spontaneous activity into behavior?

**A conditional question from the alpha.3 trial.** This account follows a Codex discovery using a 36-session planning view of IBL data. The question remained conditional because its proposed measurement and interpretation needed further work. It is included here as a historical example; beta.1 has not rerun it.

## Why ask it?

Temporal persistence describes how a neuron's activity covaries over time. An atlas measured during spontaneous activity is attractive as a compact description of neural dynamics. To use it when interpreting behavior, one needs to know what carries between recording contexts: the relative ordering of units, their absolute values, or neither.

The question was: **do the same sorted unit identities retain their relative long-lag persistence from the final task period to the subsequent spontaneous period, and is any change consistent with common rescaling or does it differ among units?** Reliable reordering would limit use of a spontaneous atlas for those units during behavior. Stable ordering could support relative portability in this recorded setting; it would not mean individual values are unchanged.

## Existing work narrows the contribution

[Shi and colleagues' BWM study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12407892/) estimates spontaneous persistence, including mixtures of decay components, and relates it to task selectivity. [Fontanier and colleagues](https://elifesciences.org/articles/63795) already examine engagement and pause timescales in the same neurons using a different spike-pair statistic. Thus, a generic claim that timescales differ between rest and task would be insufficient.

The possible contribution is a comparison of matched measurements across recording contexts in IBL. The original run also examined adjacent timescale literature and a recent IBL micropublication. It left overlap with existing code unresolved, so continuation would begin by checking the closest studies and their current implementations.

## What was actually available?

In the authorized view, 27 sessions had explicit spontaneous-interval labels. Twenty-four had at least 600 seconds of marked spontaneous time, spanning 36 insertions and 3,977 potential sorted-unit identities. These counts identify potentially usable recordings. Continuous acquisition, stable cell identity and the precision of timescale estimates still needed investigation.

The proposed comparison used the final 600 seconds of task and the first 600 seconds of the marked spontaneous block, split into two 300-second records per context. Task always preceded spontaneous recording. Time, satiety and recording drift therefore remained alternative explanations for a context difference. The comparison could describe how measurements carry between these recording periods. Attributing a difference to engagement would require separating engagement from those other changes.

## The calculation and the decisive difficulty

The plan specified count covariance at matched binning and lag support, normalized by the record's count variance. For each unit it would estimate a persistence curve in the four records, evaluate repetition within context, then compare cross-context relative and absolute agreement while respecting mouse/session dependence.

Choosing a scalar summary was consequential. A short-lag area was proposed as an easier substitute for a long-timescale mixture fit. Executed synthetic counterexamples showed that shortening the lag range could reverse unit ordering even without noise. Added task drive could also reverse raw ordering without changing latent persistence. A separate counterexample showed that perfect repeat agreement could coexist with wrong estimates when errors were shared.

The checks showed why an easy scalar and high repeat correlation were insufficient for the proposed portability claim. Further development would have to choose the measurement, reliability model and interpretation together.

## The retained handoff

The next planning step was to define one common scalar, fit/eligibility procedure, comparison functional and scientifically useful tolerance, then test the complete procedure on synthetic spikes with mixtures, variable rates, drive, drift and fit failures. The plan also needed acquisition and unit-stability evidence. No local persistence target effect was estimated.

The investigation produced a precise conditional question and identified the measurements and method decisions needed to turn it into a study. Those unresolved decisions are its stopping point.

**Source record:** adapted from the alpha.3 Codex report, persistence plan, development notes and independent review. The original records and local checks are preserved in the private development archive. The linked papers are public; the trial's scripts and inspection outputs are not included in this example.
