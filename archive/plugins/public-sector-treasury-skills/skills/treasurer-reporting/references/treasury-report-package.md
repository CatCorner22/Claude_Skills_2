# The treasury report package (reference)

A buildable skeleton. Adapt exhibit names and depth to your audiences; keep the structure
stable once adopted.

## Contents
- Audience / cadence matrix
- Executive summary template
- Per-exhibit specifications
- Narrative patterns that work
- Pre-publication checklist

## Audience / cadence matrix

| Audience | Role | Typical cadence | Depth | Leads with |
|---|---|---|---|---|
| Board / finance committee | Governance: safe, legal, sufficient | Quarterly (or per bylaws/statute — confirm yours) | 1-page summary + 5 exhibits | Compliance affirmation, direction, decisions requested |
| CFO / leadership | Decisions: funding, timing, risk | Monthly | Summary + exhibits + drill-down appendix | Variances, upcoming needs, recommendations |
| Treasury / finance operations | Execution | Weekly or daily | Working detail (positions, maturities, calendars) | Actions due this week |

The same underlying data feeds all tiers; only selection and altitude change. Build once,
excerpt upward.

## Executive summary template

One page. Four blocks, in this order:

1. **Position** — "As of [date], total cash and investments are [X], of which [Y] is
   available for operations and [Z] is restricted. Liquidity stands at [n] days/months of
   operating spend vs a floor of [target]."
2. **Direction** — trend vs prior period and same period last year; forecast for the next
   period with confidence ("we expect the seasonal drawdown through [month], consistent with
   prior years").
3. **Risks and exceptions** — the two or three things worth committee attention, each with
   status and owner. Explicit compliance line: "All holdings were within policy at
   [date] per the [date] compliance check" — or the exception, stated plainly.
4. **Decisions requested** — none is a valid answer; when there is one, pair it with a
   recommendation and the date a decision is needed by.

## Per-exhibit specifications

**1. Cash position and trend**
- Content: balances by category (operating/available, restricted, fiduciary), current vs
  prior period, vs same period last year, vs forecast; days-cash or months-of-spend metric.
- Source: bank statements / positioning worksheet (`cash-management-skills:cash-positioning`).
- One question: *do we have enough accessible cash, and which way is it moving?*
- Form: one trend line with prior-year overlay beats twelve monthly bars; annotate known
  events (tuition due dates, debt service) directly on the chart.

**2. Investment holdings vs policy**
- Content: holdings by instrument/tier from custody data; each policy limit shown as
  limit / actual / headroom; weighted-average maturity vs cap; the affirmation line.
- Source: custodian/pool statements — never the trader's own sheet; check run per
  `treasury-accounting-skills:investment-policy-compliance`.
- One question: *are public funds invested safely and legally?*
- Form: a limits table with headroom; earnings shown after compliance, never before — the
  order reflects the safety-liquidity-yield hierarchy.

**3. Debt profile** (when the entity has debt)
- Content: outstanding by issue; fixed/variable mix; maturities and payment dates in the
  next 12–24 months; covenant status; rate context if variable.
- Source: ledger + official statements/indentures.
- One question: *are obligations funded and covenants met?*

**4. Forecast vs actual**
- Content: last period's forecast vs actual by major flow; variance quantified and labeled
  timing vs structural; updated forward view.
- Source: the forecast model (`cash-management-skills:cash-forecasting`) and actuals.
- One question: *is our forward view reliable, and what changed?*
- Teach the reader: repeated same-direction "timing" variances are a structural variance
  in disguise — say so when it happens.

**5. Exceptions and actions**
- Content: policy breaches and waivers, fraud attempts and outcomes, aged/stale items,
  audit points — each with owner, action, status, and the period it first appeared.
- One question: *what went wrong or nearly wrong, and who is fixing it?*
- An empty exhibit still appears, stating "no exceptions this period" — its presence is the
  control.

## Narrative patterns that work

- **Driver, magnitude, class:** "[Flow] came in [amount] [above/below] forecast because
  [cause]; this is [timing — reverses in month X / structural — carried into the forward
  view]."
- **Anticipate the obvious question:** if a chart shows a dip, the adjacent sentence
  explains the dip. Never leave a visible anomaly unnarrated.
- **Same-period-last-year framing** neutralizes seasonality for lay readers: "the decline
  is the normal summer pattern; we are [ahead of/behind] last year by [x]."
- **Recommendation language for decisions:** "We recommend [action] by [date] because
  [reason]; the alternative is [consequence]." Committees decide better between options than
  from raw facts.
- **Plain-language glossary once:** first use of a term of art gets a one-clause definition;
  after that, use it consistently.

## Pre-publication checklist

- [ ] Every balance ties to bank/custodian/GL support, archived with the package.
- [ ] Compliance affirmation backed by an actually-run, documented check.
- [ ] Internal consistency: totals agree across exhibits; summary numbers match exhibits.
- [ ] Every visible anomaly has an adjacent explanation.
- [ ] Exceptions exhibit present (even if empty); nothing known-but-omitted.
- [ ] Same layout as last period, or the change is noted.
- [ ] Dates, "as of" stamps, and version are correct; distribution list confirmed.
- [ ] Reviewed by a second reader for a lay audience (can a non-specialist retell the
      summary accurately?).
- [ ] Written as a potentially public record: nothing you would not want quoted verbatim.
