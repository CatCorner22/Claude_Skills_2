---
name: probability-fundamentals
description: >-
  Computes probabilities with the core rules — complement, addition with
  the overlap subtracted, multiplication for independent events — and teaches
  frequency vs degree-of-belief readings, mutually exclusive vs independent
  (near-opposites), conditional probability and why P(A|B) differs from P(B|A) (the
  prosecutor's fallacy), Bayes' theorem via natural frequencies (out-of-10,000
  tables) so rare-condition screening results read right, expected value and when it
  misleads (ruin risk, one-shot decisions), plus inoculations against base-rate
  neglect, the gambler's fallacy, the conjunction fallacy, and hot-hand overreads.
  Use for any chance-of-X question, combining event probabilities, or interpreting a
  positive test, screen, or alarm; not for sample-to-population inference
  (confidence intervals, p-values). Triggers: probability, odds, chance of,
  conditional probability, Bayes, Bayes' theorem, expected value, independent
  events, mutually exclusive, base rate neglect, likelihood of both, what are the
  odds.
---

# Probability fundamentals

Probability math exists because intuition reliably fails in exactly these spots:
combining chances, reversing conditionals, weighing rare events, and summarizing
risky choices. This skill computes those answers correctly — preferring plain counts
over formulas — and inoculates against the standard fallacies.

## When to use
- Working out the chance of one event, of both of two events, of either, or of an
  event given something already known.
- Interpreting a positive test, screen, or alarm when the condition it looks for is
  rare (the low-base-rate trap).
- Deciding whether expected value is the right summary of a risky choice, and what to
  use when it is not.
- Not for: reasoning from a sample to a population — confidence intervals, hypothesis
  tests, p-values → see `data-analytics-bi-skills:statistical-inference`.
- Not for: forecasting real projects by anchoring on distributions of past cases →
  see `decision-science-skills:reference-class-forecasting` (it consumes the
  base-rate discipline this skill teaches, and owns the base-rate-anchoring
  workflow).
- Not for: running belief revision on a live decision — priors, likelihood ratios,
  update journals → see `decision-science-skills:bayesian-updating`.
- Not for: weighing competing explanations of the same body of evidence → see
  `decision-science-skills:competing-hypotheses-analysis`.
- Not for: failure-time modeling — Weibull fits, MTBF, availability → see
  `safety-and-reliability-skills:reliability-engineering`.
- For order-of-magnitude reasonableness of the inputs you feed these rules → see
  sibling `math-foundations-skills:number-sense-and-estimation`.

## Do it
1. **Fix the sample space and say what the probability means.** Long-run frequency of
   a repeatable process (a claim about the world) or degree of belief in a one-off
   statement (a claim about your information) — both obey the same rules, but the
   meaning decides what evidence could change the number.
2. **Apply the basic rules, on counts wherever possible.**
   - Complement: P(not A) = 1 − P(A).
   - Addition: P(A or B) = P(A) + P(B) − P(A and B); subtract the overlap or it is
     counted twice. Worked: drawing a heart or a face card =
     13/52 + 12/52 − 3/52 = 22/52 ≈ 42.3% (the 3 face-hearts sit in both counts).
   - Multiplication: P(A and B) = P(A) × P(B|A) always; it collapses to
     P(A) × P(B) only when the events are independent. Two aces in a row without
     replacement: 4/52 × 3/51 = 1/221 ≈ 0.45% — not (4/52)² ≈ 0.59%, because the
     first draw changes the deck.
3. **Keep "mutually exclusive" and "independent" apart — they are near-opposites.**
   Mutually exclusive means the events cannot co-occur (P(A and B) = 0), so knowing
   one happened tells you the other did not: maximal dependence. Independent means
   knowing one tells you nothing about the other. One die: "even" and "5 or higher"
   are independent — P(both) = P({6}) = 1/6 = 1/2 × 1/3. "Even" and "equals 3" are
   mutually exclusive, and therefore strongly dependent: P(even | rolled 3) = 0.
4. **Treat conditioning as shrinking the universe.** P(A|B) = P(A and B) / P(B):
   throw away every outcome where B is false, then renormalize. Worked:
   P(5 or higher | even) = (1/6)/(1/2) = 1/3 — the universe shrank to {2, 4, 6} and
   one of those three qualifies. And never flip a conditional silently:
   P(A|B) ≠ P(B|A) in general. "90% of true cases test positive" does not mean "90%
   of positives are true cases" — that reversal is the prosecutor's fallacy.
5. **Do Bayes with natural frequencies, not the formula.** Pick a round crowd, split
   it by the base rate *first*, then by test behavior. Worked screening example —
   base rate 1%, sensitivity 90%, false-alarm rate 9%:
   - Out of 10,000 people: 100 have the condition; 9,900 do not.
   - Of the 100 with it: 90 test positive, 10 test negative.
   - Of the 9,900 without it: 891 test positive (9%), 9,009 test negative.
   - Positives in total: 90 + 891 = 981. So P(condition | positive) = 90/981 ≈ 9.2%.
   Most positives are false — not because the test is bad, but because the healthy
   crowd is 99 times larger, so even its small error rate out-produces the sick
   crowd's true positives. Cross-check the table before trusting it: rows must sum
   (90 + 10 = 100; 891 + 9,009 = 9,900). More tables, and the odds shortcut, in
   references/probability-worked.md.
6. **Compute expected value, then ask the two questions.** EV = Σ p × payoff.
   Worked: 80% chance of winning 500, 20% chance of losing 1,500:
   0.8 × 500 − 0.2 × 1,500 = 400 − 300 = +100. Before letting EV decide, ask:
   (a) *Repeats* — do I get many draws, each small relative to my resources?
   (b) *Ruin* — can one loss end the game? If the answer is one-shot or ruinous, EV
   is the wrong summary; a worked EV-says-yes/ruin-says-no decision is in the
   reference.
7. **Run the fallacy inoculations** (full catalog in the reference):
   - Base-rate neglect: ask "how common is it?" before "how well does the evidence fit?"
   - Gambler's fallacy: independent trials have no memory; the long run evens out by
     swamping the past, not by correcting it.
   - Conjunction fallacy: added detail can only remove cases — P(A and B) ≤ P(A).
   - Hot hand vs small samples: short streaks arise in random sequences more often
     than intuition expects; treat them as weak evidence in either direction.

## Why / learn
The rules are counting discipline. The addition rule is just refusing to
double-count the overlap; the multiplication rule is "of the fraction where A
happens, what fraction of *that* has B"; conditioning is shrinking the universe to
what you know and renormalizing so the remaining chances sum to 1. Whenever the
formulas feel slippery, drop to a whole-number crowd and count — the arithmetic is
the same, but the denominators become visible.

P(A|B) and P(B|A) differ because they answer questions about two different
denominators — and the ratio between those denominators is the base rate. In the
screening table, P(positive | condition) = 90/100 while
P(condition | positive) = 90/981: same 90 people on top, wildly different crowds
underneath. A base rate is the prior that vivid evidence tempts you to throw away.
Evidence *updates* the prior; it never replaces it. This is Gigerenzer's insight
about why natural frequencies fix base-rate neglect: the counts carry the base rate
along (891 false positives standing next to 90 true ones), while percentage
statements quietly swap denominators mid-sentence.

Expected value is a long-run average, so it is the right summary exactly when you
live in the long run: many repeats, each small enough that no single loss changes
the game. One-shot decisions and ruinous stakes break both conditions — an average
assumes you are still around to collect it. Ruin compounds: a repeated bet of
+50%/−40% on your whole stake has EV +5% per flip, yet the typical path shrinks
about 5.1% per flip, because repeated outcomes multiply and the geometric factor
√(1.5 × 0.6) ≈ 0.949 governs — see sibling
`math-foundations-skills:exponential-growth-and-logs` for why repeated
multiplication answers to the geometric mean, not the arithmetic one.

The fallacies are not stupidity; they are good heuristics misfiring. Representative
stories feel likelier than sparse ones (conjunction), balance feels due after a
streak (gambler's), and the vivid case in front of you feels more informative than
the boring base rate (base-rate neglect). The math is the corrective lens, which is
why each fallacy gets a one-line question you can ask *before* the intuition locks in.

## Common mistakes
- Adding probabilities of events that can co-occur → subtract the overlap.
- Multiplying probabilities of dependent events as if independent → use
  P(A) × P(B|A); independence is a claim to justify, not a default.
- Using "mutually exclusive" to mean "independent" → exclusive events are maximally
  dependent; check which one you have.
- Flipping a conditional (prosecutor's fallacy) → build the natural-frequency table
  and read the direction you actually need.
- Reading a positive test on a rare condition as "probably true" → the base rate
  decides; run the 10,000-person table first.
- Justifying a one-shot, potentially ruinous bet by its positive EV → ask the
  repeats question and the ruin question first.
- Rating the detailed scenario as more probable than the plain one → conjunctions
  only remove cases.
- Expecting a run of losses to make a win "due" → independent trials have no memory.

## Tailor to your environment
Record in `references/your-environment.md`: the recurring probability questions your
work actually asks (which screens, flags, or alarms you interpret and their rough
base rates), where you look up base rates rather than assume them, your house crowd
size for natural-frequency tables, and any decisions where ruin — not EV — is the
binding constraint. Keep committed content structural — real incident rates, client
data, or account-level numbers belong in `your-environment.private.md` (git-ignored).

## References
- references/probability-worked.md — the rules with plain-language count
  walkthroughs; natural-frequency Bayes tables (screening and fraud-flag) with every
  cell recomputed, plus the odds-form shortcut; expected-value worked decisions
  including one where EV says yes and ruin says no; the fallacy catalog
- references/your-environment.md — your screens and their base rates, house table
  conventions, and ruin constraints (fill in)
