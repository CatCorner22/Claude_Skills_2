---
name: otbi-cash-management-reports
description: >-
  Builds the common Oracle Cash Management OTBI reports — bank statement balances, cash-position
  snapshot, unreconciled/exception and aging analyses, reconciliation status summary, bank-charge
  and charge-tax breakdowns, and external cash transaction audits — each mapped to its correct Cash
  Management subject area, with the security duty role required and the reconciliation-status-is-an-
  attribute caveat. Use when reporting on Oracle Fusion Cash Management data in OTBI. Triggers: cash
  management report, bank statement balances report, cash position OTBI, unreconciled report,
  reconciliation status report, bank charges report, external cash transactions, OTBI cash report,
  unreconciled aging.
---

# Oracle Cash Management OTBI reports

## When to use
- Building a standard Cash Management report in OTBI (balances, cash position, unreconciled/aging,
  reconciliation status, bank charges, external cash transactions).
- Deciding which Cash Management subject area a specific cash report should sit on.
- Not for: the reconciliation *process* itself (matching, tolerances, classifying breaks) → see
  `cash-management-skills:bank-reconciliation`. For cash-position *methodology* (sources, horizon,
  worksheet) → see `cash-management-skills:cash-positioning`.

## Do it
1. **Confirm access first.** To see Cash Management subject areas the user needs the **Cash
   Management Transaction Analysis Duty**, typically via the **Cash Manager** job role. Data security
   still limits rows by bank account / business unit / legal entity — a correct report can
   legitimately show fewer rows than expected.
2. **Map the report to its subject area (one area per analysis):**
   - **Bank statement balances** (daily/period, by account) → **Bank Statement Balances RT**.
   - **Cash position snapshot** (by bank/currency/LE, prompt-driven) → **Bank Statement Balances RT**
     — *approximation only* (see step 5).
   - **Unreconciled lines / reconciliation exceptions** → **Bank Statements RT**.
   - **Unreconciled aging** (CASE bucket column) → **Bank Statements RT**.
   - **Reconciliation status summary** → **Bank Statements RT**.
   - **Bank charges by code/type/bank** and **charge-tax breakdown** → **Bank Statement Line Charges RT**.
   - **External cash transactions audit** → **External Cash Transactions RT**.
   - **Statement line detail / drill** → **Bank Statements RT**.
   - **Bank account master / dashboard** → **Balances RT** or **Bank Statements RT**.
   - **Missing / late statement monitor** → **Balances RT**.
3. **Remember reconciliation status is an attribute, not an area.** There is no reconciliation
   subject area; **reconciliation status lives inside Bank Statements RT** (header and line level).
   Build unreconciled/exception/status reports there by filtering on that attribute.
4. **Build it.** Pick the area, add fact/dimension columns, filter early on bank account + date, add
   an aging CASE column where needed, assemble views, and add a dashboard prompt (As-of Date, Bank
   Account, Currency, Legal Entity). Mechanics: `oracle-otbi-skills:otbi-report-building`; filters,
   prompts, and CASE buckets: `oracle-otbi-skills:otbi-analysis-filters`. Column maps per report:
   `references/cash-management-report-recipes.md`.
5. **Know what one Cash Management area cannot do.** A true dynamic multi-source cash position is the
   **Essbase Cash Position Worksheet**; OTBI only approximates position off statement balances.
   Reports needing cleared **AP-payment / AR-receipt transaction-level joins** — outstanding checks,
   deposits in transit — cannot be done in one Cash Management area; use Payables/Receivables subject
   areas, a **BI Publisher SQL data model**, or Oracle's predefined Cash Management reports.
6. **Pick the right date column** for the question (statement date vs. external-transaction date) and
   **confirm the CAMT.053 version** supported for the customer's release rather than hard-coding one.

## Why / learn
Every Cash Management OTBI report is really a choice of *which of four models* holds the number you
want, because each area is scoped to one slice of the cash process: **balances** (Balances RT),
**statement lines and their reconciliation state** (Bank Statements RT), **charges on those lines**
(Line Charges RT), and **external cash transactions** (External Cash Transactions RT). Once you see
that reconciliation status is just an attribute *within* the statement-lines model, the whole family
of "unreconciled / exception / aging / status" reports collapses into one area with different filters
and a CASE column — you are not hunting for a special reconciliation report, you are filtering Bank
Statements RT. The hard boundary is the single-area limit: the moment a report needs the *other* side
of a reconciliation (the AP payment or AR receipt that cleared), no Cash Management area can reach it,
and forcing it produces confident wrong answers. Knowing that line — and that OTBI's cash position is
an approximation of the Essbase worksheet — is what keeps a cash report trustworthy.

## Common mistakes
- Looking for a reconciliation subject area → there isn't one; filter reconciliation status in Bank Statements RT.
- Building outstanding-checks / deposits-in-transit in one Cash Management area → needs AP/AR joins; use BIP or the sub-ledger areas.
- Presenting an OTBI balance snapshot as a true cash position → it approximates; the Essbase worksheet is the real thing.
- Using the balances area for line-level charge detail (or vice versa) → wrong grain; charges live in Line Charges RT.
- Forgetting the duty role → the user can't even see the subject areas; check Cash Manager access first.
- Reading fewer rows as a bug → data security limits rows by bank account / BU / LE by design.

## Tailor to your environment
Capture your real reporting setup in `references/your-environment.md` (or
`references/your-environment.private.md`, git-ignored): your bank-account and legal-entity structure,
which of the four areas your roles expose, your standard cash reports and their prompts, and sample
sanitized exports. **Never commit real bank-account numbers, IBANs, or entity names** — keep it
structural. This skill then targets your accounts, entities, and report catalog.

## References
- references/cash-management-report-recipes.md — each common report: subject area, key columns, filters, and views
- references/your-environment.md — your accounts, entities, roles, and standard reports (add when supplied)
