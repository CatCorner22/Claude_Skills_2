---
name: otbi-subject-area-selection
description: >-
  Chooses the right OTBI subject area and columns for a reporting question, explains fact vs.
  dimension folders and the one-subject-area-per-analysis limit, and gives cross-pillar
  workarounds (BI Publisher SQL, side-by-side dashboard analyses on a shared prompt, or FDI/OAC).
  Covers the four Oracle Cash Management subject areas and when to use each. Use when unsure which
  subject area or columns to query, or when a report seems to need two subject areas or two Fusion
  pillars. Triggers: which subject area, pick a subject area, what subject area for,
  cross-subject-area, join two subject areas, Cash Management subject area, single subject area
  limit, column not available, fact vs dimension folder.
---

# Choose an OTBI subject area

## When to use
- Deciding which subject area answers a question before building an analysis.
- A report seems to need columns from two subject areas or two Fusion pillars.
- Checking whether a specific column (e.g. a flexfield) even exists in an area before promising it.
- Not for: the mechanics of building the analysis once the area is chosen → see
  `oracle-otbi-skills:otbi-report-building`. For which prebuilt Cash Management report to build →
  see `oracle-otbi-skills:otbi-cash-management-reports`.

## Do it
1. **State the question as measure + grain + filters.** Name the measure (what you count/sum), the
   grain (per what — account, statement line, date), and the filters (which accounts, which dates).
2. **Find the area whose fact folder holds the measure.** A subject area models one process as
   **fact folders** (measures) and **dimension folders** (attributes). The right area contains your
   measure *and* the attributes you group/filter by — all in one area.
3. **Confirm the columns exist.** Expand the fact and dimension folders and verify each column is
   present. Some fields — especially flexfields/DFF — may not be exposed; if a column is missing,
   the area (or OTBI) may not be the right tool. Don't promise a column you haven't seen.
4. **For Cash Management, map the question to one of four areas** (full detail and columns in
   `references/cash-management-subject-areas.md`):
   - **Bank Statements Real Time** — statement lines + reconciliation status → unreconciled,
     exceptions, aging, statement-line detail.
   - **Bank Statement Balances Real Time** — opening/closing booked & available balances by
     account/date → balances, cash-position-style, missing/late statement monitoring.
   - **Bank Statement Line Charges Real Time** — bank charges (code, type, amount, rate, tax) →
     bank-fee and charge-tax analysis.
   - **External Cash Transactions Real Time** — external cash transactions (fees, interest, manual)
     → external-transaction audits.
5. **If it needs two areas, pick a workaround — don't force it:**
   - **BI Publisher SQL data model** — join across tables/pillars for one report.
   - **Side-by-side analyses on one dashboard** sharing a dashboard prompt — visually combined,
     queried separately.
   - **Fusion Data Intelligence (FDI) / OAC** — the licensed warehouse for cross-pillar and
     historical reporting.
6. **Sanity-check the grain and date column** you'll use, then hand off to
   `oracle-otbi-skills:otbi-report-building`.

## Why / learn
A subject area is a curated, business-friendly view of *one* transactional process, deliberately
scoped so its facts and dimensions are guaranteed to join correctly. That guarantee is exactly why
OTBI restricts an analysis to a single subject area: the tool will not invent a join it can't trust.
So "which subject area?" is really "which single model contains both my measure and every attribute I
need to slice it by?" — and the failure mode is discovering mid-build that a needed attribute lives
in a different area. Naming the measure, grain, and filters up front surfaces that conflict before
you invest in a layout. When a question genuinely spans two models (e.g. cleared AP payments joined
to statement lines for outstanding checks), no single Cash Management area can do it, and the honest
answer is a different tool — BIP SQL, a shared-prompt dashboard, or FDI/OAC — not a workaround that
silently returns wrong rows.

## Common mistakes
- Picking the area by its name instead of its folders → the measure or attribute isn't actually there.
- Assuming a reconciliation subject area exists → there isn't one; reconciliation status is an
  **attribute inside Bank Statements Real Time**, not a separate area.
- Promising a flexfield/DFF column without checking the folder → it may not be exposed.
- Trying to join two subject areas in one analysis → not supported; use a documented workaround.
- Choosing the balances area for line-level detail (or vice versa) → wrong grain, wrong report.
- Ignoring the date column's meaning (statement date vs. external-transaction date) → shifted results.

## Tailor to your environment
List the subject areas your team actually has access to, and any custom ones, in
`references/your-environment.md` (or `references/your-environment.private.md`, git-ignored). Note
which columns/flexfields are exposed in your release and which questions you've had to route to BIP
or FDI. **Never commit real account numbers, IBANs, or legal-entity names** — keep it structural.
This skill then narrows its generic guidance to your real catalog.

## References
- references/cash-management-subject-areas.md — the four Cash Management areas, their key columns, common dimensions, and which report each supports
- references/your-environment.md — your available subject areas and exposed columns (add when supplied)
