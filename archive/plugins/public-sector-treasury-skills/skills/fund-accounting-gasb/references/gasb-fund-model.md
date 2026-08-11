# The GASB fund model for public higher-ed (reference)

Structure-first reference. Category definitions here are stable; specific pronouncement
numbers and thresholds change over time — confirm the current GASB text (gasb.org) and your
auditor's guidance before citing.

## Contents
- Decision tree: classifying a dollar
- Higher-ed fund groups and the net-position mapping
- GASB vs FASB side by side
- Statement walkthrough
- Interfund activity matrix
- Restrictions → treasury decisions
- Pronouncements to confirm

## Decision tree: classifying a dollar

1. **Is it ours at all?** Money held purely for others (student clubs, agency deposits,
   custodial arrangements) is a liability/fiduciary balance, not institutional net position.
2. **Did an external party constrain its use?** Donor gift agreement, grant award terms,
   bond indenture, statute or enabling legislation → **restricted**. Board vote, management
   plan, internal budget → **unrestricted** (a designation at most).
3. **If restricted: must principal be maintained in perpetuity?** Yes → **restricted
   nonexpendable** (true endowment corpus). No → **restricted expendable**, sub-categorized
   by purpose (scholarships, research, loans, capital projects, debt service).
4. **Is it a capital asset or capital-related debt?** These net into **net investment in
   capital assets** regardless of the funding story.
5. Everything remaining is **unrestricted** — the only category leadership can redirect.

Edge cases worth pausing on:
- **Quasi-endowments** ("funds functioning as endowment"): board-created, so *unrestricted*
  in net position even though managed like endowment.
- **Endowment earnings**: classified by the gift terms — often restricted expendable for the
  stated purpose; unrestricted only if the donor left use open.
- **Unspent bond proceeds**: restricted expendable (capital), and additionally governed by
  the indenture and federal tax rules — a treasury flag, not just an accounting one.
- **Grant advances vs reimbursements**: an advance received before conditions are met may be
  a liability (unearned), not restricted net position yet.

## Higher-ed fund groups and the net-position mapping

Operating ledgers often still carry the classical fund groups; external statements collapse
them into net-position categories:

| Working fund group | Typical contents | Net-position category |
|---|---|---|
| Current unrestricted | Tuition, appropriations, sales/services | Unrestricted |
| Current restricted | Gifts and grants spendable for a purpose | Restricted expendable |
| Loan funds | Institutional/federal student loan pools | Restricted expendable (per program terms) |
| Endowment — true | Donor corpus held in perpetuity | Restricted nonexpendable |
| Endowment — quasi | Board-designated corpus | Unrestricted |
| Plant — unexpended | Unspent capital funding, bond proceeds | Restricted expendable (capital) |
| Plant — investment in plant | Capital assets and related debt | Net investment in capital assets |
| Agency/custodial | Money held for others | Not net position (liability/fiduciary) |

Your institution's chart of accounts implements this through a fund segment — record the
actual values and mapping in `your-environment.md`.

## GASB vs FASB side by side

| Dimension | GASB (public) | FASB (private/nonprofit) |
|---|---|---|
| Equity term | Net position | Net assets |
| Categories | Net investment in capital assets; restricted (nonexpendable/expendable); unrestricted | With donor restrictions; without donor restrictions |
| Operating statement | SRECNP with operating/nonoperating split defined by GASB | Statement of activities |
| Appropriations, gifts | Nonoperating revenue | Generally within operating support |
| Cash flow statement | Direct method, four categories | Indirect method common, three categories |
| Deferred outflows/inflows | Separate statement elements | Not used |
| Typical "optics" trap | Operating loss by design; negative unrestricted from pension/OPEB | Restriction detail lives in the notes |

## Statement walkthrough

- **Statement of Net Position**: assets + deferred outflows − liabilities − deferred inflows
  = net position, presented in the categories above. Scan restricted categories against the
  treasury view: does restricted cash/investments cover restricted net position?
- **SRECNP** (Statement of Revenues, Expenses, and Changes in Net Position): operating
  revenues (tuition net of allowances, grants/contracts, auxiliaries) minus operating
  expenses → operating income/(loss); then nonoperating (appropriations, gifts, investment
  income, interest expense); then capital items → change in net position. Tie the ending net
  position to the Statement of Net Position.
- **Statement of Cash Flows**: direct method; four categories — operating, noncapital
  financing (appropriations, noncapital gifts), capital and related financing (bond
  proceeds, capital spend, debt service), investing. Reconciliation of operating loss to
  operating cash flow appears at the bottom; it is the bridge a treasury analyst reads first.

## Interfund activity matrix

| Activity | Nature | Recording | Watch for |
|---|---|---|---|
| Interfund loan | Temporary; repayment expected | Due from (lender) / due to (borrower) | Symmetry; a "loan" never repaid is a transfer in disguise |
| Mandatory transfer | Required by external agreement (e.g. debt service) | Transfer out/in | Trace to the binding document |
| Non-mandatory transfer | Internal reallocation | Transfer out/in | Approval authority; budget vs actual |
| Internal service/charge | Payment for goods/services between units | Revenue/expense (or elimination) | Double counting in entity-wide totals |

Both sides post in the same period and eliminate in institution-wide statements.

## Restrictions → treasury decisions

- Build the cash position by fund class: total bank cash − agency/custodial − restricted
  balances with separate-account or indenture requirements = cash available for pooled
  operation. Investable "surplus" is computed after that partition, never before.
- Pooled investment of multiple funds requires an allocation method for earnings (per fund,
  per average balance) — and endowment/bond-proceeds pools usually stand apart with their
  own governing documents.
- A restricted fund in cash deficit is effectively borrowing from the pool: make it visible
  as an interfund balance with an authority and a repayment expectation.

## Pronouncements to confirm

Anchors commonly relevant to public higher-ed — verify each is current and how your
institution applies it before relying on it: the reporting-model statements that put public
universities on business-type-activity reporting; the statement renaming net assets to net
position and introducing deferred outflows/inflows; pension and OPEB standards (source of
large negative unrestricted net position); fair value measurement; certain external
investment pools (amortized cost criteria); fiduciary activities; leases and subscription
IT arrangements. Your institution's audited financial statements' note on "summary of
significant accounting policies" is the fastest authoritative map of what applies to you.
