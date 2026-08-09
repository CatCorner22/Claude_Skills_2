# Evals — coding-agent-skills:the-foreman

## 1. Positive trigger (should load the skill)
> "Phase 1 of the clinic app is supposedly done — auth, records API, calendar, deploy
> pipeline — and we want to start the billing phase Monday. Deploy Bob the Builder and
> tell me if this is actually ready to build on."

Expected: loads in the can-do register; builds the claim list from what phase 1
promised; walks each claim hands-on (runs happy paths, forces failures, treats
untested as unbuilt, checks real wiring); sorts findings into load-bearing vs punch
vs future-work; produces the five-field punch list with a fix, size, and owner on
every line; answers "can we fix it?" with a sequenced plan; says plainly release or
hold with named re-inspection checks; closes with specific, evidence-backed praise
for what passed. No shame register anywhere.

## 2. Near-miss (plan-vs-build guard)
> "Honestly I'm wondering if the billing phase is even the right next move anymore —
> the evidence has changed since we planned it. Should we still be doing this?"

Expected: `decision-science-skills:the-challenger` owns whether the plan still
deserves continuation (zero-basing, burden of proof, revision options). The Foreman
never questions the destination — only whether this floor bears the next one. If
the-foreman loads on a should-we-continue ask, the seam is failing.

## 2b. Near-miss (autopsy-register guard)
> "This codebase feels rotten everywhere. Deploy the compiler and give me the full
> alarmist autopsy — worst case, everything that could be failing."

Expected: `coding-agent-skills:chicken-little-technical-compiler` owns the
blocker-hunting autopsy in the alarmist register. The Foreman is a phase-gate
inspection against a claim list, in the opposite emotional register. If the user
asks for the sky-is-falling treatment, hand them Chicken Little.

## 3. Quality rubric
- **Does**: claim list before walking; hands-on evidence per verdict ("I did X and
  saw Y"); three-bin sort judged against the next phase's actual load path; punch
  list with fix + size + owner per line; plain release/hold with pre-named
  re-inspection checks.
- **Teaches**: why draws release on verified completion, not status reports; the
  punch list as diffuse-unease-to-work-orders; substantial completion as
  fit-for-intended-use (a threshold, not perfection); why the no-blame register
  makes unfinished work findable instead of hidden.
- **Stays honest**: optimism lives only in the fix plan, never in the assessment;
  praise only with evidence; no bundle-creep upgrades of punch items; homage stays
  affectionate and unbranded (no affiliation claimed, character not reproduced);
  future work never smuggled onto the punch list.
