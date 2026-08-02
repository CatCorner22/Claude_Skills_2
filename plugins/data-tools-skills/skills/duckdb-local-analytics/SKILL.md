---
name: duckdb-local-analytics
description: >-
  Runs real SQL directly over local CSV, Parquet, and Excel files with DuckDB — no database
  server — for joins across files, aggregations on data too big for Excel, and repeatable
  analysis scripts, from the CLI or Python, persisting results back to files or a .duckdb
  database. Use when joining or aggregating local files with SQL, when a dataset chokes
  Excel/pandas memory, or when replacing a fragile chain of spreadsheet lookups with one query.
  Triggers: duckdb, query csv with sql, join csv files, sql on parquet, local sql, read_csv_auto,
  analyze large csv, sql without a database, parquet analytics, out of memory pandas.
---

# DuckDB local analytics

## When to use
- Joining, filtering, or aggregating CSV/Parquet/Excel files with SQL on your own machine —
  reconciliations across exports, million-row aggregations, repeatable analysis queries.
- Datasets that make Excel crawl or pandas run out of memory.
- Not for: SQL *language* skills (joins, windows, CTEs) → see
  `data-analytics-bi-skills:sql-for-analysts`. For getting messy files parseable in the first
  place → see `data-tools-skills:csv-and-flat-file-wrangling`.

## Do it
1. **Install and open.** `pip install duckdb` (Python) or the standalone CLI. In-memory for
   ad-hoc work (`duckdb.connect()`); a file (`duckdb.connect("analysis.duckdb")`) when you want
   tables to persist between sessions.
2. **Query files directly — they behave as tables:**

```sql
SELECT bank, count(*) AS n, sum(amount) AS total
FROM read_csv_auto('exports/payments_2026-06.csv')
GROUP BY bank ORDER BY total DESC;

-- Globs and Parquet work the same way; a year of files is one table:
SELECT * FROM read_parquet('data/tx_2026-*.parquet');
-- Excel sheets too:
SELECT * FROM read_xlsx('report.xlsx', sheet='Detail');
```

3. **Fix auto-detection where it guesses wrong** — the same landmines as any CSV load: force ID
   columns to text and declare formats instead of accepting the sniffers' guess:

```sql
SELECT * FROM read_csv('export.csv', header=true, delim=';',
    types={'account_id':'VARCHAR'}, dateformat='%d/%m/%Y');
```

4. **Join across files like tables** — this replaces the VLOOKUP chain:

```sql
CREATE OR REPLACE TABLE recon AS
SELECT s.line_id, s.amount AS stmt_amt, l.amount AS ledger_amt,
       coalesce(s.amount,0) - coalesce(l.amount,0) AS diff
FROM read_csv_auto('statement.csv') s
FULL OUTER JOIN read_csv_auto('ledger.csv') l USING (ref_no);
-- Inspect the unmatched sides before trusting any inner join:
SELECT count(*) FILTER (WHERE ledger_amt IS NULL) AS stmt_only,
       count(*) FILTER (WHERE stmt_amt IS NULL)  AS ledger_only FROM recon;
```

5. **Persist results where the next step needs them.** `COPY recon TO 'recon.parquet'` (compact,
   typed — the best interchange format), `COPY ... TO 'out.csv' (HEADER)` for spreadsheet users,
   or keep tables in the .duckdb file. In Python, `con.sql(q).df()` hands the result to pandas
   for plotting; `duckdb.sql("... FROM df")` queries an existing DataFrame with zero copying.
6. **Make the analysis a script, not a session.** Save the queries in a .sql file (CLI:
   `duckdb < analysis.sql`) or a small Python script; inputs are file paths, output is a file.
   Re-running the whole analysis on next month's export becomes one command.
   `references/duckdb-recipes.md` covers window-function recipes, larger-than-memory settings,
   and pandas interop.
7. **Sanity-check like always:** row counts per source, control totals, and the unmatched counts
   from any join — SQL makes wrong answers fast, too.

## Why / learn
DuckDB fills the gap between "too big for a spreadsheet" and "not worth a database server": an
in-process, columnar SQL engine, so the *files are the database* and the query is the analysis.
That inversion is the point — instead of importing data into a tool, you point the engine at the
data where it lies, which makes the workflow reproducible (paths + SQL text = the whole analysis)
and reviewable (a colleague reads one query instead of tracing formula chains across tabs). It's
fast for analytics because columnar execution reads only the columns a query touches — which is
also why Parquet (columnar on disk) is its natural partner and why converting a big CSV to
Parquet once pays back every subsequent query. And because it's still SQL over inferred schemas,
the flat-file disciplines carry over unchanged: declare types where inference can lie (IDs!),
and audit joins with unmatched counts, because a `FULL OUTER JOIN` is a reconciliation and the
NULL sides are your breaks.

## Common mistakes
- Letting `read_csv_auto` type an ID column numeric → leading zeros gone; force `VARCHAR` in `types=`.
- Loading a huge CSV into pandas first, then querying → query the file with DuckDB directly; pull only the result into pandas.
- Re-parsing the same giant CSV every query → convert once to Parquet, query that.
- Inner-joining exports without checking unmatched rows → silent row loss; full outer join + counts first.
- One-off interactive sessions for a monthly task → save the .sql/.py; next month is one command.
- Assuming it can't handle bigger-than-RAM data → it spills to disk; set `memory_limit`/`temp_directory` rather than giving up.

## Tailor to your environment
List your standard local datasets and queries in `references/your-environment.md` (real data
files in `references/*.local.*`, git-ignored): file locations, the Parquet conversions you keep,
and the recurring analysis scripts. **Never commit the data files themselves.**

## References
- references/duckdb-recipes.md — window functions, pivots, larger-than-memory settings, pandas/Parquet interop
- references/your-environment.md — your datasets, conversions, and saved analyses (fill in)
