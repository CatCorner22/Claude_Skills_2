---
name: root-cause-analysis
description: >-
  Finds the true cause of a recurring problem with 5 Whys, a fishbone/Ishikawa diagram across the 6M
  categories, and Pareto analysis, separating immediate containment from the root cause and verifying
  the cause before any countermeasure. Use when diagnosing a recurring problem, chasing a defect's
  cause, or a fix that never sticks. Triggers: root cause, 5 whys, fishbone, Ishikawa, cause and
  effect, Pareto, RCA, why did this happen, recurring problem.
---

# Root-cause analysis

## When to use
- Diagnosing *why* a recurring problem or defect keeps happening (not just clearing this instance).
- A fix that keeps failing because you've been treating a symptom, not the cause.
- Prioritizing which of many problem types to attack first (Pareto).
- Not for: running a full data-driven improvement project with baseline and controls → see
  `continuous-improvement-skills:dmaic-problem-solving`. To tell the whole problem-solving story on one
  page for alignment → see `continuous-improvement-skills:a3-thinking`.

## Do it
1. **Write a sharp problem statement.** State *what* is wrong, *where*, *when it started*, *how big*
   (magnitude/frequency), and *how you know* — with evidence, no cause and no blame. "AP posted 14
   duplicate payments in Q2, up from 2 in Q1" beats "AP is careless." A vague problem yields a vague
   cause.
2. **Contain first, then investigate.** Put in an immediate action that protects the customer *now*
   (block the duplicate, correct the entry, add a temporary check) and label it clearly as
   containment. Containment stops the bleeding; it is **not** the root cause and must not be mistaken
   for the fix.
3. **Run a 5 Whys chain on the confirmed problem.** Ask "why?" of each answer, following the causal
   thread, until you reach a cause that (a) is a process/system condition you can act on and (b) whose
   removal would prevent recurrence. Five is a guide, not a quota — stop at the actionable cause. Test
   the logic backwards with "therefore": each *why* should read forward as a valid cause→effect.
4. **Widen with a fishbone (Ishikawa) when the cause isn't single-threaded.** Brainstorm candidate
   causes into the **6M** categories — **Man** (people/skill), **Method** (process), **Machine**
   (systems/tools), **Material** (inputs/data), **Measurement** (metrics/definitions), **Environment/
   Mother-nature** (surroundings, policy, timing). The 6M grid keeps you from anchoring on the first
   plausible answer — see `references/tools-and-templates.md`.
5. **Use Pareto to prioritize the vital few.** When there are many defect types, tally by category and
   sort descending — typically a small number of causes drive most of the occurrences. Fix the tallest
   bars first; don't spread effort evenly across trivial many.
6. **Verify the cause before you build a countermeasure.** Confirm with data or a controlled test: if
   this really is the cause, removing or toggling it should change the effect. Unverified causes are
   guesses wearing a diagram.
7. **Design the countermeasure and confirm it holds.** Address the *root* cause (ideally error-proofing
   so the mistake can't be made), assign an owner and date, then check recurrence over time. Only then
   remove the temporary containment.

## Why / learn
Symptoms recur until the *cause* is removed — which is the entire reason to resist the first plausible
answer. Under time pressure the brain offers a quick, blameable explanation ("someone was careless"),
you fix that, and the problem returns because the real driver — a process that *lets* the error happen —
is still there. The disciplines here are all devices for that resistance. **5 Whys** forces you past the
first layer down the causal chain to a condition you can actually change. The **fishbone's 6M grid**
counteracts anchoring by making you consider categories you'd otherwise skip — most stubborn problems are
in Method, Measurement, or Machine, not the "Man" box people reach for first. **Pareto** counters the urge
to treat every defect equally by showing that a vital few causes dominate. And **verifying before
countermeasure** is what separates analysis from storytelling: a cause you can toggle and watch the effect
follow is proven; one that merely sounds right is not. Keep containment and root cause in separate boxes,
because the great trap is shipping the temporary patch as if it were the cure and closing the problem while
the cause lives on. The aim is a countermeasure that makes the error hard or impossible to repeat, not a
reminder to "be more careful" — reminders decay, error-proofing doesn't.

## Common mistakes
- Vague problem statement → vague cause. Quantify what/where/when/how-big with evidence, no blame.
- Stopping at a symptom ("re-trained the clerk") → it recurs. Keep asking why to a process condition.
- Treating containment as the fix → the bleeding stops but the cause lives. Label and separate them.
- Anchoring on the first cause → use the 6M fishbone to force breadth before you converge.
- Skipping verification → you countermeasure a guess. Confirm the cause changes the effect first.
- Spreading effort across every defect → use Pareto; fix the vital few first.
- Blaming a person → almost always a process/system let the error through. Fix the system.

## Tailor to your environment
Record your real recurring problems and data sources in `references/your-environment.md` (use
`your-environment.private.md`, git-ignored, if it names real people, vendors, or incidents). Capture your
defect categories, where you pull occurrence counts for Pareto, your containment vs. root-cause
conventions, and who signs off that a cause is verified. Never commit real incident or client data —
sanitize to structure only.

## References
- references/tools-and-templates.md — 5 Whys worksheet, 6M fishbone prompts, Pareto tally, verification test
- references/your-environment.md — your defect categories, data sources, and sign-offs (add when supplied)
