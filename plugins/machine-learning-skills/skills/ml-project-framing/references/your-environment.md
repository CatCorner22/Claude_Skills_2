# Your ML problem (sanitized template)

Fill this in with your real problem. If any value is sensitive (actual figures, account identifiers,
sample rows, internal system names), keep it in `your-environment.private.md` instead — that suffix is
git-ignored. Commit only sanitized, structural examples.

- **Decision & owner:** <who acts on the prediction, and what action changes>
- **Cost of a wrong call:** <false positive vs false negative, or over- vs under-forecast, in business terms>
- **Target (label):** <exactly what you predict; number / category / event-in-window>
- **How the label is measured:** <window, cutoff, and the rule that decides the outcome>
- **Task type:** <regression | classification | forecasting | anomaly | ranking>
- **Unit of prediction (grain):** <one row = one …>
- **Prediction time / cadence:** <the moment a prediction is made; how often>
- **Candidate features (source → when available):**
  - `<feature>` — from <system> — known at <time relative to prediction>
  - `<feature>` — from <system> — known at <time>
- **Evaluation metric (tied to the decision):** <metric + why it matches the cost of errors>
- **Baseline to beat:** <last value | seasonal-naive | current heuristic | majority class>
- **Data availability:** <rows/history span, refresh cadence, known gaps, label coverage>
- **Known risks:** <leakage suspects, distribution shift, label noise, small sample>
