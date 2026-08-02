# Your evaluation setup (sanitized template)

Fill this in with your real setup. If any value is sensitive (real cost figures, label rates, sample
rows, business identifiers), keep it in `your-environment.private.md` instead — that suffix is
git-ignored. Commit only sanitized, structural examples.

- **Data shape:** <IID | temporal | grouped (repeats per entity) | panel>
- **Split strategy:** <holdout | stratified k-fold | time-series CV | grouped k-fold>
- **Task & target:** <regression | classification; what you predict>
- **Class balance (if classifying):** <e.g. 2% positive>
- **Cost of a false positive:** <business consequence / $>
- **Cost of a false negative:** <business consequence / $>
- **Decision metric:** <the metric your decision truly cares about, and why>
- **Threshold policy:** <fixed | tuned to cost | tuned to an alert budget of N/day>
- **Baseline:** <naive | seasonal-naive | majority class | current rule>
- **Calibration needed?** <yes, decisions use the probability | no, ranking is enough>
