# Maiwen

Turn a dataset into scientifically worthwhile questions and concrete research plans, inside Codex or Claude Code.

Start with the data. Add a research direction or local papers if you have them. Maiwen explores relevant experiments and theory, learns useful ways of asking questions from papers, and develops the opportunities your data can support.

## Start a research session

Install the package using the [quickstart](QUICKSTART.md), then open your research folder in your coding-agent host and ask:

> Use Maiwen to find scientifically worthwhile questions this dataset can answer: `/absolute/data/path`.

You can add a direction, a paper folder, known related work, or a time budget. Maiwen checks what is available and asks for consequential missing information. A direction and papers are optional. Research reports follow your preferred language.

Maiwen uses your host's tools, model settings, permissions and account. It does not require a separate model service. Python 3.11+ runs the optional data profiler; additional readers are needed only for the formats you use.

## How the work develops

1. **Understand the data and existing science.** Inspect measurements and coverage, map the dataset's previous uses, and explore open questions and competing explanations across connected fields.
2. **Learn and propose.** Follow useful reasoning from experimental and theoretical papers, form distinct candidate questions, and connect them to concrete comparisons in the data.
3. **Develop and review.** Check the scientific contribution, measurements and inferential assumptions. Independent host-native review challenges consequential claims and checks repairs within a bounded budget.
4. **Deliver an actionable plan.** Explain each supported question, why it matters, the proposed computation and what different answers would mean.

The number of recommendations follows the evidence. There is no fixed question quota. Promising ideas that need more support remain visible alongside the strongest plans.

## Your research workspace

The main deliverable is `research/<dataset>/recommendations.md`. Linked notes explain the data, field context, paper learning, candidate development and review. `NEXT.md` records practical continuation steps. You can steer the work in ordinary conversation or continue from those notes in a later session.

Maiwen's default task is research planning. It inspects authorized data for measurement, distribution and coverage checks and uses appropriate synthetic checks. Running the proposed target analysis is a separate task. Identify reserved data and use only material permitted on your host.

## Included skills

- **discover** coordinates scientific question development and delivery.
- **dataset-card** builds broad data understanding and investigates candidate-specific support.
- **prior-use** maps existing uses and close precedents, including equivalent questions under different terminology.

The pack includes a small structural profiler and a fictional worked writing example. The [quickstart](QUICKSTART.md) covers installation, input preparation, model settings and continuation.

## Availability

This repository currently holds a private preview. The method is being evaluated on real datasets; its effect on question quality remains under development. Public availability and licensing will be announced with the first public release.
