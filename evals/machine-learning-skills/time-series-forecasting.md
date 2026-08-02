# Evals — machine-learning-skills:time-series-forecasting

## 1. Positive trigger (should load the skill)
> "I have three years of daily net cash movement for our main account. I want to forecast the next two
> weeks. There's an obvious day-of-week pattern and a month-end spike. What model should I use and how do
> I test it properly?"

Expected: skill loads; decomposes trend/seasonality/residual; sets naive and seasonal-naive baselines
first; considers ETS/Holt-Winters and SARIMA for the weekly + month-end seasonality; splits by time and
backtests with rolling origin; scores with MAE/RMSE/MASE and warns against MAPE on low/zero cash values.

## 2. Near-miss (should NOT load this skill)
> "Predict whether each new vendor is high-risk based on its registration details, industry, and country."

Expected: this is a cross-sectional classification problem with no time axis to forecast along. The
`machine-learning-skills:supervised-modeling` skill should handle it. If this forecasting skill loads,
tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** decomposes the series, establishes naive/seasonal-naive baselines *before* modeling,
  picks an appropriate classical or ML model, validates with time-ordered splits and rolling-origin
  backtesting, and reports metrics suited to the series (MAE/RMSE/MASE, not MAPE on near-zero values).
- **Teaches:** explains *why* temporal order must be respected (no shuffling) and why beating a baseline
  precedes adding complexity — not just which function to call.
- **Safe:** never uses a shuffled split, never reports a single lucky hold-out as the accuracy, and does
  not feed future-only information as an exogenous feature.
