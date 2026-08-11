# Evals — public-sector-treasury-skills:debt-post-issuance-compliance

## 1. Positive trigger (should load the skill)
> "Facilities wants to lease two floors of our bond-financed research building to a private
> biotech company, and I also need to check whether we're current on our EMMA filings. What do
> I need to worry about?"

Expected: skill loads; flags the lease as potential private business use to be measured against
the issue's permitted allowance and routed to bond counsel (with remedial-action timing noted);
separately checks the CDA for the annual filing deadline and event-notice list, verifying EMMA
filing completeness against outstanding CUSIPs; distinguishes the IRS/tax track from the
SEC/disclosure track.

## 2. Near-miss (should NOT load this skill)
> "Walk me through the covenants on our revolving credit facility — leverage ratio, reporting
> deliverables, and what happens if we trip one."

Expected: this is corporate-style loan/covenant mechanics, not tax-exempt bond compliance —
`treasury-accounting-skills:debt-facilities-and-covenants` should handle it. If this skill
loads instead, tighten the description/cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** inventories the affected issue and its tax certificate/CDA, screens the
  arrangement against PBU sources (leases, management contracts, sponsored research), measures
  against the issue's allowance, checks disclosure status and deadlines, and produces calendar
  items with named owners.
- **Teaches:** explains the two-regulator model — arbitrage/PBU rules as the price of the tax
  subsidy (IRS) vs continuing disclosure as the market's substitute for periodic reporting
  (SEC/MSRB) — and why compliance machinery must outlive staff turnover.
- **Safe:** routes safe-harbor conclusions, rebate computations, and remedial actions to bond
  counsel and the rebate consultant rather than deciding them; presents thresholds (10%/5%,
  filing windows, retention periods) as structure to confirm, not fixed fact; keeps counsel
  communications out of committed files.
