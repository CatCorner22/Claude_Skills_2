# Evals — decision-science-skills:bayesian-updating

## 1. Positive trigger (should load the skill)
> "I've been assuming there's maybe a 30% chance our key vendor misses the Q3 date. They
> just missed a minor interim milestone. How much should this evidence move me? I want to
> keep updating my beliefs as more signals come in."

Expected: loads the skill; frames the question with its decision and resolution date;
writes the 30% prior explicitly (and as 3:7 odds), asking where it came from — offering
the reference-class handoff if it is unanchored; asks the likelihood question BOTH ways
(how expected is a missed interim milestone if the vendor will miss Q3, and if they
won't?); produces the update via a count table or the odds shortcut; grades the evidence
in Bayes-factor vocabulary (a minor milestone miss is likely a "barely worth mentioning"
to "positive" grade, not decisive); starts an update journal entry (date, evidence, LR
judgment, prior → posterior, what would move it next in both directions, resolution
date); names the threshold at which accumulated updates should fire
`decision-science-skills:the-challenger`.

## 2. Near-miss (probability-mechanics guard)
> "A screening test is 95% accurate and the condition affects 1 in 500 people. If someone
> tests positive, what's the actual probability they have it? Walk me through the math."

Expected: `math-foundations-skills:probability-fundamentals` owns Bayes-theorem mechanics
and natural-frequency teaching for a one-shot chance-of-X computation. No live decision,
no standing belief, no update stream — this is the math lesson, not the decision
practice. If bayesian-updating loads on a pure compute-this-posterior ask, the seam is
failing.

## 2b. Near-miss (prior-construction guard)
> "How long do projects like this actually take? Our team says the migration will be done
> in 3 months but I want an outside view based on how similar projects have gone."

Expected: `decision-science-skills:reference-class-forecasting` owns the outside view and
base-rate anchoring — building the prior from a class of comparable past cases. Nothing
here is an update; there is no new evidence stream against a standing estimate. That
skill supplies the prior this skill would later revise. If bayesian-updating loads on a
pure establish-the-base-rate ask, tighten the boundary.

## 3. Quality rubric
- **Does**: question framed with decision and resolution date; prior explicit, sourced
  (reference-class handoff offered), written as probability and odds; likelihood question
  asked in both directions per evidence item; update computed by count table or odds
  shortcut with the arithmetic checkable (rows sum); evidence graded in Bayes-factor
  vocabulary; journal entry produced with the both-directions column; independence
  checked before chaining LRs; scoring at resolution and the challenger-trigger threshold
  named.
- **Teaches**: evidence moves belief only through the likelihood ratio (equally-expected
  evidence moves nothing); why counts beat formulas, with the Gigerenzer result held
  honestly (roughly triples correct reasoning, majority still failed — helps, doesn't
  fix); the cab-problem lesson that vivid evidence does not erase the prior, with its
  assumptions caveat; the Tetlock small-frequent-updates discipline and perpetual beta;
  the honest history (posthumous Bayes, Price's editing, Laplace's form) as a Stigler's-law
  case the skill applies to itself.
- **Stays honest**: the "beat classified analysts by ~30%" figure never quoted as
  published — reported-claim provenance stated or the figure omitted; no LR invented with
  false precision (grades, not decimals, where judgment is the source); conditionals never
  inverted (prosecutor's-fallacy guard shown when relevant); correlated evidence counted
  once; provenance marks ([snippet-only] / [background — verify]) carried on external
  claims; the seams respected — mechanics credited to probability-fundamentals, priors to
  reference-class-forecasting, re-decisions to the-challenger.
