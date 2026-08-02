# Methods menu & hypothesis log

## Contents
- Method menu by material type
- Depth-control heuristics
- Hypothesis log template
- Confidence calibration language

## Method menu by material type

### Tabular / numerical data
- Profile first (shape, types, grain, missingness) — or hand off to
  `data-analytics-bi-skills:exploratory-data-analysis` for a full profile.
- Descriptive stats & distributions; robust measures under skew/outliers.
- Correlations and cross-tabs; segmentation by the dimensions that matter.
- Formal tests (t/chi-square/ANOVA) via `data-analytics-bi-skills:statistical-inference`.
- Simple models (regression, trees) when a relationship needs quantifying —
  see `machine-learning-skills:supervised-modeling`.
- Time series: decomposition, changepoints, seasonality —
  see `machine-learning-skills:time-series-forecasting`.

### Text / documents
- Thematic analysis: recurring topics, coded passages.
- Claim–evidence mapping: each claim → its support → strength of that support.
- Discourse/rhetorical structure: how the argument is built, where it's weakest.
- Stakeholder perspectives: reread the same material from each party's interest.
- Contradiction detection: internal inconsistencies, version drift across documents.

### Multi-lens passes (either material)
- **Adversarial:** what would a skeptic attack first?
- **Causal:** what would have to be true for X to cause Y? What else explains it?
- **Comparative:** against a benchmark, a prior period, a peer.
- **Systems:** feedback loops, incentives, second-order effects.
- **Triangulation:** do the quantitative and qualitative reads agree? Where they diverge is
  usually the finding.

## Depth-control heuristics
- High uncertainty → broad and shallow first; commit depth only after the map exists.
- A sub-question deserves depth in proportion to how much its answer changes the conclusion.
- Three consecutive digs with no belief change → surface and re-plan.
- Before each dig, ask: "what result would change my answer?" If none would, skip it.

## Hypothesis log template
```markdown
| # | Hypothesis | Prior | Test | Result | Updated belief |
|---|-----------|-------|------|--------|----------------|
| H1 | <candidate explanation> | plausible | <query/computation/check> | <evidence> | supported / weakened / dead |
| H2 | <rival explanation> | ... | ... | ... | ... |
```
Rules: always log at least one rival; record dead hypotheses (they're findings too);
the test column must name something executable, not "look into it."

## Confidence calibration language
- **High:** multiple independent lines of evidence agree; rivals tested and ruled out.
- **Moderate:** consistent evidence, but a plausible rival remains untested.
- **Low:** single source or untested assumption load-bearing; say what would raise it.
Always attach the *because* and the *unless*.
