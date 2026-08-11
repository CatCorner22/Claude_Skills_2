---
name: otbi-report-building
description: >-
  Builds or edits an Oracle Transactional Business Intelligence (OTBI) analysis end to end in
  Oracle Fusion Cloud: pick one subject area, add columns and column formulas on the Criteria
  tab, set filters, assemble Results views into a compound layout, save under /Shared
  Folders/Custom, and surface it on a dashboard with a shared prompt. Use when creating, editing,
  or troubleshooting any OTBI report or analysis. Triggers: build an OTBI report, create an
  analysis, OTBI analysis, Reports and Analytics, Browse Catalog, criteria tab, compound layout,
  add a column formula, put an analysis on a dashboard, edit an OTBI report.
---

# Build an OTBI analysis (Create Analysis workflow)

## When to use
- Creating a new OTBI analysis/report in Oracle Fusion Cloud, or editing an existing one.
- Troubleshooting a report that returns wrong rows, wrong totals, or an empty result.
- Assembling several views (table, pivot, chart) into one layout and placing it on a dashboard.
- Not for: choosing *which* subject area or columns to query → see
  `oracle-otbi-skills:otbi-subject-area-selection`. For scheduled, burst, or pixel-perfect delivery
  → see `oracle-otbi-skills:otbi-report-scheduling-sharing`.

## Do it
1. **Open the authoring tool.** Navigator → Tools → **Reports and Analytics** → **Browse Catalog**,
   then **Create → Analysis**. Save all custom work under **/Shared Folders/Custom/…**; never edit a
   delivered (Oracle-shipped) object — **copy it into /Custom first**, then edit the copy.
2. **Select exactly one subject area.** An analysis queries a single subject area; you cannot join
   two natively. If unsure which, or if the question spans pillars, stop and use
   `oracle-otbi-skills:otbi-subject-area-selection` before building.
3. **Build the Criteria tab.** Double-click or drag columns from the **fact** (measures) and
   **dimension** (attributes) folders. Per column set: sort, **aggregation rule**, format, and
   **conditional formatting**. Write **column formulas** for derived values (e.g. a `CASE WHEN`
   aging bucket or a computed measure) — see `oracle-otbi-skills:otbi-analysis-filters`.
4. **Add filters.** On Criteria, filter early on the columns that cut the data most — **bank account
   and date first**, then legal entity. Use the **"is prompted"** operator on any column a dashboard
   prompt will drive at runtime. Details and prompt types: `oracle-otbi-skills:otbi-analysis-filters`.
5. **Build the Results tab.** Add **views** — Table, **Pivot Table** (subtotals, multidimensional),
   Graph/Chart, Gauge, Narrative, Title — and arrange them in a **Compound Layout**. Delete views
   you don't need so the report stays fast.
6. **Save under Custom** with a clear name and a description noting the subject area and prompts used.
7. **Surface it (optional).** **New → Dashboard**, drop the analysis on a page, then add a
   **New → Dashboard Prompt** on a shared column (As-of Date, Bank Account, Currency, Legal Entity)
   so every analysis on the page responds to one set of runtime values.
8. **Verify.** Check row counts against a known figure, confirm each measure's aggregation total is
   right (not double-counted), and run once with the prompts set to real values. Full step detail
   and gotchas: `references/build-workflow.md`.

## Why / learn
OTBI is *embedded, real-time, ad-hoc* analytics: every analysis runs a live query against the Fusion
transactional tables through a **subject area** — a business-friendly model of one process, organized
into **fact folders** (the measures you aggregate) and **dimension folders** (the attributes you
group and filter by). There is no data warehouse and no overnight load, which is why results are
current to the second but also why a careless query is slow: you compete with live transaction
processing. The build order — Criteria → Filters → Results — mirrors how the query is assembled:
Criteria defines *what columns and grain*, Filters define *which rows*, Results define *how it is
presented*. Keeping presentation (Results/views) separate from the query (Criteria/Filters) is what
lets one analysis feed a table, a pivot, and a chart at once, and lets a dashboard prompt re-scope
all of them together. The single-subject-area rule is the one constraint that shapes every later
decision, so you settle it first (step 2) before investing in columns and layout.

## Common mistakes
- Editing a delivered analysis in place → an upgrade overwrites it. Copy into /Custom first.
- Starting to build before settling the subject area → rework when a needed column isn't in that area.
- Pulling every column "just in case" → slow real-time query. Select only what the views use.
- Forgetting the aggregation rule on a measure → double-counted or wrong subtotals in a pivot.
- Filtering late or not at all → full scan on live data. Filter on bank account + date early.
- Hard-coding a value (a specific account/date) that should be a prompt → the report can't be reused.

## Tailor to your environment
Record your real setup in `references/your-environment.md` (or `references/your-environment.private.md`,
which is git-ignored): the subject areas you can access, your /Shared Folders/Custom path and naming
convention, the security roles your users hold, your standard dashboard prompts, and sample analysis
exports. **Never commit real bank-account numbers, IBANs, legal-entity names, or statement data** —
sanitize to structure only. This skill then maps its generic steps onto your catalog.

## References
- references/build-workflow.md — the full Create Analysis walkthrough: catalog paths, Criteria/Filters/Results detail, dashboard and prompt setup, and performance gotchas
- references/your-environment.md — your catalog paths, subject areas, roles, and prompts (add when supplied)
