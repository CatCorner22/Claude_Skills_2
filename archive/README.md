# Archive

**This directory no longer holds any plugins.** What remains is two individual skills, a set of
standalone applications, and the record of what was removed.

## Deleted, not archived (2026-08-18, owner-directed)

Two directives landed on the same day, and between them they emptied `archive/plugins/`.

**All Oracle skills.** The two Oracle-named plugins — `oracle-fusion-finance-skills` (10 skills)
and `oracle-otbi-skills` (5) — plus the two Fusion-named skills inside
`sponsored-projects-ar-skills` (`fusion-ar-ppm-domain-knowledge`,
`sponsored-ar-fusion-analyst-master-router`) were removed from the tree entirely, together with
their evals: 17 skills, 70 files. The Oracle layer was also de-mounted from the active library —
`chicken-little` lost its Fusion data-model and SQL-pattern references and every Oracle passage in
its body, `assertion-evidence-deck` lost `oracle-cm-domain.md`, `rest-api-data-pulls` lost its
Fusion query-idiom section, and `soviet-space-graphite` and `reference-class-forecasting` lost
their OTBI-specific worked material. This superseded the earlier owner-ratified exception that had
let `chicken-little` keep its Oracle reference.

**All treasury skills.** The seven finance/treasury plugins archived on 2026-08-11 were then
deleted outright rather than left delisted: **49 skills, 154 files**, plus their archived evals and
the Oracle-era `fusioncash-architect` tool.

| Deleted plugin | Skills | What it covered |
|---|---|---|
| `accounting-skills` | 6 | Double-entry accounting, journal entries, chart of accounts, month-end close, reconciliations, financial statements |
| `banking-skills` | 6 | Payment rails, bank account structures, statement formats, bank-fee analysis, connectivity, KYC/AML basics |
| `cash-management-skills` | 6 | Treasury cash operations: positioning, bank reconciliation, forecasting, liquidity, controls, intercompany netting |
| `finance-skills` | 6 | Corporate/treasury finance: time value of money, working capital, ratios, short-term investing, FX risk, capital budgeting |
| `public-sector-treasury-skills` | 8 | Public-sector/higher-ed treasury: GASB funds, public funds investing, escheatment, merchant/PCI, NACHA, bond compliance, CTP prep |
| `sponsored-projects-ar-skills` | 9 | Sponsored projects/grants receivables, federal compliance (Uniform Guidance) — after its 2 Fusion skills went with the Oracle deletion |
| `treasury-accounting-skills` | 6 | Debt facilities and covenants, hedging/derivatives, investment policy compliance, accruals, intercompany, audit readiness |

What deliberately remains in the active library is the *word*, not the domain: Oracle as one SQL
dialect among several in `sql-for-analysts`, Oracle OTBI as one of five named BI products in
`dashboard-design`, the unrelated *test oracle* concept in `lean-six-sigma-for-software`, and
reconciliation or payment scenarios used as ordinary business worked examples. Every cross-link
that used to point into a treasury skill was rewritten to name the domain instead of promising a
restorable archive — a pointer to something that no longer exists is worse than no pointer.

**Git history still contains everything deleted; nothing else does.** `git log --diff-filter=D`
finds the removal commits, and any deleted file can be recovered from the commit before them.
Locally installed copies of these plugins keep working — installs are version-pinned snapshots —
but they will never update and no longer appear in the marketplace listing.

## Archived individual skills (2026-08-11, still archived)

Two dental-practice-mounted skills sit at skill level, their host plugins still active. The dental
app direction was not chosen at the career re-aim; both are preserved and restorable:

| Skill | From plugin | Where it lives now |
|---|---|---|
| `curve-hero-design-language` | continuous-improvement-skills | `archive/skills/continuous-improvement-skills/` |
| `chicken-little-college-kid` | coding-agent-skills | `archive/skills/coding-agent-skills/` |

Restore one with:

```
git mv archive/skills/<plugin>/<skill> plugins/<plugin>/skills/<skill>
git mv archive/evals/<plugin>/<skill>.md evals/<plugin>/<skill>.md
```

then restore any cross-links the active tree marks `archived:`, bump the host plugin's `version`
(installed copies only pick up changes on a bump), and run `bash scripts/validate.sh` followed by
`python3 scripts/gen-catalog.py`.

Also recorded here: `board-of-advisors-skills` was **merged, not archived** — its single skill and
six subagents now live in `coding-agent-skills` as `coding-agent-skills:board-review`.

## Archived applications and domain tools

`archive/apps/` holds standalone programs that predate the library's re-aim and were never
referenced by any skill: two separate dental "notes standardizer" apps (a root Vite + React 19 app
and a `tools/`-based vocabulary normalizer) and their Curve Hero benchmark docs and validation
record. They lived at the repository root, where they made a skills marketplace read as a
JavaScript app. See [apps/README.md](apps/README.md). The Oracle-era `fusioncash-architect` Python
tool that used to sit alongside them went with the Oracle deletion.

`GITHUB_SETUP.md` was **deleted** in the same 2026-08-11 pass rather than archived — every fact in
it was dead (defunct repo URL, long-merged branch, its own status line saying "not found"). It had
published an ssh-ed25519 deploy public key; if that key still exists on the repository, revoke it
in GitHub settings independently of this cleanup.

## Why

The owner's standing directive (2026-08-08, extended 2026-08-11, made a deletion on 2026-08-18):
the library's active surface is general-use and portable across future roles. The Oracle and
treasury sets were domain mounts on a role the owner has left. Keeping them delisted still cost
something real — they showed up in every audit, every residue sweep re-litigated them, and every
active skill that bordered one carried a pointer promising a restore. Deleting them ends that.
Build nothing new that mounts on these domains.
