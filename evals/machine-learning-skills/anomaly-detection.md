# Evals — machine-learning-skills:anomaly-detection

## 1. Positive trigger (should load the skill)
> "We get thousands of vendor payments a week and want to automatically flag the unusual ones — odd
> amounts, off-hours, new counterparties — for review. We have almost no labeled fraud. What methods
> should I use and how do I set the threshold so we don't drown the team in alerts?"

Expected: skill loads; starts with robust statistical checks per field; goes multivariate with isolation
forest / LOF where fields interact; sets the threshold by the precision/recall trade-off and an alert
budget given the scarce labels; ranks and routes the top-N; and stresses that a flag is triage for
investigation, not a verdict, plus managing alert fatigue.

## 2. Near-miss (should NOT load this skill)
> "Match this month's bank statement to the GL and tell me which items are still outstanding."

Expected: this is mechanical reconciliation, not statistical anomaly detection. The
`cash-management-skills:bank-reconciliation` skill should handle it (this skill would only *rank* the
resulting breaks by unusualness). If this anomaly skill loads as the primary, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** picks statistical (robust z/IQR), time-series-residual, or unsupervised (isolation
  forest/LOF) methods appropriate to the data; sets a threshold via the precision/recall trade-off and an
  alert budget; ranks alerts; and plans for investigation and alert-fatigue management.
- **Teaches:** explains *why* an anomaly is "unusual, not wrong" (triage, not verdict), why labels are scarce
  so recall is usually unmeasurable, and why robust statistics beat mean/std when hunting outliers.
- **Safe:** never treats a flag as proof, never uses plain mean/std where outliers inflate the spread, and
  never ships a hard cutoff that swamps reviewers without ranking or a budget.
