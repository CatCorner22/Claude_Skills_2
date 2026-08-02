# Time-series models, backtesting, and metrics (reference)

## Contents
- Decomposition — trend, seasonality, residual
- Stationarity and differencing
- Model selection cheat-sheet
- Rolling-origin backtesting
- Metrics and their traps

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
| Autocorrelation structure to exploit | **ARIMA / SARIMA** (auto-search orders, then check residuals) |
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

## Metrics and their traps
- **MAE** — mean absolute error, in the series' units; robust, easy to explain.
- **RMSE** — penalizes large misses more; use when big errors are disproportionately costly.
- **MAPE** — mean absolute *percentage* error; **undefined at zero** and explodes for small actuals;
  also asymmetric (punishes over-forecasts more).
- **sMAPE** — symmetric variant; tamer but still unstable near zero.
- **MASE** — error scaled by the in-sample seasonal-naive error; **< 1 means you beat seasonal-naive**,
  ≥ 1 means you didn't. The cleanest single number for "is this model worth it," and safe on zeros.
- For treasury cash series (small, zero, or negative values), prefer **MAE/RMSE in currency** and
  **MASE**; avoid MAPE/sMAPE. Always report the baseline's score next to the model's.
