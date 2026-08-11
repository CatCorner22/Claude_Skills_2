# Revenue-to-billing reconciliation worksheet (reference)

## Contents
- Reconciliation waterfall format
- Accounting entry map
- GL tie-out worksheet
- Variance-cause table

## Reconciliation waterfall format (per contract, ITD, one as-of date)
```
Recognized revenue (PPM revenue events)                      100,000
− Invoices (accepted, gross)                                  −92,000
+ Credit memos                                                 +4,000
− Rebills (netted with their credits)                          −2,000
= Net billed                                                  −90,000
= Unbilled (positive) / Deferred-overbilled (negative)         10,000
Funding ceiling (contract amount)                             120,000
Headroom: revenue / billing vs ceiling                    20,000 / 30,000
```
Portfolio view: sum positives (→ unbilled receivable account) and negatives (→ deferred/
unearned account) separately — never one netted figure.

## Accounting entry map
| Event | Entry | Effect |
|---|---|---|
| Revenue recognition (PPM Generate Revenue) | DR Unbilled Receivable / CR Revenue | Unbilled grows with earned-not-billed |
| Invoice generated + accepted (AutoInvoice → AR) | DR Trade Receivable / CR Unbilled Receivable | Unbilled relieves into billed AR |
| Billing ahead of revenue (milestone billed early) | DR Trade Receivable / CR Deferred Revenue | Liability until revenue catches up |
| Revenue catches up | DR Deferred Revenue / CR Revenue | Deferred relieves |
| Credit memo | Reverses the invoice legs | Restores unbilled (or reduces deferred) |
| Receipt applied | DR Cash / CR Trade Receivable | Outside this recon's scope (cash side) |
Account names/combinations are configuration — record yours in the environment file.

## GL tie-out worksheet
| Line | Source | Amount |
|---|---|---|
| Σ per-contract positive variances (unbilled) | This reconciliation | |
| GL unbilled receivable account balance | Trial balance, same as-of date | |
| **Difference** | | |
| Σ per-contract negative variances (deferred) | This reconciliation | |
| GL deferred/unearned revenue account balance | Trial balance | |
| **Difference** | | |
Differences decompose into: one stream posted without the other (interface failure), manual
journals against the control accounts (prevent via account rules — same discipline as
`oracle-fusion-finance-skills:fusion-period-close`), conversion/legacy artifacts, and timing
(entries in transit at the as-of date). Name every dollar.

## Variance-cause table (per contract)
| Cause | Signature | Action |
|---|---|---|
| Normal billing lag | Small positive, younger than one billing cycle | None — note the cycle |
| Billing hold/exception | Positive, matching stuck pipeline items | Route to unbilled-billed-ar-wip-recon |
| Method divergence (fixed-price) | Persistent structural variance | Explain once, monitor drift |
| Credits/rebills in flight | Variance = specific linked transactions | Net and re-check |
| Milestone billed ahead | Negative (deferred) | Normal; confirm revenue method timing |
| Over-billing vs funding | Billed > contract funding | Compliance flag — refund exposure; check hard-limit settings |
| Missing revenue events / double billing | Unexplained residual | Escalate as error; correct at source |
| Aged unexplained unbilled | Positive, old, no pipeline match | The finding — investigate before close-out expiry |
