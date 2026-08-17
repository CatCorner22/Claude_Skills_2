---
name: bayesian-updating
description: >-
  Runs belief revision as a decision discipline: starts a question from an explicit
  prior (base-rate anchor from reference-class-forecasting), weighs
  each piece of evidence by how surprising it would be under each hypothesis, updates with
  count tables or the odds shortcut rather than formulas, grades evidence in Bayes-factor
  terms (barely-worth-mentioning to strong), and keeps a Tetlock-style update journal —
  small, frequent, logged revisions scored at resolution. Teaches the honest history (Bayes
  barely wrote it; Price shaped it; Laplace built the form we use) and the cab-problem trap
  of vivid evidence swamping the prior. Use when new evidence should move a standing
  estimate or someone asks how much a result should change their mind. Triggers: bayesian
  updating, update my beliefs, belief revision, likelihood ratio, Bayes factor, posterior
  probability, prior probability, superforecasting, superforecaster, perpetual beta, how
  much should this evidence move me.
metadata:
  version: "1.1.0"
  source: >-
    Built from the general-use expansion research dossier
    (docs/research/general-use-expansion-research.md, §4), whose anchors were verified
    before authoring. Provenance legend carried through: [snippet-only] = cross-checked
    WebSearch result blocks (direct fetches egress-blocked); [background — verify] =
    well-known claim not independently confirmed, kept hedged.
---

# Bayesian updating (belief revision as decision discipline)

The theorem this skill leans on is itself an updating lesson: Thomas Bayes never published
it, never wrote its modern form, and never named it — Richard Price found the essay in
Bayes's papers, substantially edited it, and read it to the Royal Society in 1763; Laplace
independently rediscovered and generalized the result (1774; 1812), and Laplace's form is
the one everyone uses [snippet-only]. A practice built on revising beliefs when evidence
arrives should model that honesty in its own foundations. The practice itself is simple to
state: hold an explicit prior, ask of every new fact "how surprising is this under each
story?", move the belief by that much and no more, and keep the log.

## When to use
- A standing estimate, forecast, or working hypothesis meets new evidence — a test result,
  a missed milestone, a witness statement, a vendor's slipping reply times — and the
  question is how much it should move you.
- Triaging an alert, flag, or screening result with a known false-positive history, where
  the posterior (not the alarm) should drive the decision.
- Keeping a live question honestly under review — "will the vendor deliver by Q3?" — with
  small, frequent, logged updates instead of one dramatic reversal.
- Not for: the probability *mechanics* — conditional probability, Bayes' theorem itself,
  and natural-frequency teaching belong to `math-foundations-skills:probability-fundamentals`.
  The seam, named plainly: that skill teaches the math of a single computation; this skill
  is the decision practice layered above it — priors owned in advance, evidence graded as
  it arrives, updates logged and scored over the life of a real question.
- Not for: establishing the prior from comparable past cases — the outside view and
  base-rate anchoring belong to `decision-science-skills:reference-class-forecasting`. It
  supplies the prior; this skill revises it as evidence lands.
- Not for: weighing rival explanations of one accumulated evidence pool in a matrix →
  `decision-science-skills:competing-hypotheses-analysis` (the qualitative sibling — use it
  when hypotheses are many and evidence arrives as a body, this skill when evidence arrives
  as a stream against a live estimate).
- Not for: attaching probabilities to built scenarios →
  `decision-science-skills:minority-report`; deciding whether accumulated updates now
  obligate a plan revision → `decision-science-skills:the-challenger` (this skill feeds it
  the trigger).

## Do it
Worked tables, the odds shortcut, the journal template, and the trap catalog are in
`references/updating-method.md`.

1. **Name the question, the decision it serves, and the resolution date.** "Will X happen
   by Y, and what will we do differently at 30% vs 70%?" A belief that serves no decision
   needs no updating discipline.
2. **Set the prior explicitly, and say where it came from.** Best source: a reference class
   of comparable past cases (`decision-science-skills:reference-class-forecasting` owns that
   workflow). No class available? State a judgment prior and label it as judgment. Write the
   prior as both a probability and odds (30% = 3:7) — odds make the updating arithmetic
   trivial.
3. **For each new piece of evidence, ask the likelihood question both ways.** "How expected
   is this evidence if the hypothesis is true? How expected if it is false?" The ratio of
   those two answers — the likelihood ratio — is the evidence's entire moving power.
   Evidence equally expected under both stories (LR ≈ 1) moves nothing, however vivid,
   alarming, or expensive it was to obtain.
4. **Update with counts, or with the odds shortcut.** Counts: build the whole-number table
   (out of 10,000 cases: how many true, how many flagged either way) and read the posterior
   off the flagged row. Odds: posterior odds = prior odds × LR. Both give the same number;
   use whichever the audience can check. The posterior becomes the new prior — updating is
   a loop, not an event.
5. **Grade the strength in Bayes-factor vocabulary.** As rough intuition grades (Jeffreys;
   Kass & Raftery): LR around 3 — barely worth mentioning; around 20 — positive, real
   evidence; around 150 — strong [snippet-only]. Use the grades as *vocabulary* for "how
   much should this move me," not as a computation requirement. Most evidence people argue
   loudest about grades out around 2–3.
6. **Update small and often, and log every move.** The verified superforecaster discipline:
   frequent, incremental revisions, and "perpetual beta" — the commitment to keep updating —
   was the single strongest predictor of superforecaster status (Tetlock & Gardner;
   Good Judgment Project) [snippet-only]. Each journal entry: date, the evidence, the LR
   judgment, prior → posterior, and what would change your mind next.
7. **Run the trap checks before trusting a big move.** (a) Vivid evidence does not erase
   the prior — the cab problem's lesson (a "80% reliable" witness against a 15% base rate
   yields ~41%, not 80%). (b) Never invert a conditional: P(evidence|hypothesis) is not
   P(hypothesis|evidence) — the prosecutor's fallacy. (c) Multiply likelihood ratios only
   for genuinely independent evidence; correlated reports of the same underlying fact count
   once. (d) Ask what evidence you would *expect* to see and haven't — silence can carry an
   LR too.
8. **Score at resolution, and hand off big revisions.** When the question resolves, score
   the forecast against the log. And when accumulated updates push the belief past a
   decision threshold, that is a trigger for
   `decision-science-skills:the-challenger` — the update tells you the plan needs a
   revision review; it does not by itself re-plan.

## Why / learn
The core mental shift is from "what does this evidence say?" to "**how surprising is this
evidence under each hypothesis?**" Evidence has no voice of its own; it only discriminates
between stories, and only to the extent the stories predicted it differently. That framing
dissolves most bad arguments about data: the loud fact that both sides would have predicted
is worth nothing, and the quiet fact only one story predicted is worth a lot.

The arithmetic is deliberately demoted to counts because that is where the empirical
evidence points: Gigerenzer & Hoffrage showed correct Bayesian answers roughly *tripled* —
from about 16% to about 46% — when problems were recast from probabilities to natural
frequencies ("out of 10,000 people…"), a gain replicated with experienced physicians
[snippet-only]. Hold the honest limit: a majority still failed. Natural frequencies help;
they do not fix. (The teaching of that format itself belongs to
`math-foundations-skills:probability-fundamentals`; this skill just refuses to let a
formula stand where a count table would be checkable.)

The discipline half comes from the forecasting-tournament record: what separated
superforecasters was not raw intelligence or secret data but *behavior* — many small
updates, granular probabilities, and perpetual beta [snippet-only]. And here the skill
practices its own preaching about evidence provenance: the famous claim that
superforecasters "beat intelligence analysts with classified access by ~30%" is
*reported, not published* — it traces to journalistic accounts of a classified internal
comparison. Teach it, if at all, with that provenance chain visible; a skill about
weighing evidence must weigh its own.

The cab problem (Tversky & Kahneman's taxicab study: 85% Green cabs, 15% Blue, witness 80%
reliable, says "Blue" → the answer is ≈41%, yet most people say 80%+) shows *why* the
prior needs writing down: unrecorded priors get silently replaced by whatever evidence is
most vivid [snippet-only]. One honest caveat travels with it: the textbook number rests on
modeling assumptions (a color-symmetric, context-free witness error rate), and critics
have noted the setup smuggles those in — treat any single worked posterior as an estimate
under stated assumptions, not gospel.

## Common mistakes
- Setting the prior at 50% "to be neutral" → 50% is a strong claim, not neutrality; anchor
  on a reference class or label the number as judgment.
- Letting vivid evidence replace the prior → the cab trap; write the prior down before
  reading the evidence.
- Inverting the conditional ("the test is 90% accurate, so you're 90% guilty/sick/right")
  → prosecutor's fallacy; run the count table in the direction you need.
- Treating LR ≈ 3 evidence as decisive → barely worth mentioning on the standard grades;
  say the grade out loud.
- Multiplying likelihood ratios from correlated sources → three echoes of one report is
  one report; check independence before chaining.
- Saving updates for a dramatic reversal → the tournament-verified discipline is small and
  frequent; big silent jumps mean the journal was fiction.
- Updating only on confirming evidence → decide in advance what would move you *down*;
  an update log with one direction is advocacy.
- Quoting the "beat classified analysts by 30%" figure as established → reported, not
  published; cite it with its provenance or not at all.
- Logging updates but never scoring at resolution → unscored forecasts teach nothing;
  set the resolution date at question-framing time.

## Tailor to your environment
Record in `references/your-environment.md`: the standing questions you keep live forecasts
on, where your reference classes and their base rates live (link them from
`decision-science-skills:reference-class-forecasting` work), the false-positive histories
of the alerts and flags you triage, your journal location and review cadence, and the
decision thresholds that should trigger a revision review. Keep the committed file
structural — real case names, client matters, or account-level numbers belong in
`your-environment.private.md` (git-ignored), never in a committed file.

## References
- references/updating-method.md — the update loop end-to-end: prior-setting with the
  reference-class handoff, the likelihood question, a worked alert-triage count table, the
  odds shortcut with chaining rules, Bayes-factor vocabulary, the update-journal template
  with scoring, the trap catalog (cab problem worked, prosecutor's fallacy, correlated
  evidence), and the honest history
- references/your-environment.md — your live questions, base-rate sources, alert
  histories, journal, and thresholds (fill in)
