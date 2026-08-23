---
name: spreadsheet-modeling
description: >-
  Builds and audits transparent, reliable spreadsheet models (Excel/Google Sheets) using
  FAST-style structured-modeling conventions: one-directional inputs → calculations →
  outputs separation, one consistent formula per row filled across, no constants hardcoded
  inside formulas, named ranges for readable logic, check cells and control totals with a
  single OK/ERROR flag, assumptions documented with source and units, and one/two-way data
  tables and scenario toggles for sensitivity. Grounded in the EuSpRIG spreadsheet-error
  field-audit record: errors are the norm, so auditability is the design goal. Use when
  building a financial or operational model (budget, forecast, pricing, ROI), or
  reviewing/auditing an inherited workbook. Triggers: Excel model, spreadsheet model,
  financial model, named ranges, check cell, control total, model audit, sensitivity
  analysis, what-if, data table, hardcoded formula, model review, scenario toggle,
  spreadsheet error, one formula per row.
metadata:
  version: "1.2.1"
  source: >-
    Grounded in the documented spreadsheet-error research collected by EuSpRIG (Panko's
    field-audit synthesis) and FAST-style structured-modeling conventions. Claims marked
    [snippet-only] were cross-checked via web-search snippets, not the primary papers.
---

# Spreadsheet modeling

## When to use
- Building a financial or operational model in Excel or Google Sheets (budget, forecast, pricing, ROI).
- Reviewing or auditing an inherited model for structure, hardcoding, and formula errors.
- Adding sensitivity/what-if analysis or scenario toggles to an existing model.
- Not for: the forecasting *methodology* behind the numbers. Statistical method — seasonality, model
  choice, backtesting → see `machine-learning-skills:time-series-forecasting`; the treasury
  direct-vs-indirect framing is a cash-forecasting method question, which belongs to whatever
  finance source you work from — this library no longer carries one. This skill is the modeling
  craft, not the method.

## Do it
1. **Separate inputs, calculations, and outputs.** Put assumptions in one clearly marked zone (or
   sheet), calculations in another, results in a third; flow runs one direction, inputs → calcs →
   outputs. Color inputs distinctly (e.g. blue font) and never bury an assumption inside a
   calculation. If raw data feeds the model, land it analysis-ready first —
   `data-analytics-bi-skills:data-cleaning` — and paste values into a marked data zone, not into
   formulas.
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
   references, and stress the inputs to extremes — then gut-check the outputs (sign, magnitude,
   units, a rough independent re-derivation) per
   `math-foundations-skills:number-sense-and-estimation` before anyone relies on the number.
9. **Know when to leave the spreadsheet.** A workbook rebuilt by hand every period becomes a script —
   `data-tools-skills:excel-automation-python`; data that chokes the sheet or a fragile chain of
   lookups becomes one query — `data-tools-skills:duckdb-local-analytics`; outputs that feed a
   standing report get designed as a view, not more tabs —
   `data-analytics-bi-skills:dashboard-design`.

## Why / learn
A model is only as good as it is **auditable** — the value isn't the answer it prints today, it's that
someone can follow, trust, and safely change it tomorrow. Spreadsheets fail silently: a single
overwritten formula or a `0.21` typed where `0.12` belonged produces a clean-looking number that's
simply wrong, and the field-audit record says this is the norm, not the exception — Panko's synthesis
of the research EuSpRIG collects found at least one error in 94% of 88 spreadsheets audited, with an
average cell error rate around 5% across the underlying studies [snippet-only]. Structure is the
defense, and the published structured-modeling conventions (the FAST standard's "flexible,
appropriate, structured, transparent" discipline among them) all converge on the same few moves.
**Separating inputs from calculations** means there is exactly one place to change an assumption and
one place a wrong assumption can hide. **One consistent formula per row** turns a correctness question
into a visual one — a broken row *looks* different from its neighbors, so errors become visible
instead of buried. **No hardcoded constants** guarantees every driver has a single source of truth, so
a rate change propagates everywhere at once instead of leaving stale copies. **Check cells** are the
move most often built wrong, and the reference proves why: a control total only catches what it is
not already guaranteed to satisfy. Σ(monthly margins) = annual revenue − annual cost is an
*algebraic identity* of the rows themselves — true for every input set, hardcoded constants
included — so it stays green through the very error people build it to catch. A check earns its keep
only when it asserts something the model could violate: an external reconciliation to a payroll
actual, a bound the logic does not enforce. Ask of every check cell, "what input would make this
fire?"; if you cannot answer, you built a decoration. And **sensitivity analysis** turns a model
from a single guess into a tool for understanding — it shows which assumptions the answer actually
hinges on, which is usually more valuable than the base-case number itself.

## Common mistakes
- Assumptions typed inside formulas → impossible to find or update. Put every input in its own labeled cell.
- Inconsistent formulas across a row → a hidden broken cell. Write once, fill right; make rows copyable.
- No check cells, or only self-satisfying ones → errors pass silently either way. Every check must name an input that would make it fire; anchor at least one to a source outside the model.
- Hardcoding a rate or FX number in many places → they drift apart. One input cell, referenced everywhere.
- Mixing inputs, calcs, and outputs on one sheet → nobody can audit it. Separate the three zones.
- Circular references left on by accident → unstable/incorrect results. Remove them unless deliberately iterating.
- No documentation of source/units/date → the model rots. Annotate inputs; keep a cover sheet.
- "Fixing" a number by overtyping a formula with a value → destroys the logic. Change the input, not the formula.
- Quoting "90% of spreadsheets have errors" as a universal law → the audited figures vary by
  study and method; cite the field-audit record for what it is (see the reference's sources).

## Tailor to your environment
Wire in your current role here — the craft is deliberately domain-neutral, and the same structure
serves an analyst's budget, an attorney's damages or fee model, an ops manager's capacity plan, or a
developer's cost estimate, wherever you work next. Record your conventions in
`references/your-environment.md` (keep sensitive material — real assumptions, rates, client figures —
in `your-environment.private.md`, which is git-ignored). Capture your input-cell color/format
standard, your sheet-structure convention (inputs/calcs/outputs), your standard check cells, your
named-range conventions, and your review/sign-off process. Wire any domain forecasting method the
model depends on into the same file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/spreadsheet-modeling.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/model-structure.md — zone layout, formatting and named-range conventions, check-cell
  patterns, data-table sensitivity, the audit toolkit, and a worked domain-neutral example (a
  12-month staffing-and-cost model built end to end)
- references/your-environment.md — your color/format standards, check cells, and review process
  (sanitized stub; live detail goes in the `.private.md` twin)
