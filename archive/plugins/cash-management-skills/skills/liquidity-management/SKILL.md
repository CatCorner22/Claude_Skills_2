---
name: liquidity-management
description: >-
  Assesses liquidity buffers and sets target/minimum balances, structures concentration and
  zero-balance sweeps, and decides how to deploy surplus cash or cover a deficit across accounts and
  entities. Use when setting target balances, designing sweeps or a concentration structure, sizing a
  liquidity buffer, or deciding what to do with surplus or short cash. Triggers: liquidity, target
  balance, minimum balance, concentration account, ZBA, cash sweep, liquidity buffer, surplus cash,
  idle cash, cover a shortfall, committed facility.
---

# Liquidity management

## When to use
- Setting target or minimum balances for operating, disbursement, and concentration accounts.
- Designing concentration / zero-balance sweeps or sizing a liquidity buffer against stress.
- Deciding how to deploy surplus cash or how to cover a projected deficit.
- Not for: computing today's available cash or sizing a single sweep amount → see
  `cash-management-skills:cash-positioning`. For selecting the actual instruments to park surplus in →
  see `finance-skills:short-term-investments`. For the account hierarchy itself → see
  `banking-skills:bank-account-structure`.

## Do it
1. **Map the account structure and where cash pools.** List operating, disbursement, payroll, and
   concentration accounts by entity and currency, and how funds currently move between them. You are
   managing liquidity across a *structure*, not one balance — see `references/target-balances-and-sweeps.md`.
2. **Set a minimum and a target balance per account.** The **minimum** is the floor that avoids
   overdraft and covers intraday peaks; the **target** is the level a sweep leaves behind. Base them
   on that account's own outflow pattern, not a round number.
3. **Design the sweeps.** Point subsidiary/disbursement accounts at a **concentration account** via
   **ZBA** (sweep to zero) or **target-balance** sweeps (leave the target). Concentrating balances
   turns many small idle balances into one managed pool and one borrowing/investing decision.
4. **Size the liquidity buffer to stress, not comfort.** Hold a buffer at the concentration/group
   level sized to a defined stress — e.g. *N* days of net outflows or the peak forecast shortfall
   plus a margin — and back it with **committed** facilities (a revolver you can rely on), not just
   uncommitted lines.
5. **Deploy surplus / cover deficit against a policy.** Above the buffer, surplus is **investable**
   (hand instrument selection to `finance-skills:short-term-investments`); below it, cover the deficit
   in the cheapest reliable way (internal transfer, then committed facility draw), and match the tenor
   of the funding to how long you are short.
6. **Set and monitor the policy.** Document minimums, targets, buffer size, approved instruments, and
   facility triggers; review against the cash position and forecast, and re-size when the outflow
   pattern shifts. Liquidity policy is a living calibration, not a one-time set.

## Why / learn
Liquidity management lives on a single trade-off: **idle cash is a drag, and thin cash is a risk.**
Cash sitting in a low-yield account earns less than your cost of capital, so every idle dollar quietly
loses money — but hold too little and you face the far worse outcome of not meeting an obligation:
forced borrowing at a bad rate, a missed payment, a covenant breach. The whole discipline is finding
the balance point and defending it. **Target and minimum balances** encode that point per account, and
**concentration/ZBA sweeps** exist so you make the drag-vs-risk decision *once*, on a single pooled
balance, instead of leaving dozens of small buffers each making it badly. The reason to size the
**buffer to stress rather than to a comfortable round number** is that liquidity risk shows up exactly
when cash flows misbehave — a slow collection month, a pulled facility, a shock — so the buffer must be
calibrated to the bad case, and it must be backed by **committed** capacity, because an uncommitted
line is precisely what disappears when you need it. Getting this right is what lets the surplus above
the buffer be invested with confidence: you can reach for yield because you have already provisioned
for the downside. That is the mental model — *provision for the stress case, then put everything above
it to work* — and it is what separates active liquidity management from just watching the balance.

## Common mistakes
- Setting target balances to round numbers → either idle drag or overdraft risk. Base them on the account's own outflow pattern.
- Leaving cash scattered in many accounts → many small idle buffers and no single decision. Concentrate via sweeps.
- Sizing the buffer to a comfortable level → too thin when flows stress. Size to a defined stress case.
- Relying on uncommitted lines as backup → they vanish when needed. Back the buffer with committed facilities.
- Chasing yield with the buffer itself → liquidity risk for a few basis points. Invest only the surplus above the buffer.
- Setting the policy once and forgetting it → outflow patterns drift. Re-size as the position and forecast change.

## Tailor to your environment
Drop your real structure into `references/your-environment.md` (keep sensitive figures and account
details in `your-environment.private.md`, which is git-ignored): your account hierarchy by entity and
currency, current sweep rules, minimum/target balances, your buffer policy and how it is sized, your
committed and uncommitted facilities with limits and triggers, and your approved surplus-deployment
instruments and limits. This skill sets the targets and buffer; hand the daily sweep sizing to
`cash-management-skills:cash-positioning`, instrument selection to `finance-skills:short-term-investments`,
and cross-entity pooling to `cash-management-skills:intercompany-cash-netting`.

## References
- references/target-balances-and-sweeps.md — setting minimum/target balances, ZBA/concentration sweeps, buffers, and facilities
- references/your-environment.md — your structure, sweeps, buffers, and facilities (add when supplied)
