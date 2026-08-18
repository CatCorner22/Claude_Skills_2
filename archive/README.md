# Archived plugins

> **Deleted, not archived (2026-08-18, owner-directed): all Oracle skills.** The two
> Oracle-named plugins — `oracle-fusion-finance-skills` (10 skills) and `oracle-otbi-skills`
> (5) — plus the two Fusion-named skills inside `sponsored-projects-ar-skills`
> (`fusion-ar-ppm-domain-knowledge`, `sponsored-ar-fusion-analyst-master-router`) were
> **removed from the tree entirely**, together with their evals. 17 skills, 70 files. The
> Oracle layer was also de-mounted from the active library: `chicken-little` lost its
> Fusion data-model and SQL-pattern references and every Oracle passage in its body,
> `assertion-evidence-deck` lost `oracle-cm-domain.md`, and `rest-api-data-pulls` lost its
> Fusion query-idiom section. What deliberately remains is Oracle as one *vendor among
> several* — SQL dialect notes, BI-tool lists — and the unrelated *test oracle* concept in
> `lean-six-sigma-for-software`. Git history still contains everything deleted; nothing else
> does. This supersedes the earlier owner-ratified exception that let `chicken-little` keep
> its Oracle reference.

These plugins were **archived on 2026-08-11** by the owner's directive during their
career transition away from a university treasury role: the active marketplace now
carries only career-portable, domain-neutral skills, while the treasury-, Oracle-,
and finance-domain plugins are preserved here — delisted, not deleted.

Nothing was lost:

- Full git history is preserved (the plugins were moved with `git mv`; use
  `git log --follow archive/plugins/<plugin>` to see every commit).
- Locally installed copies of these plugins **keep working** — installs are
  version-pinned snapshots. They simply stop receiving updates and no longer appear
  in the marketplace listing.
- Every plugin here validated clean (0 errors) at the moment of archiving.

## Manifest

| Plugin | Skills | Last version | What it covered |
|---|---|---|---|
| `accounting-skills` | 6 | 0.1.0 | Double-entry accounting, journal entries, chart of accounts, month-end close, reconciliations, financial statements |
| `banking-skills` | 6 | 0.1.0 | Payment rails, bank account structures, statement formats, bank-fee analysis, connectivity, KYC/AML basics |
| `cash-management-skills` | 6 | 0.1.0 | Treasury cash operations: positioning, bank reconciliation, forecasting, liquidity, controls, intercompany netting |
| `finance-skills` | 6 | 0.1.0 | Corporate/treasury finance: time value of money, working capital, ratios, short-term investing, FX risk, capital budgeting |
| `public-sector-treasury-skills` | 8 | 0.1.0 | Public-sector/higher-ed treasury: GASB funds, public funds investing, escheatment, merchant/PCI, NACHA, bond compliance, CTP prep |
| `sponsored-projects-ar-skills` | 11 | 1.0.0 | Sponsored projects/grants receivables, federal compliance (Uniform Guidance) |
| `treasury-accounting-skills` | 6 | 0.1.0 | Debt facilities and covenants, hedging/derivatives, investment policy compliance, accruals, intercompany, audit readiness |

(Last-version numbers are as recorded in each plugin's `.claude-plugin/plugin.json`
at archive time; verify with the manifest files here if they ever drift.)

## Archived individual skills (2026-08-11, consolidation pass)

Two dental-practice-mounted skills were archived at skill level (their host plugins stay
active). The dental app direction was not chosen at the career re-aim; both are preserved
and restorable:

| Skill | From plugin | Where it lives now |
|---|---|---|
| `curve-hero-design-language` | continuous-improvement-skills | `archive/skills/continuous-improvement-skills/` |
| `chicken-little-college-kid` | coding-agent-skills | `archive/skills/coding-agent-skills/` |

Restore: `git mv archive/skills/<plugin>/<skill> plugins/<plugin>/skills/<skill>` and
`git mv archive/evals/<plugin>/<skill>.md evals/<plugin>/<skill>.md`, restore any
cross-links marked `archived:` in the active tree, bump the plugin version, validate.

Also recorded here: `board-of-advisors-skills` was **merged, not archived** — its single
skill and six subagents now live in `coding-agent-skills` as
`coding-agent-skills:board-review` (same content, new namespace).

## Archived applications and domain tools (2026-08-11)

`archive/apps/` holds standalone programs that predate the library's re-aim and were never
referenced by any skill: two separate dental "notes standardizer" apps (a root Vite + React 19
app and a `tools/`-based vocabulary normalizer), their Curve Hero benchmark docs and validation
record, and the Oracle-era `fusioncash-architect` Python tool. They lived at the repository
root, where they made a skills marketplace read as a JavaScript app. See
[apps/README.md](apps/README.md) for what each one is and how to restore it.

`GITHUB_SETUP.md` was **deleted** in the same pass rather than archived — every fact in it was
dead (defunct repo URL, long-merged branch, its own status line saying "not found"). It had
published an ssh-ed25519 deploy public key; if that key still exists on the repository, revoke
it in GitHub settings independently of this cleanup.

## Restore procedure

To restore a plugin to the active marketplace:

1. Move it back (history follows automatically):
   ```
   git mv archive/plugins/<plugin> plugins/<plugin>
   git mv archive/evals/<plugin> evals/<plugin>
   ```
2. Re-add its entry to `.claude-plugin/marketplace.json` (name, `source:
   "./plugins/<plugin>"`, description, category — copy the description from the
   manifest table above or the plugin's own `plugin.json`).
3. Re-check cross-links: active skills' references to this plugin were rewritten to
   archived-pointer prose at archive time (grep the active tree for
   `archived: <plugin>` and restore any seams you want live again).
4. Bump the plugin's `version` in its `plugin.json` (installed copies only pick up
   changes on a version bump), then run:
   ```
   bash scripts/validate.sh
   python3 scripts/gen-catalog.py
   ```

## Why these nine

The owner's standing directive (2026-08-08, extended 2026-08-11): the library's
active surface should be general-use and portable across future roles. These nine
plugins are domain mounts — Oracle Fusion/OTBI product skills, treasury operations,
public-sector treasury, sponsored-projects AR, and the finance/accounting/banking
domain sets. They remain professional assets; they are simply no longer the
library's active face.
