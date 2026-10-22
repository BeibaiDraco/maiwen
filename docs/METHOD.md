# Method and lineage

A useful research question connects a scientific uncertainty to observations that can resolve it. A dataset alone rarely tells us which uncertainty matters most. Conversely, an important open problem may require measurements or experimental variation that the dataset does not contain. Maiwen develops the question and the proposed comparison together.

## Learn what is open, how to ask, and what was measured

**Field knowledge establishes the scientific opportunity.** A researcher reads experiments, reviews and theoretical work to explain what is known, what is disputed and what remains open. The search includes neighboring fields when they share a problem or offer a useful comparison. For a theoretical idea, the account explains its assumptions, the prediction that follows and the observations that could test it.

**Question patterns explain how earlier studies made progress.** For each instructive paper, the library reconstructs the uncertainty that motivated the study, the comparison that addressed it and the data conditions that made the comparison informative. It then explains how that reasoning could be used elsewhere and where it would fail. For example, a study may separate change within individuals from differences between groups, turning an apparent trend into a more revealing question.

Forming a question and forming a hypothesis are related activities. A question identifies an unknown; a hypothesis proposes an answer or explanation and may imply testable predictions. The library teaches both where the papers support them. Descriptive and predictive questions can be valuable in their own right.

**Dataset knowledge establishes the available observations.** The researcher combines direct inspection with collection papers, documentation and previous analyses. This work explains what variables mean, how measurements align, which observations are independent and what selection or missingness affects a comparison. Detailed accounts of prior uses show what the same data have already taught us, including work that describes a similar question in different terms.

Independent reviewers check each account before a new questioner reads them together. The questioner receives substantive explanations and relevant paper notes, with links to their sources. The [workflow](../WORKFLOW.md) shows how this preparation becomes a set of proposals and then individual research plans.

## Generate broadly, investigate selectively

Generation explores different scientific opportunities before committing to a model or statistic. Screening examines the contribution and the closest prior work. Each promising question then gets a planner who starts with the affordable check most likely to change the decision to pursue it: reading a crucial method, verifying a measurement, inspecting joint coverage or testing a logical implication.

The planner uses that evidence to refine the question and define its computation. If the question changes substantially, the planner revisits what it would add and whether the data can answer it. An independent reviewer follows the argument from measurements through the calculation to its interpretation, checking both the scientific contribution and the proposed method.

Review includes at most two substantive rounds of repair and recheck for each knowledge source or linked question argument. If no question can advance, one further generation batch may explore an untried opportunity within the original budget. The final report explains supported questions, useful conditional directions and reasons for stopping.

## Work within the coding agent

Maiwen's skills and Markdown references describe the scientific tasks. Codex or Claude Code performs them using its model, code tools, separate agent sessions and conversation with the user. Research notes and decisions remain readable files in the user's workspace. The host and environment control data access and permissions.

This design lets improvements in the host's reasoning, tools and agent coordination benefit the research workflow directly. The quality of a question still depends on the scientific argument and its evidence; [current validation](LIMITATIONS.md) describes what the development trials have established.

## Predecessor

[Maieusis](https://github.com/BeibaiDraco/maieusis) established the focus on learning question formation from successful papers, building reusable patterns and developing plans against real data. Maiwen retains those aims while placing agent coordination in the host and making the knowledge, decisions and plans directly readable.

The [Maieusis software record on Zenodo](https://doi.org/10.5281/zenodo.21388805) documents the predecessor. Maiwen has its own [citation metadata](../CITATION.cff) and [validation record](LIMITATIONS.md).
