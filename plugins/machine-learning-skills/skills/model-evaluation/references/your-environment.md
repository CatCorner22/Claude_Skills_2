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
- **Threshold policy:** <fixed | tuned to cost | tuned to an alert budget of N/day> — **chosen on which
  split?** <validation | CV folds; never test>
- **Baseline:** <naive | seasonal-naive | majority class | current rule>
- **Calibration needed?** <yes, decisions use the probability | no, ranking is enough>
- **Test-set size and positive count:** <rows; positives — the positives are what set the interval width>
- **Independent units in the test set:** <rows, or entities/time blocks if the same entity or period
  repeats> — this is the count to bootstrap over and to quote behind any interval
- **Smallest improvement worth shipping:** <e.g. +2pp recall — compare it to the metric's CI, not to zero>
- **Slices the decision touches:** <region, channel, product line, tenure, device, recent period, protected
  groups> — report the metric per slice with each slice's own n
- **Label source and known error rate:** <who/what assigns the label, from what evidence, at what time;
  measured agreement if any> — qualify it with
  `continuous-improvement-skills:measurement-systems-analysis`
