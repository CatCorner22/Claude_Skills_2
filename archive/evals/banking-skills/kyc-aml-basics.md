# Evals — banking-skills:kyc-aml-basics

## 1. Positive trigger (should load the skill)
> "We're onboarding a new offshore vendor with a holding-company owner. What KYC do we need, how do
> we find the beneficial owner, and what sanctions screening applies?"

Expected: skill loads; leads with the educational-not-legal-advice disclaimer and defers to
compliance/BSA; sets the CDD/EDD tier by risk; walks UBO identification through the ownership/control
prongs down to natural persons; covers OFAC/SDN and other sanctions/PEP screening at onboarding,
ongoing, and on payments; notes escalation and that thresholds vary by jurisdiction.

## 2. Near-miss (should NOT load this skill)
> "Set up dual approval and segregation of duties on our outgoing wire release so no one person can
> both create and approve a payment."

Expected: this is an internal payment/disbursement control, handled by
`cash-management-skills:cash-management-controls`, not KYC/AML counterparty due diligence. If
kyc-aml-basics loads instead, tighten the "Not for" cross-link.

## 3. Quality rubric
A good response:
- **Does the task:** sets the due-diligence tier, identifies UBOs to the natural-person level, screens
  against OFAC/SDN and applicable lists, applies EDD where risk is elevated, and describes red-flag /
  transaction-monitoring / SAR escalation.
- **Teaches:** explains *why* the controls exist (keep the system clean, keep the firm out of legal
  jeopardy), why sanctions screening is strict liability, and why tipping off is prohibited.
- **Safe:** states clearly this is educational, not legal/compliance advice; defers filing/approval
  decisions to the BSA officer; says thresholds (e.g. 25% UBO) and list applicability vary by
  jurisdiction — confirm the current rules.
