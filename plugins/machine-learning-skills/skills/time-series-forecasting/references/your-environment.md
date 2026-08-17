# Your time series (sanitized template)

Fill this in with your real series. If any value is sensitive (actual balances, cash amounts, account
names, sample rows), keep it in `your-environment.private.md` instead — that suffix is git-ignored.
Commit only sanitized, structural examples.

- **Series & business meaning:** <e.g. daily net operating cash movement for the main USD account>
- **Frequency:** <daily | weekly | monthly> — **business days only?** <yes/no>
- **Forecast horizon:** <how many steps ahead you need, e.g. next 5 business days / 13 weeks>
- **Seasonal periods present:** <day-of-week, month-end, quarter-end, holidays, payroll cycle>
- **Additive or multiplicative seasonality:** <constant swing = additive; grows with level = multiplicative>
- **Known exogenous drivers (and when knowable):** <payroll dates, tax dates, rate resets, promotions>
- **Gaps / holidays / one-off spikes handling:** <how you fill or flag them>
- **Outlier policy:** <cap, flag, or leave; source of known one-offs>
- **Baseline & accuracy target:** <baseline = seasonal-naive at the decision horizon; target stated as a
  **skill ratio** — model MAE(h) ÷ baseline MAE(h) < 1 on the same backtest origins — and/or MAE < X
  currency at horizon h. Do **not** set "MASE < 1" as the target: MASE scales h-step out-of-sample error by
  an in-sample *one-step* naive error, so a good multi-step model routinely exceeds 1. Report MASE as the
  scale-free number for comparing series, not as the bar.>
- **Interval requirement:** <level you need (80% / 95%), and the **measured coverage** you accept from the
  backtest — e.g. "80% nominal, coverage within ±5 points">
- **Model-selection protocol:** <nested — re-select order/hyperparameters inside each backtest origin | frozen
  — selected on a warm-up segment before the first origin. Never selected on the full series.>
- **Tooling:** <statsmodels, pmdarima, sktime, Prophet, Darts, etc.> — **MASE seasonal lag actually used:**
  <library default is often lag 1 even on seasonal data>
