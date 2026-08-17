# Evals — machine-learning-skills:time-series-forecasting

## 1. Positive trigger (should load the skill)
> "I have three years of daily net cash movement for our main account. I want to forecast the next two
> weeks. There's an obvious day-of-week pattern and a month-end spike. What model should I use and how do
> I test it properly?"

Expected: skill loads; decomposes trend/seasonality/residual; sets naive and seasonal-naive baselines
first; considers ETS/Holt-Winters and SARIMA for the weekly + month-end seasonality; splits by time and
backtests with rolling origin, keeping order selection inside each origin's training window (or frozen
before the first origin) rather than searching orders on the full series; decides on an explicit
model-vs-seasonal-naive skill ratio at the two-week decision horizon (MASE reported as the scale-free
companion, not as a MASE < 1 pass mark); builds prediction intervals from per-horizon backtest error
quantiles and reports their measured coverage; and warns against MAPE on low/zero cash values.

## 2. Near-miss (should NOT load this skill)
> "Predict whether each new vendor is high-risk based on its registration details, industry, and country."

Expected: this is a cross-sectional classification problem with no time axis to forecast along. The
`machine-learning-skills:supervised-modeling` skill should handle it. If this forecasting skill loads,
tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** decomposes the series, establishes naive/seasonal-naive baselines *before* modeling,
  picks an appropriate classical or ML model, validates with time-ordered splits and rolling-origin
  backtesting, and reports metrics suited to the series (MAE/RMSE + skill ratio, not MAPE on near-zero values).
- **Teaches:** explains *why* temporal order must be respected (no shuffling) and why beating a baseline
  precedes adding complexity — not just which function to call.
- **Gets MASE right:** treats MASE as a **scale-free comparison** metric and *not* as a decision threshold,
  because its denominator is an in-sample **one-step** naive error while the numerator is h-step
  out-of-sample — so a good long-horizon model can score above 1 while comfortably beating a same-horizon
  seasonal-naive. A response that states "MASE < 1 means the model is worth shipping" has failed this item.
  The decision rule it should give: model MAE(h) ÷ baseline MAE(h) on the same origins at the real horizon.
- **Keeps selection out of the holdouts:** does not run auto-ARIMA on the whole series and then present the
  rolling backtest as out-of-sample; either re-selects inside each origin or freezes the order before the
  first origin, and says which.
- **Handles uncertainty:** produces prediction intervals (per-horizon empirical backtest quantiles preferred),
  warns that model-based ARIMA/ETS intervals ignore parameter and selection uncertainty and run too narrow,
  and reports measured coverage against the nominal level.
- **Safe:** never uses a shuffled split, never reports a single lucky hold-out as the accuracy, and does
  not feed future-only information as an exogenous feature.
- **Delivers the contract:** the output reads as a forecast package — decomposition read, baseline scores,
  model choice with rationale *and where its order was selected*, rolling-origin backtest results (MAE/RMSE +
  the skill ratio, MASE as companion) at the decision horizon, and the forecast with intervals whose measured
  coverage and width are stated.
