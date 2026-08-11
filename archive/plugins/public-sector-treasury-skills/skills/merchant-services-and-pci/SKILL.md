---
name: merchant-services-and-pci
description: >-
  Runs merchant card acceptance for an institution: the acquiring stack (merchant IDs/MIDs,
  acquirer, processor, gateways), settlement and funding flows into depository accounts,
  interchange and fee structures and how to read a merchant statement, chargeback and dispute
  handling, and PCI-DSS fundamentals (scope minimization, SAQ types, never storing PANs). Use
  when managing MIDs, reconciling card settlements to bank deposits, reviewing merchant fees,
  handling a chargeback, or answering PCI compliance questions. Triggers: merchant services,
  MID, merchant ID, card settlement, interchange, merchant statement, chargeback, dispute,
  PCI, PCI-DSS, SAQ, card acceptance, gateway, acquirer, merchant fees.
---

# Merchant services and PCI

## When to use
- Managing the institution's merchant accounts: opening/closing MIDs for departments, mapping
  MIDs to depository accounts, keeping the MID inventory current.
- Reconciling card settlement batches to bank deposits, or explaining a deposit that doesn't
  match the day's sales.
- Reviewing a merchant statement, computing the effective rate, or challenging fees.
- Working a chargeback/dispute, or answering PCI-DSS scope and SAQ questions.
- Not for: matching those settlement deposits inside a full bank reconciliation → see
  `cash-management-skills:bank-reconciliation`. For analyzing *depository bank* service charges
  (account analysis statements) → see `banking-skills:bank-fee-analysis`.

## Do it
1. **Map the acceptance stack first.** For each acceptance point, identify: the **MID** (and any
   chain/parent hierarchy), the **gateway** (the software doorway that captures the card), the
   **processor/acquirer** (the bank-side entity that clears and settles), which **card networks**
   are accepted, and the **depository account** each MID funds to. Most confusion downstream is
   an unmapped stack — a university typically has many department MIDs (bookstore, athletics,
   parking, clinics, online tuition) behind one or two acquirers.
2. **Trace the settlement/funding flow.** Card sale → daily **batch close** → acquirer settles →
   deposit to your DDA, typically 1–2 banking days later (confirm your funding schedule).
   Establish two facts per MID: **gross vs net funding** (are fees deducted daily from the
   deposit, or billed monthly?) and the **batch cutoff time** (sales after cutoff roll to the
   next batch). American Express and some networks may fund separately on their own timing.
3. **Reconcile settlements to deposits.** Join on **MID + batch date + amount**: batch/settlement
   report on one side, bank statement deposit lines on the other. Expected mismatches: net-funded
   fees, weekend/holiday batches funding together, separate Amex deposits, chargebacks and
   reserves netted out. Anything else is an exception — trace it to a specific batch before
   calling it a bank problem.
4. **Read the merchant statement in three layers.** Total cost = **interchange** (set by the card
   networks, paid to the card issuer, non-negotiable) + **assessments** (network fees,
   non-negotiable) + **processor markup** (the only negotiable layer). Identify your pricing
   model — **interchange-plus** (transparent: each layer shown), **tiered** (qualified /
   mid-qualified / non-qualified buckets that hide downgrades), or **flat-rate**. Compute the
   **effective rate** = total fees ÷ card volume, per MID, and trend it monthly. Investigate
   downgrade line items and any "PCI non-compliance" fee (that one means paperwork is overdue,
   not that rates changed). See `references/merchant-economics-and-pci.md`.
5. **Work chargebacks on the clock.** Lifecycle: (sometimes) retrieval request → **chargeback**
   (provisional debit to you) → **representment** (your evidence) → pre-arbitration/arbitration.
   Response windows are short and set by the card-brand rules — confirm current deadlines with
   your acquirer. Read the **reason code** family first (fraud vs. "not received" vs. processing
   error vs. authorization), assemble the matching evidence, and track outcomes by department to
   fix root causes (e.g. unclear billing descriptors drive "unrecognized" disputes).
6. **Manage PCI-DSS by shrinking scope.** The cardholder data environment (CDE) is every system
   that stores, processes, or transmits card data — so the cheapest compliance is to not touch
   the data: hosted payment pages, validated **P2PE** terminals, and **tokenization** push the
   PAN out of your systems. Hard floor regardless of scope: never store the PAN outside
   validated systems (spreadsheets, email, paper logs), and never store CVV/track data after
   authorization, encrypted or not. Validation is typically an annual **SAQ** (which SAQ type
   depends on your acceptance channel — see the reference) plus quarterly scans where required;
   merchant level (by transaction volume) sets how formal validation must be. Confirm the
   current PCI-DSS version and SAQ criteria with your acquirer or QSA.
7. **Govern centrally.** Keep a MID inventory (owner, acceptance channel, gateway, funding
   account, SAQ type, last validation date), require treasury sign-off before any department
   signs a processing or gateway agreement, run an annual fee review per MID, and write the
   incident-response path for a suspected card-data compromise before you need it.

## Why / learn
The card system is a four-party network — cardholder, issuer, network, and acquirer/merchant —
and the economics follow the risk: **interchange flows to the issuer** because the issuer fronts
the cardholder's money and eats most fraud losses, the network takes assessments for running the
rails, and your processor adds markup for its service. That is why only the markup is negotiable,
why interchange-plus pricing is the honest model (you see each layer), and why tiered pricing
ages badly — downgrades quietly reclassify transactions into expensive buckets. It is also why
data quality is money: transactions that arrive with better data (card-present, AVS-matched,
Level II/III detail on corporate and government cards) qualify for lower interchange categories.
**Chargebacks** exist because the network grants cardholders a dispute right; the merchant bears
the burden of proof, which is why evidence discipline and deadlines beat indignation.
**Settlement funding** is the whole multi-party chain collapsing into one bank deposit — so
reconciliation must join at the batch level, not eyeball daily totals. And **PCI is a scoping
exercise before it is a controls exercise**: every requirement applies only to systems that
touch cardholder data, so the strategic move is architectural (outsource, tokenize, P2PE), not
heroic patching of systems that never needed the data. For a decentralized public university the
governance point is the real lesson: any department can start taking cards with a web signup,
but the institution holds the compliance and financial risk — central MID inventory and
sign-off is the control.

## Common mistakes
- Reconciling gross sales to a net-funded deposit (or vice versa) → know each MID's funding
  basis before calling a break.
- Judging cost by the headline "rate" instead of the effective rate per MID → downgrades,
  monthly fees, and non-compliance fees hide outside the quoted rate.
- Missing Level II/III data on government/corporate card volume → paying higher interchange
  than the same transactions would qualify for with better data.
- Blowing a chargeback deadline → an automatic loss regardless of merits. Calendar the windows.
- Storing PANs "temporarily" in spreadsheets, email, or call recordings → instant scope
  explosion and a likely violation; use tokens or reference numbers instead.
- Treating the gateway as the acquirer → they are different contracts, fees, and support paths;
  outages and fee disputes go to different parties.
- Letting departments sign their own processing agreements → orphan MIDs, unknown SAQ posture,
  and deposits landing in unmapped accounts.

## Tailor to your environment
Record your real acceptance landscape in `references/your-environment.md`: acquirer(s) and
gateway(s), the MID inventory (department, channel, funding account, gross/net funding, batch
cutoff), your pricing model per MID, who works chargebacks, and your SAQ type(s) and validation
cycle. Keep anything sensitive — actual MID numbers, negotiated pricing, account numbers,
compromise history — in `your-environment.private.md`, which is git-ignored; never commit real
data. Card-brand rules, interchange tables, and PCI-DSS versions all change on their own
schedules — record *who you confirm current requirements with* (acquirer rep, QSA, brand
bulletins) rather than pinning numbers here.

## References
- references/merchant-economics-and-pci.md — fee anatomy and statement reading, chargeback
  lifecycle and reason-code families, PCI scope-reduction options and SAQ landscape
- references/your-environment.md — your acquirers, MID inventory, pricing, SAQ posture (add
  when supplied)
