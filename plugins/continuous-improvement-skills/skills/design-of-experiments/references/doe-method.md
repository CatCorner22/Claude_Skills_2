# DOE method (reference)

The design-choice table with each cell's *true* resolution, run sizing, resolution and aliasing in
plain words, blocking versus split-plot, a worked prompt-factorial with Lenth's PSE, the analysis
walkthrough, fold-over versus semifold, and Taguchi robustness with the mainstream critique of it.

## Contents
- Choosing the design (resolution stated per factor-count *and* run-count)
- Sizing: how many runs, how many replicates
- Resolution and aliasing in plain words
- Blocking, and when the "block" is really a split-plot
- Worked example: a prompt factorial (with Lenth's PSE arithmetic)
- Analysis walkthrough
- Following up: fold-over, semifold, steepest ascent
- Taguchi robustness, signal-to-noise, and the contested part

## Choosing the design

Resolution is a property of the **(factors, runs) pair**, not of the phrase "fractional factorial."
The same five factors give you resolution III in 8 runs and resolution V in 16. So the table is
indexed by both, and every resolution below was derived from the design's defining relation — the
generators are given so you can re-derive them yourself before you run.

| Factors k | Runs | Design / generators | Resolution | What you get / give up |
|---|---|---|---|---|
| 2–4 | 4–16 | **Full 2^k** | (full) | Every main effect and every interaction, cleanly separated |
| 4 | 8 | 2^(4−1), D = ABC → I = ABCD | **IV** | Mains clear of 2-factor interactions (2FIs); 2FIs alias in pairs: AB≡CD, AC≡BD, AD≡BC |
| 5 | 8 | 2^(5−2), D = AB, E = AC | **III** | Mains aliased with 2FIs (A≡BD, D≡AB, C≡AE …) — a ranked shortlist, not a result |
| 6 | 8 | 2^(6−3), D = AB, E = AC, F = BC | **III** | Same: no "main effect" from this design is safe to act on |
| 7 | 8 | 2^(7−4), saturated | **III** | Seven mains out of eight runs, every one riding on 2FIs |
| 5 | 16 | 2^(5−1), E = ABCD → I = ABCDE | **V** | Mains and all 2FIs clear; mains alias 4FIs, 2FIs alias 3FIs |
| 6 | 16 | 2^(6−2), E = ABC, F = BCD | **IV** | Mains clear; the 15 two-factor interactions fall into 7 alias groups — 6 pairs plus one triple (AE = BC = DF) |
| 7 | 16 | 2^(7−3), E = ABC, F = BCD, G = ACD | **IV** | Same trade, more crowded 2FI chains |
| 8 | 16 | 2^(8−4), E = BCD, F = ACD, G = ABC, H = ABD | **IV** | The largest resolution IV design that fits in 16 runs |
| 9–15 | 16 | 2^(k−p) | **III** | Past k = 8 in 16 runs, III is the ceiling — screening only |
| 6 | 32 | 2^(6−1), F = ABCDE | **VI** | Effectively full for anything you would model |
| 7–8 | 32 | 2^(7−2) / 2^(8−3) | **IV** | Mains clear; 2FIs alias each other |
| 8–15 | 12, 16, 20 | **Plackett–Burman** | **III** | Mains only, cheaply; each main is *partially* correlated (±1/3 in the 12-run array) with the 2FIs not containing it — a pure screen |
| any, runs nearly free | as many as useful | Full factorial anyway | (full) | When runs are cheap (prompts, configs, simulations), buy the clean answer |

> **Check that count yourself — the table said "nine aliased pairs" until 2026-08-18, which is
> arithmetically impossible.** Six factors have C(6,2) = 15 two-factor interactions, so nine
> *pairs* would need 18. With I = ABCE = BCDF = ADEF, multiplying each 2FI by every defining
> word gives: AB=CE, AC=BE, AD=EF, AF=DE, BD=CF, BF=CD, and AE=BC=DF — 7 groups, 15 members,
> all accounted for. The triple is the one worth remembering: it is why "pairs" was the wrong
> word as well as the wrong number.

**The ceiling rule, so you can sanity-check any claim including this table's.** In N runs a regular
two-level fraction reaches resolution IV only while k ≤ N/2, and resolution V only for k ≤ 5 at
N = 16 or k ≤ 6 at N = 32. So "six factors with mains clear of two-factor interactions" costs 16
runs, not 8 — and an 8-run design with five or more factors is a **resolution III screen** whose
output is a shortlist for a second experiment, nothing more. If a table, a tool, or an assistant
offers you resolution IV outside those limits, it is wrong: ask for the generators and multiply
them out.

Other rules of thumb: two levels per factor at the screening stage — you are asking *whether* a
factor matters, not mapping its curve. Add center points (all factors midway) to detect curvature
cheaply, and they double as a pure-error estimate.

## Sizing: how many runs, how many replicates

Decide this before running, not after. In a two-level design each effect estimate is a difference
between two means covering half the runs each, so with N total runs and run-to-run standard
deviation σ:

- **SE(effect) = 2σ / √N**
- to detect an effect of size δ at two-sided α = 0.05 and 80% power you need
  δ ≥ (z₀.₉₇₅ + z₀.₈₀) · SE = 2.802 · 2σ/√N, i.e. **N ≥ 31.4 σ²/δ² ≈ 32 σ²/δ² total runs**
- replicates per cell **n = ⌈N / (number of distinct runs in the design)⌉** — 2^k for a full
  factorial, the fraction's own run count otherwise

Worked, on the prompt factorial below: response = eval pass rate, σ ≈ 1.5 percentage points between
repeat runs of the same cell.

- Detect δ = 3 pp: N ≥ 31.4 × 1.5²/3² = 7.9 runs → the **unreplicated 2^4 (16 runs) more than
  covers it**. Check: SE = 2×1.5/√16 = 0.75 pp, so the detectable effect is
  2.802 × 0.75 = **2.10 pp** ✓.
- Detect δ = 1.5 pp: N ≥ 31.4 × 2.25/2.25 = 31.4 → n = ⌈31.4/16⌉ = **2 replicates, 32 runs**.
  Check: SE = 2×1.5/√32 = 0.53, detectable = 1.49 pp ✓ — where the unreplicated design's 2.10 pp
  would have missed it entirely.
- Detect δ = 1.0 pp: N ≥ 31.4 × 2.25/1² = 70.6 → **5 replicates, 80 runs** (SE = 0.34, detectable
  0.94 pp). Halving the effect you want to see roughly quadruples the run bill — the sizing
  formula's most useful consequence, and the reason to argue about δ before buying runs.

That constant is not a coincidence. `data-analytics-bi-skills:ab-test-design` sizes a two-arm test
at n ≈ 16σ²/δ² **per arm** — 32σ²/δ² in total, the same number. A factorial costs what one A/B
test costs and answers k questions with it; the run bill is set by σ, δ, and power, not by how many
factors you list. That skill refuses to launch without an MDE and an n, and a designed experiment
deserves the same discipline: the deliverable's "did it clear the noise yardstick?" column cannot
be filled honestly by a design that was never sized. If σ is unknown, run a few repeats at one
cell first to estimate it; if the budget forces an unreplicated design, plan on Lenth's PSE (below)
as the yardstick and say so up front.

## Resolution and aliasing in plain words

A full 2^5 factorial needs 32 runs. A **half-fraction** runs 16 of them, chosen so the design stays
balanced — the standard choice sets E = ABCD, which makes the defining relation **I = ABCDE**. The
price: some effects now share a column of the design, and their two estimates are literally the
same number. That sharing is **aliasing** (confounding).

Find any effect's partner by multiplying it by the defining word (letters cancel in pairs):

- A × ABCDE = BCDE → **A is aliased with BCDE.** "A's effect" is really *A plus BCDE*, and no
  analysis can separate them from these runs alone.
- AB × ABCDE = CDE → each two-factor interaction is aliased with a three-factor one.

That makes the bet explicit and gradable, which is the whole point of a fraction: a main effect
riding on a **four**-factor interaction is an easy bet; a 2FI riding on a 3FI is a fair one. Change
the design and the bet changes with it — in a 2^(4−1) with I = ABCD, A is aliased with **BCD**
(still usually safe) but AB is aliased with **CD**, which is not safe at all when both pairs are
plausible. Same word "fraction," very different exposure. Work out the alias partners for *your*
design instead of trusting the label.

**Resolution** grades how risky the sharing is:
- **Resolution III** — main effects alias with two-factor interactions. Cheapest and riskiest; fine
  as a first screen of many factors, dangerous to act on alone, because the "big main effect" you
  found may be an interaction wearing its column.
- **Resolution IV** — mains are clear of two-factor interactions, but two-factor interactions alias
  *each other*. The workhorse screening choice.
- **Resolution V+** — mains and two-factor interactions all clear. Nearly as good as full.

Always write out the alias structure before running, so every conclusion can be stated honestly:
"factor C matters — assuming the D×E interaction it's aliased with is negligible."

## Blocking, and when the "block" is really a split-plot

**A block is a nuisance grouping you did not choose and do not care about.** The run set is too big
for one afternoon so half runs Tuesday and half Thursday; two analysts split the work; the test
cases come off two different extracts. Blocking pulls that variation out of the error term instead
of letting it inflate every comparison.

**Blocking costs you an effect, and you pick which one.** Splitting a 2^k into two blocks means the
block contrast has to occupy *some* column of the design, and whatever effect owns that column is
now indistinguishable from "Tuesday vs Thursday." For a 2^3 in two blocks of four, the standard
choice confounds the block with **ABC** — the three-factor interaction, the term you were least
likely to believe anyway. Block on A's column instead and you have thrown away a main effect for
nothing. Write the sacrifice into the run sheet: "blocks confounded with ABC; ABC not estimable."

The bill grows with more blocks, because the generalized interactions go too. A 2^4 in four blocks
of four confounds two chosen contrasts **and their product** — and in four factors every pair of
three-letter words multiplies to a two-letter word (ABC × ABD = CD), so **one two-factor
interaction is unavoidably lost**. Choose which one you can live without before the first run.

**When the un-randomizable thing is a factor you actually care about, it is not a block — it is a
hard-to-change factor, and the design is a split-plot.** "Different weeks of data" is the giveaway:
if the week is merely *when* runs happened, it is a block; if the thing you are testing is itself
expensive or impossible to reset per run — the data extract, a model deployment, an index rebuild,
an oven temperature, a queue configuration that takes a day to settle — you will inevitably run
several cheap factors inside each setting of the expensive one. That is a **split-plot**:

- **whole-plot factors** — the hard-to-change ones, changed once per plot;
- **subplot factors** — the cheap ones, randomized within each plot;
- **two error terms** — whole-plot error (between plots, few degrees of freedom, usually the larger
  variance) and subplot error (within plots, smaller).

Analysing a split-plot as if it were completely randomized pools those two errors into one. The
pooled error lands below the true whole-plot error, so **the hard-to-change factor looks more
significant than the data supports** — and that expensive factor is exactly the one you least want
to be wrong about. Test whole-plot effects against whole-plot error and subplot effects against
subplot error; if you are not fitting a mixed model, at minimum state which effects were judged
against which error, and treat a whole-plot p-value from a pooled fit as unreliable.

## Worked example: a prompt factorial

Response: **eval pass rate** over a fixed test set (this repo's eval files are exactly such a
set). Four factors, two levels each:

| Factor | Low (−) | High (+) |
|---|---|---|
| A: instruction style | terse | stepwise |
| B: example count | 0 | 3 |
| C: output mechanism | format described in the prompt | provider-native structured output (schema-constrained) |
| D: reasoning effort | low | high |

**Every level has to be settable — check that before it goes in the table.** A factor whose high
level the provider refuses is not a factor, it is a failed run. Sampling temperature is the live
example: the Claude API rejects non-default `temperature`/`top_p`/`top_k` on its 4.7-and-later
generations, so "temperature 0 vs 0.7" is unrunnable there and effort level is the knob that
replaced it. This is the same discipline as the human gate on factor ranges in step 1 — levels you
are not permitted to set and levels the system will not accept fail the design identically.

Design: runs are cheap — the assistant executes them itself — so use the **full 2^4 = 16 runs**
rather than a fraction, and randomize the run order. Model output varies run to run, so repeats per
cell are what turn that variation into a measured yardstick (the within-cell spread) instead of an
adjective. Sizing decides how many: at σ ≈ 1.5 pp the **unreplicated** 16 runs detect ~2.1 pp,
while resolving 1.5 pp needs **2 repeats per cell** (32 runs). Pick which one the decision needs
*before* running. And if a model grades the outputs, qualify the grader first — a noisy judge
inflates σ and eats the run budget
(`continuous-improvement-skills:measurement-systems-analysis`).

Take the unreplicated branch for the analysis below, precisely because it is the harder case.

Suppose the 16 unreplicated runs give these effect estimates, in percentage points of pass rate
(each effect = mean(+) − mean(−)):

| Effect | Est. | Effect | Est. | Effect | Est. |
|---|---|---|---|---|---|
| A instruction style | +1.2 | AB | +3.6 | ABC | −0.7 |
| B example count | +2.0 | AC | −0.8 | ABD | +0.2 |
| C output mechanism | +7.4 | AD | +0.5 | ACD | +0.4 |
| D reasoning effort | −0.4 | BC | +0.9 | BCD | −0.5 |
| | | BD | −0.3 | ABCD | +0.3 |
| | | CD | +0.6 | | |

Unreplicated, so there is no within-cell noise to compare against — use **Lenth's PSE**, worked in
full on these m = 15 contrasts:

- sorted |cⱼ|: 0.2, 0.3, 0.3, 0.4, 0.4, 0.5, 0.5, **0.6**, 0.7, 0.8, 0.9, 1.2, 2.0, 3.6, 7.4 →
  median = 0.6, so s₀ = 1.5 × 0.6 = **0.90**
- trim at 2.5 s₀ = 2.25 — this drops 3.6 and 7.4 (the real effects) out of the noise estimate,
  leaving 13 values whose median is 0.5 → **PSE = 1.5 × 0.5 = 0.75 pp**
- d = m/3 = 5, t₀.₉₇₅,₅ = 2.571 → **ME = 1.93 pp**
- γ = (1 + 0.95^(1/15))/2 = 0.99829, t_γ,₅ = 5.219 → **SME = 3.91 pp**

Sanity check on the yardstick itself: at σ = 1.5 pp over 16 runs the true SE(effect) is
2×1.5/√16 = 0.75 pp, and Lenth's PSE returned 0.75 — it recovered the noise level from the effects
alone, with no replicates. Do not read that as a guarantee; PSE is an estimate with its own spread,
and the agreement here is a clean draw, not a property.

Reading the effects honestly: **C (+7.4)** clears both margins — provider-native structured output
helps everywhere, and that one is settled. **AB (+3.6)** clears ME and just misses SME (3.91): a
strong candidate, not a proven effect, and it is the thing the follow-up run exists to confirm —
examples paying off only with terse instructions. **B (+2.0)** clears ME barely and is nowhere near
SME, which is exactly the signature of a factor whose effect lives mostly inside its interaction.
A (+1.2), D (−0.4) and every three-way term sit inside the noise. Follow-up: fix C high, choose A/B
from the AB interaction, stop paying for high effort on this task, and verify on held-out cases.
Note what the arithmetic did *not* say — never "effort doesn't matter," only that a 0.4 pp effect is
indistinguishable from a 0.75 pp noise level, which is a real finding when the high level costs
latency and tokens. And the sizing choice shows up here concretely: with 2 repeats per cell the
pooled-error margin would have been t₀.₉₇₅,₁₆ × 0.53 = **1.12 pp** against Lenth's 1.93 — about
1.7× finer, enough to carry AB (3.6) and B (2.0) past even a multiplicity-corrected margin of
1.83 pp. That is what the extra 16 runs would have bought, priced before the fact rather than
regretted after.

**Which skill owns which prompt question.** `coding-agent-skills:prompt-engineering` states the seam
in its own iteration step, and this file holds the same line from the other side:
**one-factor-at-a-time is for attributing a fix; a factorial is for finding the best combination.**
Neither rule is a concession to the other — they answer different questions. So: a prompt is
producing wrong output and you need to know which edit caused what → one edit per run against a
fixed case set, over there. Several knobs are in play at once and you want the winning combination
plus the interactions between them → the factorial here. That skill also owns the pieces this design
treats as given: the output contract enforced by provider-native structured output rather than by
wording, reasoning depth set by *configuration* rather than elicited in the prompt, and repeat runs
as the way variance gets measured instead of switched off. Those are what make factors C and D
above settable at all, and its repeat-run practice is where the σ this design sizes against comes
from. If you have no eval set with a pass rate yet, you are not ready for this skill — build it
there first.

The same skeleton fits rule-driven config tuning offline: factors = tolerance width, date-window
days, reference-key requirement, rule sequence; response = auto-match rate on a *copy* of a
representative month of data — never designed-experiment runs against live production (that is
`continuous-improvement-skills:evolutionary-operation` territory, with its own guardrails).

## Analysis walkthrough

1. **Tabulate** runs in standard order with the response (cell means if replicated).
2. **Compute effects**: each factor's effect = mean(+) − mean(−); interactions from the product
   columns. Every run contributes to every estimate — that's the orthogonality paying off. (A
   semifolded or otherwise non-orthogonal design breaks this: fit it by least squares instead.)
3. **Separate signal from noise.**
   - *With replicates*: pool the within-cell variances into s², then SE(effect) = 2s/√N and compare
     each effect against t·SE. This is the "noise yardstick" the deliverable asks for.
   - *Unreplicated*: use **Lenth's pseudo standard error**, which builds the noise estimate out of
     the mass of small effects. From the m contrasts: s₀ = 1.5 × median|cⱼ|; then
     PSE = 1.5 × median{|cⱼ| : |cⱼ| < 2.5 s₀}; then ME = t₀.₉₇₅,d × PSE with d = m/3, and the
     simultaneous margin SME = t_γ,d × PSE with γ = (1 + 0.95^(1/m))/2. Effects past ME are
     individually significant; only those past SME survive the multiple-comparison price of
     screening m effects at once. Worked arithmetic in the prompt example above.
   - The **half-normal plot** is the same idea by eye: plot sorted |effects| against half-normal
     quantiles — noise effects fall on a line through the origin, real ones peel off to the right.
     Use it to sanity-check the PSE, not instead of it.
4. **Refit** with only surviving terms; sanity-check residuals (any pattern in time order means the
   randomization was protecting you — investigate).
5. **State conclusions with their alias caveats**, effect sizes in the response's own units, and
   whether each effect is practically material — a statistically clear +0.2% match-rate gain may
   not be worth a config change.
6. **Verify**: one confirmation run at the recommended settings, on fresh data, before anyone acts.
   For deeper significance machinery, hand off to
   `data-analytics-bi-skills:statistical-inference`.

## Following up: fold-over, semifold, steepest ascent

**Fold-over — and only where it buys something.** A fold-over reruns the fraction with signs
reversed and analyses both blocks together. What it buys depends entirely on the resolution you
started from, and the common advice ("fold over after a III/IV screen") is right for one of those
and wrong for the other.

- **Resolution III → full fold-over (reverse every factor's sign).** The classic move, and it
  works. On the 8-run 2^(5−2) (D = AB, E = AC) the original design has A ≡ BD, C ≡ AE, D ≡ AB and
  so on; after the 8 mirrored runs every main effect is orthogonal to every two-factor interaction
  — the combined 16-run design is resolution IV. The 2FIs still alias each other in pairs
  (BC ≡ DE, BD ≡ CE, BE ≡ CD). Cost: double the runs. Payoff: clean mains.
- **Resolution IV → a full fold-over buys nothing about the aliasing.** The mains were already
  clear, and reversing all the signs leaves the 2FI alias pairs *exactly* where they were: on
  2^(4−1) it is AB ≡ CD, AC ≡ BD, AD ≡ BC before and after; on the 16-run 2^(6−2), the same 7
  alias groups before and after. A second full block here buys **replication** — it halves
  SE(effect) — and nothing else. Do not spend it expecting to untangle an interaction.
- **Resolution IV → break a specific pair with a single-factor fold or a semifold.** Reverse the
  sign of *one* factor instead of all of them and every 2FI involving that factor comes free of its
  partner. On 2^(4−1), a full second block with A reversed yields the complete 2^4 — all three
  pairs de-aliased. Cheaper: a **semifold** reruns only half the original runs (those at one level
  of A) with A's sign flipped. On the 16-run 2^(6−2), 8 semifold runs (24 total — half the price of
  a full fold-over) de-alias AB, AC, AD, AE and AF from their partners, while BC ≡ DF, BD ≡ CF and
  BF ≡ CD stay aliased. That is the point: you pay to see the pairs you suspect, not all of them.
  The semifolded design is **not orthogonal** — some mains pick up ±1/3 correlations with 2FIs — so
  fit all 24 runs by least squares, never by mean(+) − mean(−) on the columns.

So the real decision is *which factor to fold on*: pick the one whose interactions your conclusion
depends on, and say why in the run sheet.

- **Steepest ascent**: from the fitted effects, step the significant factors together in the
  improving direction, run, repeat until the response turns over; then a small design around the
  peak if the region is curved.
- **Hand the winner to production carefully**: an offline-designed optimum becomes an
  `continuous-improvement-skills:evolutionary-operation` starting point — small, monitored,
  reversible steps in the live system, not a big-bang cutover.

## Taguchi robustness, signal-to-noise, and the contested part

Taguchi's move: split factors into **control factors** (you set them: prompt style, tolerance) and
**noise factors** (you can't, in production: input mix, paraphrased user requests, volume spikes,
run-to-run sampling variation). Cross an inner array of control settings with an outer array of noise
conditions, so each control setting is tested *across* the noise. Score each control setting by a
**signal-to-noise (S/N) ratio** — a single number rewarding both a good mean and a small variance
(for larger-is-better responses, S/N = −10·log₁₀ of the mean of 1/y²). Pick the control setting
with the best S/N: the winner is the configuration whose performance holds up across bad days, not
the one that peaked on a good one. If two settings tie on mean, take the one with less variance —
in prompt work and rule tuning alike, predictable beats occasionally-brilliant.

### The contested part — know both sides before you adopt this

This is the most argued-over corner of DOE, and a reader taught only the recipe above has been
taught one side. Taguchi's **goals** were absorbed into mainstream practice: design for robustness
against noise, treat variance as a cost, put the customer's loss in the objective. His **methods**
for reaching them were criticized hard and largely not adopted, on two grounds:

- **Crossed arrays are run-inefficient.** An inner array crossed with an outer array multiplies run
  counts — a 9-run inner × 4-run outer is 36 runs before any replication. The mainstream
  alternative is a **combined (single) array**: put control and noise factors into one design and
  estimate the **control × noise interactions** directly. Those interactions *are* the robustness —
  a control factor confers robustness exactly when its effect changes across noise levels — so a
  combined array reaches the same conclusion in far fewer runs *and* tells you which noise factor
  each control setting is protecting against, which the crossed-array S/N summary averages away.
- **S/N ratios confound mean and variance.** Collapsing a row to one number mixes location with
  dispersion, so a setting can win on S/N while being worse on both quantities you actually care
  about; the logarithm also bakes in a transformation you did not choose. The standard alternative
  is to model the **mean and the dispersion separately** (often log s² as its own response), look
  at both, and make the trade-off explicitly — applying a variance-stabilising transformation only
  if the data asks for one.

The critique is associated with Box's work on signal-to-noise ratios and transformations and with
the Technometrics panel discussion on parameter design edited by Nair; the combined-array approach
comes out of the same literature `[background — verify before citing]`. Working position: **use
Taguchi's question and answer it with a combined array plus separate mean and dispersion models.**
S/N remains a reasonable one-number summary for a quick screen — if you report it, report the mean
and the variance beside it so a reader can see what the single number traded away.
