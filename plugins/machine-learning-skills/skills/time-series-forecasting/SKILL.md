---
name: time-series-forecasting
description: >-
  Builds and evaluates time-series forecasts with proper temporal validation — decomposition and
  stationarity checks, naive and seasonal-naive baselines first, classical models (ETS/Holt-Winters,
  ARIMA/SARIMA), and ML approaches with lagged and exogenous features — using time-ordered splits and
  rolling-origin backtesting, and metrics chosen for the series. Use when forecasting a series over
  time such as cash flow, account balances, transaction volumes, or collections. Triggers: time series,
  forecast, forecasting, ARIMA, SARIMA, ETS, Holt-Winters, exponential smoothing, seasonality,
  backtesting, rolling forecast, rolling origin, predict future values, trend and seasonality.
---

# Time-series forecasting

## When to use
- Forecasting a value that unfolds over time: daily/weekly cash flow, account balances, payment or transaction volumes, a collections series.
- Choosing between classical (ETS, ARIMA) and ML forecasting approaches, or adding exogenous drivers.
- Validating a forecast honestly with time-based splits and backtesting instead of a shuffled hold-out.
- Not for: the treasury framing of a liquidity forecast from operational drivers (AR aging, AP runs) → see `cash-management-skills:cash-forecasting`, then hand the statistical driver-series here. For general metric/validation choice → see `machine-learning-skills:model-evaluation`.

## Do it
1. **Plot it and decompose.** Chart the raw series first. Separate **trend**, **seasonality**, and
   **residual** (additive when the seasonal swing is roughly constant; multiplicative when it grows with
   the level — log-transform to make it additive). Note the frequency, gaps, missing periods, and any
   level shifts or one-off spikes. See `references/models-and-backtesting.md`.
2. **Set naive baselines FIRST.** Before any model, compute the **naive** forecast (next = last value)
   and the **seasonal-naive** forecast (next = same period one cycle ago, e.g. same weekday last week).
   These are the bar every fancier model must clear. Many "sophisticated" models never beat seasonal-naive.
3. **Handle stationarity if you'll use ARIMA.** Check whether mean/variance drift. Difference to remove
   trend, seasonally difference to remove seasonality, and transform (log) to stabilize variance. ETS
   handles trend/seasonality directly, so this step is mainly for the ARIMA family.
4. **Fit classical models.** Use **ETS / Holt-Winters** when the story is trend + seasonality (choose
   additive vs multiplicative to match the decomposition). Use **ARIMA/SARIMA** when there's
   autocorrelation structure to exploit; let an auto-ARIMA search orders, then sanity-check residuals for
   leftover autocorrelation. These are strong, low-maintenance defaults for most business series.
5. **Add ML / exogenous regressors only if they earn their keep.** When known future drivers matter
   (calendar effects, payroll dates, promotions, rates), build **lag and rolling features** and fit a
   regression or gradient-boosted model, or use a regression-with-ARIMA-errors / Prophet-style approach.
   Keep exogenous inputs to values you'll actually know at forecast time. See `machine-learning-skills:feature-engineering`.
6. **Split by time — never shuffle.** Train on the earlier portion, test on the later portion. A random
   `train_test_split` on a time series leaks the future into training and produces fantasy accuracy.
7. **Backtest with rolling origin.** Slide the cutoff forward through history: at each origin, fit on the
   past and forecast the next *h* steps, then average errors across origins (expanding window, or a fixed
   sliding window if the process changes over time). One hold-out is one lucky or unlucky draw; rolling
   backtesting estimates real forecast skill.
8. **Score with metrics that fit the series.** Report **MAE** and **RMSE** in the series' units; use
   **MAPE/sMAPE** only when values stay comfortably away from zero — they explode or divide-by-zero on
   low volumes and intermittent series. Prefer a **scaled error (MASE)** or an explicit skill-vs-baseline
   ratio so the score says whether you beat seasonal-naive. Details in `machine-learning-skills:model-evaluation`.

## Why / learn
Two principles carry almost all of time-series forecasting. First, **respect temporal order**: the whole
point is to predict the unseen future, so any evaluation that lets the model peek at future rows — a
shuffled split, a feature computed over the whole series, target-derived aggregates — reports a number
you will never see in production. Time-based splits and rolling-origin backtesting exist to make the test
mimic reality. Second, **beat a baseline before adding complexity.** Naive and seasonal-naive are
free, robust, and shockingly hard to beat; they encode the two things most series mostly do — persist,
and repeat their season. If ARIMA or a boosted model can't beat seasonal-naive out of sample, the extra
complexity is buying nothing but risk. Decomposition is the lens that tells you which tool to reach for:
a series that is mostly trend + seasonality is ETS's home turf; strong autocorrelation in the residual is
ARIMA's; genuine dependence on known external drivers is where ML/exogenous models start to pay off.
MAPE's traps matter in treasury specifically, where volumes can be small, zero, or negative — a metric
that divides by the actual value quietly lies exactly where cash series are hardest.

## Common mistakes
- Random/shuffled train-test split on a time series → leaks the future, inflates accuracy. Always split by time.
- Skipping baselines → you can't tell if the model helps. Compute naive and seasonal-naive first, then beat them.
- One hold-out period → a single lucky draw. Use rolling-origin backtesting to average over many origins.
- MAPE on low-volume, zero, or negative values → blows up or is undefined. Use MAE/RMSE or a scaled error (MASE).
- Additive model on a multiplicative series (seasonal swing grows with level) → biased. Log-transform or model it multiplicatively.
- Feeding future-only information as an exogenous feature → leakage. Use only drivers known at forecast time (or forecast them too).
- Over-differencing / chasing tiny ARIMA gains → brittle model. Check residual autocorrelation; prefer the simpler model that backtests as well.

## Tailor to your environment
Record your series in `references/your-environment.md` (keep real values, account names, and sample rows
in `your-environment.private.md`, which is git-ignored): the series and its business meaning, frequency
and horizon, its seasonal periods (weekly/monthly/holiday/quarter-end), known exogenous drivers and when
they're knowable, how you treat gaps and outliers, and your accuracy target and baseline. If you're
building a treasury liquidity forecast, frame it with `cash-management-skills:cash-forecasting` first and
feed the statistical forecast of a driver series (e.g. collections) back as an input there.

## References
- references/models-and-backtesting.md — decomposition, stationarity, ETS/ARIMA choice, rolling-origin backtesting, and metric traps
- references/your-environment.md — your series, frequency, seasonality, drivers, and accuracy target (add when supplied)
