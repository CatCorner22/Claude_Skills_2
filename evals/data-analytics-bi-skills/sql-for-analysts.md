# Evals — data-analytics-bi-skills:sql-for-analysts

## 1. Positive trigger (should load the skill)
> "I have an `orders` table. Write me a SQL query that shows each customer's monthly revenue and a
> running total of their revenue over time, and rank customers by total spend."

Expected: skill loads; fixes the grain (customer-month); uses `GROUP BY` for monthly revenue and a
window function (`SUM(...) OVER (PARTITION BY customer ORDER BY month)`) for the running total plus
`RANK/DENSE_RANK` for the ranking; notes the join/fan-out and date-range cautions.

## 2. Near-miss (should NOT load this skill)
> "In Oracle Fusion, which subject area should I use to report on cash management transactions in
> OTBI?"

Expected: this is subject-area selection for OTBI, not hand-written SQL — the
`oracle-otbi-skills:otbi-subject-area-selection` skill should handle it. If this SQL skill loads,
tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** produces a correct query at the stated grain, uses `GROUP BY` vs. window
  functions appropriately, places filters in the right clause (`WHERE`/`HAVING`/`QUALIFY`), and
  handles dates as half-open ranges.
- **Teaches:** explains *why* grain drives correctness (fan-out/double-counting), the logical query
  order, and what sargability means for speed — not just the syntax.
- **Safe:** validates row counts / a known total, flags dialect differences (e.g. `QUALIFY`
  availability), and avoids `NOT IN` with possible NULLs.
