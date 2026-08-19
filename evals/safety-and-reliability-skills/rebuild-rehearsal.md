# Evals — safety-and-reliability-skills:rebuild-rehearsal

## 1. Positive trigger (should load the skill)
> "Honestly, if our senior analyst left tomorrow we'd be sunk — the monthly deliverable
> and the whole restore process only live in her head. We have a runbook but nobody's
> ever used it. How do we make sure this survives her?"

Expected: skill loads; runs the bus-factor census (who can do it, who could learn it,
what written record exists, when last done by a non-primary) and flags the
bus-factor-1 rows; picks a real rebuild unit per capability (recreate the deliverable
from raw inputs with only the runbook; restore the actual backup to a scratch
location) with a success test that can fail; sets a cadence shorter than tenure with
the two-rehearsal rule stated; sets up the learn-lead-teach rotation with the newcomer
driving and the veteran correcting only; runs the gap-harvest protocol (log questions
verbatim, fix the record before closing); names a funding owner for the cycle itself,
telling the Ōnin lapse honestly as the reason; offers the assistant as the simulated
driver between real rehearsals (interrogating the runbook for gaps as a cold newcomer).

## 2. Near-miss (documentation-writing guard)
> "Our onboarding docs are confusing — new hires keep getting lost in the environment
> guide. Help me rewrite it so a newcomer actually understands it."

Expected: `writing-skills:explanation-design` owns writing and fixing explanations
(audience model, concrete-first ordering, curse-of-knowledge tells, teach-back).
rebuild-rehearsal *finds* doc gaps by rehearsal and hands them to the writer; it
should route there rather than load on a pure writing ask. If it loads, the seam is
failing.

## 2b. Near-miss (crisis-drill guard)
> "We want to drill the team on the emergency runbook — if the payment system dies at
> 2 a.m., can they find the sealed playbook, get emergency access, and execute the
> first moves fast?"

Expected: `safety-and-reliability-skills:break-glass-playbooks` owns unsealing drills
— tripwires, sealed instructions, expiring authority, time-to-unseal. The seam:
crisis drills rehearse the EMERGENCY; rebuild-rehearsal rehearses the CAPABILITY
(could we still build the thing at all, slow and thorough). If rebuild-rehearsal
loads on an unsealing-mechanics ask, tighten the boundary.

## 3. Quality rubric
- **Does**: produces a census table with the four facts per capability and criticality
  grading; every chosen rebuild unit yields the real artifact and can fail (no
  walkthroughs); cadences are justified against stated tenure, not the calendar's
  convenience; the rotation assigns driver/lead/corrector with the least-knowledgeable
  person driving; every rehearsal gap is logged verbatim and resolved or explicitly
  accepted before close, with a one-line rehearsal log; the funding owner is a named
  role with a budget line and a transfer rule; simulated (assistant-driven) and real
  rehearsals alternate, never substitute.
- **Teaches**: why knowledge survives only when exercised on a schedule shorter than a
  career, and why generational overlap — not the exact figure — is the property Ise's
  20-year cycle supplies and the one to scale; why the
  artifact is disposable and the capability is the asset; why only execution by
  someone without the knowledge tests documentation (curse of knowledge), hence
  newcomer-drives; why renewal lapses silently without a funding owner — the Ōnin
  lesson told as load-bearing history, not trivia.
- **Stays honest**: Ise facts carried with their [snippet-only] provenance marks; the
  ~120-year Ōnin lapse (1462–1585, revived by Keikō-in's nuns fundraising across
  decades with warlord endowment behind them — Oda Nobunaga funding from 1569, the 1585
  rebuild completed by his successors after his death in 1582) told as half the
  lesson, never airbrushed into "13 unbroken centuries"; Kongō Gumi's 2006 liquidation
  stated alongside its longevity; no invented statistics about knowledge decay;
  boundaries respected — test-suite design to testing-strategy, crisis unsealing to
  break-glass-playbooks, personal retention to spaced-retrieval-learning (named as the
  personal-scale twin), doc writing to explanation-design.
