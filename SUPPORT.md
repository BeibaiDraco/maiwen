# Support

Report installation problems, unclear instructions and scientific workflow errors through [GitHub issues](https://github.com/BeibaiDraco/maiwen/issues). Responses depend on maintainer availability.

A useful report gives the Maiwen version, host and version, operating system, request or command, expected behavior and a small example that reproduces the problem. For a scientific error, identify the claim, its source or calculation and the decision it affected. A counterexample or corrected interpretation is especially helpful.

Use synthetic data and a redacted excerpt where possible. Keep API keys, account tokens, private datasets, unpublished PDFs and unreviewed transcripts out of public issues. For sensitive reports, first ask the maintainer for a private channel.

## Common starting problems

- **The host cannot find Maiwen's skills.** Check the package root, marketplace registration and installed version, then start a fresh session. Earlier previews used `maiwen-local`; remove a duplicate installation if both identities are present.
- **The report stopped partway through.** Read `README.md` and `NEXT.md` for the missing source, data access, review or remaining budget. They should identify what can continue.
- **The data cannot be read.** Check the path, mounted drive and optional reader for the file format. Resolve access restrictions through the host.
- **Subagents are unavailable.** Continue in a host session that supports them, or save the preparation for independent review elsewhere. Label the review that remains to be done.

The [quickstart](QUICKSTART.md) covers installation, updates and removal. Contributions should explain the problem they address and include checks suited to the change.
