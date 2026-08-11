# Sponsored aging and collections worksheets (reference)

## Contents
- Aging summary format
- Heatmap reading guide
- Collection prioritization scoring
- Cash-flow handoff format

## Aging summary format
Header carries: **as-of date**, **aging basis** (invoice date / schedule-due date), currency,
and the population statement (RECEIVABLE-class accounts only; draw-based awards excluded).

| Sponsor (× contract) | Future (not due) | Current | 1–30 | 31–60 | 61–90 | 90+ | Total open | % overdue | Avg days overdue (wtd) |
|---|---|---|---|---|---|---|---|---|---|
Counts in a mirror table (or as `amount / n`) — a bucket of one big invoice and a bucket of
forty small ones need different work.
Dimension cuts on separate views: award type, business unit, ledger, GL account. Keep sponsor
terms visible (a column or grouping) so "overdue" reads contractually.

## Heatmap reading guide
Build sponsor × bucket with amount-shaded cells; read for:
- **Hot cells:** one sponsor dominating one old bucket → a specific conversation.
- **Hot rows:** a sponsor overdue across buckets → relationship/terms problem, escalate.
- **Hot columns:** everyone stacking in 31–60 → a process event (billing cycle slip, portal
  change), not forty coincidences.
- **Drift:** compare to last quarter's map; rightward migration per sponsor is deterioration
  before any single cell alarms.
- **Concentration line:** top-5 sponsors' share of total open and of 90+; report both.

## Collection prioritization scoring
Per sponsor (or contract within sponsor):
```
Priority = normalized amount (open overdue $)
         × age factor (weighted avg days overdue / terms)
         × sponsor-risk factor (payment pattern tier 1–3)
```
Before listing, apply the cross-reference scrub: remove/annotate unapplied receipts, partials
(list the open remainder), credits in flight, and disputes (different workflow — route
disputes to the dispute owner, not the call list).
Call-list row: sponsor, contracts, open overdue (net), oldest item, terms, last payment date,
prior contact note, **next action** (call/email/portal/escalate), owner, follow-up date.

## Cash-flow handoff format
For `cash-management-skills:cash-forecasting`: expected collections by week/month from the
prioritized list — amount × probability by bucket (e.g. current 95%, 1–30 90%, 31–60 75%,
61–90 50%, 90+ 25% — tune to your history), plus known large single receipts (milestone
payments, LOC draws handled separately). State the probabilities used; they're assumptions,
not facts.
