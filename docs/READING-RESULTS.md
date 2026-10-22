# Reading Maiwen's results

Start with `research/<dataset>/recommendations.md`. For each developed question, the report explains what is unknown, why it matters, what earlier work established and how the proposed calculation would answer it. You should be able to discuss the study with a colleague who has not followed the conversation.

## What is ready, and what needs more work?

| Outcome | Meaning | Useful next step |
| --- | --- | --- |
| Supported recommendation | The question's contribution and answerability have supporting evidence, and the current plan has completed independent review | Assess the plan and decide whether to authorize analysis |
| Conditional direction | A promising question depends on a named unresolved fact or method choice | Resolve that condition before beginning the study |
| Review pending | The current version still needs independent review | Complete the indicated review |
| Deferred for capacity | Time or review capacity ended before the idea could be developed | Decide whether it merits further work |
| Rejected | Evidence gives a reason to stop pursuing the question in its present form | Read the reason and any different opportunity it leaves open |

A report may contain no supported recommendation. In that case, it should explain what was learned, why the investigated questions could not advance and which opportunities remain untested. It should also distinguish a demonstrated data constraint from a search that ended because time or evidence ran out.

## Inspect how the question developed

The project `README.md` links the research documents; `brief.md` records the inputs, scope and budget. Under `knowledge/`, you can read the field overview, detailed paper notes, data card, collection history, previous analyses and selected question patterns. `questioner-input.md` identifies the material given to the questioner. A reusable pattern library may live separately under `paperbanks/`.

`candidates.md` and `screening.md` explain the proposed ideas and the decisions to pursue, combine, reject or defer them. Each `questions/<id>/` directory contains the question's development, plan, checks and independent review. `final-review.md` covers the finished report; `NEXT.md` records the stopping point and remaining work. The [workflow guide](../WORKFLOW.md#find-every-artifact) lists all outputs.

Follow the evidence beside the claim that interests you. A coverage check tells you which observations are available. A precision calculation asks whether they can resolve a difference of scientific interest. A synthetic counterexample shows why an inference can fail under particular conditions. Together, these records should explain why the final question has its particular form.

## Continue with a colleague or a new session

Share the main report and its linked plans and evidence, within your data and paper-sharing permissions. A scientific colleague can then assess the contribution, measurements and assumptions. To resume with an agent, ask it to read the index, brief and `NEXT.md` and continue the unresolved work within the remaining budget. Authorize the proposed analysis separately when you are ready to run it.
