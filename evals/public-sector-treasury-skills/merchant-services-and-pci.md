# Evals — public-sector-treasury-skills:merchant-services-and-pci

## 1. Positive trigger (should load the skill)
> "The bookstore's card deposits don't match their daily sales reports, and their merchant
> statement has a $125 'PCI non-compliance' fee. Can you help me figure out both?"

Expected: skill loads; asks/determines gross vs net funding and batch cutoff for the MID;
reconciles at the MID + batch date grain (weekend batching, separate Amex funding, netted
fees/chargebacks); explains the PCI non-compliance fee as an overdue SAQ/scan validation issue
to cure with the acquirer, not a rate change.

## 2. Near-miss (should NOT load this skill)
> "Our bank's account analysis statement shows monthly service charges way up — can you review
> our depository bank fees and the earnings credit?"

Expected: this is depository bank fee analysis (account analysis / ECR), not merchant card
economics — `banking-skills:bank-fee-analysis` should handle it. If this skill loads instead,
tighten the description/cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** maps the acceptance stack (MID, gateway, acquirer, funding account),
  reconciles settlement batches to deposits at the right grain, decomposes fees into
  interchange + assessments + markup and computes an effective rate, and gives concrete next
  steps (cure the SAQ, root-cause downgrades, calendar chargeback deadlines).
- **Teaches:** explains *why* only the markup is negotiable (interchange flows to issuers for
  fronting money and fraud risk), why tiered pricing hides downgrades, and why PCI is a scoping
  exercise before a controls exercise.
- **Safe:** never suggests recording or storing PANs/CVVs anywhere outside validated systems;
  flags that interchange tables, brand dispute deadlines, and PCI-DSS versions change and must
  be confirmed with the acquirer/QSA; keeps real MIDs and pricing in `*.private.md`.
