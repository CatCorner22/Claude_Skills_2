# Sponsored-AR KPI definitions (reference)

Fix one definition per metric and label it on every output. Formulas below are the defaults;
your environment file overrides.

## Contents
- Core KPI formulas
- Sponsored-specific formulas
- Trend and decomposition formats
- Forecast disclosure template

## Core KPI formulas
| KPI | Default formula | Notes |
|---|---|---|
| AR outstanding | Sum of open billed AR (payment schedules balance due) | State as-of date; net of credits |
| DSO (simple) | Ending AR / period billings × days in period | Cheap, mix-sensitive |
| DSO (countback) | Walk back months of billings until AR is consumed | Slower, steadier under lumpy billing — prefer for milestone-heavy portfolios |
| Aging distribution | % of open AR per bucket (current, 1–30, 31–60, 61–90, 90+) | Label the basis: invoice date vs due date |
| Aging turnover | Period collections / average AR | Velocity check on the whole book |
| Receipts vs transactions | Cash applied vs new billings, per period | > 1 = book clearing; < 1 = growing |
| Average invoice | Billings / invoice count | Mix-shift detector |

## Sponsored-specific formulas
| KPI | Default formula | Signal |
|---|---|---|
| Burn rate | ITD expense / total award funding (and per period) | Spend pace vs award size |
| Burn vs billing gap | ITD billable cost − ITD invoiced | Unbilled build-up (cost-reimbursable) |
| Invoice-to-revenue ratio | ITD invoiced / ITD recognized revenue, per contract | Persistent < 1 = pipeline lag |
| Collections effectiveness (CEI-style) | Collections / (beginning AR + billings − ending current AR) | Closer to 1 = collecting what's collectible |
| Award close-out exposure | Unbilled + open AR on awards within N days of end date | The money that expires |

## Trend and decomposition formats
**Trend table:** metric × period (12–24 months), one table per segment; totals only alongside
segments, never instead of them.
**Mix decomposition:** ΔTotal = Σ(segment share × segment change) + Σ(share change × segment
level) — report "behavior" (first term) vs "mix" (second) so a sponsor-mix shift isn't read as
a collections change.
**YoY view:** same-period-last-year columns for portfolios with academic/fiscal seasonality.

## Forecast disclosure template
Every forecast carries this block:
- **Method:** <linear trend / seasonal naive / average of last N>
- **Window:** <periods used>
- **Assumptions:** <billing cadence holds, sponsor mix stable, no new major awards, ...>
- **Not modeled:** <award starts/ends, policy changes, disputes>
- **Sensitivity:** <what one bad month does to the number>
If the question needs drivers or confidence intervals, route to
`machine-learning-skills:time-series-forecasting` instead of stretching this.
