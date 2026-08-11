# Reconciliation schedule, roll-forward, and risk-ranking (reference)

## Contents
- Reconciliation header
- Point-in-time supporting schedule
- Roll-forward format
- Reconciling-item classification and aging
- Risk-ranking matrix and frequency
- Support source by account type

## Reconciliation header
Every rec states, up front:
- Account (number + name), entity, currency, as-of date
- **GL balance** (from the trial balance)
- **Supported balance** (from the independent schedule)
- **Difference** = GL − supported (must be fully explained by classified reconciling items)
- Preparer / date, Reviewer / date, risk rating

## Point-in-time supporting schedule
For accounts that are a list of components at a date. The component total must equal the supported balance.
```
Component / item          Amount     Source / evidence
-----------------------   --------   ------------------------
<item 1>                   x,xxx      <contract / invoice / confirmation>
<item 2>                   x,xxx      <...>
-----------------------   --------
Supported balance          xx,xxx
GL balance                 xx,xxx
Difference                     xx     <explained by reconciling items below>
```

## Roll-forward format
For activity-driven accounts (fixed assets, prepaids, accruals, debt). Proves the *movement*, not just the ending
number.
```
Opening balance (= prior close)        xx,xxx
  + Additions                           x,xxx     <new prepaids / assets / accruals>
  - Reductions (amortization/usage)    (x,xxx)    <expensed / reversed / paid / disposed>
  +/- Other adjustments                    xxx
--------------------------------------  -------
Closing balance (per schedule)         xx,xxx
Closing balance (per GL)               xx,xxx
Difference                                  --    <should be zero or fully explained>
```

## Reconciling-item classification and aging
Each item goes in exactly one bucket:
| Bucket | Meaning | Action |
|---|---|---|
| Timing | Self-clears next period | Carry; confirm it clears |
| Error / misclassification | GL is wrong | Post a correcting entry now |
| Unsupported / unknown | No evidence yet | Investigate — highest risk |

Age open items and escalate the old ones:
| Age bucket | Typical treatment |
|---|---|
| 0–30 days | Normal; monitor |
| 31–60 days | Explain; assign owner |
| 61–90 days | Escalate; likely error, not timing |
| 90+ days | Findings — resolve or write off with approval |

## Risk-ranking matrix and frequency
Rate each account on the factors below; the highest factor drives the rating.
| Factor | Low | Medium | High |
|---|---|---|---|
| Balance size / materiality | small | moderate | large |
| Volatility of activity | stable | some | high |
| Estimation / judgment | none | some | significant |
| Error history | clean | occasional | recurring |

| Rating | Frequency | Rigor |
|---|---|---|
| High | Every period | Full schedule + independent review |
| Medium | Monthly/quarterly | Schedule + review |
| Low | Quarterly or as policy allows | Lighter support; periodic review |

## Support source by account type (independent of the GL)
| Account | Independent support |
|---|---|
| Prepaids | Amortization schedule from underlying contracts/invoices |
| Accruals | Accrual detail / estimate basis; subsequent invoices |
| Fixed assets | Fixed-asset register (cost, accumulated depreciation) |
| Intercompany | Counterparty confirmation / IC matching report |
| Debt | Lender amortization schedule / loan statement |
| Inventory | Inventory subledger / physical count |
| Accrued payroll | Payroll register / provider report |
