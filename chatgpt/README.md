# ChatGPT and Work workflow adapters

Version **1.0.0-chatgpt.1**, adapted from PR [#65](https://github.com/CatCorner22/Claude_Skills_2/pull/65)
at merge commit `44a01bceb2083f174a07d652a1d078abca19617c`.

| Adapter | Source version | Role |
| --- | --- | --- |
| [Puppet Master](skills/puppet-master/SKILL.md) | 1.0.0 | Efficient execution with unchanged requirements, evidence, and checks. |
| [Project Manager and QC](skills/project-manager-qc/SKILL.md) | 2.1.0 | Cross-session/agent ledger, checkpoints, and complete delivery sweep. |
| [Creative Workaround Genius](skills/creative-workaround-genius/SKILL.md) | 2.0.0 | Recover technical obstacles through permitted routes with exact identity proof. |

Maximum-Delegation Auditor continues to own every feasible authorized step.
Puppet Master selects an efficient execution shape; it does not transfer work to
the user. Selected specialist skills retain their checks and manual activation
boundaries. [Integration details](docs/integration.md) describe the reciprocal
updates to the user's existing Auditor and Cursor selector.

These adapters live outside `plugins/` deliberately. They do not alter or register
the Claude plugins, change their versions, or add to their catalog counts. The
existing Claude catalog generator still targets the unchanged Claude library.
The table above is the separate adapter index.

## Use and installation scope

“Use Puppet Master with Maximum-Delegation Auditor” invokes the read instructions
conversationally. In a host that exposes native skills, a valid package may also
be persisted and discovered through that host's supported workflow. Repository
publication, persisted package files, registry discovery, and an actual native
invocation are separate facts. No file in this repository claims automatic or
account-wide installation.

Resources resolve relative to each actual host-reported skill root, not a Claude
plugin variable, an assumed current directory, or a hidden transcript path.
See [the portability map and benchmark caveats](skills/puppet-master/references/portability.md),
[the audit format](skills/puppet-master/references/execution-audit.md),
and [validation results](docs/validation.md).

From the repository root, run portable checks with:

```bash
python3 -m unittest discover -s chatgpt/tests -p 'test_*.py'
python3 chatgpt/skills/puppet-master/scripts/execution_audit.py --self-test
```

The audit reports explicit normalized metadata only. It contains no fixed prices,
does not find private transcripts, and does not equate tool calls with tokens.
The functional workflow checks are not a matched ChatGPT savings benchmark.

MIT notices are retained inside each adapted skill. Synthetic fixtures and tests
contain no user financial, medical, credential, or client data.
