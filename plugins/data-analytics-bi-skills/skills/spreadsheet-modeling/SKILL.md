---
name: spreadsheet-modeling
description: >-
  Builds and audits transparent, reliable spreadsheet models (Excel/Google Sheets) — a clean
  input/calculation/output separation, consistent one-formula-per-row logic, named ranges, check
  cells and control totals, no constants hardcoded inside formulas, and sensitivity/what-if analysis.
  Use when building a financial or operational spreadsheet model, or reviewing/auditing one for
  errors. Triggers: Excel model, spreadsheet model, financial model, named ranges, check cell,
  control total, model audit, sensitivity analysis, what-if, data table, hardcoded formula, model
  review.
---

# Spreadsheet modeling

## When to use
- Building a financial or operational model in Excel or Google Sheets (budget, forecast, pricing, ROI).
- Reviewing or auditing an inherited model for structure, hardcoding, and formula errors.
- Adding sensitivity/what-if analysis or scenario toggles to an existing model.
- Not for: the forecasting *methodology* (drivers, seasonality, direct vs. indirect method) behind a
  cash model → see `cash-management-skills:cash-forecasting`. This skill is the modeling craft; that
  one is the method.

## Do it
1. **Separate inputs, calculations, and outputs.** Put assumptions in one clearly marked zone (or
   sheet), calculations in another, results in a third. Color inputs distinctly (e.g. blue font) and
   never bury an assumption inside a calculation. This one rule prevents most model errors.
2. **One formula per row, consistent across all columns.** Write a formula once in the first period
   and fill it right unchanged. If a row needs an exception in one column, restructure it — a row you
   can't copy across is a row that hides a bug.
3. **Never hardcode a constant inside a formula.** `=Revenue*0.21` should be `=Revenue*TaxRate`, with
   `TaxRate` living in an input cell. Every number a user might change must be a findable, single-source
   input — magic numbers buried in formulas are unauditable and get out of sync.
4. **Name the key inputs and structured references.** Use `=Price*Units` (named ranges) rather than
   `=$B$4*$C$4`. Names make formulas read like the logic they represent and make auditing far faster.
   Keep names for genuine inputs and important intermediates, not every cell.
5. **Build check cells and control totals.** Add explicit reconciliations — cross-foot rows and
   columns, balance identities (assets = liabilities + equity; sum of parts = total), and a single
   top-level "all checks OK" flag that turns red on any break. A model without checks fails silently.
6. **Add sensitivity and what-if.** Use one- and two-way **data tables** and scenario toggles to see
   how outputs move with key drivers, and to find which inputs actually matter. Vary inputs in the
   input zone, never by editing formulas. See `references/model-structure.md`.
7. **Document assumptions and sources.** Note the source, units, and as-of date beside each input, and
   keep a cover/README sheet stating purpose, owner, version, and key assumptions. Future-you and the
   reviewer both need this.
8. **Audit before you trust it.** Trace precedents/dependents on the outputs, scan for inconsistent
   formulas across a row (Excel error-checking / `FORMULATEXT`), confirm no unintended circular
   references, and stress the inputs to see the outputs respond sensibly.

## Why / learn
A model is only as good as it is **auditable** — the value isn't the answer it prints today, it's that
someone can follow, trust, and safely change it tomorrow. Spreadsheets fail silently: a single
overwritten formula or a `0.21` typed where `0.12` belonged produces a clean-looking number that's
simply wrong, and studies of real-world spreadsheets find such errors astonishingly common. Structure
is the defense. **Separating inputs from calculations** means there is exactly one place to change an
assumption and one place a wrong assumption can hide. **One consistent formula per row** turns a
correctness question into a visual one — a broken row *looks* different from its neighbors, so errors
become visible instead of buried. **No hardcoded constants** guarantees every driver has a single
source of truth, so a rate change propagates everywhere at once instead of leaving stale copies.
**Check cells** convert silent failures into loud ones: a control total that must tie to zero is a
tripwire that catches the mistake you didn't anticipate. And **sensitivity analysis** is what turns a
model from a single guess into a tool for understanding — it shows which assumptions the answer
actually hinges on, which is usually more valuable than the base-case number itself.

## Common mistakes
- Assumptions typed inside formulas → impossible to find or update. Put every input in its own labeled cell.
- Inconsistent formulas across a row → a hidden broken cell. Write once, fill right; make rows copyable.
- No check cells → errors pass silently. Add control totals and a top-level OK/ERROR flag.
- Hardcoding a rate or FX number in many places → they drift apart. One input cell, referenced everywhere.
- Mixing inputs, calcs, and outputs on one sheet → nobody can audit it. Separate the three zones.
- Circular references left on by accident → unstable/incorrect results. Remove them unless deliberately iterating.
- No documentation of source/units/date → the model rots. Annotate inputs; keep a cover sheet.
- "Fixing" a number by overtyping a formula with a value → destroys the logic. Change the input, not the formula.

## Tailor to your environment
Record your conventions in `references/your-environment.md` (keep sensitive material — real
assumptions, rates, client figures — in `your-environment.private.md`, which is git-ignored). Capture
your input-cell color/format standard, your sheet-structure convention (inputs/calcs/outputs), your
standard check cells, your named-range conventions, and your review/sign-off process. This skill then
applies its generic structure to your house style. For the forecasting logic that feeds a cash model,
use `cash-management-skills:cash-forecasting`.

## References
- references/model-structure.md — input/calc/output layout, check-cell patterns, named ranges, and data-table sensitivity
- references/your-environment.md — your color/format standards, check cells, and review process (add when supplied)
