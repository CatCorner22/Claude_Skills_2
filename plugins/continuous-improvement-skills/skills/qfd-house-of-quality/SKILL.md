---
name: qfd-house-of-quality
description: >-
  Builds a Quality Function Deployment House of Quality — translating weighted customer needs
  (the WHATs, e.g. what a co-design session heard from users) into measurable technical
  characteristics (the HOWs) through a relationship matrix, a correlation roof that exposes
  engineering tradeoffs, computed importance scores, competitive benchmarks, and targets, then
  cascading each level's HOWs into the next matrix's WHATs. It is the translation bridge
  between the customer input that kaizen-and-codesign produces and the CTQs that
  lean-six-sigma-for-software consumes. Use when translating customer needs into engineering
  specs, prioritizing features or requirements against weighted needs, or deciding what to
  build first with a defensible matrix. Triggers: house of quality, QFD, quality function
  deployment, translate customer needs to specs, requirements matrix, what should we build
  first, voice of customer to CTQ, customer needs to engineering characteristics.
---

# QFD — the House of Quality

## When to use
- Translating gathered, weighted customer needs into measurable technical characteristics with
  computed priorities, benchmarks, and targets — the step where "patients want easy booking"
  becomes "steps-to-book ≤ 3, confirmed in < 60 seconds".
- Prioritizing features or requirements defensibly: dental-app features (patient and dentist
  WHATs vs. development HOWs), or the requirements behind a
  `data-analytics-bi-skills:dashboard-design` build.
- Bridging this library's improvement chain: `continuous-improvement-skills:kaizen-and-codesign`
  produces the customer input; `continuous-improvement-skills:lean-six-sigma-for-software`
  consumes the CTQs — this skill is the translation matrix between them.
- Not for: running the co-design session or interviews that *gather* the needs → see
  `continuous-improvement-skills:kaizen-and-codesign` (it produces this skill's input). The full
  build-and-verify discipline downstream → see
  `continuous-improvement-skills:lean-six-sigma-for-software` (it consumes this skill's output).

## Do it
1. **Gather the WHATs and weight them.** Pull customer needs from interview notes, co-design
   output, support logs — stated in the customer's words, grouped into a short hierarchy (aim
   for 10–25 leaf needs). Weight each (1–5 or 1–10). **The human gate: weightings are ratified
   by actual customers/users, not invented by the team or the LLM** — draft them as a proposal
   and take them back to the people they claim to represent.
2. **List the HOWs** — technical characteristics the team can measure and set: each needs a
   unit, a direction of improvement (↑/↓/target), and an owner. "Good UX" is not a HOW;
   "steps-to-book" is.
3. **Fill the relationship matrix.** For every WHAT × HOW cell ask: does moving this HOW move
   this WHAT? Score strong = 9, medium = 3, weak = 1, blank = none. Draft fast, then challenge
   the surprises (see `references/house-of-quality-method.md` for the walkthrough).
4. **Build the roof** — HOW-vs-HOW correlations (+/−). Negative cells are the engineering
   tradeoffs that otherwise surface mid-build; each one needs a named resolution or a conscious
   compromise.
5. **Compute importance, benchmark, set targets.** Importance of each HOW = Σ (WHAT weight ×
   relationship score) down its column. Benchmark WHATs against alternatives as customers see
   them, and HOWs against measured competitor values where obtainable. Set a target value per
   HOW — these targets are the CTQs handed downstream.
6. **Cascade.** The prioritized HOWs (with targets) become the WHATs of the next house — product
   characteristics → part/module characteristics → process settings — so customer weight
   survives translation all the way to build decisions.

## Why / learn
QFD (Akao and Mizuno, Japan, late 1960s; first full-scale deployment at Mitsubishi's Kobe
shipyard in 1972; carried west by Hauser & Clausing's HBR article "The House of Quality")
attacks the oldest failure in development: what customers said gets silently replaced, hop by
hop, with what engineers found interesting to build. The house prevents the substitution by
making the translation *explicit and arithmetical* — every technical priority must trace back
through a relationship cell to a weighted customer need, so a pet feature with no strong
relationships visibly earns a near-zero score, and an unglamorous characteristic that serves
five weighted needs visibly dominates. The roof does the complementary job for engineering
honesty: tradeoffs between characteristics are declared before commitment, not discovered in
integration. The evidence claim that made the method famous comes from Toyota's body-rust work:
cumulative development-cost reductions of ~61% against a 1977 base by 1984, with development
time down about a third [snippet-only, HBR]. The method's Western failure mode was never logic
but *labor* — the house took weeks of matrix workshops, so most adoptions collapsed under their
own ceremony. That barrier is gone: an LLM drafts the entire house from interview notes —
candidate WHATs, proposed weights, measurable HOWs, relationship cells, roof conflicts — in
minutes, and the humans do what only they legitimately can: correct the cells they know better,
and ratify the weights with the customers whose voice the house claims to carry. A drafted house
is a hypothesis about what customers meant; only they can confirm it.

## Common mistakes
- The team (or the LLM) invents the weightings → the house launders opinion as customer voice.
  Ratify weights with actual customers/users.
- HOWs that aren't measurable ("intuitive", "robust") → nothing downstream can verify them.
  Every HOW gets a unit and a direction.
- Skipping the roof → the tradeoffs don't disappear; they surface mid-build as surprises.
- Too many WHATs (50+ rows) → an unreadable wall. Group into a hierarchy; matrix the leaf level.
- Filling the matrix by vibe and never challenging it → audit the surprises: empty rows (an
  unserved need) and empty columns (a characteristic serving no one) are the findings.
- Treating the drafted house as final → it's a correction artifact; the value is in the cells
  humans change.
- Stopping after one house → without the cascade, customer weight dies at the first translation.

## Tailor to your environment
Record in `references/your-environment.md` your recurring WHAT sources (co-design notes, support
tickets, survey exports), your standard HOW catalog with units, benchmark sources, and who
ratifies weights (use `your-environment.private.md`, which is git-ignored, for real customer
names, competitor data, or product plans). Never commit raw customer feedback — sanitize to
structure.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/qfd-house-of-quality.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/house-of-quality-method.md — matrix construction walkthrough, weighting math, roof
  analysis, a worked dental-app house with patient WHATs, and cascade mechanics
- references/your-environment.md — your WHAT sources, HOW catalog, benchmarks, and ratifiers
