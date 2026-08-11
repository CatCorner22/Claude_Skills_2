# Your time-value environment (sanitized template)

Fill in your real conventions. If any value is sensitive (actual deal rates, live forecasts), keep it
in `your-environment.private.md` instead — that suffix is git-ignored, so raw data never gets
committed. Commit only sanitized, structural examples.

- **Default discount rate / WACC:** <e.g. 8.5% nominal after-tax; how it is derived and reviewed>
- **Rate by risk tier:** <if you use different rates for low/medium/high-risk cash flows>
- **Compounding convention:** <annual | semi-annual | monthly | continuous>
- **Day-count basis:** <30/360 | actual/365 | actual/360 — for interest and discounting>
- **Cash-flow timing assumption:** <period-end (ordinary) | period-start (due) | mid-period>
- **Real vs nominal:** <do you model in nominal currency with a nominal rate, or real with real?>
- **NPV/IRR schedule template:** <link or description of your standard layout, e.g. XNPV/XIRR by date>
- **Approval thresholds:** <NPV or IRR hurdle at which a valuation goes for sign-off>
