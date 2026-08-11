# Evals — public-sector-treasury-skills:nacha-ach-rules

## 1. Positive trigger (should load the skill)
> "Our returns report shows an R10 on a student-payment debit from three weeks ago and a C02 on
> yesterday's payroll file. What do these mean and what are we required to do?"

Expected: skill loads; identifies the seat (originator) and entry types; explains R10 as a
consumer unauthorized claim on the extended (~60-day) window that must not be re-initiated
without new authorization; explains C02 as a NOC requiring the routing number to be corrected
in master data within the rules' window; routes each to an owner and notes deadlines should be
confirmed against current NACHA rules.

## 2. Near-miss (should NOT load this skill)
> "Should we pay this $250,000 construction invoice by wire or ACH?"

Expected: this is rail selection, not ACH-rule interpretation — `banking-skills:payment-rails`
should handle it (finality, cost, cutoff trade-offs). If this skill loads instead, tighten the
description/cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** identifies originator vs receiver seat, reads the R/C code by family,
  states the applicable timeframe structure and the required action (fix data, obtain new
  authorization, apply NOC), and produces a concrete next step with an owner.
- **Teaches:** explains *why* the rules differ — SEC code declares the authorization, corporate
  vs consumer windows follow from who is expected to monitor the account, reversals are narrow
  because ACH has no recall right.
- **Safe:** never advises re-initiating an unauthorized return; never states a current dollar
  limit, window count, or deadline as fixed fact without saying to confirm current NACHA rules
  with the ODFI; keeps company IDs/account data out of committed files.
