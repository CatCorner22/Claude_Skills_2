# Analytical SQL patterns (reference)

Copy-ready patterns for the most common analyst tasks. Adjust identifiers and dialect syntax.

## Contents
- Window functions (running total, moving average, rank, period-over-period)
- Latest-row-per-key (dedup)
- Aggregation vs. window side by side
- Date/time handling
- Sargability and performance
- Dialect quick notes

## Window functions
```sql
SELECT
  account_id,
  month,
  amount,
  SUM(amount)  OVER (PARTITION BY account_id ORDER BY month
                     ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)      AS running_total,
  AVG(amount)  OVER (PARTITION BY account_id ORDER BY month
                     ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)              AS moving_avg_3m,
  RANK()       OVER (PARTITION BY account_id ORDER BY amount DESC)          AS amount_rank,
  LAG(amount)  OVER (PARTITION BY account_id ORDER BY month)                AS prior_month,
  amount - LAG(amount) OVER (PARTITION BY account_id ORDER BY month)        AS mom_change
FROM monthly_activity;
```
- `ROW_NUMBER` = no ties; `RANK` = ties share a rank and leave gaps; `DENSE_RANK` = ties share, no gaps.
- Default frame with `ORDER BY` is `RANGE UNBOUNDED PRECEDING` — for a true running total, state
  `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` explicitly to avoid tied-row surprises.

## Latest row per key (deduplication)
```sql
-- Dialects with QUALIFY (Snowflake, BigQuery, Databricks):
SELECT * FROM events
QUALIFY ROW_NUMBER() OVER (PARTITION BY entity_id ORDER BY updated_at DESC) = 1;

-- Portable version (Postgres, Oracle, SQL Server): wrap in a CTE, filter outside.
WITH ranked AS (
  SELECT e.*,
         ROW_NUMBER() OVER (PARTITION BY entity_id ORDER BY updated_at DESC) AS rn
  FROM events e
)
SELECT * FROM ranked WHERE rn = 1;
```

## Aggregation vs. window, side by side
```sql
-- GROUP BY: one row per customer (collapses rows)
SELECT customer_id, COUNT(*) AS orders, SUM(net_amount) AS revenue
FROM orders GROUP BY customer_id;

-- Window: keep every order, add the customer total alongside it
SELECT order_id, customer_id, net_amount,
       SUM(net_amount) OVER (PARTITION BY customer_id) AS customer_revenue
FROM orders;
```

## Date/time handling
- Half-open range (safe across timestamp precision, DST, and index use):
  `WHERE ts >= DATE '2026-01-01' AND ts < DATE '2026-02-01'`.
- Bucket to a grain: `DATE_TRUNC('month', ts)` (Postgres/Snowflake/BigQuery),
  `TRUNC(ts,'MM')` (Oracle), `DATEFROMPARTS`/`DATETRUNC` (SQL Server 2022+).
- Prefer storing/comparing in UTC and converting for display; state the zone when it matters.
- Avoid `WHERE YEAR(ts)=2026` or `WHERE DATE(ts)=…` — both wrap the column and disable index seeks.

## Sargability and performance
- **Sargable** = the predicate can use an index/partition. Keep the filtered column bare on one side:
  `col = value`, `col >= a AND col < b`, `col IN (...)`. Non-sargable: `FUNC(col) = value`,
  `col + 1 = value`, leading-wildcard `LIKE '%x'`.
- Filter and aggregate as early as possible; join on already-reduced sets.
- Select only needed columns (helps columnar stores and covering indexes).
- Beware fan-out: a join to a finer grain multiplies rows. Aggregate the finer table to the target
  grain in a CTE *before* joining, or use `COUNT(DISTINCT …)`.
- `EXISTS`/`NOT EXISTS` is usually safer and faster than `IN`/`NOT IN` on subqueries, and is
  NULL-safe (`NOT IN` with a NULL returns no rows).

## Dialect quick notes
- **QUALIFY**: Snowflake, BigQuery, Databricks, Teradata — yes. Postgres, MySQL, SQL Server, Oracle — no (use a CTE).
- **Row limit**: `LIMIT n` (Postgres/MySQL/Snowflake/BigQuery), `FETCH FIRST n ROWS ONLY` (Oracle/DB2/SQL Server), `TOP n` (SQL Server).
- **String concat**: `||` (Postgres/Oracle/Snowflake), `CONCAT()` everywhere, `+` (SQL Server).
- **NULL-safe default**: `COALESCE(x, 0)` is portable; `NVL` is Oracle-only, `ISNULL` is SQL Server-only.
