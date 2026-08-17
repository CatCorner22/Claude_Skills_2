# Your statistical-inference environment (sanitized template)

Fill this in with your real setup. If any value is sensitive (real metric names, client data, actual
test results), keep it in `your-environment.private.md` instead — that suffix is git-ignored. Commit
only sanitized, structural examples.

- **Decisions you routinely test:** <A/B tests, region-vs-region KPI, before/after a change>
- **Outcome types:** <numeric means | proportions/rates | counts in categories>
- **Estimand per decision:** <does this decision ride on a mean that rolls up to a total (revenue, cost,
  hours), a median, a rate, or "which group tends to be larger"? This picks the test — and the conclusion
  sentence you are allowed to write.>
- **Validity gate for experimental readouts:** <who supplies assignment counts for the SRM chi-square;
  where the pre-committed stopping rule is recorded; required exposure window; the randomization unit your
  analysis must aggregate to> — design side lives in `data-analytics-bi-skills:ab-test-design`
- **Resampling defaults:** <bootstrap replicates (e.g. 10,000), CI type (percentile/BCa), permutation
  replicates, and whether resampling must respect clusters/pairs>
- **House conventions:** <α (e.g. 0.05), target power (e.g. 0.80), one- vs. two-sided default>
- **Minimum effect that matters (per metric):** <e.g. +0.5pp conversion, +$X order value>
- **Design:** <independent groups | paired / before-after | repeated measures>
- **Assumption reality:** <are observations independent? sample sizes? known skew?>
- **Multiplicity policy:** <how you handle many comparisons — Bonferroni, Benjamini–Hochberg, none>
- **Tool you test in:** <Python scipy/statsmodels | R | Excel | BI stats add-in>
- **Where results go:** <who decides on the result and what action follows>
