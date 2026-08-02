# Evals — banking-skills:payment-rails

## 1. Positive trigger (should load the skill)
> "We owe a supplier $85,000 and it has to be irrevocable and settle today. Should I send a wire or
> can I use ACH? What's the difference in finality?"

Expected: skill loads; establishes the finality/speed/cost requirements; steers to Fedwire (final,
same-day) over ACH (reversible, batch); explains push vs pull and the irrevocability of wires vs
ACH returns; notes cutoff timing and to verify the beneficiary before releasing an irrevocable wire.

## 2. Near-miss (should NOT load this skill)
> "How do we set up the SFTP host-to-host connection so our ERP can send payment files to the bank?"

Expected: this is about the connectivity **channel**, not choosing a payment rail. The
`banking-skills:bank-connectivity` skill should handle it. If payment-rails loads instead, tighten
the "Not for" cross-link and the description.

## 3. Quality rubric
A good response:
- **Does the task:** compares the candidate rails on cost, speed, finality, reversibility, limits,
  and cutoffs; recommends a rail with reasons; distinguishes "sent" from "settled/final."
- **Teaches:** explains *why* finality and the cost/speed trade-off drive rail choice, and why SWIFT
  is a messaging network settling through correspondents rather than a rail itself.
- **Safe:** flags that wires are irrevocable (verify beneficiary first) and that ACH/checks can be
  returned; says to confirm exact limits/cutoffs for the user's bank and region.
