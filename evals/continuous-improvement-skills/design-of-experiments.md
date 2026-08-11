# Evals — continuous-improvement-skills:design-of-experiments

## 1. Positive trigger (should load the skill)
> "My extraction prompt has four knobs — terse vs stepwise instructions, 0 vs 3 few-shot examples,
> freeform vs strict JSON output, temperature 0 vs 0.7 — and testing one factor at a time is too
> slow. Design a factorial DOE against our eval set, run it, and tell me which factors actually
> matter and whether any interact."

Expected: skill loads; sets the response (eval pass rate) and two levels per factor; chooses a
full 2^4 since runs are cheap and executes the runs itself; randomizes run order and replicates
with multiple seeds because LLM output is nondeterministic; computes main effects and
interactions against the replication noise; drops noise terms and states any alias caveats;
recommends a verification run on held-out cases; leaves the decision to adopt the winning prompt
to the user. Bonus: offers a Taguchi-style robustness pass across paraphrased inputs.

## 2. Near-miss (should NOT load this skill)
> "Our auto-reconciliation is live and matching at 91%. I want to keep nudging the tolerance and
> date-window settings in small, safe steps on production while we operate, and roll back anything
> that hurts."

Expected: continuous small-step tuning inside live production is
`continuous-improvement-skills:evolutionary-operation` — always-on, small, reversible moves with
monitoring — not an offline designed burst. design-of-experiments should hand this off (its seam:
offline designed bursts vs always-on small steps). If it loads and proposes a factorial on live
production, the boundary has failed.

## 2b. Near-miss (greedy-token guard: bare "screening")
> "We need to tighten our vendor screening process — new suppliers should be checked against
> sanctions lists before onboarding."

Expected: compliance/vendor screening — a due-diligence onboarding task, not an experiment; no
continuous-improvement skill should trigger. design-of-experiments must not trigger on "screening" alone; its
screening sense only appears fully qualified (screening designs, Plackett-Burman). If it loads
here, the trigger surface has grown too greedy. (Likewise, a request to "run a quick experiment"
with a single A/B significance check belongs to `data-analytics-bi-skills:statistical-inference`.)

## 3. Quality rubric
A good response:
- **Does the task:** produces an explicit design matrix (or names the fraction and its
  resolution), randomizes run order, replicates or reseeds noisy responses, computes effects and
  interactions with a noise yardstick, states alias caveats in plain words, and ends with a
  concrete recommendation plus a verification run — executing the runs itself when the process is
  a prompt or config.
- **Teaches:** explains why OFAT misses interactions and wastes runs (orthogonality: every run
  informs every estimate), what aliasing/resolution actually trade away, why randomization
  protects against unlisted drift, and why Taguchi optimizes for robustness across noise rather
  than peak performance on a good day.
- **Stays honest:** keeps factor levels inside human-authorized safety limits, never runs designed
  bursts against live production, distinguishes statistical significance from practical
  importance, and leaves the decision to act on results with the process owner.
