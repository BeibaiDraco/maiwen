# Validation and limitations

Maiwen is a research preview. Development has tested parts of the workflow and examined the questions it produced, principally in neuroscience. The evidence below separates real discovery trials, focused method checks and installation exercises so that readers can judge what each establishes.

## Scientific development trials

A full IBL trial with `0.2.0-alpha.3` used a 36-session planning view on each of Codex and Claude Code. It produced useful conditional directions and exposed scientific errors and process problems. Permission denials limited the Claude run. These observations helped identify changes to make; they do not support a controlled comparison between hosts or a claim of superiority over a general coding agent.

Alpha.4 revised how planners choose early checks, review the complete inference and verify proposed repairs. Alpha.5 added one optional return to question generation. Focused fictional failure cases and valid controls exercised these changes. Neither version received a new full discovery trial. Beta.1 packages that method with user documentation and a corrected fictional measurement example. Beta.2 expands the IBL scientific explanation, including the proposed calculation and possible outcomes, without changing the workflow or adding a discovery trial. The [IBL example](../examples/ibl-conditional-question.md) is drawn from the earlier alpha.3 trial.

Evidence in other scientific fields remains limited. A new project requires current literature research, inspection of its measurements and a fresh assessment of whether a reused pattern applies. Literature searches have practical limits, and unavailable sources or unresolved collection details may leave a question conditional. Separate reviewers can catch errors, but agents using the same model may share assumptions and blind spots.

## Installation and first use

Candidate checks used Codex CLI 0.163.0 and Claude Code 2.1.303. Both installed the four-skill package. Each also completed one small input and data-card exercise with a native independent reviewer and English saved documents. Codex took 8.49 minutes and Claude took 3.98 minutes. Codex used the installed cache; Claude used the same exported package through its session-local plugin option after installation had been checked.

These exercises ended before field research, pattern learning and question generation. They establish first-use observations for those CLI configurations. A complete desktop App workflow, other operating systems, future host versions and resumption in a separate model session remain untested. Resume instructions received static inspection.

The Claude exercise also exposed two problems: the card was repaired without an independent recheck, and its summary implied that prior planning exposure always required new data. The latter led to a clarification that independent evaluation should address the choices and claims affected by exposure. This clarification and the corrected measurement example received independent document review. There was no further live host run.

Installation, refresh, removal and package checks passed. These checks establish that the package can be loaded and its resources found; scientific quality must be assessed from the research itself.

## Scope of use

The complete workflow uses local Codex or Claude Code with native subagents and tools for reading data and literature. The host determines model access, account usage, permissions and available tools. When independent contexts are unavailable, Maiwen can prepare knowledge and identify the review still needed.

Planning may inspect authorized data structure, counts, coverage, marginal distributions and suitable synthetic cases. The proposed study's target-effect analysis, significance searches and confirmation outcomes require a separate scope. If an inspected summary later becomes a question's target, the notes must record that exposure and its implications for evaluation. The host and environment enforce access restrictions.
