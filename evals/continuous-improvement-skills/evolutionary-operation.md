# Evals — continuous-improvement-skills:evolutionary-operation

## 1. Positive trigger (should load the skill)
> "Our auto-reconciliation match rate has been stuck around 91%. I want to keep tuning the
> matching-rule tolerances — amount tolerance, date window — but we can't take reconciliation
> offline to run experiments, and a false match posts wrong cash. Can we keep improving this in
> production?"

Expected: skill loads; gets safe operating limits and the false-match hard bound from the
process owner BEFORE any perturbation; picks 2–3 factors; defines a small 2×2-plus-center
pattern inside the bounds; runs randomized cycles on live production with no interruption;
maintains the EVOP log; tests effects against experimental error from cycle-to-cycle scatter and
acts only past ~2 standard errors; shifts the operating center on an owner-ratified win; states
the stopping/revert rules (guard breach or out-of-spec drift stops the experiment).

## 2. Near-miss (should NOT load this skill)
> "We cloned prod into a test environment — design a proper factorial experiment across four or
> five matching-rule factors so we can find the best settings before go-live."

Expected: an offline designed experiment in a dedicated burst with bold factor settings —
`continuous-improvement-skills:design-of-experiments` owns it. The seam: DOE stops the world
(or uses a sandbox) and takes big steps; EVOP never stops production and takes steps small
enough that every unit still ships. If evolutionary-operation loads here, tighten the
description toward live/in-production language.

## 2b. Near-miss (improve-in-production phrasing, wrong problem)
> "Match rate dropped from 91% to 84% overnight after the bank changed its statement format —
> help me figure out what happened and fix production."

Expected: an incident diagnosis, not continuous improvement by perturbation —
`continuous-improvement-skills:root-cause-analysis` owns the cause hunt. EVOP's own
stopping rule says a process upset halts experimentation. If evolutionary-operation loads on any
"improve the match rate" phrasing without the tune-while-running intent, its triggers are too
greedy.

## 3. Quality rubric
A good response:
- **Does the task:** obtains owner-set safe limits and guard bounds first; defines a within-
  bounds factorial pattern around the current center; runs randomized live cycles recording both
  improvement and guard responses; keeps the EVOP log; computes effects ± standard errors from
  replicate cycles; shifts the center only on significant, owner-ratified wins; states stopping
  and revert rules.
- **Teaches:** explains Box's core idea — a process at a fixed setting yields product but no
  information, while tiny perturbations yield both, with replication shrinking the error until
  small effects become visible — and the DOE-vs-EVOP trade (bold offline steps vs. timid
  perpetual in-production steps).
- **Stays honest:** never moves the center on a non-significant effect (tampering); treats the
  guard response as a hard cliff measured independently of the engine being tuned; keeps limit-
  setting and ratification with the process owner, not the analyst or the LLM.
