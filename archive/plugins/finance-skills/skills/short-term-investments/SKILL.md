---
name: short-term-investments
description: >-
  Evaluates money-market instruments — T-bills, commercial paper, CDs, repos, and money-market funds
  — and builds an approach for investing surplus operating cash under a safety-then-liquidity-then-
  yield priority, including yield-basis conversions, an investment policy statement, and maturity
  laddering. Use when investing surplus or idle cash, comparing money-market instruments, converting
  between discount and bond-equivalent yields, or setting a short-term investment policy. Triggers:
  short-term investment, money market, T-bills, commercial paper, CDs, repo, money market fund,
  investment policy statement, laddering, surplus cash, discount yield, bond-equivalent yield.
---

# Short-term investments

## When to use
- Deciding where to place surplus operating or reserve cash for days-to-months horizons.
- Comparing money-market instruments on risk, liquidity, and a common yield basis.
- Drafting or applying an investment policy statement, or designing a maturity ladder.
- Not for: sizing how much cash to hold and structuring buffers/facilities overall → see
  `cash-management-skills:liquidity-management`. For the discounting/PV math behind yields → see
  `finance-skills:time-value-of-money`.

## Do it
1. **Segment the cash first.** Split balances into **operating** (needed within days — must stay
   liquid), **reserve/buffer** (weeks to a few months), and **strategic/core** (longer, more stable).
   The horizon and certainty of each bucket, not the headline yield, drive what it can hold.
2. **Rank every candidate by S-L-Y, in that order.** Score instruments on **Safety** (credit and
   principal risk) first, **Liquidity** (how fast to cash, at what cost) second, and **Yield** last.
   Yield only breaks ties among options that already clear the safety and liquidity bar for that bucket.
3. **Match instruments to buckets** (see `references/instruments.md` for the full profiles):
   - Operating: T-bills, government money-market funds, overnight repo — cash-like, minimal risk.
   - Reserve: short T-bills/agencies, high-grade commercial paper, negotiable CDs, prime MMFs.
   - Strategic: laddered T-bills/CDs out to the policy's maximum maturity.
4. **Put every yield on the same basis before comparing.** Discount instruments (T-bills, CP) are
   quoted on a **bank discount** basis that uses face value and a 360-day year and *understates* the
   true return; convert to a **bond-equivalent yield (BEY)** so a T-bill and a CD are comparable:
   - Bank discount yield: `(Face − Price)/Face × 360/days`
   - Bond-equivalent yield: `(Face − Price)/Price × 365/days`
   Never rank instruments on mixed yield conventions.
5. **Apply (or draft) the investment policy statement.** Confirm eligible instruments, minimum credit
   quality, maximum maturity and portfolio duration, per-issuer and per-sector concentration limits,
   approved counterparties/dealers, and who is authorized to trade. If none exists, draft one — the
   IPS is the control that keeps "yield" from quietly overriding safety.
6. **Ladder maturities for the reserve/strategic buckets.** Stagger maturities (e.g. equal tranches
   maturing every month) so a portion always matures soon (liquidity) while later tranches capture
   term yield, and reinvestment is spread across rates rather than timed. See `references/instruments.md`.
7. **Document the placement.** For each holding: instrument, issuer/credit, maturity, amount, yield on
   a stated basis, and the bucket/policy limit it sits under — an auditable trail, not a yield table.

## Why / learn
Treasury investing runs on an ordered priority the discipline abbreviates **SLY — Safety, Liquidity,
Yield** — and the order is the entire lesson. This is not the firm's investment portfolio; it is
*operating cash*, money the business will need to pay wages, suppliers, and debt. Losing a few basis
points of yield is an annoyance; being unable to make payroll because the cash was locked up or
impaired is an existential failure. So safety of principal comes first, ready access second, and return
only third — you accept the yield that safe, liquid instruments happen to pay, you do not reach for
yield and hope the risk stays away. That reframes the whole exercise: the job is not "maximize return on
idle cash," it is "preserve and access the cash, and earn what's left over safely." The instrument
profiles fall straight out of this — T-bills and government MMFs sit at the safe, liquid top and pay
least; commercial paper and prime funds add issuer credit risk for a few more basis points; anything
reaching for materially more yield is taking on risk that operating cash should not carry. The yield-
basis conversions matter for the same reason: a discount yield flatters a T-bill by dividing the gain
by face value over a 360-day year, so comparing it raw to a CD's yield tilts you toward the wrong
choice — put both on a bond-equivalent basis first. Laddering and the IPS are how you institutionalize
SLY so that a tempting high-yield name cannot quietly breach the safety and liquidity rules the moment
someone is chasing a number.

## Common mistakes
- Ranking on headline yield → inverts SLY. Clear safety and liquidity first; yield is the tiebreaker.
- Comparing a T-bill's discount yield to a CD's yield raw → convert both to bond-equivalent yield.
- Investing operating cash at a horizon it can't afford → match maturity to when the cash is needed.
- Treating a prime money-market fund as risk-free cash → it can float NAV and impose fees/gates.
- Concentrating in one high-yield issuer → set per-issuer limits; diversify credit exposure.
- No investment policy statement → "yield" silently overrides safety. Write the IPS as the control.
- Assuming FDIC/insurance blanket coverage → it applies to specific products up to specific limits.

## Tailor to your environment
Record your setup in `references/your-environment.md` (or `your-environment.private.md`, git-ignored, if
it names real balances, counterparties, or holdings — never commit real data). Capture your cash-bucket
definitions and minimums, your IPS limits (eligible instruments, credit floor, max maturity/duration,
concentration caps), approved dealers/custodians, benchmark, and reporting cadence. The generic S-L-Y
process then runs against your actual policy.

## References
- references/instruments.md — instrument profiles (risk/liquidity/yield), yield-basis math, IPS contents, and laddering
- references/your-environment.md — your buckets, IPS limits, approved counterparties, and benchmark (add when supplied)
