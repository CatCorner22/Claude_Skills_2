# Anomaly-detection methods and thresholds (reference)

## Contents
- Statistical methods (single feature)
- Time-series residual anomalies
- Multivariate / unsupervised methods
- Threshold setting and the precision/recall trade-off
- Evaluation under label scarcity
- Alert fatigue

## Statistical methods (single feature)
- **Z-score:** `(x − mean) / std`; flag `|z| > 3` (or your cut). Simple, but **mean and std are themselves
  inflated by outliers**, so it loses sensitivity in the messy data you care about.
- **Robust z-score:** `0.6745 · (x − median) / MAD`, where MAD is the median absolute deviation. Resistant to
  outliers; prefer it over plain z-score for anomaly work.
- **IQR rule:** flag below `Q1 − 1.5·IQR` or above `Q3 + 1.5·IQR` (widen to 3·IQR for "far out"). Distribution-free.
- **Percentile / rank:** flag the top/bottom p% — transparent and easy to tie to an alert budget.
Use these when a single quantity (a fee, a balance change, a transaction amount) carries the signal.

## Time-series residual anomalies
1. Model the expected value: forecast or decompose the series (see `machine-learning-skills:time-series-forecasting`).
2. Compute the **residual** = actual − expected.
3. Flag residuals large relative to a **local, season-aware** spread (rolling MAD, or prediction intervals).
This flags an *off-pattern* month-end while leaving a *normal* month-end alone — the point a plain global
threshold misses.

## Multivariate / unsupervised methods
| Method | Idea | Notes |
|---|---|---|
| **Isolation forest** | Randomly partitions; anomalies isolate in fewer splits | Fast, scales well, few assumptions; a strong default |
| **Local outlier factor (LOF)** | Compares a point's density to its neighbors' | Catches *local* outliers; **scale features first**; needs a neighborhood size |
| **DBSCAN** | Density clustering; points in no cluster are outliers | No preset cluster count; sensitive to its `eps`/`min_samples` |
| **Mahalanobis distance** | Distance accounting for feature correlation | Assumes roughly elliptical data; **scale/covariance-aware** |
| **Autoencoder reconstruction error** | High reconstruction error = anomaly | For high-dimensional data; needs more data and care |

Use these when "unusual" only appears across features jointly (amount + counterparty + hour + channel).

## Threshold setting and the precision/recall trade-off
- Every method outputs a **score**; the alert is a **cut** on that score. There is no universal right cut.
- Lower the cut → more alerts → **higher recall, lower precision** (more false alarms). Raise it → fewer
  alerts → **higher precision, lower recall** (more misses). Choose the point that matches your costs.
- Practical anchors: a **contamination / expected-anomaly rate**, a **score quantile**, or an **alert budget**
  (the number of alerts/day the team can truly investigate) — often the budget is the binding constraint.

## Evaluation under label scarcity
- With few/no labels you usually **cannot compute recall** — you don't know how many anomalies you missed.
- You *can* estimate **precision** by having reviewers adjudicate a sample of the top alerts.
- Track **precision@k** (of the top k alerts, how many were real) over time; fold confirmed cases back as labels;
  as labels accumulate you can move toward supervised evaluation (`machine-learning-skills:model-evaluation`).

## Alert fatigue
- Precision that's too low trains reviewers to ignore the stream — then even true positives are lost.
- **Suppress known-benign recurrences** (scheduled transfers, expected month-end movements) with a whitelist.
- Rank and route the **top-N**, don't dump every above-threshold point.
- Review precision periodically and re-tune the cut; a distrusted alert stream is worse than none.
