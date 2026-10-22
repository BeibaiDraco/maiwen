# Start with Maiwen

Use Codex or Claude Code with local file/code tools and native subagents. Sign in through your host. Maiwen uses its existing model, account, permissions and tools; no separate model API key is required. Literature work also needs a way to search and read sources.

## Install the complete plugin

This review candidate is installed from a local checkout or an extracted ZIP. Keep the directory in a stable location, such as a `plugins/maiwen` folder. Replace the example path with that directory; it must contain `plugin.json` and `skills/`.

**Codex CLI**

```bash
codex plugin marketplace add /absolute/path/to/maiwen
codex plugin add maiwen@maiwen
```

**Claude Code CLI**

```bash
claude plugin marketplace add /absolute/path/to/maiwen
claude plugin install maiwen@maiwen
```

In an interactive Claude Code session, the equivalent commands are `/plugin marketplace add /absolute/path/to/maiwen` and `/plugin install maiwen@maiwen`.

Start a fresh session in your research workspace. Ask the host to list Maiwen's skills and confirm version `0.2.0-beta.1`: `discover`, `learn-patterns`, `dataset-card` and `prior-use`. The [validation record](docs/LIMITATIONS.md) describes the tested CLI configurations and the App checks still to do. Public GitHub installation and official directory listing are pending.

### Existing private-preview users

The marketplace name is now `maiwen`; earlier previews used `maiwen-local`. Remove the old plugin before installing the new identity to avoid loading two versions:

```bash
# Codex
codex plugin remove maiwen@maiwen-local
# Claude Code
claude plugin uninstall maiwen@maiwen-local
```

Your research workspace is separate from the plugin. Keep it; open a fresh host session after changing the installed method. Do not edit an installed cache to update the plugin.

## Begin discovery

In Codex, ask the host to use Maiwen `discover`. In Claude Code, invoke `/maiwen:discover` or ask for it in ordinary conversation:

> Find scientifically worthwhile questions this dataset can answer: `/absolute/data/path`. I have no seed question. First check the inputs, tell me what is missing or optional, and agree on a finite budget. Save the research in English.

The host starts with what it knows, what is needed now, and what would help. It can discover files and documentation itself. It may ask you about collection details, permitted data use or the time available. PDFs, a direction and a prebuilt pattern bank are optional. Unresolved facts are recorded with the questions they affect.

A full discovery may take hours, even with parallel tasks. For a shorter first look, ask for a data card or a pattern library covering a defined set of papers. You can stop or narrow the work at any point.

## Choose the model in the host

Choose the model and reasoning effort in Codex or Claude Code. Maiwen keeps those settings and uses the same account unless you explicitly request a change. For complex scientific reasoning, use a capable reasoning model available on your plan; higher reasoning effort may trade latency and usage for deeper work. There is no Maiwen-specific model name or universal best setting. Keep the host/model settings with the run's notes when comparing outputs.

The full workflow needs native subagents so that authors and reviewers work separately. If subagents or essential sources are unavailable, the host saves the useful preparation and explains which reviews remain.

## Build a reusable pattern bank

Use `learn-patterns` (Claude Code: `/maiwen:learn-patterns`):

> Learn useful ways of forming research questions and hypotheses from the papers in `/absolute/papers/path`. Have an independent agent review the sources and transfer conditions. Save a portable English bank in `paperbanks/my-field`.

You can instead name a field and ask the host to find instructive papers. During discovery, Maiwen coordinates this work automatically. Bring the library to later projects, checking whether its reasoning and data requirements apply to each new setting.

## Read and continue

Open `research/<dataset>/README.md`, then `recommendations.md`. The index links all preparation, candidate development, checks and reviews; `NEXT.md` gives the actual stopping point. See [Reading results](docs/READING-RESULTS.md).

To continue in a fresh session:

> Read `research/<dataset>/README.md`, `brief.md` and `NEXT.md`. Summarize the unresolved decisions and continue the authorized work within the remaining budget.

## Update or remove

For a local marketplace, put the new reviewed package at the registered source location. In Codex, remove and reinstall `maiwen@maiwen` to refresh its cached payload. In Claude Code, use `claude plugin update maiwen@maiwen`. Start a fresh session and verify the version; if a host retains an old local snapshot, remove/reinstall the plugin from the new directory. Removing the marketplace registration is a separate host action.

Uninstall with `codex plugin remove maiwen@maiwen` or `claude plugin uninstall maiwen@maiwen`. These are plugin-management actions; do not delete your research directory.

## Optional data readers

The bundled structural profiler needs Python 3.11 or later. CSV/TSV and JSON use the standard library. Parquet needs `pyarrow`; HDF5/NWB needs `h5py`. Local Zarr metadata inspection uses the standard library; reading Zarr array values may require additional tools. Install only the reader your data require in your chosen Python environment. The host can also write a suitable inspection script. There is no `pip install maiwen` step.

See [Support](SUPPORT.md) for troubleshooting and [Data and privacy](PRIVACY.md) before using private research material.
