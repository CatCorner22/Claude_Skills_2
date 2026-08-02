# Evals — coding-agent-skills:python-for-analysts

## 1. Positive trigger (should load the skill)
> "I have a monthly CSV of transactions. Write me a Python script that reads it, sums amounts by
> account, and writes the result out — and set it up so a coworker can actually reproduce it."

Expected: skill loads; creates a venv + pinned `requirements.txt`; writes a script with imports at
top, small functions, a `if __name__ == "__main__":` entry point, `pathlib` paths, and `logging`;
uses `read_csv(parse_dates=...)` then `groupby(...).sum()` then `to_csv(index=False)`; notes how to
verify (row counts / a known total, fresh-environment re-run).

## 2. Near-miss (should NOT load this skill)
> "What's the right way to decide which rows are true duplicates versus legitimate repeat
> transactions when cleaning a dataset?"

Expected: this is data-cleaning *judgment* (dedup logic), handled by
`data-analytics-bi-skills:data-cleaning`, not Python project structure. If this skill loads instead,
tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** produces a runnable script + reproducible environment (pinned deps), uses the
  right pandas calls at the right grain, and states how to check the output is correct.
- **Teaches:** explains why reproducibility and readability beat clever one-liners — pinned envs,
  named functions, restart-and-run-all for notebooks, logging over print.
- **Safe:** no swallowed exceptions, no chained-index assignment, no hard-coded absolute paths or
  committed secrets.
