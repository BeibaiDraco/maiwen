---
name: discover
description: Autonomously develop scientifically worthwhile, dataset-answerable research questions through reviewed field knowledge, reusable question patterns, dataset investigation and independent per-question planning. A direction and local papers are optional; use for question discovery and planning rather than a full analysis.
---

# Develop worthwhile questions the data can answer

Use [intake](references/intake.md) to establish the accessible dataset, existing permissions, user intent and a bounded work budget. Create or resume `research/<dataset>/brief.md` and a readable `README.md` linking current work. Apply the [planning scope](../dataset-card/references/generic-probes.md#default-planning-scope). **Write every saved intermediate and final research artifact in English**, including intake, source notes, candidates, checks, reviews, handoffs and delivery. Conversation may follow the user's language. Inherit the host's model and effort unless the user chooses otherwise.

## Coordinate the work

Read [coordination](references/coordination.md) before delegating. **Use separate native subagents for the knowledge authors and their independent reviewers, the questioner, screening, and each shortlisted question's planning and review.** The main host coordinates, collects results and writes the synthesis. Queue tasks within available concurrency; authors and reviewers work in different contexts. Pass role instructions and actual input paths rather than assuming a child inherits this skill. Collect completion and inspect artifacts before advancing. If independent contexts are unavailable, prepare useful notes and label missing reviews; do not claim the complete reviewed workflow ran. The [workflow guide](../../WORKFLOW.md) maps roles and outputs for people.

## Prepare three reviewed knowledge sources

After a small reconnaissance establishes the data identity and relevant concepts, assign these author tasks. They may run concurrently and share source notes through explicit links. Save early ideas in `early-ideas.md` with what prompted each; do not use them to narrow formal knowledge preparation. They go to screening, not to the questioner.

1. **Field knowledge:** give the [field researcher](roles/field-researcher.md) the broad data description and user intent. Explain empirical findings, theories, open problems and connections across subfields in `knowledge/field/overview.md`, with detailed notes for consequential papers.
2. **Question patterns:** invoke [learn-patterns](../learn-patterns/SKILL.md) to build or reuse a portable, source-backed question-pattern bank with independent review. PDFs, an existing bank and a direction are optional. Save `knowledge/pattern-selection.md` linking the bank, reviewed revision and applicability conditions. A citation or short transfer anecdote does not replace the bank.
3. **Dataset knowledge:** give the [dataset researcher](roles/dataset-researcher.md) the authorized data and source locations. Produce `knowledge/dataset/card.md`, `source-report.md` and `prior-use.md`: observed data facts, collection papers/documentation, and what studies using these observations actually asked and established.

Commission a separate [knowledge review](references/knowledge-review.md) for each stream; the pattern skill supplies its own reviewer instructions. Repair material misunderstanding within the finite allowance. Preserve local unknowns and proceed where the reviewed material supports informed generation. If a whole stream lacks usable knowledge, deliver preparation and its gap instead of silently dropping it. Readiness does not require exhaustive literature coverage or complete per-question feasibility.

## Hand off, generate and screen

Prepare `questioner-input.md` using [coordination](references/coordination.md#handoff-to-the-questioner), confirming that each stream's completed review covers its current version. Collect any pending material recheck before launching generation. Link the three knowledge bodies, pattern bank, decisive paper notes, user intent and unresolved facts. Spawn a fresh [questioner](roles/questioner.md), without early candidate answers or preferred verdicts. Have it read all three bodies and consequential sources, then generate substantively different candidates in `candidates.md`. Describe what knowledge or reasoning move opened each question; untested support remains provisional. No successful-question quota applies.

Give a separate screening agent the candidates, `early-ideas.md` and full inputs using [screening](references/screening.md). Let it seek additional evidence. Collect `screening.md` with contribution, closest comparisons, duplication, obvious data barriers and reasons to develop, combine, reject or defer. Separate lack of capacity from scientific rejection. Size the shortlist to the remaining planning, review and delivery budget.

## Develop each shortlisted question

Spawn one fresh [question planner](roles/question-planner.md) per shortlisted question, queued as needed. Provide the candidate, screening reasoning, knowledge and permitted data access. Have the planner first perform the affordable check most likely to change further investment, then develop the surviving comparison. Collect that decision in `questions/<id>/development.md`, with `plan.md` and necessary local checks. Allocate further work or a queued alternative from the result and remaining review capacity; do not require every shortlisted idea to become an elaborate plan. Planners may narrow or reframe, renew literature and data checks, or return supported rejection; a calculation that runs is not proof of answerability.

Commission an independent [plan review](roles/plan-reviewer.md) for each developed question. Verify objections and proposed remedies against sources, measurements and appropriate logical or synthetic checks. Use [bounded critique](references/critique.md) to repair and independently recheck consequential changes. The same allowance follows linked arguments through reframing and final review. Preserve supported, conditional, review-pending, deferred and rejected outcomes as evidence warrants.

If no worthwhile direction can advance after screening or planning, use the [single bounded return to generation](references/coordination.md#one-evidence-guided-return-to-generation), or stop with the evidence and search limits explicit.

## Write and check the complete delivery

Use [delivery](references/delivery.md) to write a self-contained `recommendations.md`, linking knowledge, candidate history and final plans. Explain the concrete question, scientific stakes, proposed computation and plausible interpretations in direct English prose. Write `NEXT.md` with actual unresolved decisions and next authorized work; save an English user-facing summary for checking.

Have a fresh final reviewer read the **actual finished** report, plans, NEXT and summary using [final-document checks](references/critique.md#check-the-finished-document). Compare the scientific claim in the opening, actual computation, interpretation, summary and NEXT. Resolve contradictions in meaning as well as value, source overlap and implementability; a conditional heading cannot qualify a stronger claim elsewhere. Collect results and verify substantive repairs within the remaining allowance. Deliver useful partials honestly when preparation, planning or review is incomplete. Update the workspace index; a conversational translation may explain the checked disposition without adding scientific claims.
