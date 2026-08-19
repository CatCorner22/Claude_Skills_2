---
name: time-series-forecasting
description: >-
  Builds and evaluates time-series forecasts with proper temporal validation — decomposition and
  stationarity checks, naive and seasonal-naive baselines first, classical models (ETS/Holt-Winters,
  ARIMA/SARIMA), and ML approaches with lagged and exogenous features — using time-ordered splits,
  rolling-origin backtesting with model selection re-run inside each origin, a skill-vs-baseline ratio at
  the decision horizon, and empirical prediction intervals with a coverage check. Use when forecasting a
  series over time such as cash flow, account balances, transaction volumes, or collections. Triggers:
  time series, forecast, forecasting, ARIMA, SARIMA, ETS, Holt-Winters, exponential smoothing,
  seasonality, backtesting, rolling forecast, rolling origin, predict future values, trend and
  seasonality, prediction interval, forecast uncertainty.
metadata:
  version: "1.3.0"
---

# Time-series forecasting

## When to use
- Forecasting a value that unfolds over time: daily/weekly cash flow, account balances, payment or transaction volumes, a collections series.
- Choosing between classical (ETS, ARIMA) and ML forecasting approaches, or adding exogenous drivers.
- Validating a forecast honestly with time-based splits and backtesting instead of a shuffled hold-out.
- Not for: the finance framing of a liquidity forecast built from operational drivers (receivables aging, payment runs) — that is direct-method cash forecasting, a domain method this library does not carry; hand the statistical driver-series here. For general metric/validation choice → see `machine-learning-skills:model-evaluation`.

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
4. **Fit classical models — and keep order selection inside the training window.** Use **ETS /
   Holt-Winters** when the story is trend + seasonality (choose additive vs multiplicative to match the
   decomposition). Use **ARIMA/SARIMA** when there's autocorrelation structure to exploit; let an
   auto-ARIMA search orders, then sanity-check residuals for leftover autocorrelation. **Never run the
   order search on the whole series and then backtest it** — the search will have seen every future
   holdout, and the backtest reports a number you cannot get in production. Either re-run selection inside
   each origin's training window (step 7), or select once on an early warm-up segment and **freeze** the
   order before the first backtest origin. Say in the writeup which you did.
5. **Add ML / exogenous regressors only if they earn their keep.** When known future drivers matter
   (calendar effects, payroll dates, promotions, rates), build **lag and rolling features** and fit a
   regression or gradient-boosted model, or use a regression-with-ARIMA-errors / Prophet-style approach.
   Keep exogenous inputs to values you'll actually know at forecast time. See `machine-learning-skills:feature-engineering`.
6. **Split by time — never shuffle.** Train on the earlier portion, test on the later portion. A random
   `train_test_split` on a time series leaks the future into training and produces fantasy accuracy.
7. **Backtest with rolling origin — and re-fit everything inside each origin.** Slide the cutoff forward
   through history: at each origin, fit on the past and forecast the next *h* steps, then average errors
   across origins (expanding window, or a fixed sliding window if the process changes over time). One
   hold-out is one lucky or unlucky draw; rolling backtesting estimates real forecast skill. Everything
   *learned from data* has to be re-learned inside each origin's window — the transformation (Box-Cox λ),
   the differencing orders, the ARIMA/ETS order, hyperparameters, feature selection, scaler statistics. Any
   of them chosen once on the full series makes every holdout partly seen and the backtest optimistic.
8. **Score at the decision horizon, against the baseline, at the same origins.** Report **MAE** and
   **RMSE** in the series' units; use **MAPE/sMAPE** only when values stay comfortably away from zero —
   they explode or divide-by-zero on low volumes and intermittent series. The **decision rule is the
   explicit skill ratio**: `model MAE(h) ÷ seasonal-naive MAE(h)`, both computed on the *same* backtest
   origins at the *same* horizon *h* you will actually decide on; below 1 you beat the baseline, above 1
   you didn't. Report **MASE** alongside as a scale-free number for comparing across series — but never as
   the pass/fail bar, because its denominator is an *in-sample* naive error at a fixed lag (1, or the
   seasonal lag *m*) while your errors are *h*-step, so the number floats with the horizon, with which lag
   your library used, and with the series' own seasonality (see
   `references/models-and-backtesting.md`). Metric definitions live in
   `machine-learning-skills:model-evaluation`.
9. **Build prediction intervals from the backtest, per horizon step.** Point forecasts alone can't support
   a decision about buffers, limits, or worst cases. The most defensible interval is **empirical**: collect
   the backtest errors for each horizon step *h* separately (errors widen with *h*, so never pool them) and
   take their quantiles — e.g. the 10th and 90th percentiles of the h-step errors added to the h-step point
   forecast give an 80% interval. Model-based ARIMA/ETS intervals are a fallback, and treat them as a
   lower bound on the true width (step 10).
10. **Check the interval's coverage, then state it.** Count how often the backtest actual fell inside the
   interval at each horizon and compare with the nominal level: 48 of 60 h-step actuals inside a nominal
   95% interval is **80% coverage**, and the interval is too narrow — widen it or report the measured
   coverage instead of the label. Report interval width too: an interval can only be honest *and* useful if
   it is both calibrated and tight enough to act on.

**Deliverable — the forecast package.** The finished output contains: (1) the decomposition read —
trend, seasonal periods, additive vs multiplicative, level shifts and one-offs noted; (2) naive and
seasonal-naive baseline scores; (3) the chosen model, why the decomposition points to it, and where
its order/hyperparameters were selected (inside each origin, or frozen before the first origin);
(4) rolling-origin backtest results at the decision horizon — MAE/RMSE in the series' units, the
explicit model-vs-seasonal-naive skill ratio at that horizon, and MASE as the scale-free companion;
(5) prediction intervals built from the per-horizon backtest error quantiles, with their **measured
coverage** against the nominal level and their typical width. The assistant builds and backtests the
models; the human owns the horizon, the business calendar, and forecast acceptance.

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

**"Beat the baseline" has to be measured at the horizon you decide on, which is why MASE is not the
decision rule.** MASE divides your *out-of-sample* errors by the mean *in-sample* naive error at a fixed
lag — lag 1, or the seasonal lag *m* where the implementation is told the series is seasonal. The numerator
and the denominator are answering different questions: a 13-week-ahead forecast is scored against a
fixed-lag benchmark, and forecast errors grow with the horizon. For a pure random walk with independent
Gaussian steps, even the *optimal* forecaster has h-step error scale σ√h, so its MASE lands near √13 ≈ 3.6
at h = 13 — while the ratio against a 13-week-ahead naive forecast is ≈ 1.0, correctly saying "no skill
here." Read as a bar, MASE < 1 rejects good long-horizon models and rewards short-horizon ones for nothing.
The distortion does not even keep a fixed sign. Score a strongly seasonal series against the **lag-1**
denominator — the default in several libraries even when the data is seasonal — and the month-to-month
swing inflates the denominator instead: a plain seasonal-naive forecast scores around 0.3–0.4, comfortably
"passing" a bar it has earned nothing against, while the seasonal-lag denominator puts the same forecast
near 1.0 — the honest reading. Same metric, same threshold, opposite verdict.
Read for what it is — a **scale-free** error, safe on zeros, comparable across series of wildly different
magnitudes — it is genuinely useful, and the ratio of two models' MASE on the same series is exactly the
skill ratio because the shared denominator cancels. So: MASE to compare, skill ratio at horizon *h* to
decide.

**Order selection is model fitting, so it obeys the same temporal rule as everything else.** An auto-ARIMA
search over the full series has read the holdouts; the backtest that follows is scoring a model that was
chosen with knowledge of the answers, exactly as tuning on test does. Re-selecting inside each origin's
window is the honest version and costs compute; freezing the order on an early segment is the cheap version
and costs a little realism (the order came from less history). Both are defensible; running the search on
everything and reporting the backtest as out-of-sample is not.

**Finally, uncertainty is the part of a forecast a decision actually consumes.** Nobody sizes a buffer from
a point estimate. Model-based intervals from ARIMA/ETS are conditional on the fitted model being right:
they propagate the innovation variance forward but generally ignore parameter-estimation uncertainty and
model-*selection* uncertainty, and they assume the residual distribution (usually Gaussian, constant
variance) holds — so they are systematically **too narrow**, a repeatedly reported finding in the
forecasting literature (Hyndman & Athanasopoulos state the caveat plainly; the M-competition interval
evaluations found empirical coverage below nominal — treat both as reported findings and measure your own
coverage). Empirical intervals from per-horizon backtest error quantiles inherit whatever the model got
wrong across many origins, which is why they are the more teachable default. Then check coverage, because
an interval with a "95%" label and 80% coverage is worse than no interval — it launders a bad forecast into
a false guarantee.

## Common mistakes
- Random/shuffled train-test split on a time series → leaks the future, inflates accuracy. Always split by time.
- Skipping baselines → you can't tell if the model helps. Compute naive and seasonal-naive first, then beat them.
- One hold-out period → a single lucky draw. Use rolling-origin backtesting to average over many origins.
- MAPE on low-volume, zero, or negative values → blows up or is undefined. Use MAE/RMSE or a scaled error (MASE).
- Treating MASE < 1 as the pass mark → it scales *h*-step out-of-sample error by an *in-sample* naive error at a fixed lag, so the number floats with the horizon and with which lag the library used: a good long-horizon model on a random walk scores near √h, while a bare seasonal-naive forecast on a seasonal series scored against the lag-1 default scores well under 1. Decide on the model-vs-baseline ratio at your actual horizon; use MASE to compare across series.
- Searching ARIMA orders (or tuning anything) on the full series before backtesting → selection has seen every holdout. Re-select inside each origin, or freeze the order before the first origin.
- Shipping a point forecast with no interval, or quoting the model's own 95% interval unchecked → ARIMA/ETS intervals ignore parameter and selection uncertainty and run too narrow. Build empirical intervals from per-horizon backtest quantiles and measure coverage.
- Pooling backtest errors across horizons to make one interval → h=1 and h=13 errors have different spreads; the interval is too wide early and too narrow late. Quantile per horizon step.
- Additive model on a multiplicative series (seasonal swing grows with level) → biased. Log-transform or model it multiplicatively.
- Feeding future-only information as an exogenous feature → leakage. Use only drivers known at forecast time (or forecast them too).
- Over-differencing / chasing tiny ARIMA gains → brittle model. Check residual autocorrelation; prefer the simpler model that backtests as well.

## Tailor to your environment
Record your series in `references/your-environment.md` (keep real values, account names, and sample rows
in `your-environment.private.md`, which is git-ignored): the series and its business meaning, frequency
and horizon, its seasonal periods (weekly/monthly/holiday/quarter-end), known exogenous drivers and when
they're knowable, how you treat gaps and outliers, and your accuracy target expressed as a **skill ratio at
your decision horizon** (plus the interval level and the coverage you need) next to your baseline. If you're
building a liquidity forecast, frame it with a direct-method cash-forecast structure first — from
whatever finance source you use, since this library does not carry one — and feed the statistical
forecast of a driver series (e.g. collections) back as an input there.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/time-series-forecasting.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/models-and-backtesting.md — decomposition, stationarity, ETS/ARIMA choice, rolling-origin backtesting with in-origin model selection, metric traps and what MASE does/doesn't decide, and prediction intervals with the coverage check
- references/your-environment.md — your series, frequency, seasonality, drivers, and accuracy target (add when supplied)
