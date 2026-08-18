---
name: design-of-experiments
description: >-
  Designs and analyzes multi-factor experiments — full and fractional two-level
  factorials and Plackett-Burman arrays, each design's true resolution and alias structure in plain
  words, run and replicate sizing for a target effect size, randomized run order, blocking and
  split-plots for factors that cannot be randomized, main effects and interactions judged against a
  noise yardstick (Lenth's PSE when unreplicated), and Taguchi robustness against noise factors
  with the combined-array critique of it — so many factors are tested at once.
  Use when deciding which of many candidate factors actually matter, tuning settings such as
  tolerance or prompt, model, and effort-level combinations, or replacing slow
  one-factor-at-a-time trials with a designed test. Triggers: design of experiments, DOE, factorial, fractional factorial,
  which factors actually matter, orthogonal array, screening design, split-plot, Taguchi, robust
  design, one-factor-at-a-time is too slow.
metadata:
  version: "1.2.1"
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
- Prompt *optimization* across several knobs at once — instruction style × example count × output
  mechanism × model or effort level — where you have a scored eval set and the knobs plainly interact.
  That is a factorial this assistant can design *and run itself*.
- The Improve phase of `continuous-improvement-skills:dmaic-problem-solving` today pilots one
  solution against baseline; a designed experiment tests several candidate changes at once and
  reads their interactions.
- Not for: **debugging one prompt** → `coding-agent-skills:prompt-engineering`, which states the
  same seam from its side: **one-factor-at-a-time is for attributing a fix, a factorial is for
  finding the best combination.** It also owns what this design takes as given — the output contract
  enforced by provider-native structured output, reasoning depth set by configuration, and repeat
  runs as how variance gets measured. With no scored eval set yet, start there. Continuous
  in-production tuning by always-on small steps →
  `continuous-improvement-skills:evolutionary-operation` (offline designed bursts here; live
  perpetual nudging there). One live two-variant test on real traffic or real cases, with an MDE and
  a stopping rule → `data-analytics-bi-skills:ab-test-design`. Significance testing on data you
  already have → `data-analytics-bi-skills:statistical-inference`.

## Do it
`references/doe-method.md` has the design-choice table with each cell's true resolution and the
ceiling rule, run sizing, aliasing in plain words, blocking versus split-plot, a worked
prompt-factorial with Lenth's PSE arithmetic, fold-over versus semifold, and Taguchi
signal-to-noise with the combined-array critique. The deliverable is three
artifacts: a **run sheet** (the design matrix with factor levels, the design's resolution, any block
or whole-plot structure, randomized order, and the replication plan), an **effects table** (each
effect, its alias statement, and whether it cleared the noise yardstick — named, either the pooled
replication error or Lenth's ME/SME), and a **recommendation** naming the winning settings with the
verification-run result. If the design was never sized against a target effect δ, say so on the run
sheet rather than implying a yardstick you don't have.
1. **Define the response and list candidate factors.** One measurable response (auto-match rate,
   eval pass rate, cycle time). For each factor set **two levels** — low/high, current/candidate —
   far enough apart to show an effect. **Human gate:** the process owner sets the safety limits;
   levels never exceed what they authorize, and nothing runs against production without their say.
2. **Choose the design, and state its real resolution.** Few factors (2–4): a **full 2^k
   factorial** — every combination, all interactions readable. Many factors (5+): a **fractional
   2^(k-p)** or **Plackett–Burman** array to screen for the vital few, accepting known blind spots —
   *aliasing* means some effects share a column and can't be told apart; *resolution* names how bad
   that confounding is. Resolution belongs to the **(factors, runs) pair**, never to the phrase
   "fractional factorial": five factors are resolution III in 8 runs and resolution V in 16. Read
   the resolution off the table in `references/doe-method.md` — or derive it from the generators —
   and remember the ceiling: **resolution IV needs k ≤ runs/2.** Eight runs with 5–7 factors is a
   resolution III screen, so its "main effects" may be two-factor interactions in disguise.
3. **Size the experiment, then randomize and replicate.** With σ the run-to-run spread of the
   response and δ the smallest effect worth acting on, **N ≥ 32σ²/δ² total runs**
   (SE(effect) = 2σ/√N), so replicates = N ÷ the design's run count. Say δ out loud before running,
   the way `data-analytics-bi-skills:ab-test-design` refuses to launch without an MDE — the
   deliverable's "cleared the noise yardstick?" column is unfillable otherwise. Randomize run order
   so time trends (drift, warm-up, learning) can't masquerade as factor effects. Replicate —
   including repeated runs for nondeterministic responses like model output — where it's cheap; where
   it isn't, plan on **Lenth's PSE** as the yardstick instead of an eyeball. For a nuisance grouping
   you can't randomize away, **block** — and name the effect the block confounds. For a factor of
   interest that's expensive to change, it's a **split-plot** with two error terms, not a block.
4. **Run, then fit main effects and interactions.** Each factor's effect = mean(response at high)
   − mean(response at low). Judge each against the yardstick — pooled within-cell error if
   replicated; Lenth's PSE margins (ME, and SME for the multiple-comparison price) if not. Drop the
   rest and refit. State clearly what each surviving effect is aliased with before believing it.
5. **Follow up on the survivors.** After a **resolution III** screen, a full fold-over (all signs
   reversed) clears the mains of two-factor interactions. After a **resolution IV** design the mains
   are already clear, so a full fold-over buys replication and nothing else — to break a specific
   two-factor alias pair, flip **one** factor's sign (a single-factor fold, or a half-price
   *semifold*). Then move factor levels in the winning direction (steepest ascent) and finish with a
   **verification run** at the recommended settings before declaring victory.
6. **Taguchi variant — optimize for robustness.** Add *uncontrollable* noise factors (input-mix
   shifts, paraphrased user inputs, run-to-run sampling variation) so each setting is tested across
   noise: the winner performs well *across* noise, not just on a good day. Taguchi's crossed inner
   and outer arrays with a signal-to-noise score are one way; mainstream practice prefers a
   **combined array** (control and noise factors in one design, control × noise interactions
   estimated directly) plus separate mean and dispersion models, because crossed arrays multiply run
   counts and an S/N ratio confounds mean with variance. Both sides are in the reference — the goal
   is Taguchi's, the machinery need not be.
7. **Act on results — human decision.** The analysis recommends; the process owner decides what
   changes, where, and when. When the process under test is itself a prompt or a config file, the
   assistant can execute the runs; it never carries results into production on its own authority.

## Why / learn
Why one-factor-at-a-time (OFAT) loses *as an optimizer*: it holds everything else fixed, so it can
never see an **interaction** — a tolerance that helps under one matching rule and hurts under
another, few-shot examples that help terse prompts but not stepwise ones — and it spends runs
inefficiently. Note the qualifier. One-change-at-a-time is not a mistake in general; it is the only
way to get **attribution**, which is why debugging advice everywhere (including
`coding-agent-skills:prompt-engineering`) insists on it. Change five things, see improvement, and
you know the bundle worked and nothing else. So the two rules live together, on the axis that skill
names: **one at a time attributes a fix; a factorial finds the best combination.** Confusing the two
questions is the actual error. A
factorial design is **balanced (orthogonal)**: every run informs *every* factor's estimate
simultaneously, so eight runs of a 2^3 give each of three factors a four-vs-four comparison — three
experiments for the price of one. Fractional designs push the same logic further: you deliberately
run only a fraction of the combinations and pay with **aliasing** — some effects become
indistinguishable — betting that high-order interactions are negligible (they usually are). That
bet is stated up front as the design's *resolution*, which is what makes a fraction honest: you
know exactly which blind spots you bought — which is also why the bet must be priced honestly: a
design's resolution follows from its generators and its run count, so a promise of "resolution IV"
that the arithmetic doesn't support is not a rule of thumb, it is a wrong answer that reads as a
clean one. **Randomization** is the insurance policy against the factor you didn't list — anything
drifting with time spreads evenly across conditions instead of piling onto one; **blocking** is what
you do when a nuisance grouping can't be randomized away, and it is never free (the block eats one
column, so you choose which effect to lose). Taguchi's *question* is the deepest reframe: the best
setting on your best day is not the best setting, because the world is noisy; you want the
configuration whose performance *doesn't collapse* when the uncontrollable varies. His answer —
crossed arrays scored by a signal-to-noise ratio — is the part the field argued over and largely
replaced with combined arrays and separate mean/variance models, because one number that mixes mean
with variance can crown a setting that is worse on both. DOE faded in offices because
fractional design, aliasing arithmetic, and the analysis needed a statistician on staff; that
mechanism is exactly what an LLM now supplies conversationally — designing the array, randomizing,
analyzing, explaining the confounding — and when the factors are prompt wording or config values,
executing the runs too. What it must not supply: factor ranges beyond authorized limits, or the
decision to act.

## Common mistakes
- Varying one factor at a time *to optimize* → interactions invisible, runs wasted. Design factorially. (One at a time attributes a fix; a factorial finds the best combination → `coding-agent-skills:prompt-engineering`.)
- Listing a factor whose high level the system rejects → a failed run, not a data point. Confirm every level is settable before the run sheet is signed.
- Assuming any fraction is resolution IV → at 8 runs only k=4 is; k=5–7 are resolution III. Derive resolution from the generators; resolution IV needs k ≤ runs/2.
- Running an unsized design → no δ, no yardstick, no honest effects table. Compute N ≥ 32σ²/δ² first.
- Not randomizing run order → drift and warm-up masquerade as factor effects. Randomize; block what you can't, and say which effect the block cost you.
- Calling a hard-to-change factor a "block" → it's a split-plot; a single pooled error overstates that factor's significance. Two error terms, stated.
- Setting levels timidly close together → real effects drown in noise. Be bold within the safety limits.
- Trusting a screening fraction's aliased mains blindly → a "main effect" may be an interaction in disguise. Fold over (resolution III) or semifold (resolution IV) to confirm.
- Full fold-over of a resolution IV design to "de-alias" it → the alias pairs come back unchanged; you bought replication. Flip one factor instead.
- No replication *and* no PSE on a noisy response → no yardstick at all. Replicate where cheap; otherwise run Lenth's PSE.
- Skipping the verification run → the model's predicted optimum may not reproduce. Confirm before rollout.
- Optimizing on one golden day with no noise factors → a fragile winner. Test robustness across noise.
- Reporting an S/N ratio alone → it hides whether the mean or the variance moved. Report mean and variance beside it.
- Reading statistical significance as practical importance → check the effect size against what the process needs.

## Tailor to your environment
Record your real setup in `references/your-environment.md` (use `your-environment.private.md`,
git-ignored, if it names real systems, accounts, or data). Capture the responses you tune
(auto-match rate, eval pass rate, close cycle time), your candidate factors and their authorized
safe ranges, who signs off on levels and on acting on results, your replication conventions,
and where designs and results are recorded. Never commit real transaction or client data —
sanitize to structure only.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/design-of-experiments.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/doe-method.md — design-choice table with per-cell resolution and the ceiling rule, run
  and replicate sizing, resolution and aliasing in plain words, blocking versus split-plot, a worked
  prompt-factorial with Lenth's PSE, fold-over versus semifold, Taguchi signal-to-noise and the
  combined-array critique, and the analysis walkthrough
- references/your-environment.md — your responses, factors, and sign-offs (add when supplied)
