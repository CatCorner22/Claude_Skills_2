# Your statistical-inference environment (sanitized template)

Fill this in with your real setup. If any value is sensitive (real metric names, client data, actual
test results), keep it in `your-environment.private.md` instead — that suffix is git-ignored. Commit
only sanitized, structural examples.

- **Decisions you routinely test:** <A/B tests, region-vs-region KPI, before/after a change>
- **Outcome types:** <numeric means | proportions/rates | counts in categories>
- **House conventions:** <α (e.g. 0.05), target power (e.g. 0.80), one- vs. two-sided default>
- **Minimum effect that matters (per metric):** <e.g. +0.5pp conversion, +$X order value>
- **Design:** <independent groups | paired / before-after | repeated measures>
- **Assumption reality:** <are observations independent? sample sizes? known skew?>
- **Multiplicity policy:** <how you handle many comparisons — Bonferroni, Benjamini–Hochberg, none>
- **Tool you test in:** <Python scipy/statsmodels | R | Excel | BI stats add-in>
- **Where results go:** <who decides on the result and what action follows>
