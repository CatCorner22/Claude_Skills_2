# Ratio catalog and DuPont (reference)

## Contents
- Liquidity (short-term solvency)
- Leverage / solvency
- Profitability
- Efficiency (activity)
- DuPont decomposition (3-step and 5-step)
- Interpretation caveats

Convention: when a ratio pairs an income-statement flow with a balance-sheet stock (ROA, ROE, all
turnover ratios), use the **average** balance `(opening + closing) / 2`. Pure balance-sheet ratios
(current, quick, D/E) use period-end figures.

## Liquidity (short-term solvency)
| Ratio | Formula | Higher means |
|---|---|---|
| Current ratio | `Current Assets / Current Liabilities` | more short-term cover (too high can signal idle assets) |
| Quick / acid-test | `(Current Assets − Inventory − Prepaids) / Current Liabilities` | cover excluding hard-to-sell inventory |
| Cash ratio | `(Cash + Cash equivalents) / Current Liabilities` | cover from cash alone (most conservative) |

## Leverage / solvency
| Ratio | Formula | Reads as |
|---|---|---|
| Debt-to-equity | `Total Debt / Total Equity` | financing mix (define "debt": interest-bearing vs total liabilities) |
| Debt-to-assets | `Total Debt / Total Assets` | share of assets financed by debt |
| Equity multiplier | `Total Assets / Total Equity` | leverage factor used in DuPont |
| Interest coverage (TIE) | `EBIT / Interest Expense` | how many times operating profit covers interest |

State the debt definition explicitly — "debt" as only interest-bearing borrowings gives a very
different D/E than "debt" as total liabilities.

## Profitability
| Ratio | Formula |
|---|---|
| Gross margin | `Gross Profit / Revenue` |
| Operating margin | `EBIT / Revenue` |
| Net margin | `Net Income / Revenue` |
| Return on assets (ROA) | `Net Income / Average Total Assets` |
| Return on equity (ROE) | `Net Income / Average Total Equity` |

## Efficiency (activity)
| Ratio | Formula | Related day-metric |
|---|---|---|
| Asset turnover | `Revenue / Average Total Assets` | — |
| Inventory turnover | `COGS / Average Inventory` | `DIO = 365 / turnover` |
| Receivables turnover | `Credit Sales / Average AR` | `DSO = 365 / turnover` |
| Payables turnover | `COGS / Average AP` | `DPO = 365 / turnover` |

(Day-metrics and the cash conversion cycle live in `finance-skills:working-capital-management`.)

## DuPont decomposition
- **3-step** — splits ROE into operating profitability, asset efficiency, and leverage:
  `ROE = (NI / Sales) × (Sales / Assets) × (Assets / Equity)`
  `    = Net margin × Asset turnover × Equity multiplier`
- **5-step (extended)** — further splits net margin to separate operations from financing and tax:
  `ROE = (NI/EBT) × (EBT/EBIT) × (EBIT/Sales) × (Sales/Assets) × (Assets/Equity)`
  `    = Tax burden × Interest burden × Operating margin × Asset turnover × Equity multiplier`
  - Tax burden `NI/EBT` < 1 (the fraction of pre-tax income kept after tax).
  - Interest burden `EBT/EBIT` < 1 (the fraction of operating income left after interest).
  Use the 5-step to tell whether ROE is earned in operations or manufactured with leverage/tax effects.

## Interpretation caveats
- **Benchmark or trend, always.** A ratio's meaning is relative — peer group, own history, or target.
- **Industry structure differs.** High-turnover/low-margin (retail) vs low-turnover/high-margin (software)
  reach the same ROE by opposite routes; do not cross-apply norms.
- **Averages vs point-in-time.** Seasonal businesses distort period-end balance-sheet ratios.
- **Accounting policy.** LIFO vs FIFO, capitalize vs expense, lease treatment — normalize before peers.
- **One-time items.** Strip non-recurring gains/losses/impairments before drawing a trend.
- **Unstable denominators.** Near-zero equity or negative EBIT make D/E and coverage meaningless.
- **Window dressing.** Period-end actions can flatter liquidity ratios; corroborate with the trend.
