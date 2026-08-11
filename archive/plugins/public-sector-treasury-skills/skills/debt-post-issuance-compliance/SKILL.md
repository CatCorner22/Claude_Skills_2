---
name: debt-post-issuance-compliance
description: >-
  Maintains post-issuance compliance for tax-exempt debt: arbitrage yield restriction and
  rebate concepts, spend-down expectations for bond proceeds, private business use monitoring
  of bond-financed facilities, continuing disclosure obligations (EMMA filings), record
  retention, and the compliance calendar. Use when monitoring bond compliance, assessing
  private use of a financed facility, preparing or checking continuing disclosure, or
  explaining arbitrage and rebate. Triggers: post-issuance compliance, arbitrage, rebate,
  yield restriction, private business use, continuing disclosure, EMMA, tax-exempt bonds,
  bond compliance, spend-down, bond proceeds.
---

# Debt post-issuance compliance (tax-exempt bonds)

## When to use
- Monitoring an outstanding tax-exempt issue: arbitrage/rebate exposure, proceeds spend-down,
  private business use (PBU), continuing disclosure, record retention.
- Assessing whether a lease, management contract, sponsored-research arrangement, or naming
  deal creates private use of a bond-financed facility.
- Preparing or checking an annual EMMA filing or a material-event notice.
- Building or refreshing the institution's post-issuance compliance calendar and procedures.
- Not for: bank loans, lines of credit, and covenant mechanics on corporate-style debt → see
  `treasury-accounting-skills:debt-facilities-and-covenants`. For the discounting/yield math
  underneath arbitrage concepts → see `finance-skills:time-value-of-money`.

## Do it
1. **Inventory the debt and its governing documents.** For each issue: dated date, par, purpose,
   financed facilities, final maturity, funds and accounts (project/construction fund, reserve,
   escrow), and — critically — the **tax certificate** (the issuer's arbitrage and use covenants,
   signed at closing) and the **continuing disclosure agreement/undertaking (CDA)**. Those two
   documents, not memory, define what compliance means for that issue.
2. **Track arbitrage in two halves.** (a) **Yield restriction**: gross proceeds generally may
   not be invested above the bond yield except during defined **temporary periods** (e.g. a
   project-fund window while proceeds are spent) and in minor allowances; after a temporary
   period expires, restrict the investments or use yield-reduction mechanisms. (b) **Rebate**:
   even where higher-yield investing was allowed, the cumulative excess earnings over the bond
   yield are generally owed to the IRS at periodic **computation dates** (the structure is at
   least every five years and at final redemption — confirm dates per issue). Engage a rebate
   consultant for the computations; your job is clean data — investment records by fund, by
   issue — and the calendar. See `references/compliance-concepts-and-calendar.md`.
3. **Check spend-down expectations.** The tax certificate states expected proceeds expenditure
   (and spending exceptions to rebate exist for fast spenders — 6-month, 18-month, and 2-year
   patterns; confirm which was elected). Maintain a proceeds expenditure schedule per issue;
   slow spend-down versus the certificate's expectations is a flag for counsel, not just a
   footnote.
4. **Monitor private business use continuously.** Inventory bond-financed spaces, then screen
   every arrangement that gives a non-governmental party special legal rights to them: leases,
   **management and service contracts** (safe harbors exist for compensation structures —
   route to bond counsel), **sponsored research** (federal/basic-research safe harbors exist),
   naming/sponsorship rights, cell-tower and food-service arrangements, and joint ventures.
   Measure PBU as a percentage of proceeds/use per issue against the small permitted allowance
   (structurally around 10%, tighter for unrelated or disproportionate use — confirm per issue);
   if a change of use threatens the limit, **remedial action** provisions exist, but only if
   caught and taken promptly.
5. **Deliver continuing disclosure on time.** From the CDA, extract: what annual financial
   information and operating data is promised, the filing deadline (measured from fiscal year
   end), and the enumerated **material events** (rating changes, defeasances, bond calls,
   payment defaults, financial-obligation events, etc. — the current list comes from SEC Rule
   15c2-12) that must be filed on **EMMA** within the rule's short window (structurally 10
   business days). Assign an owner for *watching for events*, not just for filing; log every
   filing with date and confirmation.
6. **Retain records as if the IRS will ask in 20 years.** Keep the transcript, expenditure and
   requisition detail, investment records, rebate computations, PBU contracts and analyses, and
   disclosure filings for the life of the bonds **plus any refunding chain plus** the audit
   tail (structurally ~3 years after final redemption of the last refunding — confirm). A
   refunding extends the clock on the *original* issue's records.
7. **Assemble the compliance calendar and written procedures.** One calendar across issues:
   rebate computation dates, CDA filing deadlines, annual PBU questionnaire to facility/contract
   owners, records checkpoints. Written post-issuance procedures with named roles are expected
   practice (and asked about in IRS questionnaires and future offering diligence). Escalation
   rule: this skill explains concepts and builds the monitoring machinery; **conclusions about
   tax consequences, safe harbors, and remedial actions go to bond counsel and the rebate
   consultant.**

## Why / learn
Tax-exempt debt is a bargain with two different regulators, and post-issuance compliance is
keeping both promises for decades. The **tax side (IRS)**: investors accept a lower yield
because interest is exempt, so the issuer promises not to exploit the subsidy — **arbitrage
rules** stop you borrowing at tax-exempt rates to invest at taxable rates (yield restriction
limits the investing; rebate claws back allowed excess), and **private business use rules**
stop private parties enjoying subsidized facilities the public paid for. Breach the tax
covenants badly enough and the bonds can become retroactively taxable — a bondholder harm the
issuer must then fix through settlement programs. The **securities side (SEC/MSRB)**:
municipal issuers sell into a market with no ongoing registration, so **continuing disclosure
via EMMA** is the market's substitute for periodic reporting; failures don't tax the bonds, but
they must be disclosed in future offerings and damage market access and pricing. Keeping the
two regimes mentally separate tells you where each obligation comes from and what failure
costs. The deepest operational truth: bonds outlive the people who issued them. Compliance
failures are rarely acts of bad faith — they are a lease signed by a department that never
heard of PBU, an event notice nobody was watching for, records purged on a normal retention
schedule. That is why the deliverables of this skill are *institutional memory*: a calendar,
written procedures, an annual questionnaire, and a records vault.

## Common mistakes
- Treating compliance as finished at closing → the obligations start at closing and run to
  final maturity (and beyond, through refundings).
- Screening only leases for private use → management contracts, sponsored research, naming
  rights, and rooftop/cell agreements create PBU too; screen anything granting special rights.
- Missing event notices because no one owns *detecting* events → assign a watcher for rating
  actions, defeasances, and new financial obligations, separate from the annual filing owner.
- Letting investment records live only in the bank/custodian portal → you need issue-level,
  fund-level records for rebate computations years later; extract and archive them.
- Applying the institution's normal records-retention schedule to bond files → bond records
  outlive it; life-of-bonds-plus-refundings-plus-audit-tail.
- Doing rebate math or safe-harbor calls in-house without review → concepts here, computations
  and legal conclusions to the rebate consultant and bond counsel.
- Ignoring slow spend-down → it can void expected rebate exceptions and raises hedge-bond-type
  questions; flag it early.

## Tailor to your environment
Record your real debt landscape in `references/your-environment.md`: the list of outstanding
issues with their tax certificates and CDAs, your rebate consultant and bond counsel, computation
and filing dates, who answers the annual PBU questionnaire per facility, and where the records
vault lives. Keep anything sensitive — internal legal analyses, draft filings, counsel
communications — in `your-environment.private.md`, which is git-ignored; never commit real
data. Thresholds, safe harbors, and the Rule 15c2-12 event list evolve — record *who confirms
current requirements* (bond counsel, rebate consultant, NABL/GFOA guidance) rather than pinning
regulatory numbers here.

## References
- references/compliance-concepts-and-calendar.md — arbitrage/rebate mechanics, spend-down
  exception structure, PBU measurement and screening list, EMMA filing types, calendar template
- references/your-environment.md — your issues, advisors, deadlines, owners (add when supplied)
