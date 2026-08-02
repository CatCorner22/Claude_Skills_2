---
name: python-for-analysts
description: >-
  Writes clean, reproducible Python for data work and automation — virtual environments and
  pinned dependencies, script vs notebook structure, pandas essentials (load, select, filter,
  groupby, merge, write), small functions, and basic error handling and logging. Use when
  scripting an analysis, automating a repetitive task, cleaning up messy analysis code, or
  setting up a Python project so it runs the same way twice. Triggers: python, pandas, script,
  automate, virtualenv, notebook, dataframe, read csv, python for analysis.
---

# Python for analysts

## When to use
- Scripting a one-off or recurring analysis, or automating a manual data chore.
- Setting up a Python project so a colleague (or future you) can reproduce the result.
- Cleaning up notebook-grade code into something readable and re-runnable.
- Not for: the *statistics/transform logic* of cleaning a dataset → see
  `data-analytics-bi-skills:data-cleaning`; querying a database instead of a file → see
  `data-analytics-bi-skills:sql-for-analysts`.

## Do it
1. **Create an isolated environment and pin what you install.** From the project folder:
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   python -m pip install -U pip
   pip install pandas openpyxl      # add what you actually import
   pip freeze > requirements.txt    # pin exact versions so it reproduces
   ```
   Add `.venv/` to `.gitignore`. Anyone can rebuild with `pip install -r requirements.txt`.
   (Tooling varies — `uv`, Poetry, and conda solve the same problem; confirm your team's choice.)
2. **Structure a script so it can be read and re-run.** Imports at top, logic in small named
   functions, one guarded entry point:
   ```python
   from pathlib import Path
   import argparse, logging
   import pandas as pd

   def load(path: Path) -> pd.DataFrame:
       return pd.read_csv(path, parse_dates=["date"])

   def summarize(df: pd.DataFrame) -> pd.DataFrame:
       return df.groupby("account", as_index=False)["amount"].sum()

   def main(in_path: Path, out_path: Path) -> None:
       logging.info("reading %s", in_path)
       out = summarize(load(in_path))
       out.to_csv(out_path, index=False)
       logging.info("wrote %d rows to %s", len(out), out_path)

   if __name__ == "__main__":
       logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
       p = argparse.ArgumentParser()
       p.add_argument("in_path", type=Path); p.add_argument("out_path", type=Path)
       a = p.parse_args()
       main(a.in_path, a.out_path)
   ```
   Use `pathlib.Path` for paths (portable), `logging` instead of `print`, and parameters instead
   of hard-coded file names.
3. **Do the data work with a small pandas vocabulary** — load, inspect, select, filter, derive,
   group, merge, write. The recurring operations and their gotchas are in
   `references/pandas-essentials.md`. Two rules that prevent most bugs: pass `parse_dates=` and
   check `df.dtypes` right after loading, and assign with `.loc[mask, col] = ...` (not chained
   indexing) to avoid `SettingWithCopyWarning`.
4. **Choose notebook vs script deliberately.** Notebook for exploration and narrative; script for
   anything scheduled, reused, or handed off. Before trusting a notebook result, **Restart & Run
   All** — out-of-order cells hide state and are the #1 source of "works for me" irreproducibility.
   Once logic is stable, lift it into functions in a `.py` module the notebook imports.
5. **Handle errors loudly and specifically.** Validate inputs early (file exists, expected columns
   present), catch the *specific* exception you can handle, and let everything else raise with a
   clear message. Never `except: pass` — a silently swallowed error becomes a wrong number.
6. **Verify before you trust it.** Re-run on the same input and confirm identical output; check row
   counts and a known total against a source you trust; run it once in a fresh clone of the repo
   (or a clean environment) to prove the pins and paths are complete.

## Why / learn
The job of analysis code is not to be clever — it is to produce a number someone will act on, and
to still produce the *same* number next month when you or a teammate re-run it. That is why
**reproducibility and readability beat one-liners**: code is read far more often than it is written,
and an analysis you cannot re-run is an analysis you cannot defend. A pinned virtual environment
removes the "it worked on my machine" failure by making the dependency set explicit and rebuildable.
Functions with names turn a wall of statements into steps a reviewer can follow and a tester can
check one at a time. `logging` over `print` gives you a timestamped trail when a scheduled job fails
at 2 a.m. And the notebook discipline — restart-and-run-all — exists because a notebook's *visible*
output can silently disagree with the code that would actually run top to bottom. Optimize for the
next person to open the file; most of the time that person is you, three months from now, with no
memory of what `df2` meant.

## Common mistakes
- Installing packages globally with no `requirements.txt` → nobody can reproduce it. Use a venv + pins.
- Chained indexing (`df[df.x>0]["y"] = 1`) → `SettingWithCopyWarning`, silent no-op. Use `.loc[mask, "y"]`.
- Trusting notebook output run out of order → phantom results. Restart & Run All before believing it.
- `except: pass` or bare `except` → hides the bug that changes the answer. Catch specific exceptions.
- Hard-coded absolute paths and magic numbers → breaks on the next machine. Use `pathlib` + parameters.
- `inplace=True` everywhere and 200-line cells → unreadable and hard to test. Prefer returning values from small functions.

## Tailor to your environment
Record your real setup in `references/your-environment.md`: your Python version, package manager
(pip/uv/Poetry/conda), where source files land, and the scheduler that runs your scripts. **Never
commit real data or credentials** — put anything sensitive (file paths with client names, sample
rows, connection strings) in `references/your-environment.private.md`, which `.gitignore` keeps out
of git. This skill then adapts its generic structure to your stack.

## References
- references/pandas-essentials.md — load, inspect, select, filter, derive, groupby, merge, write, with gotchas
- references/your-environment.md — your Python version, tooling, paths, and scheduler (fill in)
