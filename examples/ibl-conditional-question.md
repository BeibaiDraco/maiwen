# IBL: are neurons that are slow during spontaneous activity also slow during a task?

A map of neural timescales tells us which neurons have activity that fluctuates quickly and which have activity that persists over longer intervals. If that map was measured while an animal was outside a task, how much does it tell us about the same neurons during behavior?

**The question:** in the same recorded units, does the ordering of long-lag persistence carry between the final task period and the subsequent spontaneous period? If the values change, can one common rescaling describe the change, or do units change differently?

This is a conditional research proposal from Maiwen's alpha.3 IBL trial. The account below explains its scientific purpose, proposed analysis and possible outcomes. The trial checked data availability and mathematical counterexamples; it did not estimate persistence in the local neural recordings.

## Why this question matters

Here, **persistence** means how long fluctuations in a neuron's spike count remain correlated with its own earlier activity. A neuron can fire frequently yet have rapidly decorrelating activity. “Slow” refers to the decay of those correlations, not to a low firing rate or a slow behavioral response.

Persistence is relevant to theories of how neural systems retain and combine information over time. It also offers a measurable way to compare neural dynamics across cells and brain regions. The scientific opportunity is to establish which uses of a spontaneous-activity map remain justified during a task.

Consider a researcher who uses such a map to label recorded neurons as relatively fast or slow. Three distinct assumptions could enter the subsequent study: the numerical timescales are unchanged during behavior; their ordering is preserved even if all values shift; or only a broad regional tendency carries over. Those assumptions lead to different predictions and different ways of grouping neurons. A direct comparison can establish which description the recordings support.

An association between spontaneous persistence and task selectivity is already informative in its own right. The additional question here is whether spontaneous persistence also describes the temporal structure of activity **during the task itself**. Answering it would clarify how to interpret and reuse an existing atlas. The proposed observation is a property of the recorded activity; assigning it to recurrent circuitry, memory or a causal effect of engagement would require further evidence.

## What earlier work already establishes

| Study | Relevant comparison | How it shapes this proposal |
| --- | --- | --- |
| [Shi and colleagues, *Brain-wide organization of intrinsic timescales at single-neuron resolution*](https://pmc.ncbi.nlm.nih.gov/articles/PMC12407892/) | Estimates single-neuron timescales from spontaneous IBL activity using mixtures of exponential decays, maps their anatomical organization, and relates them to task selectivity. | Supplies the atlas and measurement to examine. Relating a spontaneous timescale to task selectivity is different from measuring the same persistence quantity in both contexts. |
| [Fontanier and colleagues, *Inhibitory control of frontal metastability sets the temporal signature of cognition*](https://elifesciences.org/articles/63795) | Compares engagement and pause timescales in the same frontal neurons, using a spike-time-difference statistic. | Same-neuron engagement/pause comparisons already exist. The contribution must concern the particular IBL atlas, a common measurement and the reliability of its transfer. |
| [Gülenç and colleagues, *A Brain-Wide Atlas of Intrinsic Neural Timescales in Mice*](https://impact-scholars.github.io/suheylgulenc-2026-brainwide-intrinsic-timescales/) | Uses an alternative autocorrelation estimator and multiexponential fits to examine spontaneous IBL timescales. | Adds a close measurement precedent. The trial's review found no matched task/spontaneous transfer comparison in the inspected article and supplement; its code and exact data overlap remained unchecked. |

The possible increment is therefore specific: determine whether a common, seconds-scale persistence measurement retains its ordering and magnitude in the same IBL units across the two recording periods, with enough precision to distinguish change from measurement error. Checking the closest implementations remains part of developing that contribution.

## Why IBL offers a useful comparison

The International Brain Laboratory records neural activity while mice perform a visual decision task: they turn a wheel to bring a stimulus toward the center of a screen. Some sessions also contain a later, explicitly marked spontaneous period without task stimuli. This combination offers paired observations within a recording session, rather than a comparison between unrelated sets of neurons. [The atlas paper describes the recording design](https://pmc.ncbi.nlm.nih.gov/articles/PMC12407892/).

The trial inspected a selected local planning view, not the complete IBL collection:

| Observed availability | What it contributes to the design |
| --- | --- |
| 36 sessions from 36 mice were inspected. | Defines the starting subset. |
| 27 sessions had explicit spontaneous-period labels. | Provides timing information for selecting the comparison period. |
| 24 sessions had at least 600 seconds of marked spontaneous time and sufficient elapsed task time. | Supports a proposed design with two 300-second records per context. |
| Those 24 sessions contained 36 probe insertions and 3,977 sorted-unit metadata identities. | Provides potential paired units; recording continuity, sorting stability and measurement precision determine which are usable. |

The proposed windows are the **last 600 seconds of the task** and the **first 600 seconds of the marked spontaneous period**, each divided into two contiguous 300-second records. Matching the same probe and cluster identifiers allows a within-unit comparison once identity stability is supported. The repeated records help investigate measurement variability. Keeping record duration and processing consistent makes the comparison easier to interpret.

These features make the study plausible. They do not establish that 3,977 units can yield precise timescales. The 600-second requirement supplies two records of the proposed length; it is not a validated precision threshold. The three shorter spontaneous periods need a different, separately assessed design.

## What would actually be calculated?

The proposed analysis follows the activity of each unit through four records: task 1, task 2, spontaneous 1 and spontaneous 2.

1. **Establish valid observation windows.** Check acquisition coverage and sorting stability across both periods. Preserve missing recording time as missing. Determine the eligible paired unit set and report why other units cannot be measured.
2. **Measure the same temporal quantity in every record.** The plan proposes spike counts in 5-ms bins and normalized temporal covariance at delays from 5 ms through 5 seconds. At each delay, it asks whether above-average counts tend to be followed by above-average counts. Use identical centering, normalization and lag support in both contexts, with no joins between separate records.
3. **Choose and validate a summary of persistence.** One route comparable to the atlas is to fit a sum of exponential decays and summarize their time constants by their amplitude-weighted mean. A small slow component can matter substantially to this mean. The exact fitting, component selection, failed-fit treatment and uncertainty calculation were still unresolved in the trial. The final procedure must also reconcile its normalization with the source implementation.
4. **Compare repetition within context with agreement across contexts.** Estimate how much a unit's measurement varies between task records and between spontaneous records. Then compare its values across contexts: ordering, absolute differences and departures from a common multiplicative shift. Two adjacent records can share drift or estimation bias, so agreement between them requires a calibrated error model before it can establish accurate measurement.
5. **Separate unit-level agreement from anatomical averages.** Report the comparison within sessions and, where supported, within regions, alongside any pooled summary. A correlation across all units could be driven by regional means even when individual units do not retain their positions. Uncertainty must reflect shared mouse/session conditions and fitting failures; thousands of units are not thousands of independent animals.

The resulting scientific display would show each unit's paired persistence estimates, their repeat variability, the extent of a common shift and any remaining unit-specific changes. The accepted tolerance for change should come from the intended atlas use—for example, how much disagreement would change a proposed fast/slow grouping—not from whichever threshold makes the observed data look stable. Neither that tolerance nor a complete inference procedure was settled in this trial.

## What could the results mean?

These are possible outcomes, not findings from IBL. Each substantive interpretation assumes a validated measurement and enough precision to resolve a difference relevant to the stated use.

| Possible outcome | Scientific interpretation and consequence |
| --- | --- |
| Ordering and absolute values agree within the justified tolerance. | Supports using both relative labels and numerical values across these recording periods for the specified use. It would provide evidence that this description of persistence carries across contexts. |
| Ordering is retained and values change by approximately one common factor. | Supports relative fast/slow labels while showing that numerical values need context-specific calibration. For example, doubling every unit's timescale preserves its rank but changes the temporal scale of the activity. |
| Ordering is retained, but individual changes do not follow one common factor. | The atlas could remain useful as an ordinal description, while a single conversion between contexts would be inadequate. |
| Units reliably change order beyond the uncertainty and instability accounted for by the procedure. | Limits the use of spontaneous fast/slow labels to describe task-period persistence. Follow-up work could ask which recorded events or states accompany that change. |
| Repeated measurements are too variable, or the available between-unit variation is too small to assess ordering. | Leaves transfer unresolved at this recording duration and measurement resolution. It motivates longer records or a different, scientifically justified measurement rather than a claim of stability or reorganization. |

For a purely illustrative example, spontaneous values of 0.2, 0.5 and 1.0 seconds becoming task values of 0.4, 1.0 and 2.0 seconds preserve ordering through a common rescaling. Task values of 0.8, 0.3 and 1.0 seconds would reorder the first two units. The study would have to establish that such an apparent reversal exceeds the uncertainty of measuring those particular units.

Task recording always preceded spontaneous recording in the proposed design. A difference would therefore describe these two periods together with their changes in input, movement, arousal, elapsed time and recording conditions. Separating a causal effect of engagement would require a design that separates those influences.

## What the checks changed

The most consequential check concerned an attractive shortcut: replacing a long-timescale fit with the area under the first half-second of the covariance curve.

In an executed mathematical example, unit A had a large 50-ms component and a small 2-second component; unit B had one 200-ms component. Their effective timescales were **245 ms for A and 200 ms for B**. Yet integrating only to 0.5 seconds gave areas of approximately **89 ms for A and 184 ms for B**, reversing their order. The slow tail carried information that the shortcut discarded. This occurred with known, noiseless curves.

A second example added slowly varying drive to one unit without changing its underlying latent component. Its raw persistence then increased enough to reverse the ordering. That result clarifies the proposed measurement: raw persistence describes the combined activity in each context, including its inputs. A third check showed that shared estimation error can produce perfect repeat agreement while estimates remain wrong.

Together, these checks changed the next step from “calculate a convenient summary and correlate the two contexts” to **“validate a common measurement and the interpretation of its comparison.”** The examples establish specific failure modes; recovery from simulated spike trains through the complete fitting and comparison procedure remained to be tested.

## Where the proposal stands

The trial produced a worthwhile, specific comparison and verified timing and identity counts that make further development reasonable. Two pieces of work determine whether it can become an analysis-ready study: establish continuous, stable recordings for the proposed paired units; and validate the complete persistence estimator, selection rules and comparison at a scientifically useful precision. The closest available implementations also need to be checked for overlap.

If those conditions can be met, the study can answer a practical scientific question: **which information about neural dynamics survives when a spontaneous-activity atlas is used to describe behavior—numerical values, relative ordering, or neither?** Its contribution would be to establish the scope of that use with a matched comparison.

**Source record:** expanded from the alpha.3 Codex persistence plan, structural outputs, development notes and independent review. The numerical availability counts and synthetic examples above were checked against those saved records. Public papers are linked beside the relevant claims; the original scripts and inspection outputs remain in the private development archive. This explanation adds no new neural analysis or discovery run.
