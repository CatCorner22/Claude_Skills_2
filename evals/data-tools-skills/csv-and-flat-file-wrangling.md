# Evals — data-tools-skills:csv-and-flat-file-wrangling

## 1. Positive trigger (should load the skill)
> "This bank export CSV loads with garbled é characters, the account numbers lost their leading
> zeros, and some rows shift columns. Fix the load."

Expected: skill loads; inspects raw bytes before parsing; declares encoding (cp1252 vs
utf-8-sig), `dtype="string"` for IDs, diagnoses shifted columns as unquoted delimiters;
validates the parse with row counts and a control total.

## 2. Near-miss (should NOT load this skill)
> "The file loads fine — now dedupe these customer records and handle the missing values and
> outliers."

Expected: post-parse cleaning — `data-analytics-bi-skills:data-cleaning`. If this skill loads,
sharpen the parse/ingest framing.

## 2b. Near-miss (scale guard)
> "I have 40 GB of CSVs and just need group-by totals across all of them — pandas runs out of
> memory."

Expected: SQL-over-files analytics — `data-tools-skills:duckdb-local-analytics`. This skill may
be *referenced* for the type-declaration discipline, but the task belongs to DuckDB; if this
skill loads as primary, sharpen the parse-vs-analytics boundary.

## 3. Quality rubric
A good response:
- **Does the task:** produces an explicit `read_csv` call (encoding, sep, dtypes, dates,
  na_values) that parses correctly, plus schema/count/total validation.
- **Teaches:** that a flat file has no schema so every load is declared interpretation; why IDs
  are strings (the numeric-coercion/leading-zero hazard destroys join keys silently); the
  outer-join-with-indicator audit before any merge decision.
- **Routes:** hands post-parse cleaning to `data-analytics-bi-skills:data-cleaning`, oversized
  or join-heavy work to `data-tools-skills:duckdb-local-analytics`, script hardening to
  `coding-agent-skills:python-for-analysts`, and raw/processed file discipline to
  `data-tools-skills:data-file-hygiene` where those seams appear.
- **Safe:** never "fixes" encoding by trial-and-error until errors vanish; hardens recurring
  feeds to fail loudly on layout changes; no real bank/customer exports in examples.
