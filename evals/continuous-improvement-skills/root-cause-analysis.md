# Evals — continuous-improvement-skills:root-cause-analysis

## 1. Positive trigger (should load the skill)
> "We keep getting duplicate vendor payments even though we re-trained the AP team twice. Can you help
> me find the actual root cause with 5 Whys and a fishbone?"

Expected: skill loads; writes a quantified, blame-free problem statement; puts in containment and labels
it as such; runs a 5 Whys chain to a process/system condition; widens with a 6M fishbone; uses Pareto if
there are several defect types; verifies the cause before proposing an error-proofing countermeasure.

## 2. Near-miss (should NOT load this skill)
> "Set up a full Six Sigma project to cut our invoice error rate — I need a baseline, a control plan, and
> a way to prove the variation actually dropped."

Expected: this is a structured DMAIC improvement project with measurement and controls, not a one-off
cause hunt. The `continuous-improvement-skills:dmaic-problem-solving` skill should handle it (RCA is one
step inside its Analyze phase). If root-cause-analysis loads instead, tighten the cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** produces a sharp problem statement, separates containment from root cause, runs a
  5 Whys chain to an actionable condition, uses the 6M fishbone to avoid anchoring, applies Pareto to
  prioritize, and verifies the cause before countermeasuring.
- **Teaches:** explains *why* symptoms recur until the cause is removed and why the discipline is
  resisting the first plausible (often blame-based) answer.
- **Safe:** doesn't ship containment as the cure, doesn't blame a person where a process let the error
  through, and doesn't countermeasure an unverified guess.
