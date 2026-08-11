---
name: kyc-aml-basics
description: >-
  Explains and applies KYC / CDD / EDD, beneficial-ownership (UBO) identification, sanctions and
  OFAC/SDN screening, AML red flags, transaction monitoring, and SARs when onboarding or transacting
  with a counterparty — educational fundamentals, not legal advice. Use when onboarding a
  counterparty, screening a payment, or understanding an AML/KYC control. Triggers: KYC, CDD, EDD,
  AML, know your customer, customer due diligence, beneficial ownership, UBO, sanctions screening,
  OFAC, SDN, PEP, red flags, SAR, transaction monitoring, correspondent banking risk.
---

# KYC / AML basics

> **Educational only — not legal or compliance advice.** This skill explains common KYC/AML concepts
> to help you understand and work with your firm's controls. It does **not** set your obligations.
> Requirements depend on your jurisdiction, regulator, and firm policy. Always defer to your firm's
> **compliance / BSA officer** and follow your written program.

## When to use
- Onboarding a new counterparty (customer, vendor, bank) and understanding what due diligence applies.
- Understanding why a payment was flagged, held, or screened, and what the control is checking.
- Learning the fundamentals of sanctions screening, beneficial ownership, red flags, or SARs.
- Not for: internal payment approval, segregation of duties, and disbursement fraud controls → see
  `cash-management-skills:cash-management-controls`.

## Do it
1. **Confirm you are not the decision-maker of record.** These are regulated determinations. Your job
   is to gather, route, and understand — escalate to **compliance / the BSA officer** for approvals,
   filings, and any judgment call. When unsure, escalate; do not improvise.
2. **Identify the counterparty and set the risk tier.** Perform **KYC/CDD**: verify legal name,
   registration, address, industry, and the purpose/expected nature of the relationship. Rate the
   risk (product, geography, entity type, channel). Higher risk triggers **EDD**. See
   `references/kyc-aml-reference.md` for tier criteria.
3. **Identify beneficial owners (UBO).** For legal-entity counterparties, identify the natural persons
   who ultimately **own or control** it — an **ownership prong** (typically an equity threshold, often
   25% — **confirm the current threshold for your jurisdiction**) and a **control prong** (a senior
   manager who directs it). Unwind layers until you reach real people; verify their identities.
4. **Screen against sanctions and watchlists.** Screen the counterparty, its UBOs, and related
   parties against **OFAC's SDN** list and other applicable lists (UN, EU, UK/OFSI, and local), plus
   **PEP** lists. Screen at onboarding **and** on an ongoing basis, and screen **payments** in real
   time (names, addresses, countries, and — for trade — vessels/goods). Resolve alerts before
   proceeding; a true match means **block or reject** and escalate — **confirm which** with compliance.
5. **Apply EDD where risk is elevated.** For PEPs, high-risk jurisdictions, correspondent banks,
   cash-intensive or high-risk industries, and complex ownership: obtain **source of funds / source of
   wealth**, deeper ownership verification, senior-management approval, and enhanced ongoing monitoring.
6. **Watch for AML red flags in activity.** Compare transactions to the expected profile from step 2.
   Flag **structuring** (amounts kept just under reporting thresholds), rapid pass-through / layering,
   activity inconsistent with the business, unexplained third-party payments, high-risk geographies,
   shell-company traits, and reluctance to provide information. See the red-flag list in the reference.
7. **Escalate suspicious activity properly.** Route anything suspicious to compliance for **transaction
   monitoring** review and a possible **SAR** (Suspicious Activity Report) filing. **Do not tip off**
   the customer that a report may be filed, and keep the matter confidential. The **decision to file
   is compliance's**, not yours.

## Why / learn
These controls exist for one purpose: to **keep dirty money and sanctioned parties out of the
financial system** — and, for your firm, to stay out of severe legal, regulatory, and reputational
jeopardy. Each layer targets a different question. **KYC/CDD** answers *"who is this, really, and does
their activity make sense?"* — you cannot spot abnormal behavior without first establishing what normal
looks like, which is why the expected-activity profile is the anchor everything else compares against.
**Beneficial ownership** exists because criminals hide behind layers of entities; unless you reach the
**natural persons** who own or control a counterparty, screening the shell tells you nothing. **Sanctions
screening** is categorically different from the rest: it is **strict liability** — dealing with a
sanctioned party is prohibited regardless of intent or knowledge, which is why it runs at onboarding,
continuously, *and* on every payment, and why a true hit stops the transaction cold. **EDD** is simply
proportionality — spend more scrutiny where the risk is higher (PEPs, high-risk geographies,
correspondent relationships) and less where it is routine. **Transaction monitoring and SARs** are the
back end: patterns like **structuring** and **layering** are designed to defeat single-transaction
checks, so monitoring looks across time and the SAR is how the private sector alerts law enforcement —
which is exactly why **tipping off is prohibited**, as a warned criminal defeats the whole point.
**Correspondent banking** concentrates all of this risk, because you inherit the risk of your
respondent's customers you never see. The mental model: *know who you deal with, reach the real humans
behind them, never touch a sanctioned party, and surface what doesn't fit — then let compliance decide.*

## Common mistakes
- Treating KYC as a one-time onboarding checkbox → risk changes. Screening and due diligence are ongoing.
- Screening only the entity, not its UBOs and related parties → misses the sanctioned/PEP person behind it.
- Verifying ownership only to the first layer → stop only when you reach natural persons.
- Confusing "block" and "reject" on a sanctions hit → they are different legal actions. Confirm with compliance.
- Tipping off a customer about a SAR or investigation → prohibited. Keep it confidential; escalate quietly.
- Making the filing/approval decision yourself → these are compliance/BSA determinations. Gather and escalate.
- Assuming thresholds (e.g. 25% UBO) are universal → they vary by jurisdiction. Confirm the current rule.

## Tailor to your environment
Drop your firm's actual program into `references/your-environment.md` (keep counterparty names, IDs,
and case details in `your-environment.private.md`, which is git-ignored — customer and screening data
is sensitive and often legally protected). Capture your risk-rating model and tiers, your UBO
threshold and verification standard, which sanctions/PEP lists you screen and with what tool, your
escalation path to the BSA officer, and your firm's definitions for block vs reject and for SAR
routing. Legal obligations differ by jurisdiction, regulator, and firm — **your written program and
compliance team govern**, not this skill.

## References
- references/kyc-aml-reference.md — CDD/EDD tiers, UBO rules, sanctions lists and screening, red-flag catalog, SARs, and correspondent-banking risk
- references/your-environment.md — your firm's program, tiers, lists, tools, and escalation path (add when supplied)
