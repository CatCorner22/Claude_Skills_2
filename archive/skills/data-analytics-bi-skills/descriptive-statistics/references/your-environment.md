# Your descriptive-statistics environment (sanitized template)

Fill this in with your real setup. If any value is sensitive (actual column names, client-specific
thresholds, sample rows), keep it in `your-environment.private.md` instead — that suffix is
git-ignored. Commit only sanitized, structural examples.

- **Variables you routinely summarize:** <e.g. order value, days-to-pay, ticket resolution time>
- **Expected shape of each:** <which are right-skewed by nature (amounts, durations) vs. symmetric>
- **Default reporting convention:** <mean + SD | median + IQR | both>
- **Percentile / quartile method:** <Excel INC | Excel EXC | pandas/numpy linear | SQL PERCENTILE_CONT>
- **Rounding / units:** <decimals, currency, thousands vs. millions>
- **Sample vs. population:** <almost always sample (n − 1) unless you truly hold the full population>
- **Tool you compute in:** <SQL | pandas/Python | Excel | BI tool>
- **Where the summary goes:** <who reads it and what decision it feeds>
