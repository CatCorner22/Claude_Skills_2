# Time-series models, backtesting, and metrics (reference)

## Contents
- Decomposition — trend, seasonality, residual
- Stationarity and differencing
- Model selection cheat-sheet
- Rolling-origin backtesting
- Keeping model selection inside the origin
- Metrics and their traps
- MASE: what it decides and what it doesn't
- Prediction intervals and the coverage check

## Decomposition — trend, seasonality, residual
Every series is a mix of a slow **trend**, a repeating **seasonal** pattern, and irregular **residual**.
- **Additive** (`y = trend + seasonal + residual`) when the seasonal swing is roughly constant in size.
- **Multiplicative** (`y = trend × seasonal × residual`) when the swing grows with the level — take a
  `log` to turn it additive, model, then exponentiate back.
- Identify the **seasonal period(s)**: weekly (period 7 on daily data), monthly, quarter-end, holiday,
  payroll cycles. A series can carry more than one (e.g. day-of-week *and* month-end).

## Stationarity and differencing
A series is (weakly) **stationary** when its mean and variance don't drift and autocorrelation depends
only on lag. ARIMA assumes stationarity; ETS does not.
- Trend → **first-difference** (`y_t − y_{t-1}`), the `d` in ARIMA(p,`d`,q).
- Seasonality → **seasonal difference** (`y_t − y_{t-m}`), the `D` in SARIMA(p,d,q)(P,`D`,Q)m.
- Growing variance → **log or Box-Cox** transform before differencing.
- Test with a plot first, then a unit-root test (ADF/KPSS) if you want a number. Don't over-difference —
  each difference adds noise; stop when the mean is flat and the ACF decays.

## Model selection cheat-sheet
| Situation | Reach for |
|---|---|
| Any series, first move | **naive** and **seasonal-naive** baselines |
| Clear trend + seasonality, little else | **ETS / Holt-Winters** (additive or multiplicative) |
| Autocorrelation structure to exploit | **ARIMA / SARIMA** (auto-search orders *inside the training window*, then check residuals) |
| Known external drivers matter | regression w/ ARIMA errors, Prophet-style, or **ML on lag + exogenous features** |
| Many related series, long history | global ML / gradient boosting on engineered features |

Check ARIMA residuals for leftover autocorrelation (Ljung-Box, ACF plot). White-noise residuals mean the
model captured the structure; patterned residuals mean it didn't.

## Rolling-origin backtesting
A single train/test cut is one draw. Backtesting slides the cutoff (the "origin") through history:
1. Pick a minimum training window and a forecast horizon *h*.
2. At each origin *t*: fit on data up to *t*, forecast *t+1 … t+h*, record errors vs actuals.
3. Advance the origin (by 1 step or by *h*) and repeat to the end of the series.
4. Average the errors across all origins for an honest skill estimate.

- **Expanding window** (training grows) uses all history; good when the process is stable.
- **Sliding window** (fixed training length) adapts to a process that changes; good after regime shifts.
- Never let the training window include anything at or after its origin — that is temporal leakage.
- **How many origins?** More than the intuitive answer, and the count that matters is
  *effectively independent* errors, not forecasts. With origins advanced one step, two consecutive
  *h*-step errors share *h*−1 of their increments, so the effective count is roughly **origins ÷ h**.
  A band built from the empirical quantiles of correlated errors is systematically too narrow, and
  the shortfall grows with the horizon.

  Measured on a random walk with a naive forecast, realised coverage of a nominal **80%** band
  (4,000 trials per cell, band fitted on the errors shown and tested on a fresh out-of-sample error):

  | h | 30 overlapping origins | 30 non-overlapping | 30·h overlapping | 120 non-overlapping |
  |---|---|---|---|---|
  | 1  | 0.742 | 0.744 | — | 0.804 |
  | 4  | 0.692 | 0.749 | 0.769 | 0.790 |
  | 13 | **0.565** | 0.756 | 0.770 | 0.784 |

  Two separate effects, and the table separates them. At **h = 1 there is no overlap at all**, and
  30 errors still yield only ~0.74 — that is pure small-sample quantile estimation: the empirical
  10th and 90th percentiles of 30 draws sit *inside* the true ones. Overlap is what turns that mild
  shortfall into a severe one: at h = 13, thirty overlapping origins realise **0.565** against a
  claimed 0.80, while thirty *non-overlapping* h-step errors realise 0.756.

  So the practical floor is: **~30·h overlapping origins** (or ~30 non-overlapping blocks) to get 30
  effectively-independent errors — and note that even 30 effective errors buys ~0.75, not 0.80. For a
  band that a buffer, a limit, or a staffing decision will rest on, aim for **~100 effective errors**
  and treat anything less as indicative. Where the history cannot afford that, say so plainly in the
  deliverable: the band is too narrow, by an amount that grows with horizon, and the coverage check
  is not optional — it is the only thing standing between the band and a decision it cannot support.
  Don't read the average error as if it came from independent draws either, for the same reason.

## Keeping model selection inside the origin
Everything the procedure *learns from data* must be re-learned inside each origin's training window.
Otherwise the backtest scores a pipeline that has already seen its own holdouts, and the reported error is
optimistic — the temporal version of tuning on the test set.

Re-fit at every origin, using only data up to that origin:

| Learned thing | Why it leaks if fitted on the full series |
|---|---|
| Box-Cox / log λ, scaling stats | Chosen using future variance |
| Differencing orders `d`, `D` (and unit-root tests) | Chosen using future trend/seasonality |
| ARIMA orders from an auto-search, ETS component choice | The search compared candidates on the holdouts |
| Hyperparameters (lags, tree depth, regularization) | Same as any tuned-on-test parameter |
| Feature selection, outlier flags, imputation values | Encode future information into "known" inputs |
| Seasonal indices, holiday effects estimated from data | Estimated from periods being predicted |

Two defensible protocols — name the one you used:
1. **Nested selection (honest, expensive).** At each origin, run the whole selection procedure on that
   window, fit, forecast *h*, record errors. Cost: one full search per origin. Cheap trick that keeps most of
   the honesty — re-run the search every *k*-th origin and carry it forward, and say so.
2. **Freeze-then-backtest (cheap, slightly conservative).** Run selection once on an early warm-up segment
   that ends *before* the first backtest origin, freeze the order/hyperparameters, then backtest with fitting
   (coefficient re-estimation) only. No holdout was ever seen by the selector; the trade is that the order
   came from less history than you'd use in production.

Reporting a full-series `auto_arima` search followed by a rolling backtest as "out-of-sample" is neither.

## Metrics and their traps
- **MAE** — mean absolute error, in the series' units; robust, easy to explain.
- **RMSE** — penalizes large misses more; use when big errors are disproportionately costly.
- **MAPE** — mean absolute *percentage* error; **undefined at zero** and explodes for small actuals;
  also asymmetric (punishes over-forecasts more).
- **sMAPE** — symmetric variant; tamer but still unstable near zero.
- **MASE** — error scaled by the **in-sample naive** error at a fixed lag (seasonal lag *m* for a seasonal
  series, lag 1 otherwise — check which one your library actually used). Scale-free and safe on zeros, so it
  is the right metric for **comparing across series** — but it is *not* a pass/fail bar. See the next section.
- **The decision rule: an explicit skill ratio.** `skill = model MAE(h) ÷ baseline MAE(h)`, both measured on
  the **same backtest origins** at the **same horizon** *h* you decide on. Below 1 you beat the baseline.
  Report it per horizon step if the decision spans several (h = 1 may win while h = 13 loses).
- For treasury cash series (small, zero, or negative values), prefer **MAE/RMSE in currency** plus the skill
  ratio, with **MASE** as the cross-series companion; avoid MAPE/sMAPE. Always report the baseline's score
  next to the model's.

## MASE: what it decides and what it doesn't
`MASE = mean(|out-of-sample errors|) / Q`, where `Q` = mean absolute error of the **in-sample** naive
forecast at a fixed lag — lag 1, or the seasonal lag *m* where the implementation is told the series is
seasonal (Hyndman & Koehler 2006 — attribution, no numbers taken from it). Three consequences:

1. **The numerator and the denominator are measured at different lags, and the mismatch has no fixed
   sign.** Your errors are *h*-step-ahead; `Q` is a one-step (or one-season) error. Forecast error grows
   with the horizon, so on a series with little seasonal structure the bar tightens as *h* grows for
   reasons that have nothing to do with model quality: for a random walk with independent Gaussian steps
   the *optimal* h-step forecast has error scale σ√h while the in-sample one-step naive error scale is σ,
   so its MASE (lag-1 denominator) sits near **√h** — at h = 13 that is √13 ≈ **3.6** (simulated over 400
   paths: 3.60). A "MASE < 1" policy rejects the best possible model on that series. Meanwhile the skill
   ratio against a 13-step-ahead naive forecast is ≈ **1.0**, which is the correct verdict: on a random walk
   nothing beats the last value.
   Reverse the structure and the error reverses with it. On a strongly seasonal series scored with the
   **lag-1** denominator, the season-to-season swing inflates `Q`, and a bare seasonal-naive forecast scores
   around **0.3–0.4** — it sails past a "MASE < 1" bar without beating anything (checked in sktime on a
   monthly sine-plus-noise series: 0.31 at `sp=1`). Given the seasonal-lag denominator the same forecast
   scores **near 1** (0.93 at `sp=12`), which is the honest reading. The bar's meaning is set by a
   denominator you did not choose for this decision.
2. **The denominator is in-sample.** `Q` comes from the training period, so a calmer or wilder training
   stretch moves MASE without any change in forecast quality — and after a level shift or regime change the
   comparison is across two different processes.
3. **Implementations differ.** Some libraries default to the lag-1 naive even on seasonal data — sktime's
   `MeanAbsoluteScaledError` ships with `sp=1`, so a monthly series stays on the lag-1 denominator until you
   pass `sp=12` — which changes `Q` and makes numbers incomparable across tools. Check which lag yours used
   before quoting a MASE.

What MASE *is* good for: a scale-free error you can average across series of different magnitudes, and a
same-series model comparison — `MASE_A / MASE_B` equals `MAE_A / MAE_B` because the shared `Q` cancels, so
the ratio of two MASEs on one series *is* a skill ratio. Use it to compare; use the horizon-matched skill
ratio to decide.

## Prediction intervals and the coverage check
A point forecast can't size a buffer, a limit, or a worst case. Build the interval, then prove it.

**Empirical intervals from the backtest (preferred, and teachable).**
1. From the rolling-origin run, collect the errors `e_h = actual − forecast` **grouped by horizon step h**.
   Errors widen with *h*; pooling h = 1 with h = 13 produces an interval that is too wide early and too
   narrow late.
2. For each *h*, take the quantiles of that error set: the 10th and 90th percentiles give an **80%**
   interval, the 2.5th/97.5th a 95% one. Add them to the point forecast for that step.
3. Mind the tail arithmetic: with 60 origins, the 2.5th percentile sits between the 1st and 2nd smallest
   errors — one observation decides your lower bound. The 10th percentile sits near the 6th of 60, which is
   far steadier. **With few origins, an honest 80% interval beats a fictional 95% one.**

**Model-based intervals (ARIMA/ETS) are a fallback, and run too narrow.** They propagate the innovation
variance forward *conditional on the fitted model*, and in standard implementations ignore
parameter-estimation uncertainty and model-selection uncertainty, while assuming the residual distribution
(usually Gaussian, constant variance) is right. Under-coverage is a repeatedly reported finding — Hyndman &
Athanasopoulos state the caveat plainly, and the M-competition interval evaluations reported empirical
coverage below nominal (both cited as reported findings; measure your own).

**The coverage check — one line, and it settles the argument.** Over the backtest, count how often the
actual fell inside the interval, per horizon:

- 60 origins at h = 13, **48** actuals inside a nominal **95%** interval → coverage 48/60 = **80%**.
- Is 80% distinguishable from 95%? Under a true 95% interval the count's standard error is
  `√(0.95 × 0.05 / 60) ≈ 0.028`, so ±1.96 SE ≈ ±5.5 points — 80% is far outside. The interval is too narrow,
  not unlucky. (Overlapping horizons make the errors serially dependent, so this is a rough guide, not a test.)
- Fixes, in order: widen from the empirical quantiles; re-check whether residual variance is
  changing (heteroscedasticity, or a variance that needs a log/Box-Cox); if the label still can't be earned,
  report the *measured* coverage instead of the nominal one.

Also report **width**: a calibrated interval so wide that every decision fits inside it is honest and
useless. Width plus coverage together is the interval's report card. (For sharpness scoring, quantile/pinball
loss or a Winkler-style interval score does this in one number.)
