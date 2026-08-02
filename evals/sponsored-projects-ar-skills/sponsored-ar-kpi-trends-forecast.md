# Evals — sponsored-projects-ar-skills:sponsored-ar-kpi-trends-forecast

## 1. Positive trigger (should load the skill)
> "Build a sponsored-AR performance view: DSO and aging by sponsor category for the last 8
> quarters, burn vs funding on our biggest awards, and a rough forecast of next quarter's
> collections."

Expected: skill loads; validates input and segments by award type before any blended metric;
computes the core set with fixed, labeled formulas; adds burn-vs-funding and invoice-to-revenue;
decomposes trends into mix vs behavior; delivers a linear/seasonal-naive forecast with full
assumption disclosure; reads results from liquidity, sponsor-health, and budget angles.

## 2. Near-miss (should NOT load this skill)
> "Build a proper time-series model of our cash receipts with seasonality and confidence
> intervals."

Expected: real forecasting — `machine-learning-skills:time-series-forecasting`. If this skill
loads, tighten the lightweight-forecast scope in the description.

## 3. Quality rubric
A good response:
- **Does the task:** KPI table with definitions labeled, segmented trends with mix
  decomposition, sponsored-specific gauges, and a disclosed-assumption forecast.
- **Teaches:** why commercial-AR metrics mislead on mixed award types, what the sponsored-
  specific risks are (unbilled build-up, funding misalignment), and forecast honesty.
- **Safe:** one DSO formula throughout, aging basis labeled, LOC sponsors not benchmarked on
  DSO against invoice sponsors, no undisclosed forecast assumptions.
