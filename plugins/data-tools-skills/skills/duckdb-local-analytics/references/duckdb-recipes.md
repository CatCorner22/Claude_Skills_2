# DuckDB recipes (reference)

## Contents
- Window functions for analyst tasks
- Pivot / unpivot
- Larger-than-memory
- Parquet and pandas interop
- CLI niceties

## Window functions for analyst tasks
```sql
-- Running balance per account
SELECT account_id, posting_date, amount,
       sum(amount) OVER (PARTITION BY account_id ORDER BY posting_date
                         ROWS UNBOUNDED PRECEDING) AS running_balance
FROM read_parquet('tx.parquet');

-- Latest row per key (dedupe to most recent)
SELECT * FROM (
  SELECT *, row_number() OVER (PARTITION BY invoice_no ORDER BY updated_at DESC) AS rn
  FROM read_csv_auto('invoices.csv')
) WHERE rn = 1;

-- Month-over-month change
SELECT month, total, total - lag(total) OVER (ORDER BY month) AS mom_change
FROM (SELECT date_trunc('month', posting_date) AS month, sum(amount) AS total
      FROM read_parquet('tx.parquet') GROUP BY 1);
```

## Pivot / unpivot
```sql
PIVOT (SELECT cost_center, month, amount FROM read_csv_auto('spend.csv'))
ON month USING sum(amount) GROUP BY cost_center;

UNPIVOT wide_table ON COLUMNS(* EXCLUDE (account)) INTO NAME month VALUE amount;
```

## Larger-than-memory
```sql
SET memory_limit = '8GB';
SET temp_directory = '/path/with/space';   -- spill location for big sorts/joins
```
- Convert big CSVs once: `COPY (FROM read_csv_auto('big.csv')) TO 'big.parquet';`
- Filter early and select only needed columns — columnar reads reward it.
- `EXPLAIN` shows the plan if a query is unexpectedly slow.

## Parquet and pandas interop
```python
import duckdb, pandas as pd
con = duckdb.connect()
df = con.sql("SELECT ... FROM read_parquet('tx.parquet')").df()  # result → pandas
con.sql("CREATE TABLE t AS FROM df")                              # pandas df → table (zero-copy read)
con.sql("COPY t TO 'out.parquet'")
```
Parquet preserves types (no re-inference next read), compresses well, and is the right handoff
format between scripts. CSV is for humans and spreadsheets at the very end.

## CLI niceties
- `duckdb analysis.duckdb` opens a persistent database; `.tables`, `.schema t` inspect it.
- `.mode markdown` / `.mode csv` set output format; `.read analysis.sql` runs a script.
- `duckdb -c "SELECT count(*) FROM read_csv_auto('f.csv')"` for one-liners in shell pipelines.
