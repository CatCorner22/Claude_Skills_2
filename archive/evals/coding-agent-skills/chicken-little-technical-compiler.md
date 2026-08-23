# Evals — coding-agent-skills:chicken-little-technical-compiler

## 1. Positive trigger (should load the skill)
> "Deploy compiler. Target: this Flask app — one global SQLAlchemy session, retries
> hand-rolled around a third-party eligibility API, and a nightly cron that rebuilds the
> whole cache."

Expected: skill loads and acknowledges in character; runs the exact autopsy template —
load-bearing pillars first, then the Jenga bottom block (e.g., the unpinned third-party
API or the shared global session) with a concrete cascade chain (if X fails, Y drops
state, Z crashes), the fragility table with defensible likelihood ratings and remediation
difficulty, compute-bleed analysis (what throttles at 10x), the proactive pivot with an
offer to generate the refactor now, and mandated actions split Critical (gates
deployment) vs Strategic (with tradeoffs). Every recommendation names its actor — zero
passive voice.

## 2. Near-miss (should NOT load this skill)
> "Deploy advisor — autopsy our plan to switch the whole practice to a new PMS vendor."

Expected: `coding-agent-skills:chicken-little-executive-advisor` owns
strategic/vendor/process autopsies. The compiler edition targets code and architecture.

## 2b. Near-miss (plain-review guard)
> "Review this PR before I merge it."

Expected: an ordinary code review — `coding-agent-skills:board-review` or a direct
review, not the persona. The compiler engages on explicit deployment or an adversarial
stress-test ask, not routine merges.

## 3. Quality rubric
- **Does**: pillars → Jenga → fragility table → inefficiencies → pivot → mandated
  actions, in order; the bottom block is singular and load-bearing, not a smell list;
  Critical items are deploy-gating.
- **Teaches**: why the cascade analysis precedes bug-hunting; why likelihood ratings must
  trace to base rates or measured variance; why passive-voice recommendations don't get
  executed.
- **Stays honest**: acknowledges clean logic before criticizing; probabilities defensible,
  never vibes; offers the fix rather than only the alarm.
