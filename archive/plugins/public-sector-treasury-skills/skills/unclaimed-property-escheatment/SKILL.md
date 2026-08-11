---
name: unclaimed-property-escheatment
description: >-
  Manages unclaimed property from stale outstanding checks and dormant balances through the
  escheatment lifecycle: identifying dormancy, statutory due-diligence letters,
  reissue-versus-report decisions, state holder reporting and remittance cycles,
  record-keeping, and reducing future escheatment at the source through payee data quality
  and e-payments. Use when handling stale or uncashed checks, preparing an unclaimed-property
  holder report, responding to a state inquiry or audit, or designing the escheatment
  process. Triggers: unclaimed property, escheatment, stale checks, dormant, due diligence
  letter, state report unclaimed, outstanding check aging, remit to state, holder report.
---

# Unclaimed property and escheatment

## When to use
- Working stale outstanding checks (vendor, payroll, student refunds) or dormant credit
  balances toward reissue or state reporting.
- Preparing or reviewing the annual holder report and remittance; designing the recurring
  escheatment cycle; responding to a state unclaimed-property inquiry or audit.
- Cutting future escheatment at the source (payee data, e-payments, early follow-up).
- Not for: producing the outstanding-check list itself — stale items surface from
  `cash-management-skills:bank-reconciliation`. For the controls around void/reissue and
  payment fraud → see `cash-management-skills:cash-management-controls`.

## Do it
1. **Inventory property types and owners.** Start from the reconciliation's outstanding-check
   aging, split by type (payroll, vendor, refund — including student refunds), then add
   non-check property: customer/student credit balances, unapplied receipts, deposits held.
   Each property type can carry a different dormancy treatment.
2. **Screen for dormancy under the governing act.** The clock generally runs from issuance
   or the owner's last contact/activity. Dormancy periods vary by property type and state
   and are amended over time — pull the current dormancy table from the state administrator
   (in Tennessee the unclaimed-property program is administered under the State Treasurer;
   confirm current periods and thresholds rather than hard-coding them). Wages often go
   dormant faster than vendor payments.
3. **Determine which state gets the property.** Apply the jurisdiction priority rules from
   the U.S. Supreme Court's Texas v. New Jersey line: first, the state of the owner's last
   known address in your records; if no address (or a foreign one), the holder's state of
   domicile. This is why the quality of the address field is a compliance matter.
4. **Run statutory due diligence.** Within the state's required window before filing, send
   the prescribed letters to owners above the state's de minimis threshold; keep proof of
   the attempts. Responses route to reissue; undeliverable or silent items route to the
   report.
5. **Decide reissue vs report — and account for it correctly.** A stale check is never
   income: void it and carry the amount as an unclaimed-property liability. Reissue clears
   the liability by payment (with controls — verify the payee's identity and keep the
   void-and-reissue trail; owner-claim moments are a known fraud vector). Otherwise the
   liability clears when you remit to the state. Entries are in
   `references/escheatment-lifecycle.md`.
6. **File the holder report and remit** in the state's required format (most states take the
   NAUPA standard electronic format) by the statutory deadline; file negative reports where
   required; retain the supporting records for the state's retention period.
7. **Institutionalize the cycle.** Put the sequence on the calendar — aging pull → dormancy
   screen → due diligence → report → remit — with a named owner, and feed it from the
   reconciliation's stale-item flags so nothing waits for a year-end scramble.
8. **Reduce it at the source.** Validate payee addresses and banking at onboarding; prefer
   e-payments over checks; chase uncashed items at 30/60/90 days while the payee is still
   reachable; coordinate an unclaimed-wages path with HR and a refund design that avoids
   orphan credits.

## Why / learn
Unclaimed property law is custodial: the state never takes ownership, it takes *custody*,
standing in the owner's shoes (the "derivative rights" idea) while the owner's claim runs
essentially forever. That single fact explains the whole discipline. The money was never
yours — so writing old checks off to income books someone else's property as your gain,
which is both wrong and the classic audit finding: states audit holders, sometimes through
contingent-fee firms, with long lookbacks and estimation techniques where records are
missing, so complete records are the holder's defense. The priority rules turn the humble
address field into the routing key for the whole obligation. Due diligence is not a
formality: for a university, the owners are often its own students and employees, and a
letter that reunites them with their money is cheaper and better for everyone than remitting
and letting them claim from the state later. Public institutions sometimes sit under
modified rules — some states treat their own agencies' property through special processes —
so confirm your institution's actual status rather than assuming exemption or full coverage.
Finally, notice that steps 1–7 only *process* the pipeline; step 8 is the only one that
shrinks it. A treasury team that pays electronically, keeps payee data clean, and chases
items early converts a legal-compliance problem back into ordinary operations.

## Common mistakes
- Writing stale checks off to income → it is a liability with a perpetual owner claim; the classic audit finding.
- Voiding a check and losing track of it → a void without an escheat evaluation breaks the trail; reclass to the liability.
- Reporting everything to your own state → priority rules send it to the owner's address state first.
- Skipping or mistiming due diligence → it is a statutory step with a defined window; document every attempt.
- Reissuing on a phone request without verifying the payee → owner-claim moments attract fraud; verify, then pay.
- Treating it as a one-time cleanup → dormancy accrues continuously; run a calendar cycle with an owner.
- Assuming a public entity is exempt (or fully covered) without checking → status varies; confirm with the administrator.
- Destroying records after remitting → retention obligations continue; the records are your audit defense.

## Tailor to your environment
Record in `references/your-environment.md`: the states you report to, your property types
and their dormancy treatment (with the date you last verified them), the reporting calendar
and format, thresholds, and the process owners. Owner-level detail — names, addresses,
amounts, check numbers — is real data and never belongs in git: keep working files in
`your-environment.private.md` or other git-ignored `*.private.md` files.

## References
- references/escheatment-lifecycle.md — dormancy screening, priority-rule decision tree, due-diligence letter skeleton, accounting entries, holder-report checklist, source reduction
- references/your-environment.md — your states, calendar, thresholds, and owners (fill in)
