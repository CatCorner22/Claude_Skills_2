# OTBI Create Analysis — full build workflow (reference)

Detailed companion to `otbi-report-building`. Covers the path from opening the catalog to publishing
on a dashboard, plus the performance and security gotchas that most often bite. Confirm exact menu
paths and options in your release.

## Contents
- 1. Where you build (catalog paths)
- 2. Select the subject area
- 3. Criteria tab — columns, properties, formulas
- 4. Filters
- 5. Results tab — views and the compound layout
- 6. Save
- 7. Dashboard and dashboard prompt
- 8. Verify and tune
- 9. Gotchas
- 10. Sources

## 1. Where you build (catalog paths)
- Navigate: **Navigator → Tools → Reports and Analytics → Browse Catalog**.
- Create: **Create → Analysis** (a report is an *analysis* object in the catalog).
- Save location: **/Shared Folders/Custom/…**. Objects under Oracle-delivered folders are
  overwritten by upgrades — always **copy a delivered analysis into /Custom before editing**.
- Personal drafts can live under **/My Folders**, but anything shared must sit in a Shared folder
  whose permissions the audience can reach (see `otbi-report-scheduling-sharing`).

## 2. Select the subject area
- Create → Analysis opens the **Select Subject Area** list. Pick the one area whose fact folder
  holds your measure and whose dimension folders hold your attributes.
- One analysis = one subject area; there are no native cross-subject-area joins. If the question
  needs data from two areas or two pillars, use the workarounds in `otbi-subject-area-selection`
  (references/cash-management-subject-areas.md).

## 3. Criteria tab — columns, properties, formulas
- **Add columns:** expand fact and dimension folders in the Subject Areas pane and double-click or
  drag columns into the Selected Columns area.
- **Column properties (Column Properties dialog):** data format, **aggregation rule** (Sum, Count,
  Average, None…), **conditional formatting**, sort, and hidden/excluded.
- **Column formula (Edit formula / fx):** write a formula on any column — a derived measure or a
  `CASE WHEN … THEN … END` that buckets values (aging days, status groups). Formula syntax and
  bucket recipes live in `otbi-analysis-filters`.
- **Grain matters:** the set of dimension columns you add defines the row grain; a measure is
  aggregated *within* that grain by its aggregation rule. Mixing a fine attribute (statement line)
  with a coarse total can multiply rows — check subtotals after adding each measure.

## 4. Filters
- Add filters on the Criteria tab (Filters pane → add on a selected column). Choose an operator
  (is equal to, is between, is greater than, is in, is null, **is prompted**, etc.).
- **is prompted** leaves the value open so a column or dashboard prompt supplies it at runtime.
- Filter **early and selectively** — bank account and date first — to keep the live query small.
- Filters cut rows in the query; selection steps/views trim in the result. Prefer filters for
  anything that reduces data volume.

## 5. Results tab — views and the compound layout
- The default is a Title + Table. Add views with the view toolbar:
  - **Table** — flat detail.
  - **Pivot Table** — multidimensional, row/column edges, subtotals and grand totals.
  - **Graph / Chart** — bar, line, pie, etc.
  - **Gauge** — single-value KPIs against thresholds.
  - **Narrative** — templated text per row (e.g. one-line exception notes).
  - **Title / Filters views** — labels and a visible filter summary.
- Assemble them in the **Compound Layout** (the container that renders multiple views together).
  Remove unused views; each view re-renders the query.

## 6. Save
- **Save As** into /Shared Folders/Custom/… with a name that states the content and, ideally, the
  subject area. Add a description noting prompts and intended audience.

## 7. Dashboard and dashboard prompt
- **New → Dashboard**, add a page, drag the analysis (and others) onto it.
- **New → Dashboard Prompt** built on a shared column (As-of Date, Bank Account, Currency, Legal
  Entity). Save it and add it to the dashboard page so every analysis whose matching column filter
  is **is prompted** re-scopes together.
- **Prompt types:** column prompt, named/inline prompt (Prompts tab of the analysis), and reusable
  **dashboard prompt**. Presentation/repository variables set by prompts can feed formulas and
  titles. Detail: `otbi-analysis-filters`.

## 8. Verify and tune
- Tie a row count or a total to a known figure (a statement, a prior report).
- Confirm each measure's aggregation is correct and subtotals are not double-counted.
- Run once with prompts set to real values; confirm the "is prompted" filters actually bind.
- If slow, remove columns the views don't use and tighten the leading filters.

## 9. Gotchas
- **Security to even see the area:** Cash Management subject areas require the **Cash Management
  Transaction Analysis Duty** (typically via the **Cash Manager** job role); data security still
  restricts rows by bank account / business unit / legal entity.
- **Missing columns:** some fields — especially flexfields/DFF — may not be exposed. Check the
  folders before promising a column.
- **Performance:** real-time queries hit the live DB and degrade during period close; filter on bank
  account + date early and avoid selecting every column.
- **Right date column:** pick the date that matches the question (statement date vs.
  external-transaction date). Using the wrong one silently shifts results.
- Diagnose slow reports with the **OTBI Usage/Performance Real Time** subject areas.

## 10. Sources
- Create your first analysis —
  https://docs.oracle.com/en/cloud/saas/otbi/otbi-user/create-your-first-analysis.html
- Cash Management subject areas, folders, and attributes —
  https://docs.oracle.com/en/cloud/saas/financials/25c/fappp/cash-management-subject-areas-folders-and-attributes.html
