# Bayesian updating — full method

Contents: 1. The update loop · 2. Setting the prior (reference-class handoff, and the hypothesis
list) · 3. The likelihood question · 4. Updating with counts (worked alert triage) ·
5. The odds shortcut, chaining, and LR-error compounding · 6. Bayes-factor vocabulary ·
7. The update journal (Tetlock discipline) · 8. The trap catalog (incl. the catch-all hypothesis) ·
9. The honest history · 10. Provenance notes

## 1. The update loop

Belief revision is a loop, not an event:

    explicit prior → evidence arrives → likelihood question (both ways) →
    posterior → posterior becomes the new prior → …  → resolution → score

Every stage leaves a written trace. The prior is written *before* the evidence is read;
the likelihood judgment is written *before* the posterior is computed; the posterior is
logged with its triggering evidence. The writing is not bureaucracy — it is what prevents
the silent prior-swap that vivid evidence performs on unrecorded beliefs (§8).

## 2. Setting the prior (reference-class handoff)

Best prior: the base rate of a reference class of comparable past cases. That workflow —
choosing the class, computing its outcome distribution, anchoring on it — is owned by
`decision-science-skills:reference-class-forecasting`; run it there and import the result.
Examples of the handoff:
- "Will the vendor deliver by Q3?" → your delivery history with this vendor and vendors
  like it: 9 of 30 comparable commitments landed on time → prior ≈ 30%.
- "Is this alert a real incident?" → the alert channel's own resolved history: 2% of the
  last 1,000 fired alerts were true incidents → prior = 2%. Note which population that
  rate is over: the share of *fired alerts* that resolved true is already post-alarm, so
  it is your answer for a fired alert — do not then update it again on "the alert fired."
  §4 starts from the pre-alarm rate instead.

When no reference class exists, state a judgment prior and *label it as judgment* — it is
still better written down than implicit, because an implicit prior defaults to whichever
number the first vivid fact suggests. Avoid reflexive 50%: "even odds" is a specific,
strong claim about the world, not an absence of opinion.

Always write the prior in both forms: probability 30% = odds 3:7. Odds feed §5 directly.

**Write the whole hypothesis list, not just the prior on your favourite.** A prior of 30% on H is
also a prior of 70% on *everything else*, and "everything else" is a real set with real members. If
the alternative is a genuine complement ("the vendor delivers by Q3" vs "does not"), the two-way
form is exhaustive and safe. If instead you are weighing two named stories — "the break is a timing
difference" vs "the break is a duplicate posting" — the pair is **not** exhaustive, and the missing
member is the one that will bite. Name a catch-all (H_other) with a non-zero prior at this step,
before any evidence arrives; §8 explains why a catch-all set to zero can never recover.

## 3. The likelihood question

For each piece of evidence E, ask in both directions, in words, before any arithmetic:
- How expected is E **if the hypothesis is true**?
- How expected is E **if the hypothesis is false**?

The ratio is the likelihood ratio (LR) — the evidence's entire moving power:
- LR ≈ 1: expected either way; moves nothing. Most headline-grabbing facts live here.
- LR > 1: supports the hypothesis, in proportion.
- LR < 1: cuts against it (an LR of 0.2 is 1:5 *against*).

Two habits make this operational:
1. **Force the second question.** People evaluate evidence only against their favored
   story ("consistent with!") — consistency is cheap if the rival story predicts the same
   observation. This is the quantitative twin of the diagnosticity rule in
   `decision-science-skills:competing-hypotheses-analysis`.
2. **Price the silence.** Evidence you would expect to see under H and haven't seen
   carries an LR below 1. "No customer complaints yet" is data if complaints were expected
   by now.

## 4. Updating with counts — worked alert triage

Setting (domain-neutral): a monitoring flag — fraud rule, failing check, quality alarm —
fires. History: 2% of all monitored cases are true issues — the prior, taken *before* the
flag is known; the flag catches 90% of true issues; it also fires on 10% of clean cases.
The flag just fired. How worried should anyone be?

Build the whole-number table. Out of 10,000 cases:

| | True issue (200) | Clean (9,800) | Total |
|---|---|---|---|
| Flag fires | 180 | 980 | 1,160 |
| No flag | 20 | 8,820 | 8,840 |

Posterior = true-and-flagged / all-flagged = 180 / 1,160 ≈ **15.5%**.

Readings that matter for the decision:
- The alarm moved the belief from 2% to ~15.5% — a real update (LR = 9; see §5), *and*
  ~5 of every 6 fired flags are still false. Both statements are true at once; decisions
  need both.
- Cross-check the table before trusting it: rows must sum (180+20 = 200; 980+8,820 =
  9,800). A table that doesn't sum is a wrong posterior waiting to be quoted.
- The decision threshold is separate from the posterior: if investigating costs little and
  a missed issue costs much, 15.5% may warrant action; if investigation is expensive,
  maybe only a second, independent signal does. Write the threshold next to the question.

(The count-table format itself — natural frequencies — is taught in
`math-foundations-skills:probability-fundamentals`; this skill applies it to live
decisions.)

## 5. The odds shortcut and chaining

Same example in one line: prior odds 200:9,800 = 1:49; LR = 90%/10% = 9;
posterior odds = 9:49 → 9/(9+49) = 9/58 ≈ **15.5%**. Identical answer, checkable in a
margin note.

**Chaining.** Independent evidence multiplies: posterior odds = prior odds × LR₁ × LR₂ × …
A second, genuinely independent signal with LR 4 moves 9:49 to 36:49 ≈ 42%.

**The independence caveat carries the whole shortcut.** Three colleagues repeating the
same rumor is ONE piece of evidence, not LR³. Correlated sources — same underlying report,
same data feed, same motivated narrator — count once, at the strength of the best of them.
Before multiplying, ask: "if the first signal were wrong, would the second one probably be
wrong for the same reason?" If yes, do not multiply.

**Independence licenses the multiplication; it does not make the factors accurate.** Every LR in
a chain is a judgment, judgments carry error, and the chain multiplies the errors too. Worked, from
the §4 alert prior of 1:49:

| | Judged LRs | Chained odds | Posterior |
|---|---|---|---|
| Four independent signals, each judged **LR 3** | 3⁴ = 81 | 81:49 | 81/130 ≈ **62.3%** |
| Same four signals, each *truly* **LR 1.5** (each judgment over-read 2×) | 1.5⁴ ≈ 5.06 | 5.06:49 | 5.06/54.06 ≈ **9.4%** |

A uniform 2× over-read per signal is a **2⁴ = 16×** error in the posterior odds (81 / 5.06 = 16),
and it moves the answer from "act on this" to "keep watching." Two features make this worse than a
random-error problem:

- **The errors compound multiplicatively, not additively** — they do not shrink with more evidence,
  they grow. Chaining is the one place in this method where more work makes the answer less robust.
- **Judged LRs err in a *correlated direction*.** The analyst who reads the first signal
  generously reads the second one generously; the estimate that flatters the working hypothesis
  flatters it four times. So the errors do not cancel the way independent noise would.

Three cheap guards:
1. **Grade, don't decimalize.** "Roughly a 3" (§6 bands) is honest about the resolution of the
   judgment; "LR = 3.4" is not, and it chains into false precision.
2. **Round each LR toward 1.** Deliberate conservative rounding biases the chain *against* your own
   conclusion, which is the direction you want to be wrong in.
3. **Halve-and-double the chain.** Recompute with every LR halved, then with every LR doubled. If
   the decision is the same across that band, the chain is safe to act on; if it flips, the honest
   report is the band, not the point.

And sanity-check the aggregate, which is often easier to judge than the parts: the four-signal chain
above claims the evidence *as a whole* is 81:1 in favour. Said out loud, "the whole file is
81-to-1" is a claim people can accept or reject on the spot — sometimes catching an error the
individual ratios hid.

**Direction discipline.** An LR below 1 is an update too. A practice that only ever
multiplies by numbers above 1 is advocacy with arithmetic on top.

## 6. Bayes-factor vocabulary

Rough evidence grades, simplified from Jeffreys (*Theory of Probability*) via Kass &
Raftery (*JASA* 1995) [snippet-only]:

| LR / Bayes factor | Grade |
|---|---|
| ~1–3 | barely worth mentioning |
| ~3–20 | positive evidence |
| ~20–150 | strong |
| >~150 | very strong |

**Read the numbers as boundaries, not labels.** 3, 20 and 150 are the doors between bands, so an LR
of 20 is the entrance to *strong* and 150 the entrance to *very strong* — quoting "20, so positive"
or "150, so strong" is a one-band understatement, and the error is easy to make from memory. When
in doubt, name the band, not the number.

Use the grades as *vocabulary*, not as a computation mandate: the point is to be able to
say "this witness/result/metric is maybe a 3, not a 100" in a meeting, out loud, before
anyone treats it as decisive. Two practical corollaries:
- Most evidence people argue loudest about grades out around 2–3 — real, mentionable,
  nowhere near settling.
- A "highly reliable" single source rarely justifies an LR above ~20 once its own error
  modes are priced in; LRs of 100+ usually come from *convergent independent* lines, not
  one impressive one.

## 7. The update journal (Tetlock discipline)

The tournament-verified behaviors: superforecasters update **often and in small
increments**, use granular probabilities, and treat their beliefs as permanently
provisional — "perpetual beta," the single strongest predictor of superforecaster status
in the Good Judgment Project research (Tetlock & Gardner, *Superforecasting*)
[snippet-only].

Journal entry template (one line per update):

    date | question | prior → posterior | evidence that moved it | LR judgment (grade) |
    what would move it next (both directions) | resolution date

Rules that keep the journal honest:
- **Small and often beats big and dramatic.** A 62% → 58% move on a minor signal is the
  discipline working. If the journal shows months of silence then a 70-point reversal,
  the updating happened invisibly and the journal recorded theater.
- **Small-and-often applies to the belief, not to the estimating rule.** These are different
  objects with different correct cadences: a *belief* about an open question should move a few
  points whenever you learn something about that case; the *rule* that generates your estimates (a
  model's curve, a lag, an uplift percentage, a reference-class definition) should change rarely and
  only on diagnosed error from closed cases — re-tuning it after every miss is Deming's funnel
  Rule 2 and roughly doubles variance. `decision-science-skills:reference-class-forecasting` owns
  that guard and states the distinction in full. The one-question test: *is this new information
  about the case in front of me, or the realized error of a case already closed?*
- **Both-directions column is mandatory.** Deciding in advance what would move you *down*
  is the cheapest available guard against confirmation-only updating.
- **Score at resolution.** When the question resolves, compare the trajectory to the
  outcome (Brier-style scoring lives with the decision-journal practice in
  `decision-science-skills:reference-class-forecasting`). Unscored forecasts improve
  nothing.
- **Provenance discipline, self-applied.** The famous claim that superforecasters beat
  intelligence analysts with classified access by ~30% is *reported, not published* — it
  traces to journalistic accounts of a classified internal comparison, repeated via
  Tetlock's book [snippet-only for the claim's ubiquity; underlying data not public].
  Quote it only with that chain visible. A journal-keeper who hedges their own
  discipline's founding statistic is practicing the discipline.
- When accumulated updates cross a pre-named decision threshold, fire the revision
  review (`decision-science-skills:the-challenger`) — the journal supplies the trigger
  and the evidence trail; the review owns the re-decision.

## 8. The trap catalog

**Base-rate neglect — the cab problem, worked.** (Tversky & Kahneman's taxicab study;
canonical print treatment in the 1982 *Judgment under Uncertainty* collection
[snippet-only].) A city's cabs: 85% Green, 15% Blue. A witness, tested at 80% correct
color identification, says the cab in an accident was Blue. Out of 100 accidents like
this: 15 involve Blue cabs — the witness correctly says "Blue" for 12; 85 involve Green —
the witness wrongly says "Blue" for 17. So "witness says Blue" happens 29 times, and is
right in 12: P(Blue | says Blue) = 12/29 ≈ **41%**. Most people answer 80%+ — the base
rate vanishes under the vivid testimony. The honest caveat: the textbook number assumes
the witness's error rate is color-symmetric and context-free — assumptions the setup
smuggles in, as critics have noted. Any single worked posterior is an estimate under
stated assumptions, not gospel; the *direction* of the lesson (the prior survives the
evidence) is the robust part.

**The prosecutor's fallacy.** "The forensic match would occur by chance only 1 in 1,000,
so there's a 999/1,000 chance the defendant is the source" inverts
P(evidence | innocent) into P(innocent | evidence). In a suspect pool of 10,000, ~10
innocent people match by chance; one true source makes 11 matches, and the posterior from
the match alone is ~1/11, not 999/1,000. Likelihood-ratio framing keeps the direction
straight: state the evidence as "this match is N× more likely if the defendant is the
source than if not," then let the prior (the rest of the case) do its work. Same guard
applies outside law: "only 5% chance of seeing this metric by luck" is not "95% chance
the feature caused it."

**The catch-all hypothesis — confident answers about an incomplete world.** The most common way
real Bayesian reasoning goes wrong is not arithmetic; it is the hypothesis list. Bayes' theorem
normalizes over **the hypotheses you supplied**: the denominator is Σ P(E | Hᵢ) · P(Hᵢ) across your
list, so the posteriors always sum to 100% *of that list*, whether or not the list covers reality.
Two non-exhaustive hypotheses therefore yield a crisp, well-calibrated-looking posterior about a
world you have mis-described.

The structure of the error, plainly:
- Comparing H1 against H2 gives a valid **relative** verdict — posterior odds of H1 *versus H2* —
  and nothing more. Renormalizing that ratio and reporting "78% chance it's H1" silently asserts
  that H1 and H2 exhaust the possibilities.
- It gets *worse* with striking evidence, not better. Evidence that is unlikely under both stories
  still discriminates sharply between them, so the ratio moves hard while the real message —
  "neither of these explains what I'm seeing" — is exactly what normalization deletes.

Two guards, both cheap:
1. **Carry an explicit catch-all** — H_other, "something we haven't thought of," with a real
   non-zero prior (a plain 10% is a defensible default for a question you have not decomposed).
   Then ask the likelihood question of it too: "how expected is this evidence if the explanation is
   something not on my list?" Often the answer is "more expected than under either named story,"
   and the mass belongs there. A catch-all with prior 0 can never receive posterior mass no matter
   what arrives — a prior of zero is a commitment you cannot update out of.
2. **Watch the marginal likelihood of the evidence.** Compute P(E) = Σ P(E | Hᵢ) · P(Hᵢ) over your
   list. If that number is tiny, the observed evidence was surprising under *everything you named*
   — a direct, checkable signal that the list is incomplete. Widen the list; do not crown the
   winner of a two-horse race.

Building the full hypothesis set is a discipline of its own, and this skill hands it off:
`decision-science-skills:competing-hypotheses-analysis` owns enumeration (its rule that starting
from "favorite plus strawman" is the standard failure is this same lesson, stated qualitatively,
plus the deception hypothesis most lists omit). Use it when the question is *which* explanations
exist; use this skill once the list is stable and the evidence is arriving as a stream.

**Correlated evidence double-counting.** §5's caveat, restated as the failure: chaining
LRs from sources that share a root (one report quoted three times; two dashboards fed by
one pipeline) manufactures certainty. Count root causes of evidence, not mentions.

**LR-error compounding.** §5's chaining table, restated as the failure: five eyeballed ratios
multiplied to a two-digit posterior. Independence licenses multiplication; it does not make the
factors accurate, the errors multiply rather than average, and they run in a correlated direction.
Grade in bands, round toward 1, and report the halve-and-double band when the decision is close.

**Confirmation-only updating.** If every journal entry moves the same direction, either
the world is astonishingly cooperative or the likelihood question is being asked in one
direction only. Audit: for the last five updates, was the "how expected if false?" side
written down first?

**The dramatic-reversal pattern.** Withholding updates to preserve a public position,
then flipping — the anti-pattern the small-frequent discipline exists to prevent. The
update journal makes position-preservation visible as a flat line through moving evidence.

## 9. The honest history

Thomas Bayes died in 1761. "An Essay towards solving a Problem in the Doctrine of
Chances" was found in his papers by **Richard Price**, who substantially edited it,
replaced the introduction, added an appendix, and communicated it to the Royal Society
(read December 1763; *Philosophical Transactions* 53:370–418). **Laplace independently
rediscovered and generalized** the result ("Mémoire sur la probabilité des causes par les
événements," 1774; the mature formulation in *Théorie analytique des probabilités*,
1812). The theorem as used today is substantially Laplace's; Price's editorial role was
large enough that historians debate near-co-authorship [snippet-only, incl. Royal Society
and the Diniz *Significance* piece "Bayes and Price: when did it start?"].

Why the history sits in a methods file: "Bayes' theorem" is a textbook case of Stigler's
law (discoveries named for someone other than their discoverer), and a skill whose whole
content is *revising beliefs to fit evidence* should not open on an attribution it knows
to be folklore. The history is also a working example of the method: the folk prior
("Bayes wrote Bayes' theorem") meets documentary evidence (posthumous publication, Price's
editing, Laplace's generalization) and yields a revised posterior. Updating applies to
one's own citations first.

## 10. Provenance notes

- Bayes/Price/Laplace history — [snippet-only, incl. Royal Society; Diniz, *Significance*].
- Gigerenzer & Hoffrage, *Psychological Review* 102(4):684–704 (1995): correct Bayesian
  answers rose from ~16% to ~46% across 15 problems when recast as natural frequencies;
  Hoffrage & Gigerenzer (1998) replicated in experienced physicians. Effect is
  computational (shallower arithmetic), and a majority still failed — claim "roughly
  triples," never "solves" — [snippet-only].
- Taxicab problem (Tversky & Kahneman; canonical print treatment in the 1982 *Judgment
  under Uncertainty* collection): 12/(12+17) ≈ 41% vs modal answers ≥80% — [snippet-only];
  the color-symmetry caveat is a documented criticism of the setup.
- Tetlock & Gardner, *Superforecasting* (2015); Good Judgment Project / IARPA ACE:
  small frequent updates; perpetual beta as the strongest predictor — [snippet-only].
  The "~30% better than classified analysts" figure: reported (journalistic accounts of a
  classified comparison), not published — always hedged.
- Jeffreys evidence grades; Kass & Raftery, *JASA* 90:773–795 (1995) — [snippet-only]. The bands
  used here (1–3 / 3–20 / 20–150 / >150) are the Kass & Raftery presentation of the scale; the
  numbers are band boundaries.
- The catch-all problem is a standard point about Bayes' theorem's normalizing denominator rather
  than a single-source claim; the hypothesis-enumeration discipline is credited in-library to
  `decision-science-skills:competing-hypotheses-analysis` (Heuer lineage).
- All worked arithmetic in §4, §5, and §8 recomputed at authoring time and re-verified on revision:
  180/1,160 = 9/58 ≈ 15.5%; 12/29 ≈ 41.4%; 36/(36+49) ≈ 42.4%; the §5 compounding table —
  3⁴ = 81, 81/130 ≈ 62.3%; 1.5⁴ = 5.0625, 5.0625/54.0625 ≈ 9.4%; odds-ratio error 81/5.0625 =
  16 = 2⁴.
