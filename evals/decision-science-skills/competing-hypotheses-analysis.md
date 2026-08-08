# Evals — decision-science-skills:competing-hypotheses-analysis

## 1. Positive trigger (should load the skill)
> "Our operating account has carried an unexplained $12,480 break for three days and the standard
> reconciliation pass didn't clear it. It could be a timing difference, a duplicate statement
> line, a gap in the matching rule, a bank error, or a keying error — help me work out which
> explanation actually fits the evidence."

Expected: skill loads and runs all eight steps. It expands the user's five causes into a full
rival set (adding at least one deception hypothesis), lists the evidence including
absence-of-evidence items, builds the matrix row-by-row with C/I/N marks, drops the
non-diagnostic rows (materiality, month-end pressure), ranks by fewest inconsistencies,
sensitivity-checks the load-bearing items (naming the primary source to re-pull for each),
reports the relative likelihood of every hypothesis, and names the future observations that would
change the answer. It argues against its own preferred hypothesis before ranking, and it defers
evidence-credibility judgments and the final call to the user.

## 2. Near-miss (should NOT load this skill)
> "AP posted 14 duplicate payments this quarter, up from 2 last quarter. Run a root cause
> analysis — take me through the 5 whys on why this keeps happening."

Expected: `continuous-improvement-skills:root-cause-analysis` handles it — the cause family is
already known (duplicate payments) and the ask is to drill ONE causal chain to its root, not to
weigh rival explanations. If this skill loads, tighten the description toward
rival-explanation language.

## 2b. Near-miss (closer — should NOT load this skill)
> "Here's this month's bank statement and the GL cash activity — reconcile them, match the
> transactions, and list the outstanding items."

Expected: `cash-management-skills:bank-reconciliation` owns the mechanics of matching and
classifying. This skill mounts only when a break *resists* that pass and rival causes must be
weighed. A response that jumps straight to a hypothesis matrix for a routine reconciliation is
over-triggering.

## 3. Quality rubric
A good response:
- **Does the task:** full hypothesis set (4–8 rivals, unlikely and deception included); evidence
  list with dates, sources, and absence-of-evidence items; matrix filled row-by-row with C/I/N;
  non-diagnostic rows dropped before judging; winner chosen by fewest inconsistencies, never most
  consistencies; sensitivity check run on the load-bearing items with a named primary source for
  each; all hypotheses reported with relative likelihoods; future discriminating observations
  named and mapped to the hypothesis each would promote or kill.
- **Teaches:** explains satisficing and why support-counting cannot separate rivals, what
  diagnosticity is (the fever example or equivalent), why one solid inconsistency outweighs many
  consistencies, and why deception hypotheses must be written down to be considered at all.
- **Stays honest:** never reports the winner alone; flags any ranking that rests on unverified
  load-bearing evidence as provisional; argues the strongest case against its own preferred
  hypothesis before ranking; leaves credibility judgments and the final call with the human;
  routes a surviving deception hypothesis to escalation, not quiet closure; and never shortens
  the method's name to the three-letter initialism (which means Automated Clearing House in this
  library).
