# Archived plugins

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
| `oracle-fusion-finance-skills` | 10 | 0.5.0 | Functional Oracle Fusion Cloud Financials: GL, FBDI, AP, AR, Cash Management, period close, treasury-architect subagent |
| `oracle-otbi-skills` | 5 | 0.1.0 | OTBI reports and analyses in Oracle Fusion Cloud, deep Cash Management subject-area coverage |
| `public-sector-treasury-skills` | 8 | 0.1.0 | Public-sector/higher-ed treasury: GASB funds, public funds investing, escheatment, merchant/PCI, NACHA, bond compliance, CTP prep |
| `sponsored-projects-ar-skills` | 13 | 1.0.0 | Sponsored projects/grants receivables across Oracle Fusion AR + PPM, federal compliance (Uniform Guidance) |
| `treasury-accounting-skills` | 6 | 0.1.0 | Debt facilities and covenants, hedging/derivatives, investment policy compliance, accruals, intercompany, audit readiness |

(Last-version numbers are as recorded in each plugin's `.claude-plugin/plugin.json`
at archive time; verify with the manifest files here if they ever drift.)

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
