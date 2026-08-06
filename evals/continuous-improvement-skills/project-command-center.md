# Evals — continuous-improvement-skills:project-command-center

## 1. Positive trigger (should load the skill)
> "Our team ran a pilot of the new reconciliation engine and it 'passed' — but halfway
> through they reloaded the golden dataset because the first run corrupted it, and they
> loosened the match threshold to hit the target rate. Review whether this validates the
> engine, and red team our go-live plan."

Expected: skill loads; identifies the reload and threshold change as interventions that
must be logged (what, why, who authorized, what evidence they invalidated); separates
continuation from validation — post-reload results no longer validate the end-to-end
hypothesis; checks whether acceptance criteria predated results; runs the Chicken Little
pass on the go-live plan (rollback rehearsal, silent failure modes, ownership); ends with
the intervention log, the decision/blocker, and Now / Next / Later / Watch.

## 2. Near-miss (should NOT load this skill)
> "Build our new scheduling feature end to end with lean six sigma rigor — charter,
> co-design, accessible UI, adversarial testing."

Expected: `continuous-improvement-skills:lean-six-sigma-for-software` owns the full
software-build discipline. project-command-center is the command/validity doctrine, not
the build methodology; loading here means the two skills' boundary is failing.

## 2b. Near-miss (statistics-only guard)
> "What's the difference between sensitivity and specificity?"

Expected: a definitional statistics question —
`data-analytics-bi-skills:statistical-inference` or a direct answer, not a
project-command doctrine. This skill engages when a risk/diagnostic CLAIM needs auditing
in a project context, not for concept explanations.

## 3. Quality rubric
- **Does**: fixes criteria-before-results; produces an intervention log; scales controls
  to stakes; reports absolute AND relative risk with the full 2×2 when metrics appear;
  ends consequential reviews with Now / Next / Later / Watch.
- **Teaches**: the Millennium Challenge lesson (an exercise that can't fail proves
  nothing); continuation ≠ validation; orientation as OODA's decisive element;
  instrumentation ≠ understanding.
- **Stays honest**: attributes every claim to evidence actually examined; says where it
  did not verify; Chicken Little findings carry severity/evidence/owner — never
  speculation-as-certainty, never blocking on trivia.
