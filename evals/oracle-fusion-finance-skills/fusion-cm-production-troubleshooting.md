# Evals — oracle-fusion-finance-skills:fusion-cm-production-troubleshooting

## 1. Positive trigger (should load the skill)
> "Auto-reconciliation matched 95% of statement lines in UAT, but since go-live production
> is matching about 40%, and yesterday's BAI2 import finished with Import Warnings. Nothing
> in the rule set changed. What's going on?"

Expected: skill loads; asks the targeted intake questions (ESS output, account setup,
rule-set assignment, a prod file sample, environment deltas); runs the parity check FIRST
(volume/threshold, security visibility, feed encoding, scheduling) before touching rules;
classifies the Import Warnings (likely undefined balance/transaction codes); delivers the
mandatory format — ranked root causes with evidence, diagnostic steps, questions, fixes
with FSM task names, validation-in-non-prod-first.

## 2. Near-miss (should NOT load this skill)
> "Walk me through setting up a new bank account in Fusion Cash Management and loading its
> first statement."

Expected: normal module operation → `oracle-fusion-finance-skills:fusion-cash-management-module`.
This skill is for production failures and config-gap evaluation. If it loads here, tighten
the description.

## 3. Quality rubric
A good response:
- **Does the task:** parity-first ordering; error-class taxonomy applied; ranked causes
  with evidence (not an undifferentiated list); exact FSM task names; before/after tables
  where they help; validation plan gated on non-prod.
- **Teaches:** explains *why* test-passes-prod-fails is usually parity (volume, security
  visibility, feed reality, timing) rather than a broken rule.
- **Safe:** config backup before changes; fixes tested in non-prod first; release-dependent
  names/values flagged "confirm in your release"; asks rather than guesses when intake is
  incomplete.
