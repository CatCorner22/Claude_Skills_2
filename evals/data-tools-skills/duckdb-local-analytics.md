# Evals — data-tools-skills:duckdb-local-analytics

## 1. Positive trigger (should load the skill)
> "I have a 4-million-row transactions CSV and a ledger extract — Excel dies and pandas eats
> all my RAM. I need to join them and total differences by account."

Expected: skill loads; queries the files directly with DuckDB (`read_csv_auto` with forced
VARCHAR IDs), full outer join with unmatched-count audit, converts the big CSV to Parquet once,
persists results, and packages the analysis as a rerunnable script.

## 2. Near-miss (should NOT load this skill)
> "Explain window functions vs GROUP BY and when to use a CTE."

Expected: SQL language teaching — `data-analytics-bi-skills:sql-for-analysts`. If this skill
loads, tighten the local-files/engine framing.

## 3. Quality rubric
A good response:
- **Does the task:** working SQL over the actual files, join audited via unmatched counts,
  results persisted (Parquet/CSV) and reproducible from a saved script.
- **Teaches:** files-are-the-database inversion, why columnar + Parquet pays off, and that
  flat-file disciplines (typed IDs, join audits) carry over unchanged.
- **Safe:** doesn't load everything into pandas first, doesn't trust `read_csv_auto` typing on
  IDs, and mentions `memory_limit`/spill rather than declaring big data impossible.
