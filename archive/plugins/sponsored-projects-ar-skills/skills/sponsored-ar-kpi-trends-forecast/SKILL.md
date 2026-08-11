---
name: sponsored-ar-kpi-trends-forecast
description: >-
  Computes the core KPI set for sponsored-project receivables — AR outstanding, DSO, aging
  distribution and turnover, receipts vs transactions, plus sponsor/project-specific measures
  like burn rate vs funding, invoice-to-revenue ratio, and collections effectiveness — then
  runs trend analysis by sponsor, project type, and award category, and builds simple disclosed-
  assumption forecasts, reading results from liquidity, sponsor-relationship, and budget angles.
  Use for performance overviews, benchmarking, trend, or forward-looking sponsored-AR questions.
  Triggers: sponsored AR KPIs, DSO by sponsor, AR aging trend, collections effectiveness,
  burn rate vs funding, grant AR metrics, receivables benchmark, forecast collections,
  invoice to revenue ratio, sponsor AR performance, YoY AR comparison.
---

# Sponsored AR KPIs, trends, and forecasts

## When to use
- Building a performance view of sponsored AR: level, mix, aging, velocity, and how they're
  trending.
- Benchmarking sponsors/projects against each other or over time, and simple forecasting of
  collections or DSO.
- Not for: the unbilled pipeline mechanics behind the numbers → see
  `sponsored-projects-ar-skills:unbilled-billed-ar-wip-recon`. Detailed aging and the
  prioritized collections worklist → see
  `sponsored-projects-ar-skills:sponsored-ar-aging-collections`. For serious forecasting
  models → see `machine-learning-skills:time-series-forecasting`. Enter via the router
  (`sponsored-projects-ar-skills:sponsored-ar-fusion-analyst-master-router`).

## Do it
1. **Validate the input first** (per the router's rule): source, as-of date, aging basis
   (invoice vs schedule date), award-type mix, currency handling. Segment cost-reimbursable vs
   milestone awards before any blended metric — their aging and billing rhythms differ by
   design.
2. **Compute the core KPI set** (standard Fusion-analytics-style baselines):
   - **AR outstanding** (billed, open) — level and mix by sponsor/segment.
   - **DSO** — state the formula used (e.g. ending AR / billings × days, or countback);
     consistency beats formula choice.
   - **Aging distribution** — % current / 1–30 / 31–60 / 61–90 / 90+, and **aging turnover**
     (how fast buckets clear).
   - **Receipts vs transactions** — cash applied vs new billings per period (the burn-down
     test: is the book growing or clearing?).
   - **Average invoice amount** and count — mix shifts explain many "trends."
3. **Add the sponsored-project-specific layer:**
   - **Burn rate vs funding** — expenses incurred vs award funding (Projects - Funding
     concepts): flags both over-spend risk and under-billing (high burn + low invoicing =
     unbilled build-up; tie to the recon skill).
   - **Invoice-to-revenue ratio** — invoiced / recognized revenue per contract: persistent
     <1 means the pipeline lags recognition.
   - **Collections effectiveness** — collections / (beginning AR + billings − ending
     current AR)-style CEI, or simpler receipts-to-due measures; define and stick to one.
4. **Trend the segments, not just the totals.** Monthly/quarterly series by sponsor, project
   type, and award category; YoY where seasonality matters (academic-year rhythms are real).
   Decompose any total trend into mix vs behavior (did sponsors slow down, or did the mix
   shift toward slower sponsor types?). `references/kpi-definitions.md` fixes each formula and
   the trend-table formats.
5. **Forecast lightly and disclose everything.** Linear trend or seasonal-naive on DSO,
   collections, or aging migration is appropriate here; state the window, method, and
   assumptions in the output ("linear trend on 8 quarters of receipts; assumes billing cadence
   and sponsor mix hold"). Anything beyond that (drivers, models) → hand to
   `machine-learning-skills:time-series-forecasting`.
6. **Read the results from three angles before recommending:** **liquidity** (what does this
   AR level/velocity mean for cash — tie to `cash-management-skills:cash-forecasting`),
   **sponsor relationship health** (which sponsors are slowing, disputing, or drifting), and
   **budget adherence** (burn vs funding vs billing alignment). Deliver in the router's
   standard structure — summary, validation, metrics/insights, recommendations, edge cases.

## Why / learn
Sponsored AR needs its own KPI layer because the standard commercial-AR metrics quietly assume
things sponsored portfolios violate: DSO assumes billing follows sale (but cost-reimbursable
billing follows *spend*, and milestone billing follows *calendar*), aging assumes overdue means
distressed (but federal sponsors on LOC draw on their own rhythm), and a blended number over
mixed award types measures the mix, not the behavior. That's why segmentation isn't a nicety
here — it's what makes the metrics mean anything. The sponsored-specific layer exists because
the real risks are different too: the commercial fear is non-payment; the sponsored fears are
*unbilled build-up* (value earned but never claimed before an award closes) and *funding
misalignment* (spending past funding, or leaving funded work unbilled) — burn-vs-funding and
invoice-to-revenue are the early-warning gauges for exactly those. And the light-forecast rule
is epistemic honesty: a linear trend with disclosed assumptions is a planning aid; the same
line presented as a prediction is a liability. The three-angle reading, finally, keeps the
analysis from collapsing into one department's view — the same aging table is a cash question
to treasury, a relationship question to research administration, and a compliance question to
the controller.

## Common mistakes
- Blended KPIs over cost-reimbursable + milestone + LOC awards → measures the mix; segment first.
- DSO formula switched between periods → the trend becomes an artifact; fix one formula and label it.
- Reading a total-AR trend without mix decomposition → sponsor-mix shift masquerades as behavior change.
- Aging basis unlabeled → invoice-date and due-date agings differ materially; say which.
- Forecasts without disclosed assumptions/window → fiction with a trendline; disclose or don't forecast.
- Ignoring unbilled while celebrating low billed-AR aging → the risk moved upstream; pair with the recon skill's pipeline view.
- Benchmarking sponsors without noting payment-mechanism differences → LOC vs invoice sponsors aren't comparable on DSO.

## Tailor to your environment
Fix your definitions in `references/your-environment.md` (real results in
`your-environment.private.md`, git-ignored): your DSO formula, CEI definition, segment scheme,
seasonal calendar, benchmark levels, and which KPIs your leadership actually tracks.
**Never commit sponsor names or real balances.**

## References
- references/kpi-definitions.md — every formula fixed, trend/decomposition table formats, forecast disclosure template
- references/your-environment.md — your formulas, segments, seasonality, benchmarks (fill in)
