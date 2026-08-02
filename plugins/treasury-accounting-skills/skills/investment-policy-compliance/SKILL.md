---
name: investment-policy-compliance
description: >-
  Writes and enforces a corporate investment policy for excess cash — permitted instruments and
  ratings, concentration and counterparty limits, maturity/liquidity tiers matched to the cash
  forecast, and the monthly compliance check that proves the portfolio sits inside policy, plus
  the exception/waiver process when it doesn't. Use when drafting or updating an investment
  policy statement, checking holdings against policy, setting counterparty or concentration
  limits, or handling a rating downgrade or policy breach. Triggers: investment policy, IPS,
  permitted investments, counterparty limit, concentration limit, rating downgrade, policy
  compliance check, excess cash investment, money market fund policy, portfolio compliance,
  investment guidelines.
---

# Investment policy and compliance

## When to use
- Drafting or refreshing an investment policy statement (IPS) for corporate cash, or adapting
  limits after the cash balance, rates, or bank landscape changes.
- Running the periodic compliance check: holdings vs permitted instruments, ratings,
  concentration, and maturity limits — and working an exception (downgrade, breach, waiver).
- Not for: what the instruments are and how they yield → see
  `finance-skills:short-term-investments`. For how much cash is investable and for how long →
  see `cash-management-skills:cash-forecasting` and
  `cash-management-skills:liquidity-management`.

## Do it
1. **Order the objectives and mean it: safety, liquidity, yield.** Every policy decision flows
   from that ranking — corporate cash exists to fund the business, so return is what you earn
   *after* principal and access are protected. Write the objectives clause first; every later
   argument about a tempting yield gets settled by pointing at it.
2. **Tier the portfolio to the cash forecast.** Split investable cash by horizon:
   **operating** (0–30 days: overnight MMFs, deposits), **reserve** (1–6 months: T-bills, CP,
   CDs laddered to forecast needs), **strategic** (6–12+ months, only for cash the forecast
   says you won't touch). The forecast drives the tiers — invest long only what liquidity
   analysis proves is idle.
3. **Define permitted instruments with hard edges.** A table, not prose: instrument, minimum
   rating (e.g. A-1/P-1 short-term; AA- for MMF portfolios), maximum maturity, maximum % of
   portfolio and $ per issuer/fund. Explicitly *prohibit* what you don't want argued about
   later (equities, crypto, structured notes, anything the team can't price independently).
   `references/policy-template.md` has a full skeleton with typical limit ranges.
4. **Set counterparty and concentration limits on entities, not products.** Aggregate *all*
   exposure to a bank group — deposits, CDs, CP, plus positive derivative MTM (tie in
   `treasury-accounting-skills:hedging-and-derivatives`) — against one limit per counterparty,
   scaled to its rating tier. Diversification limits (max % per issuer, per fund, per asset
   class) protect against the failure you didn't predict.
5. **Run the compliance check on a schedule, from custody data.** Monthly (weekly in stress):
   pull holdings from custodian/portal statements — not the trader's spreadsheet — and test
   every position against the tables: permitted? rating current? issuer within limit? maturity
   within cap? weighted-average maturity within policy? Document the result even when it's
   all-clear; a compliance check that only fires on breaches proves nothing to an auditor.
6. **Handle exceptions with a process, not improvisation.** A downgrade below policy or a
   passive breach (a limit tripped by the portfolio shrinking) triggers: report it, assess
   (hold to maturity vs sell — forced same-day selling of a sound credit is often the worse
   trade), decide at the authority the policy names, and time-bound any waiver in writing.
   Active breaches (someone bought outside policy) are control failures — escalate as such.
7. **Review the policy annually and get it re-approved** (board or committee, per governance).
   Rates, bank health, and the company's cash profile drift; a stale policy is either violated
   or irrelevant. Log changes so the audit trail shows the policy evolving deliberately.

## Why / learn
An investment policy is a *pre-commitment device*: it makes the safety-liquidity-yield ranking
binding before anyone is staring at an extra 40 basis points. Every mechanism in it exists
because some treasury lost money without one — concentration limits are the lesson of single-bank
failures (uninsured deposits over one weekend), rating floors and the entity-level counterparty
view are the lesson of chasing yield into paper that froze, and the "prohibited" list is the
lesson that anything not explicitly excluded eventually gets proposed. The tiering logic is just
liability matching brought down to cash: the forecast defines when money is needed, so maturity
risk is taken only where the forecast proves slack. The compliance ritual matters as much as the
rules — testing from custody data keeps the checker independent of the doer (the same
segregation instinct as `cash-management-skills:cash-management-controls`), and documenting
all-clear runs is what turns "we have a policy" into "we can prove we follow it." And the
exception process exists because markets move faster than committees: a downgrade isn't a
scandal, but an undocumented, undecided response to one is.

## Common mistakes
- Yield creep: stretching maturity or credit for basis points → re-read the objectives clause; safety and liquidity outrank.
- Limits per product instead of per entity → three "small" exposures to one bank group is one big one; aggregate.
- Investing the strategic tier on hope → only the forecast's provably idle cash goes long.
- Compliance checked from the trader's own records → custody statements; separate the checker from the doer.
- No documentation of clean checks → unprovable compliance; write down the all-clears.
- Auto-selling on every downgrade → assess hold-to-maturity vs sale; a panic sale of sound paper realizes the loss the policy tried to avoid.
- Policy never re-approved → drifts into irrelevance or silent violation; annual review with change log.
- Vague prohibitions ("exotic instruments") → name them; ambiguity is where the bad trade lives.

## Tailor to your environment
Put your actual policy parameters in `references/your-environment.md` (approved policy document
and holdings in `your-environment.private.md`, git-ignored): tiers and their sizes, permitted
instrument table, counterparty list with limits, check cadence and owner, and the exception
authority chain. **Never commit real holdings, balances, or counterparty exposures.**

## References
- references/policy-template.md — IPS skeleton with typical limit ranges and the compliance-check worksheet
- references/your-environment.md — your tiers, limits, counterparties, and owners (fill in)
