# Prompts, variables, and formulas (reference)

Companion to `otbi-analysis-filters`. Prompt types, the variables that carry values, and CASE recipes
for buckets and derived columns. Column names below are illustrative — confirm exact names against
your subject area's folders (they vary by area and release).

## Contents
- 1. Filter operators
- 2. Prompt types
- 3. Variables
- 4. CASE recipes
- 5. Notes

## 1. Filter operators
- Common: is equal to / is in, is not equal to, is between, is greater/less than, is null / is not
  null, is LIKE (pattern).
- **is prompted** — the filter carries no fixed value; a column or dashboard prompt supplies it at
  run time. Required on any column you want a dashboard prompt to drive.

## 2. Prompt types
- **Column prompt** — bound to a column; renders as a dropdown, calendar, list, etc. Good for a
  single selector.
- **Named / inline prompt** — created on the analysis's **Prompts** tab; travels with that analysis.
- **Dashboard prompt** — a reusable object placed on a dashboard page; drives **every** analysis on
  the page whose matching filter is "is prompted." Use for a shared As-of Date, Bank Account,
  Currency, or Legal Entity.

## 3. Variables
- **Presentation variable** — set by a prompt; reference it in filters, column formulas, and view
  text (e.g. a Title view that prints the chosen As-of Date). Blank if no prompt sets it.
- **Repository variable** — defined in the repository/metadata (e.g. a current-period value);
  available to formulas and titles without a prompt.
- Use variables to keep one source of truth: the prompt sets the value, formulas and titles read it.

## 4. CASE recipes
Aging buckets (days between statement date and as-of date):
```
CASE
  WHEN <days> <= 30 THEN '0-30'
  WHEN <days> <= 60 THEN '31-60'
  WHEN <days> <= 90 THEN '61-90'
  ELSE '90+'
END
```
Status grouping:
```
CASE
  WHEN "Bank Statement"."Reconciliation Status" = 'Reconciled' THEN 'Reconciled'
  ELSE 'Open'
END
```
Derived / conditional measure (flag unreconciled as 1 to sum a count):
```
CASE WHEN "Bank Statement"."Reconciliation Status" <> 'Reconciled' THEN 1 ELSE 0 END
```
- Order WHEN branches low-to-high with a single comparison each so every row lands in exactly one
  bucket. Use the real folder/column names from your subject area (names above are illustrative).

## 5. Notes
- Bucketing belongs in a **column formula**, not a filter — a filter drops the other buckets.
- After adding a bucket column, confirm the buckets sum back to the unbucketed total.
- Confirm exact column names against your subject area's folders; they vary by area and release.
