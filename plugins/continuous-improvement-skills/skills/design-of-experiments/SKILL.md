---
name: design-of-experiments
description: >-
  Designs and analyzes efficient multi-factor experiments — full and fractional two-level
  factorials and Plackett-Burman arrays, randomized run order, replication, main effects and
  interactions with resolution and aliasing explained in plain words, and Taguchi robustness
  against noise factors — so many factors are tested at once instead of one at a time. Use when
  deciding which of many candidate factors actually matter, tuning settings such as reconciliation
  tolerances or prompt-model-temperature combinations, or replacing slow one-factor-at-a-time
  trials with a designed test. Triggers: design of experiments, DOE, factorial, fractional
  factorial, which factors actually matter, orthogonal array, Taguchi, robust design,
  one-factor-at-a-time is too slow.
---

# Design of experiments

## When to use
- Several candidate factors might drive an outcome and you need to know which actually matter —
  and how they interact — in far fewer runs than trying one factor at a time. The method runs from
  Fisher's agricultural work at Rothamsted through Box's industrial statistics at ICI to Taguchi's
  robust design `[snippet-only]`.
- Tuning a rule-driven system configuration — e.g. an auto-reconciliation engine, where tolerance
  and matching-rule settings are the factors and auto-match rate is the response. For *ongoing*
  small-step tuning of live settings after go-live, the sibling is
  `continuous-improvement-skills:evolutionary-operation`.
- Prompt engineering: instruction style × few-shot count × output format × model or temperature is
  a factorial this assistant can design *and run itself* against an eval set — see
  `coding-agent-skills:prompt-engineering` and this repo's own evals.
- The Improve phase of `continuous-improvement-skills:dmaic-problem-solving` today pilots one
  solution against baseline; a designed experiment tests several candidate changes at once and
  reads their interactions.
- Not for: continuous in-production tuning by always-on small steps → see
  `continuous-improvement-skills:evolutionary-operation` (offline designed bursts here; live
  perpetual nudging there). Significance testing on data you already have → see
  `data-analytics-bi-skills:statistical-inference`.

## Do it
`references/doe-method.md` has the design-choice table, aliasing in plain words, a worked
prompt-factorial, Taguchi signal-to-noise, and the analysis walkthrough.
1. **Define the response and list candidate factors.** One measurable response (auto-match rate,
   eval pass rate, cycle time). For each factor set **two levels** — low/high, current/candidate —
   far enough apart to show an effect. **Human gate:** the process owner sets the safety limits;
   levels never exceed what they authorize, and nothing runs against production without their say.
2. **Choose the design.** Few factors (2–4): a **full 2^k factorial** — every combination, all
   interactions readable. Many factors (5+): a **fractional 2^(k-p)** or **Plackett–Burman** array
   to screen for the vital few, accepting known blind spots — *aliasing* means some effects share
   a column and can't be told apart; *resolution* names how bad that confounding is.
3. **Randomize run order; replicate where cheap.** Randomization keeps time trends (drift, warm-up,
   learning) from masquerading as factor effects. Replication — including repeated seeds for
   nondeterministic responses like LLM output — gives you a noise yardstick to judge effects against.
4. **Run, then fit main effects and interactions.** Each factor's effect = mean(response at high)
   − mean(response at low). Real effects stand out from the noise yardstick; drop the rest and
   refit. State clearly what each surviving effect is aliased with before believing it.
5. **Follow up on the survivors.** Fold over the fraction to de-alias what matters; move factor
   levels in the winning direction (steepest ascent); finish with a **verification run** at the
   recommended settings before declaring victory.
6. **Taguchi variant — optimize for robustness.** Add *uncontrollable* noise factors (input-mix
   shifts, paraphrased user inputs, temperature jitter) in an outer array and pick settings that
   maximize signal-to-noise: the winner performs well *across* noise, not just on a good day.
7. **Act on results — human decision.** The analysis recommends; the process owner decides what
   changes, where, and when. When the process under test is itself a prompt or a config file, the
   assistant can execute the runs; it never carries results into production on its own authority.

## Why / learn
Why one-factor-at-a-time (OFAT) loses: it holds everything else fixed, so it can never see an
**interaction** — a tolerance that helps under one matching rule and hurts under another, few-shot
examples that help terse prompts but not stepwise ones — and it spends runs inefficiently. A
factorial design is **balanced (orthogonal)**: every run informs *every* factor's estimate
simultaneously, so eight runs of a 2^3 give each of three factors a four-vs-four comparison — three
experiments for the price of one. Fractional designs push the same logic further: you deliberately
run only a fraction of the combinations and pay with **aliasing** — some effects become
indistinguishable — betting that high-order interactions are negligible (they usually are). That
bet is stated up front as the design's *resolution*, which is what makes a fraction honest: you
know exactly which blind spots you bought. **Randomization** is the insurance policy against the
factor you didn't list — anything drifting with time spreads evenly across conditions instead of
piling onto one. Taguchi's reframe is the deepest: the best setting on your best day is not the
best setting, because the world is noisy; optimizing signal-to-noise picks the configuration whose
performance *doesn't collapse* when the uncontrollable varies. DOE faded in offices because
fractional design, aliasing arithmetic, and the analysis needed a statistician on staff; that
mechanism is exactly what an LLM now supplies conversationally — designing the array, randomizing,
analyzing, explaining the confounding — and when the factors are prompt wording or config values,
executing the runs too. What it must not supply: factor ranges beyond authorized limits, or the
decision to act.

## Common mistakes
- Varying one factor at a time → interactions invisible, runs wasted. Design factorially.
- Not randomizing run order → drift and warm-up masquerade as factor effects. Randomize; block what you can't.
- Setting levels timidly close together → real effects drown in noise. Be bold within the safety limits.
- Trusting a screening fraction's aliased mains blindly → a "main effect" may be an interaction in disguise. Fold over to confirm.
- No replication on a noisy response → no yardstick to separate effect from noise. Replicate (or reseed) where cheap.
- Skipping the verification run → the model's predicted optimum may not reproduce. Confirm before rollout.
- Optimizing on one golden day with no noise factors → a fragile winner. Test robustness across noise (Taguchi).
- Reading statistical significance as practical importance → check the effect size against what the process needs.

## Tailor to your environment
Record your real setup in `references/your-environment.md` (use `your-environment.private.md`,
git-ignored, if it names real systems, accounts, or data). Capture the responses you tune
(auto-match rate, eval pass rate, close cycle time), your candidate factors and their authorized
safe ranges, who signs off on levels and on acting on results, your replication/seed conventions,
and where designs and results are recorded. Never commit real transaction or client data —
sanitize to structure only.

## References
- references/doe-method.md — design-choice table, resolution and aliasing in plain words, a worked
  prompt-factorial, Taguchi signal-to-noise, and the analysis walkthrough
- references/your-environment.md — your responses, factors, and sign-offs (add when supplied)
