---
name: sql-for-analysts
description: >-
  Writes, reviews, and optimizes analytical SQL — joins, GROUP BY aggregation, window functions,
  CTEs, subqueries, and date/time handling — with a working sense of performance (grain,
  sargability, indexing). Use when turning a business question into a query for a report or
  analysis, adding window logic like running totals or rankings, or reviewing a query for
  correctness and speed. Triggers: SQL, query, write a query, join, GROUP BY, aggregate, window
  function, OVER, PARTITION BY, running total, moving average, rank, lag, lead, CTE, subquery,
  QUALIFY, slow query, optimize query, group by grain.
---

# SQL for analysts

## When to use
- Translating a business question into an analytical query (aggregations, trends, rankings, cohorts) against a warehouse or database.
- Adding window functions (running totals, moving averages, rank, period-over-period) or restructuring a query with CTEs.
- Reviewing a query for correctness (grain, join fan-out, filter placement) or making a slow one faster.
- Not for: choosing between OTBI/BI Publisher and hand-written SQL in Oracle Fusion → see
  `oracle-otbi-skills:otbi-subject-area-selection`. For profiling a dataset before you query it → see
  `data-analytics-bi-skills:exploratory-data-analysis`.

## Do it
1. **State the grain of the answer first.** Write down what one output row represents (one
   customer-month, one order, one product). Those grain columns *are* your `GROUP BY`. A wrong grain
   is the number-one cause of wrong numbers.
2. **Reason in logical query order, not top-to-bottom.** SQL evaluates `FROM/JOIN → WHERE → GROUP BY
   → HAVING → window functions → SELECT → QUALIFY → ORDER BY → LIMIT`. This is why a `SELECT` alias
   can't be used in `WHERE`, and why a window function can't sit in `WHERE`.
3. **Pick the join type deliberately.** `INNER` drops non-matches; `LEFT` keeps every left row.
   Watch for many-to-many joins that fan out and multiply rows — they silently inflate every `SUM`
   and `COUNT`. Compare row counts before and after each join to catch it.
4. **Aggregate vs. window — choose by output shape.** Use `GROUP BY` when you want *fewer* rows (one
   per group). Use a window (`OVER (PARTITION BY … ORDER BY …)`) when you want a per-group
   calculation but keep *every* row: running totals with `SUM(...) OVER`, ranking with
   `ROW_NUMBER/RANK/DENSE_RANK`, period comparisons with `LAG/LEAD`.
5. **Filter in the right clause.** `WHERE` filters raw rows before grouping (fast, index-friendly).
   `HAVING` filters after aggregation, on aggregates. `QUALIFY` (Snowflake/BigQuery/Databricks)
   filters on window results — e.g. keep the latest row per key with
   `QUALIFY ROW_NUMBER() OVER (PARTITION BY id ORDER BY ts DESC) = 1`. On dialects without `QUALIFY`,
   wrap the window in a CTE and filter outside it.
6. **Layer with CTEs for readability.** Break a gnarly query into named `WITH` steps (stage →
   aggregate → join → final). Prefer CTEs over deeply nested subqueries for anything you'd re-read.
7. **Handle dates as half-open ranges.** Filter with `ts >= '2026-01-01' AND ts < '2026-02-01'`
   rather than `WHERE FUNC(ts) = …`; bucket with `DATE_TRUNC`; be explicit about time zone. This
   both avoids boundary bugs and stays sargable (next step).
8. **Sanity-check, then tune.** Validate row counts and one or two known totals against a trusted
   source. For speed: keep predicates **sargable** (compare the bare column, not `WHERE UPPER(col)=…`),
   filter early, select only needed columns, and ensure join/filter keys are indexed or clustered.
   See `references/query-patterns.md` for copy-ready patterns and dialect notes.

## Why / learn
The core shift is to **think in sets, not row-by-row loops**. SQL is declarative: you describe the
shape of the result and the engine figures out how to build it, so your job is to get two things
right — the **grain** (what one row means) and the **predicates** (which rows and which clause).
Grain drives correctness: a join that fans out to a finer grain than your `GROUP BY` expects will
double-count, and no amount of tuning fixes a query that's answering the wrong question. Predicates
drive both correctness and speed — `WHERE` runs before aggregation on raw rows, `HAVING` after, and
window functions in between, which is the whole reason the logical order matters. Aggregation and
windows are the same idea (compute over a group) with a different output contract: collapse to one
row, or annotate every row. Sargability is just the physical echo of the same principle — when you
leave a column bare on one side of a comparison, the engine can seek an index or partition instead of
scanning everything. Master grain, clause placement, and set thinking, and every dialect's syntax
becomes a detail.

## Common mistakes
- Not fixing the grain first → double-counted `SUM`s from a fan-out join. Decide what one row means, then join to it.
- `SELECT *` with `GROUP BY` a few columns → wrong or non-deterministic results. Group by exactly the grain; aggregate the rest.
- Putting a window function in `WHERE` → error or wrong logic. Filter windows with `QUALIFY` or a wrapping CTE.
- Mixing up `WHERE` and `HAVING` → `WHERE` is pre-aggregation on rows, `HAVING` is post-aggregation on aggregates.
- Wrapping the filtered column in a function (`WHERE DATE(ts)=…`) → kills index use. Use a half-open range on the bare column.
- `COUNT(col)` when you meant `COUNT(*)` → `COUNT(col)` skips NULLs. Know which you want.
- `NOT IN (subquery)` with a NULL in the list → returns no rows. Prefer `NOT EXISTS`.

## Tailor to your environment
Record your setup in `references/your-environment.md` (keep anything sensitive — connection strings,
real table/column names, sample data — in `your-environment.private.md`, which is git-ignored). Note
your **SQL dialect** (Postgres, Snowflake, BigQuery, Oracle, SQL Server — they differ on `QUALIFY`,
date functions, and `LIMIT`/`FETCH`), your core tables and their grain, standard join keys, and any
naming or partitioning conventions. This skill then maps its generic steps onto your schema. In
Oracle Fusion, prefer the subject-area/OTBI path where it exists — see
`oracle-otbi-skills:otbi-subject-area-selection`.

## References
- references/query-patterns.md — window-function, QUALIFY, date, and sargability patterns with dialect notes
- references/your-environment.md — your dialect, tables, grain, and conventions (add when supplied)
