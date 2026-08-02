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
- **Baseline & accuracy target:** <seasonal-naive; target MASE < 1 or MAE < X currency by horizon>
- **Tooling:** <statsmodels, pmdarima, sktime, Prophet, Darts, etc.>
