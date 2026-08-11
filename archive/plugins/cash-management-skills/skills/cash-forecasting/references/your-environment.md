# Your cash forecasting environment (sanitized template)

Fill this in with your real conventions. If any value is sensitive (real figures, customer/vendor
names), keep it in `your-environment.private.md` instead — that suffix is git-ignored.

- **Method:** <direct (treasury) | indirect (planning) | both, by horizon>
- **Horizon and grain:** <e.g. 13 weeks, weekly; plus 12 months, monthly>
- **Receipt categories:** <AR collections, card/lockbox settlement, interest/maturities, other>
- **Disbursement categories:** <AP runs, payroll, debt service, tax, capex, dividends, rent>
- **Collection assumptions:** <collection curve by cohort, or DSO by segment/region>
- **Payment calendars:** <AP run days; payroll pay dates; tax/VAT dates; debt-service schedule>
- **Minimum / target balance checked against:** <the floor the forecast must not breach>
- **Reforecast cadence:** <e.g. every Monday, roll and reforecast near weeks with actuals>
- **Accuracy targets:** <e.g. week 1 MAPE < 5%, week 13 MAPE < 15%; acceptable bias band>
- **Systems / data sources:** <ERP AR/AP, TMS, bank actuals for variance, Oracle Fusion cube>
- **Owners:** <who owns each driver line; who reviews variance and by when>
- **Known seasonality / one-offs:** <seasonal troughs, annual bonus, tax true-ups, debt maturities>
