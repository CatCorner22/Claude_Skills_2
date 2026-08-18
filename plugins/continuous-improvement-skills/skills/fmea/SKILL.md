---
name: fmea
description: >-
  Runs a Failure Mode and Effects Analysis — structuring a process or design into steps, chaining
  each failure mode to its effects and causes, rating Severity, Occurrence, and Detection on
  anchored 1–10 scales, and prioritizing action by the Action Priority table rather than raw RPN
  multiplication — then keeps the register living by re-rating after actions and incidents. Use
  when anticipating and ranking what could go wrong before it fails: ordering reconciliation break
  types for investigation, design-reviewing an auto-match rule set before go-live, or choosing what
  to test hardest. Triggers: FMEA, failure modes, failure mode and effects analysis, severity
  occurrence detection, action priority, RPN, risk priority number, rank what could go wrong.
---

# FMEA (failure mode and effects analysis)

## When to use
- Anticipating what could go wrong in a process, rule set, or design *before* it fails, and ranking
  the failures so scarce attention goes to the worst first. The method comes from US military
  standard MIL-P-1629, was hardened on NASA's Apollo program as FMECA, and spread through Ford into
  the automotive AIAG/VDA handbook lineage `[snippet-only]`.
- Ordering a reconciliation break investigation: break types — duplicate statement line, truncated
  addenda, tolerance mismatch — are failure modes; rate them S/O/D and work the register in priority
  order.
- Design-FMEA on an auto-reconciliation rule set before go-live, where Detection asks: "will this
  failure surface in the unreconciled report, or silently auto-match the wrong pair?"
- The Improve phase of `continuous-improvement-skills:dmaic-problem-solving` names FMEA as its
  new-risk check — this skill is that method, defined.
- Prioritizing what an adversarial release gauntlet fuzzes and property-tests hardest, by Action
  Priority (see `continuous-improvement-skills:lean-six-sigma-for-software`).
- Not for: finding the cause of one incident that already happened → see
  `continuous-improvement-skills:root-cause-analysis` (FMEA anticipates; RCA autopsies). Mapping a
  hazard's full prevention/mitigation barrier architecture with escalation factors and barrier
  owners → see `safety-and-reliability-skills:bowtie-barrier-analysis`.

## Do it
Work the seven steps in order — `references/fmea-method.md` has each step expanded, the anchored
rating scales, and a worked bank-reconciliation FMEA table.
1. **Scope and structure.** Fix boundaries, then decompose: system → subsystem → step (for a
   process: process → stage → task). One FMEA per coherent slice; a whole department is a swamp.
2. **Analyze functions.** For each element, state what it must do, measurably ("auto-match posts
   each statement line to exactly one book transaction"). A failure is a function not performed.
3. **Analyze failures.** For every function list its failure **modes** (the ways it fails), chain
   each mode **upstream to its effect** (what the customer/system experiences) and **downstream to
   its cause** (the mechanism that produces it). Pre-draft the *entire* inventory from the process
   description — the multi-day worksheet grind is what killed FMEA in offices, and drafting is
   where an LLM collapses that cost so the team's hour goes to correcting, not composing.
4. **Rate Severity, Occurrence, Detection** on the anchored 1–10 scales in the reference (S = how
   bad the effect; O = how often the cause; D = how likely current controls catch it — 10 is
   *worst*, i.e. no control). **Human gate:** drafted ratings are proposals, never final — a
   documented LLM weakness is rating inconsistency, so every S/O/D score is adjudicated by the
   process owner before it enters the register, and hallucinated failure modes are pruned here.
5. **Prioritize with the Action Priority table** (High/Medium/Low), not by multiplying S×O×D into
   an RPN. AP reads the three ratings in order of dominance — Severity first — so a catastrophic
   failure can never be averaged away by arithmetic.
6. **Act, then re-rate.** Actions cut **Occurrence** (prevention: remove or error-proof the cause)
   or improve **Detection** (a control that surfaces the failure sooner); Severity rarely moves
   without redesigning the process itself. Re-rate the row after the action lands and keep both
   ratings, so the register shows risk actually retired — not just actions listed.
7. **Keep it living.** Re-run after every incident and process change. An incident is feedback: a
   mode you missed, an Occurrence rated too low, or a Detection rated too optimistically.

## Why / learn
The heart of the method is the **mode → effect → cause chain**: a mode is not a cause (duplicate
statement line is the mode; the bank re-transmitting the file is the cause; overstated cash is the
effect), and separating them is what lets you attack prevention and detection independently. The
**Action Priority story is the transferable lesson**: for decades practitioners ranked by
RPN = S×O×D, and the multiplication had a quirk — a Severity-9 failure with low O and D scores
could rank *below* a trivial annoyance, so teams polished cosmetics while catastrophic-but-rare
failures sat unaddressed. The harmonized AIAG-VDA handbook replaced RPN with an Action Priority
lookup in which Severity dominates `[snippet-only]`. The general rule: whenever you compress a
multi-dimensional risk into one score, check whether arithmetic can silence the dimension you can
least afford to ignore. The second lesson is economic: FMEA's value was never the worksheet, it was
the disciplined anticipation — and the worksheet's cost is what made offices skip it. An LLM
inverts that economics by drafting the full rated inventory from a process description in minutes.
But copying the artifact while dropping the mechanism nulls the result: the mechanism here is human
adjudication of every rating and an owner who acts on the register. Keep the gate; skip the grind.

## Common mistakes
- Ranking by RPN and working the biggest products → Severity-9 rows languish. Use the AP table.
- Accepting drafted ratings unreviewed → inconsistent scores pollute the register. Owner adjudicates each.
- Writing causes in the mode column ("clerk error") → you lose the prevention/detection split. Mode = how the function fails.
- One-and-done FMEA → the register is stale by the first incident. Re-run on incidents and changes.
- Every action is "add a review" → detection-only patches pile up. Prefer cutting Occurrence at the cause.
- Scoping "all of AP" → a 200-row swamp nobody maintains. Structure first; FMEA one slice at a time.
- Rating without anchors → scores drift between raters and sessions. Use the anchored scales, calibrated once.

## Tailor to your environment
Record your real setup in `references/your-environment.md` (use `your-environment.private.md`,
git-ignored, if it names real accounts, systems, or counterparties). Capture the processes you
FMEA, your failure-mode taxonomy (e.g. your reconciliation break types), your anchored S/O/D
scales calibrated to your volumes and materiality, where the register lives, the re-run cadence,
and who owns rating adjudication and actions. Never commit real transaction or client data —
sanitize to structure only.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/fmea.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/fmea-method.md — the seven steps expanded, anchored S/O/D scales for office
  processes, the Action-Priority-vs-RPN story, and a worked bank-reconciliation FMEA table
- references/your-environment.md — your registers, scales, taxonomy, and owners (add when supplied)
