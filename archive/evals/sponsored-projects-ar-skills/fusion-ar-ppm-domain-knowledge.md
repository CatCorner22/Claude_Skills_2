# Evals — sponsored-projects-ar-skills:fusion-ar-ppm-domain-knowledge

## 1. Positive trigger (should load the skill)
> "I have an extract with columns like 'billing status', 'contract number', and 'recognized
> revenue' — map these to Fusion concepts and tell me which subject areas this came from and
> what I can trust it for."

Expected: skill loads; maps columns to their side of the seam (PPM / AR / bridge); identifies
Project Billing - Bill Transactions Real Time for billing status; profiles completeness, date
range, and filters; flags the grouping-rule and aging-basis gotchas; outputs glossary +
profile table + recommended filters.

## 2. Near-miss (should NOT load this skill)
> "Which OTBI subject area should I use for a supplier payments report?"

Expected: general subject-area selection — `oracle-otbi-skills:otbi-subject-area-selection`.
If this skill loads, tighten the sponsored/PPM framing.

## 3. Quality rubric
A good response:
- **Does the task:** correct column-to-concept mapping with unmappables flagged as questions,
  a data-profile table, and the integration flow (PPM → AutoInvoice → AR → Confirm Invoice
  Acceptance) explained where relevant.
- **Teaches:** the two-systems-of-record model, why unbilled lives in the bridge area, and why
  PPM revenue isn't collectible AR until the flow completes.
- **Safe:** documented public subject areas only; attribute absence read as grouping-rule
  configuration, not missing data; no assumed instance config.
