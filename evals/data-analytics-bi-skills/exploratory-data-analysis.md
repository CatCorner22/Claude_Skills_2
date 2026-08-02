# Evals — data-analytics-bi-skills:exploratory-data-analysis

## 1. Positive trigger (should load the skill)
> "I just got a CSV of 200k transactions I've never seen before. Before I build anything, how should
> I explore it — distributions, missing values, outliers, that kind of thing?"

Expected: skill loads; starts from the question/grain; profiles shape, types, and missingness; goes
univariate (mean vs. median, spread, histograms) then bivariate (correlation, cross-tabs); flags but
investigates outliers; ends with a data-quality memo and a handoff to cleaning.

## 2. Near-miss (should NOT load this skill)
> "My address column has `NY`, `N.Y.`, and `New York` all mixed together — write me the steps to
> standardize and dedupe it."

Expected: this is a cleaning/wrangling task, not first-look profiling — the
`data-analytics-bi-skills:data-cleaning` skill should handle it. EDA may be mentioned as the prior
step, but if EDA is the primary skill loaded, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** establishes grain and types, quantifies missingness, computes univariate
  summaries and plots before pairwise ones, flags outliers with a stated rule, and produces a concise
  findings memo.
- **Teaches:** explains *why* to understand the data before trusting any number — mean vs. median on
  skew, visualize-before-summarize (Anscombe), and why missingness mechanism matters.
- **Safe:** does not delete outliers on sight and does not treat missingness as automatically random.
