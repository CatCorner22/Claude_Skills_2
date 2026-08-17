# Evals — decision-science-skills:pre-mortem

## 1. Positive trigger (should load the skill)
> "We're about to flip the new reconciliation rulesets live at month-start and load opening
> balances from a bulk-import file. Before we commit, run a premortem — assume it's a year
> from now and the cutover was a fiasco. It's mostly just me on this, so play the
> stakeholders too."

Expected: skill loads; declares the failure as fact (verbatim certainty framing, not
"what might go wrong"); runs the solo-analyst variant — ~20 heterogeneous failure
narratives forced across technical/data/political/timing categories, grounded in the
actual cutover plan, plus in-role stakeholder reasons (operations manager, DBA, upstream data
provider, auditor); buckets and deduplicates; hands the RANKING to the user with proposed criteria
(likelihood × damage × detection lag); ends with plan changes / tripwires / explicit
acceptances, each with owner and date, filed to the go-live checklist, and the AAR date
set.

## 2. Near-miss (should NOT load this skill — live-plan adversarial seam)
> "The recon-engine pilot already ran and 'passed,' but they loosened the match threshold
> mid-run. Red team our go-live plan and audit whether the pilot actually validates the
> engine."

Expected: `continuous-improvement-skills:project-command-center` owns adversarial
challenge of plans under way and epistemic validity of tests (interventions, fixed
criteria, continuation vs. validation). pre-mortem is the BEFORE-commitment companion —
loading it here means the before/during boundary is failing.

## 2b. Near-miss (looking-back seam)
> "The bulk data load failed Saturday night and we scrambled all weekend. Walk the team
> through what was supposed to happen, what actually happened, and what we do differently
> next time."

Expected: `decision-science-skills:after-action-review` — the event already happened;
this is the four-question team debrief, not prospective hindsight. A pre-mortem load here
means the before/after boundary is failing. (Likewise, the assistant reflecting on its own
correction routes to `metacognition-skills:reflective-learner`, never here.)

## 3. Quality rubric
- **Does**: uses the verbatim it-already-failed declaration; enforces silent independent
  writing before any discussion in the team variant; generates heterogeneous,
  plan-grounded failure narratives across all four categories (not just technical);
  round-robins without rebuttal; leaves ranking and ownership to the humans; converts top
  items into plan changes, tripwires, or explicit acceptances with named owners and
  dates; files output where the plan is commanded and schedules the AAR.
- **Teaches**: prospective hindsight (Mitchell/Russo/Pennington 1989, ~30% better reason
  identification) as the lab mechanism; Klein's HBR 2007 meeting as its
  operationalization; why declared certainty beats "what might go wrong"; why silence
  and independence kill anchoring and HiPPO deference; why the exercise legitimizes
  dissent that planning momentum suppresses.
- **Stays honest**: keeps the ~30% claim scoped to reason generation in the lab, with the
  full-meeting benefit stated as practitioner-grounded; never lets the LLM rank or assign
  owners; never runs the ritual after commitment and calls it protection; flags when the
  plan is too vague to fail specifically.
