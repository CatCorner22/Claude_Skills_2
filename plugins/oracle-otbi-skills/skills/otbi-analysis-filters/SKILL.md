---
name: otbi-analysis-filters
description: >-
  Scopes and parameterizes an OTBI analysis: builds filters and "is prompted" filters,
  column/named/dashboard prompts, presentation and repository variables, and column-formula CASE
  logic for aging or classification buckets. Use when adding filters to a report, making it
  interactive or prompt-driven, passing runtime parameters, or writing a CASE column for aging
  buckets and derived measures. Triggers: add a filter, is prompted, dashboard prompt, column
  prompt, named prompt, presentation variable, runtime parameter, prompt-driven report, aging
  buckets, CASE formula, bucket a column, as-of date prompt.
---

# Filter and parameterize an OTBI analysis

## When to use
- Adding filters to scope an analysis, or making it interactive with prompts.
- Building an As-of Date / Bank Account / Currency / Legal Entity prompt that drives one or many
  analyses.
- Writing a `CASE WHEN` column formula for aging buckets, status groups, or derived measures.
- Not for: choosing the subject area/columns first → see
  `oracle-otbi-skills:otbi-subject-area-selection`. For the overall build and where filters/prompts
  fit → see `oracle-otbi-skills:otbi-report-building`.

## Do it
1. **Filter to scope rows.** On the Criteria tab, add a filter on a selected column and pick an
   operator (is equal to, is between, is greater than, is in, is null, **is prompted**…). Filter the
   most selective columns first — **bank account and date** — to keep the live query small.
2. **Make a filter runtime-driven with "is prompted."** Set the filter operator to **is prompted**
   so it holds no fixed value; a prompt supplies the value when the report runs. This is what lets a
   dashboard prompt re-scope the analysis.
3. **Choose the prompt type for the job:**
   - **Column prompt** — a runtime selector bound to a column (dropdown, calendar, list…).
   - **Named / inline prompt** — built on the analysis's **Prompts** tab, local to that analysis.
   - **Dashboard prompt** — a reusable prompt on a dashboard page that drives **every** analysis
     whose matching filter is "is prompted." Use this to share one As-of Date / Bank Account /
     Currency / Legal Entity across a page.
4. **Pass values with variables where needed.** **Presentation variables** (set by a prompt) and
   **repository variables** can feed column formulas, filter values, and view/title text — e.g. show
   the selected As-of Date in a Title view. See `references/prompts-and-formulas.md`.
5. **Write CASE logic for buckets and derived columns.** In a column's formula editor, use
   `CASE WHEN … THEN … ELSE … END` to build aging buckets, status groupings, or computed measures.
   Aging pattern (bucket days between a statement date and the as-of date):
   ```
   CASE
     WHEN <days> <= 30 THEN '0-30'
     WHEN <days> <= 60 THEN '31-60'
     WHEN <days> <= 90 THEN '61-90'
     ELSE '90+'
   END
   ```
   Order the WHEN branches low-to-high so each row lands in exactly one bucket. More recipes:
   `references/prompts-and-formulas.md`.
6. **Test the binding.** Run the analysis (or the dashboard) and change each prompt to confirm the
   "is prompted" filters actually move the results, and that the buckets sum back to the unbucketed
   total.

## Why / learn
Filters, prompts, and formulas are three different levers and it helps to keep them straight. A
**filter** decides *which rows* the query returns. A **prompt** is a runtime input that *supplies a
filter's value* — "is prompted" is the hinge that connects them, telling the filter "wait for a value
at run time" instead of baking one in. A **column formula** decides *how a column is computed* before
it is grouped — which is why aging buckets belong in a formula (a derived attribute), not in a
filter. Presentation variables are the wiring that carries a prompt's chosen value into formulas and
titles so the report can *say* what it is showing. Building for prompts instead of hard-coded values
is what turns a one-off analysis into a reusable, self-service report: one dashboard prompt re-scopes
a whole page, and the same analysis serves every bank account and period without a rebuild.

## Common mistakes
- Hard-coding an account or date that should be a prompt → the report can't be reused; use "is prompted."
- Bucketing in a filter instead of a CASE column → you drop the other buckets. Bucket in a formula.
- Overlapping CASE branches (a `>=` and a `<=` that both catch a boundary) → rows double-count. Order
  branches low-to-high with a single comparison each.
- A dashboard prompt that doesn't drive an analysis → its filter wasn't set to "is prompted."
- Filtering on a non-selective column first → the live query still scans everything. Lead with account + date.
- Referencing a presentation variable no prompt sets → blank or default value at runtime.

## Tailor to your environment
Put your standard prompts and bucket definitions in `references/your-environment.md` (or
`references/your-environment.private.md`, git-ignored): your default As-of Date behavior, your aging
band boundaries (0-30/31-60/… or your policy's), the currency/LE prompt defaults, and any
presentation variables your titles rely on. **Never commit real account numbers or entity names.**
This skill then uses your bands and prompts instead of the generic examples.

## References
- references/prompts-and-formulas.md — prompt types, presentation/repository variables, and CASE/formula recipes (aging, status, derived measures)
- references/your-environment.md — your standard prompts and bucket bands (add when supplied)
