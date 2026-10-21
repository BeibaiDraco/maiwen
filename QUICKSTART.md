# Start a Maiwen research session

Maiwen develops scientific questions and analysis plans inside your existing Codex or Claude Code session. Give it an accessible dataset; a direction and local PDFs are optional. The current package is a private release candidate. Its methods still need evaluation on additional real datasets; no tool can guarantee a discovery or publishable result.

## Prerequisites

Use a current host with local file and command access plus literature search. Sign in through your intended host subscription. Maiwen does not choose a model, supply an API key or start another inference service; host account settings and usage limits still apply. Python 3.11+ runs the optional structural profiler. Parquet needs `pyarrow`, HDF5/NWB needs `h5py`; install readers only when your data require them.

Unpack the supplied plugin directory somewhere stable. Open a separate research folder in your host, so your data, notes and research instructions stay separate from plugin development history. Make the authorized data path accessible to that host; a path on another machine is not automatically mounted. Permissions and any confirmation-data isolation are enforced by the host/environment, not these skills.

## Codex

Register the unpacked directory as a local marketplace:

```bash
codex plugin marketplace add /absolute/path/to/maiwen-plugin
```

Install `maiwen` from `maiwen-local` in the App's Plugins directory, then start a new chat in your research folder. On Codex CLI versions exposing `plugin add`, the equivalent installation is:

```bash
codex plugin add maiwen@maiwen-local
```

Select the installed Maiwen `discover` skill or explicitly ask the host to use Maiwen for the request below. Confirm that it finds the installed skill and resolves its accompanying references. Updating the source folder alone may leave an old cached copy: refresh/reinstall through the host and start a new chat, checking the reported version.

The [official packaging guide](https://developers.openai.com/plugins/build/plugins) describes local marketplaces and App installation. Menu names can vary by host version. If the plugin is unavailable, explicitly reading the supplied `skills/discover/SKILL.md` is a temporary method trial, not proof installation worked.

## Claude Code

For a session-local test from your research folder:

```bash
claude --plugin-dir /absolute/path/to/maiwen-plugin
```

Invoke `/maiwen:discover` with your dataset. For persistent installation, register the directory and install it:

```bash
claude plugin marketplace add /absolute/path/to/maiwen-plugin
claude plugin install maiwen@maiwen-local
```

Start a new session and verify `/maiwen:discover`, `/maiwen:dataset-card` and `/maiwen:prior-use` are available. For Claude's desktop Code surface, use its plugin installation UI and check the commands in a new project chat; CLI success alone does not certify that UI. See [Claude's plugin documentation](https://code.claude.com/docs/en/plugins) and [marketplace installation](https://code.claude.com/docs/en/plugin-marketplaces).

## First request

> Use Maiwen to find scientifically worthwhile questions this dataset can answer: `/absolute/data/path`.

The dataset or an accessible location is the essential input. You can have no research direction and no local papers. If the location is not yet usable, Maiwen can work with supplied documentation or literature while you resolve access, but it cannot yet claim the data can answer a question.

Expect a short opening showing what Maiwen already knows, what it still needs to begin, and what you can optionally add:

- A direction or seed question focuses the search; “I have no direction” is fine.
- A local PDF folder supplies starting examples; Maiwen can also find literature itself.
- Known publications or ongoing work help it avoid duplication.
- Priorities and a time or usage budget help it allocate effort.

Maiwen reads accessible documentation and data details itself, then groups the few consequential questions it cannot resolve. If you have already supplied enough, it starts. You do not need to fill out a form or write a research protocol. Missing information limits the affected questions, while other useful work continues. The [intake guide](skills/discover/references/intake.md) describes this behavior.

The default is planning: inspect authorized data and coverage, including outcome counts, distributions and missingness; develop and check questions; deliver proposed analyses. It does not run candidate target-effect tests, search for significance, execute the full study or inspect confirmation outcomes. See [planning scope](skills/dataset-card/references/generic-probes.md#default-planning-scope).

The host may send inspected fields, bounded samples and summaries to its model provider. Use data permitted on that host and identify reserved/confirmation data. Existing permissions carry forward; Maiwen asks only when an action needs unresolved authorization. Installing it does not authorize new transmission. Unanswered questions stay visibly unresolved in the workspace notes.

For demanding autonomous discovery, choose a capable model available in your host and raise reasoning effort when complexity warrants the extra time and usage. Maiwen inherits that choice. When the host supports it within your authorized budget, a different model family can add a perspective to critique; it does not guarantee independence of scientific errors. Notes record visible settings, not inferred routing.

## What to expect and how to intervene

The session inspects the data and prior science, learns useful question-forming moves from papers, proposes different directions, then checks and revises the strongest ones. The main result is `research/<dataset>/recommendations.md`, linked to data checks, paper notes, precedents and critique. Supported questions include a concrete analysis plan. Conditional ideas clearly name the missing evidence; an empty supported list is possible.

Intervene in normal chat: “focus on prediction,” “this code means no response,” “we have already studied that,” or “spend the remaining time resolving this concern.” To continue later, ask a new session to use Maiwen and read the workspace brief, recommendations and `NEXT.md`. Notes preserve evidence; they do not automatically recreate every prior conversation.

Before handing notes to others, review their contents for private information. Raw data and PDFs stay in your own workspace. Maiwen plans research; executing the resulting full study is a separate task.
