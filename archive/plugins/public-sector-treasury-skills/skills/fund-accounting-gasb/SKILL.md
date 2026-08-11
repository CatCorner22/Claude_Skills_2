---
name: fund-accounting-gasb
description: >-
  Applies governmental and fund accounting under GASB for public higher-ed: fund types and
  net-position categories (unrestricted, restricted expendable/nonexpendable), GASB vs FASB
  framing, restricted-fund discipline, interfund loans and transfers, and how fund
  restrictions drive cash and investment decisions. Use when classifying funds or net
  position, explaining the GASB treatment of a transaction, handling restricted monies, or
  reading a public university's financial statements. Triggers: fund accounting, GASB, net
  position, restricted funds, unrestricted, expendable, fund balance, governmental
  accounting, public university financials, interfund.
---

# Fund accounting under GASB (public higher-ed)

## When to use
- Classifying money into funds or net-position categories at a public university or other
  GASB-reporting entity, or deciding whether a restriction is real (external) or internal.
- Explaining the GASB treatment of a gift, grant, appropriation, transfer, or bond proceeds —
  and how restrictions constrain what cash may be spent or invested where.
- Reading or explaining a public institution's financial statements (Statement of Net
  Position, SRECNP, direct-method cash flows).
- Not for: FASB/corporate or private-university statements → see
  `accounting-skills:financial-statements`. For actually investing the public monies once
  classified → see `public-sector-treasury-skills:public-funds-investing`.

## Do it
1. **Confirm the framework first.** Public institutions report under GASB (most public
   universities as special-purpose governments engaged in business-type activities); private
   ones under FASB. Statement names, net-position categories, and the cash flow method all
   depend on this. If the statements say "net assets with donor restrictions," you are
   reading FASB, not GASB.
2. **Classify each dollar at receipt by who restricted it.** Only an *external* party —
   donor, grantor, bondholder, statute — creates a restriction. Board or management earmarks
   are *designations* and stay unrestricted. The test: could the board vote tomorrow to
   spend this on something else? If yes, it is not restricted.
3. **Map to the net-position categories** (and your working fund groups):
   - *Net investment in capital assets* — capital assets less related debt.
   - *Restricted nonexpendable* — principal held in perpetuity (true endowment).
   - *Restricted expendable* — spendable, but only for the stated purpose (gifts, grants,
     debt service, capital projects, loan funds).
   - *Unrestricted* — everything else, including board designations.
   Operating ledgers usually keep the classical higher-ed fund groups (current
   unrestricted/restricted, loan, endowment, plant, agency/custodial) — the mapping is in
   `references/gasb-fund-model.md`.
4. **Enforce restricted-fund discipline.** Spend restricted money only on qualifying costs;
   apply the institution's flow assumption consistently (restricted-first vs
   unrestricted-first when either could pay); track restriction satisfaction; and surface —
   rather than quietly cover — any restricted fund running a cash deficit against
   unrestricted cash.
5. **Record interfund activity by its true nature.** A *loan* (due to/due from, repayment
   expected) is not a *transfer* (permanent reallocation — e.g. mandatory debt-service
   transfers vs non-mandatory support). Keep both sides symmetric so they eliminate cleanly
   in entity-wide statements.
6. **Trace restrictions into treasury decisions.** Some restricted balances need separate
   bank accounts or investment treatment (bond proceeds under indenture and arbitrage rules,
   endowment under its own policy, agency funds held for others). The daily cash position
   and any "surplus to invest" figure must net out cash that is legally spoken for.
7. **Read the statements with the GASB lens.** Statement of Net Position uses the
   categories above; the SRECNP splits operating from nonoperating — state appropriations,
   gifts, and investment income are *nonoperating*, so a healthy public university routinely
   shows an operating loss; the cash flow statement is direct-method with four categories.
   Check that the change in net position ties across statements.

## Why / learn
Fund accounting exists because government and university resources arrive with strings
attached, and its job is *accountability* — proving each pool was used as its provider
intended — rather than measuring profit. That is why the categories are organized around
"who may spend this, and on what," not around earnings. The external-vs-internal test in
step 2 is the load-bearing distinction: an external restriction is a legal obligation the
board cannot undo, while a designation is only intent; blurring them either overstates the
institution's flexibility (dangerous) or hides genuinely spendable resources from
decision-makers. The GASB/FASB split matters because imported intuitions mislead: the
operating loss on a public university's SRECNP is an artifact of where GASB parks
appropriations and gifts, not a distress signal, and unrestricted net position is often
deeply negative at institutions carrying pension and OPEB liabilities under GASB standards —
read it with those effects in mind. For a treasury analyst the payoff is the "one bank
account, many funds" model: cash is physically fungible but legally partitioned, so
positioning, sweeping, and investing all start from *whose* dollars these are. GASB
pronouncements evolve (the reporting model, fair value, and fiduciary-activity standards
have all shifted over the years), so anchor on this structure and confirm the current
pronouncement text before citing a specific statement number.

## Common mistakes
- Treating board designations as restricted → only external parties restrict; designations are unrestricted.
- Reading a public university's operating loss as distress → appropriations and gifts are nonoperating by design.
- Netting interfund due-to/due-from, or booking a loan as a transfer → preserve nature and symmetry so eliminations work.
- Covering a restricted-fund cash deficit silently with unrestricted cash → surface it; document authority and repayment.
- Confusing endowment principal (nonexpendable) with its spendable earnings (expendable or unrestricted per the gift terms).
- Citing a GASB statement number from memory → standards are amended and superseded; confirm the current text.
- Applying FASB "net assets with donor restrictions" language to a GASB entity → wrong framework, wrong categories.

## Tailor to your environment
Record your institution's specifics in `references/your-environment.md`: the fund segment
values in your chart of accounts, the fund-group-to-net-position mapping, your flow
assumption, transfer approval authorities, and which funds carry separate bank or investment
treatment. Commit sanitized structure only — real COA extracts, balances, or donor terms go
in `your-environment.private.md` (git-ignored), never in committed files.

## References
- references/gasb-fund-model.md — fund groups, net-position decision tree, GASB vs FASB table, statement walkthrough, interfund matrix
- references/your-environment.md — your fund structure, mappings, and authorities (fill in)
