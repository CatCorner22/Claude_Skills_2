# Your short-term-investment environment (sanitized template)

Fill in your real setup. If it names real balances, counterparties, or holdings, keep it in
`your-environment.private.md` instead — that suffix is git-ignored, so raw data never gets committed.
Commit only sanitized, structural examples.

## Cash buckets
| Bucket | Horizon | Minimum balance | Eligible instruments |
|---|---|---|---|
| Operating | <days> | <floor> | <T-bills, gov't MMF, overnight repo> |
| Reserve / buffer | <weeks–months> | <target> | <short T-bills, high-grade CP, NCDs, prime MMF> |
| Strategic / core | <months+> | <target> | <laddered T-bills/CDs to policy max> |

## Investment policy limits
- **Priority:** preservation of principal → liquidity → yield (SLY)
- **Minimum credit quality:** <e.g. A-1/P-1 for CP; min fund rating>
- **Max maturity per holding:** <e.g. 397 days>
- **Max weighted-average portfolio maturity/duration:** <e.g. 90 days>
- **Concentration limits:** <per issuer % | per sector % | per instrument type %>
- **Approved counterparties / dealers / custodians:** <list>
- **Authorized traders & segregation:** <who trades; who settles; who reconciles>

## Reporting
- **Benchmark:** <e.g. 3-month T-bill; iMoneyNet peer>
- **Yield-quote basis:** <bond-equivalent yield; effective annual>
- **Cadence & reviewer:** <weekly/monthly holdings report; who reviews policy compliance>
