# Your EDA environment (sanitized template)

Fill this in with your real setup. If any value is sensitive (actual column names, sample rows,
client-specific thresholds), keep it in `your-environment.private.md` instead — that suffix is
git-ignored. Commit only sanitized, structural examples.

- **Typical data sources / formats:** <warehouse tables | CSV extracts | Excel | API pulls>
- **Tools you profile with:** <SQL, pandas/Python, Excel, BI tool data panel>
- **Common tables and their grain:** <table → one row per …>
- **Domain validity rules:**
  - <e.g. amount ≥ 0>
  - <e.g. status ∈ {open, closed, void}>
  - <e.g. dates fall within the fiscal calendar>
- **Known data-quality gotchas:** <late-arriving data, timezone of timestamps, placeholder dates>
- **Outlier thresholds you use:** <IQR fence | z>3 | domain caps>
- **Where the memo goes:** <who reads the data-quality findings and decides next steps>
