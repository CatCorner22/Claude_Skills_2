---
name: public-funds-investing
description: >-
  Invests public and institutional funds under statutory constraint: the safety-liquidity-yield
  hierarchy as law rather than preference, permitted-investment statutes, collateralization of
  public deposits (pledged securities and state collateral pools), local government investment
  pools (LGIPs), delivery-versus-payment custody, and board-approved investment policies for
  public entities. Use when investing public funds, checking an investment or deposit for
  statutory compliance, collateralizing deposits over insurance limits, or evaluating an LGIP.
  Triggers: public funds, permitted investments, collateralization, pledged collateral,
  collateral pool, LGIP, local government investment pool, public deposit, state statute
  investment, public investment policy.
---

# Investing public funds

## When to use
- Investing or advising on operating cash, reserves, or bond proceeds of a public entity
  (state university, municipality, authority) governed by state statute and board policy.
- Checking whether an instrument, deposit, or pool is legal and within policy; setting up or
  monitoring collateralization of public deposits; evaluating an LGIP or state pool.
- Not for: how the instruments themselves work (T-bills, CP, MMFs, yield math) → see
  `finance-skills:short-term-investments`. For drafting the policy document and running the
  periodic holdings-vs-policy compliance check → see
  `treasury-accounting-skills:investment-policy-compliance`. For classifying which monies are
  restricted before investing them → `public-sector-treasury-skills:fund-accounting-gasb`.

## Do it
1. **Establish the legal chain of authority before touching a dollar.** State statute →
   governing-board policy → delegation to named officers. Pull the actual current text of
   your state's permitted-investments statute(s) for your entity type (a Tennessee public
   university, for example, sits under Tennessee's public-funds investment statutes plus any
   system-level policy — confirm the current code sections rather than working from memory
   or summaries). For public funds the default is inverted from corporate practice: anything
   not expressly permitted is prohibited.
2. **Inventory the pots of money and their regimes.** Operating cash, reserves, bond
   proceeds, endowment, and agency/custodial funds may each answer to different law — bond
   indentures and federal arbitrage/rebate rules for proceeds, endowment law for endowments.
   Label each pool with its governing authority; never assume one permitted list covers all.
3. **Apply safety–liquidity–yield as a binding hierarchy.** Test every choice in order:
   does it protect principal, can the money come back when needed, and only then what does
   it earn. In public investing this ordering is typically written into statute or policy,
   so a yield-driven argument that weakens the first two is a legality problem, not a
   preference debate.
4. **Build the working permitted list as an intersection.** Statute ∩ board policy ∩ what
   the team can operationally settle, safekeep, and independently value. Record it as a
   table — instrument, authority citation, limits, maturity cap — so every trade traces to
   a line.
5. **Collateralize deposits above insurance.** Public deposits over federal deposit
   insurance must be secured under your state's scheme: pledged securities at the statutory
   margin held by an independent third-party custodian and revalued on a set cycle, or
   membership in a state collateral pool (Tennessee operates a Collateral Pool for Public
   Deposits; pool membership changes a bank's pledging mechanics — confirm the program's
   current rules). Monitor sufficiency both ways: collateral market value against actual
   balances, especially around deposit spikes like tuition due dates.
6. **Use LGIPs deliberately.** A local government investment pool is a managed portfolio,
   not a bank account: before joining, read its investment policy, portfolio composition,
   rating, and its NAV or amortized-cost basis; re-check periodically. Pools are excellent
   liquidity tiers but concentrate operational reliance in one vehicle.
7. **Settle delivery-versus-payment with third-party custody.** Securities deliver to your
   custodian against payment — never held by the selling dealer — and safekeeping receipts
   name your entity.
8. **Document and report.** Every purchase carries its authority citation; collateral status
   and compliance roll up to the board on a set cadence — package it with
   `public-sector-treasury-skills:treasurer-reporting`.

## Why / learn
Public money is trust money: the entity holds taxes, tuition, and appropriations on behalf
of the public, so the legal architecture is built to make loss nearly impossible and every
decision defensible after the fact. The permitted list is a closed set because statutes are
written from historical failures — leveraged derivatives, repos with unsafekept collateral,
concentration in a single failed bank — and each prohibition is a scar. The
safety-liquidity-yield hierarchy being *law* changes how arguments end: a corporate CFO may
accept more risk for yield, but a public officer making that trade can be acting outside
anyone's authority to decide. Collateralization exists because public balances routinely
exceed deposit insurance and taxpayers cannot be asked to absorb a bank failure; the margin
above the deposit and the independent custodian exist because collateral only protects if it
is worth enough *and* is actually reachable on the day the bank fails. Delivery-versus-payment
is the same idea for securities — the classic failure mode is paying for securities a dealer
never delivered. Statutes, collateral programs, and pool rules are amended regularly; the
durable skill is the structure (authority chain, closed permitted set, secured deposits,
independent custody) plus the habit of confirming the current text of your state's statute
and program rules before acting.

## Common mistakes
- Treating the statute's list as advisory or a starting point → it is the outer boundary; not listed means not legal.
- Working from a remembered or paraphrased statute → codes are amended; pull and cite the current text.
- Assuming deposit insurance covers the balances → most public balances exceed it; collateralize the excess.
- Letting the pledging bank hold its own collateral → use an independent custodian or the state pool; otherwise it may be unreachable in a failure.
- Set-and-forget collateral → balances spike and collateral values drift; monitor both on a schedule.
- Treating an LGIP as a guaranteed bank account → it is a portfolio; do due diligence and repeat it.
- Investing bond proceeds like operating cash → indenture and federal arbitrage/rebate rules apply; involve bond counsel.
- Buying anything the team cannot independently price or safekeep → operational capability is part of "permitted."

## Tailor to your environment
List in `references/your-environment.md`: your governing statute citations and policy
version, entity type, banks and pools used, the collateral arrangement (pledge vs pool,
custodian, monitoring cadence), and the delegation chain. Commit sanitized structure only —
balances, bank exposures, and collateral schedules belong in
`your-environment.private.md` (git-ignored), never in committed files.

## References
- references/statutes-collateral-pools.md — reading a permitted-investments statute, collateral mechanics and monitoring, LGIP due-diligence checklist
- references/your-environment.md — your statutes, policy, banks, and collateral setup (fill in)
