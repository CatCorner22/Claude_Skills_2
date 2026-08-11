# Evals — banking-skills:bank-connectivity

## 1. Positive trigger (should load the skill)
> "We're adding six new banks across three countries. Should we build host-to-host SFTP to each one
> or go through SWIFT? And how do we secure the payment files?"

Expected: skill loads; weighs per-bank H2H integration effort vs SWIFT's standardization/reach for a
multi-bank, multi-country footprint; covers SWIFT access models (direct/Alliance Lite2, service
bureau, SCORE); recommends securing files with PGP + SSH keys and dual control; suggests standardizing
on ISO 20022 and parallel-running before cutover.

## 2. Near-miss (should NOT load this skill)
> "For a $2M same-day supplier payment, should we use a wire or RTP?"

Expected: this is a payment-rail choice, handled by `banking-skills:payment-rails`, not a connectivity
channel decision. If bank-connectivity loads instead, tighten the "Not for" cross-link.

## 3. Quality rubric
A good response:
- **Does the task:** shortlists portal / H2H SFTP / SWIFT / API against the requirement, weighs cost,
  per-bank effort, resilience, and standardization, matches batch vs real-time to channel, and covers
  file security (PGP, SSH keys, non-repudiation).
- **Teaches:** frames connectivity as a cost/standardization/resilience trade-off, explains why SWIFT
  scales with bank count while H2H scales cost per bank, and when APIs beat file transfer (latency).
- **Safe:** never suggests password-based or unencrypted transfer; says to confirm each bank's ISO
  20022 flavor and channel availability; recommends a parallel run at cutover.
