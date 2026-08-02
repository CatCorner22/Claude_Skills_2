# Money-market instruments, yield basis, and laddering (reference)

## Contents
- Instrument profiles (safety / liquidity / yield)
- Yield conventions and conversions
- Investment policy statement (IPS) contents
- Laddering

## Instrument profiles
Ordered roughly safest/most-liquid first. "Yield" is relative within the money market — all are low.

| Instrument | What it is | Safety | Liquidity | Yield | Notes |
|---|---|---|---|---|---|
| Treasury bills | Short-term government debt, sold at a discount | Highest (sovereign) | Highest (deep secondary market) | Lowest | Quoted on bank-discount basis |
| Government MMF | Fund holding Treasuries/agencies/repo | Very high | Daily (same-day) | Low | Stable NAV; not FDIC-insured |
| Repo (repurchase agreement) | Collateralized loan vs securities, often overnight | High (collateralized) | Overnight/term | Low | Credit ≈ collateral quality + haircut |
| Agency discount notes | Short debt of gov't-sponsored agencies | Very high | High | Low+ | Slight spread over Treasuries |
| Negotiable CDs | Bank time deposits, tradeable | High (bank credit) | Secondary market; term to maturity | Low+ | FDIC only for non-negotiable up to the limit |
| Bankers' acceptances | Bank-guaranteed trade drafts | High (bank credit) | Moderate | Low+ | Discount instrument, trade finance |
| Commercial paper (CP) | Unsecured short corporate debt, ≤270 days | Issuer credit risk | Limited (mostly held to maturity) | Higher | Rated; A-1/P-1 tier for quality |
| Prime MMF | Fund holding CP/CDs/repo | Moderate (credit) | Daily, but subject to fees/gates | Higher | Institutional prime can **float NAV** |

Key risk reminders: money-market funds are **not** bank deposits and are not FDIC-insured; prime and
some institutional funds can float their NAV and impose liquidity fees or redemption gates under stress.
FDIC/insurance coverage applies to specific deposit products up to specific limits — never assume a
blanket guarantee.

## Yield conventions and conversions
Discount instruments (T-bills, CP, BAs) are quoted on a **bank discount** basis that uses **face value**
and a **360-day** year — which understates the true return. Convert before comparing:

- Bank discount yield: `d = (Face − Price)/Face × 360/days`
- Money-market yield (CD-equivalent, 360-day): `(Face − Price)/Price × 360/days`
- Bond-equivalent yield (BEY, investment yield): `(Face − Price)/Price × 365/days`
- From discount to price: `Price = Face × (1 − d × days/360)`

BEY is higher than the discount yield for the same instrument because it divides the gain by **price**
(what you actually invested) and uses **365** days. Always compare instruments on the *same* basis —
ideally BEY — and, for multi-period comparisons, on an effective annual basis.

## Investment policy statement (IPS) contents
A short-term IPS is the control that keeps SLY intact. It should specify:
- **Objective and priority:** preservation of principal, then liquidity, then yield (SLY).
- **Eligible instruments** and any explicitly prohibited ones.
- **Minimum credit quality** (e.g. A-1/P-1 for CP; minimum fund rating).
- **Maximum maturity per holding** and **maximum weighted-average portfolio maturity/duration**.
- **Concentration limits** per issuer, per sector, and per instrument type.
- **Approved counterparties, dealers, and custodians.**
- **Authorized personnel** and segregation of trading vs settlement vs reconciliation.
- **Benchmark and reporting** cadence.

## Laddering
Split the investable amount into tranches maturing at staggered dates (e.g. equal amounts maturing each
month out to the policy maximum). Benefits:
- A tranche always matures soon → recurring **liquidity** without selling early.
- Reinvestment is spread across dates → dampens **reinvestment/rate risk** vs a single maturity.
- Captures more **term yield** than holding everything overnight, without a big duration bet.
Rebuild the ladder as tranches mature by reinvesting at the long end.
