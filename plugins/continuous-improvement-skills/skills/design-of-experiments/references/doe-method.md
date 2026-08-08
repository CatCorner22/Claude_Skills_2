# DOE method (reference)

The design-choice table, resolution and aliasing in plain words, a worked prompt-factorial,
Taguchi robustness and signal-to-noise, and the analysis walkthrough.

## Contents
- Choosing the design
- Resolution and aliasing in plain words
- Worked example: a prompt factorial
- Taguchi robustness and signal-to-noise
- Analysis walkthrough
- Following up

## Choosing the design

| Factors | Runs you can afford | Design | What you get / give up |
|---|---|---|---|
| 2–4 | 2^k (4–16) | **Full 2^k factorial** | Every main effect and every interaction, cleanly separated |
| 4–7 | 8–16 | **Fractional 2^(k-p)**, resolution IV+ | Mains clear of two-factor interactions; two-factor interactions alias each other |
| 8–15 | 12–20 | **Plackett–Burman** | Mains only, cheaply; interactions smeared across all columns — a pure screen |
| any, runs nearly free | as many as useful | Full factorial anyway | When runs are cheap (prompts, configs, simulations), buy the clean answer |

Rules of thumb: two levels per factor at the screening stage — you are asking *whether* a factor
matters, not mapping its curve. Add center points (all factors midway) to detect curvature
cheaply. If a factor can't be randomized (e.g. different weeks of statement data), treat it as a
*block*, not a factor.

## Resolution and aliasing in plain words

A full 2^5 factorial needs 32 runs. A **half-fraction** runs 16 of them, chosen so the design
stays balanced. The price: some effects now share a column of the design — their estimates are
literally the same number. That sharing is **aliasing** (confounding): if column A is aliased with
the BCD interaction, "A's effect" is really *A plus BCD*, and no analysis can pull them apart from
these runs alone. The bet you're making — usually safe — is that three-factor-and-higher
interactions are negligible, so the number is mostly A.

**Resolution** grades how risky the sharing is:
- **Resolution III** — main effects alias with two-factor interactions. Cheapest and riskiest;
  fine for a first screen of many factors, dangerous to act on alone.
- **Resolution IV** — mains are clear of two-factor interactions, but two-factor interactions
  alias *each other*. The workhorse screening choice.
- **Resolution V+** — mains and two-factor interactions all clear. Nearly as good as full.

Always write out the alias structure before running, so every conclusion can be stated honestly:
"factor C matters — assuming the D×E interaction it's aliased with is negligible."

## Worked example: a prompt factorial

Response: **eval pass rate** over a fixed test set (this repo's eval files are exactly such a
set). Four factors, two levels each:

| Factor | Low (−) | High (+) |
|---|---|---|
| A: instruction style | terse | stepwise |
| B: few-shot examples | 0 | 3 |
| C: output format | freeform | strict schema |
| D: temperature | 0 | 0.7 |

Design: runs are cheap — the assistant executes them itself — so use the **full 2^4 = 16 runs**
rather than a fraction. Randomize the run order. Because LLM output is nondeterministic, replicate
each cell with n seeds/repeats and use the cell means; the within-cell spread is the noise
yardstick.

Analysis sketch: A's main effect = mean pass rate of the eight (+) runs minus the eight (−) runs;
likewise B, C, D; the A×B interaction = half the difference between B's effect when A is high vs
low. A typical finding shape: strict schema (C) helps everywhere; few-shot (B) helps only with
terse instructions (an A×B interaction — invisible to OFAT); temperature (D) is noise. Follow up:
fix C high, choose A/B by the interaction, drop D from tuning, verify with a fresh run on held-out
cases.

The same skeleton fits Oracle recon tuning offline: factors = tolerance width, date-window days,
reference-key requirement, rule sequence; response = auto-match rate on a *copy* of a
representative statement month — never designed-experiment runs against live production (that is
`continuous-improvement-skills:evolutionary-operation` territory, with its own guardrails).

## Taguchi robustness and signal-to-noise

Taguchi's move: split factors into **control factors** (you set them: prompt style, tolerance) and
**noise factors** (you can't, in production: input mix, paraphrased user requests, statement-volume
spikes, temperature jitter). Cross an inner array of control settings with an outer array of noise
conditions, so each control setting is tested *across* the noise. Score each control setting by a
**signal-to-noise (S/N) ratio** — a single number rewarding both a good mean and a small variance
(for larger-is-better responses, S/N = −10·log₁₀ of the mean of 1/y²; the formula matters less
than the idea). Pick the control setting with the best S/N: the winner is the configuration whose
performance holds up across bad days, not the one that peaked on a good one. If two settings tie
on mean, take the one with less variance — in reconciliation and prompt work alike, predictable
beats occasionally-brilliant.

## Analysis walkthrough

1. **Tabulate** runs in standard order with the response (cell means if replicated).
2. **Compute effects**: each factor's effect = mean(+) − mean(−); interactions from the product
   columns. Every run contributes to every estimate — that's the orthogonality paying off.
3. **Separate signal from noise.** With replicates: compare effects to the replication noise.
   Without: rank the effect magnitudes — in a plain-words half-normal sense, most effects are
   noise and hug a line near zero; real ones stick out visibly. When in doubt, keep the borderline
   term and let the follow-up decide.
4. **Refit** with only surviving terms; sanity-check residuals (any pattern in time order means
   the randomization was protecting you — investigate).
5. **State conclusions with their alias caveats**, effect sizes in the response's own units, and
   whether each effect is practically material — a statistically clear +0.2% match-rate gain may
   not be worth a config change.
6. **Verify**: one confirmation run at the recommended settings, on fresh data, before anyone
   acts. For deeper significance machinery, hand off to
   `data-analytics-bi-skills:statistical-inference`.

## Following up

- **Fold-over**: rerun the fraction with signs flipped to de-alias mains from two-factor
  interactions (or to untangle a specific pair) — the standard second step after a resolution
  III/IV screen.
- **Steepest ascent**: from the fitted effects, step the significant factors together in the
  improving direction, run, repeat until the response turns over; then a small design around the
  peak if the region is curved.
- **Hand the winner to production carefully**: an offline-designed optimum becomes an
  `continuous-improvement-skills:evolutionary-operation` starting point — small, monitored,
  reversible steps in the live system, not a big-bang cutover.
