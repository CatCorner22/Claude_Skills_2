---
name: intercompany-cash-netting
description: >-
  Designs and runs intercompany netting cycles and in-house-bank settlements to cut cross-entity
  payments, float, and FX conversions, and evaluates pooling structures (notional, physical/ZBA,
  POBO/COBO). Use when consolidating intercompany cash, running a bilateral or multilateral netting
  cycle, or assessing an in-house bank or cash-pooling structure. Triggers: netting, intercompany
  netting, netting cycle, bilateral netting, multilateral netting, in-house bank, cash pooling,
  notional pooling, physical pooling, POBO, COBO, settlement cycle.
---

# Intercompany cash netting

## When to use
- Consolidating intercompany payables/receivables so entities settle **net** instead of gross.
- Running a bilateral or multilateral netting cycle, or setting up its calendar and rules.
- Evaluating an in-house bank / POBO-COBO or a notional vs. physical pooling structure.
- Not for: setting group target balances, buffers, and sweeps → see
  `cash-management-skills:liquidity-management`. For hedging the net FX exposure netting leaves behind →
  see `finance-skills:fx-risk-basics`.

## Do it
1. **Decide bilateral or multilateral.** With two entities, **bilateral** netting (offset mutual
   balances into one payment) is enough. With many entities, **multilateral** netting through a
   **netting center** is far more efficient — each participant makes/receives *one* net payment to/from
   the center. See `references/netting-cycle-and-structures.md`.
2. **Set the netting calendar.** Fix the recurring cycle (commonly monthly): an **invoice cutoff**, a
   **matching/dispute window**, the **netting calculation** date, **settlement advices** to
   participants, and the **settlement date**. Everyone books to the same cutoff or the cycle won't tie.
3. **Collect and match intercompany balances.** Gather each entity's intercompany AR and AP, match
   pairs, and quarantine **disputed** items out of this cycle (they distort the net and delay
   settlement). Only agreed balances net.
4. **Handle FX before you net.** Group balances by currency; decide the **settlement currency** per
   participant and let the **netting center bear the FX**, converting at a stated rate. Netting first
   and converting the *net* exposure is what saves the spread — see step in Why. Hedge the residual
   net exposure with `finance-skills:fx-risk-basics`.
5. **Calculate net positions and issue advices.** Compute each participant's single net pay/receive,
   publish advices with the cutoff FX rates, and give a short confirmation window before settlement.
6. **Settle and post.** On the settlement date, each participant settles its **one** net amount with
   the center; post the intercompany clearing and FX entries. Reconcile the netting clearing account
   to zero after the cycle.
7. **(If evaluating a structure) size the in-house bank / pool.** For an **in-house bank**, subsidiaries
   hold internal accounts and the IHB pays/collects externally on their behalf (**POBO/COBO**),
   replacing external accounts with internal ones. For **pooling**, choose **notional** (offset
   balances for interest, no cash moves) or **physical/ZBA** (cash swept to a header). Weigh the
   savings against intercompany-loan, tax, and legal-set-off consequences.

## Why / learn
Netting attacks the cost of *moving* intercompany money, and there are three costs to cut. First,
**transaction cost and float:** every cross-border payment carries a wire fee and a day or two of
float; replacing dozens of gross payments with one net payment per participant collapses both. Second,
**FX spread**, and this is the subtle one — if Entity A owes EUR and Entity B is owed EUR, settling
gross means the group buys and sells the *same* euros and pays the bank's bid-offer spread twice on
money that never needed to leave the group. Netting nets the **exposure first** so you convert only the
true residual, once. That is why FX handling belongs *before* the settlement, not after. Third,
**control and visibility:** a netting center sees every intercompany position in one place, which is
also why disputed items must be pulled out — an unagreed balance dropped into the net turns one
disagreement into a wrong payment for everyone. An **in-house bank** is netting taken to its
conclusion: instead of settling intercompany balances periodically, the IHB *is* the bank for the
group, running internal accounts and paying/collecting externally on subsidiaries' behalf (POBO/COBO)
so most intercompany flows never touch an external bank at all. **Pooling** then optimizes the interest
on what cash remains — notionally offsetting or physically concentrating it. The through-line: the
fewer times money crosses a bank boundary or a currency, the less the group leaks in fees, float, and
spread — netting, in-house banking, and pooling are three depths of the same idea.

## Common mistakes
- Netting disputed balances → one disagreement becomes a wrong net payment for everyone. Quarantine disputes out of the cycle.
- Converting FX after settling gross → you pay the spread twice on offsetting exposures. Net the exposure first, convert the residual.
- Loose or drifting cutoffs → entities book to different dates and the cycle won't tie. Enforce one calendar and cutoff.
- Ignoring tax/legal set-off on pooling → notional/physical pools create intercompany loans with real consequences. Get tax and legal sign-off.
- No confirmation window before settlement → errors settle irreversibly. Publish advices and allow a confirm window.
- Leaving the netting clearing account un-reconciled → breaks hide there. Reconcile it to zero each cycle.

## Tailor to your environment
Drop your real structure into `references/your-environment.md` (keep sensitive figures, entity, and
bank details in `your-environment.private.md`, which is git-ignored): your participating entities and
currencies, your netting calendar and cutoffs, bilateral vs. multilateral and the netting center/
system, your settlement-currency and FX-rate policy, and any in-house-bank / POBO-COBO or pooling
arrangement with its tax/legal notes. Set group targets and buffers with
`cash-management-skills:liquidity-management` and hedge the residual net FX exposure with
`finance-skills:fx-risk-basics`.

## References
- references/netting-cycle-and-structures.md — netting cycle steps, bilateral vs. multilateral, in-house bank, and pooling types
- references/your-environment.md — your entities, calendar, netting center, and pooling setup (add when supplied)
