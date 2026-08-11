---
name: competing-hypotheses-analysis
description: >-
  Weighs rival explanations against the same body of evidence using Heuer's structured
  competing-hypotheses method from intelligence analysis: brainstorm the full hypothesis set
  including unlikely and deception hypotheses, list the significant evidence, build the
  hypothesis matrix (hypotheses across the top, evidence down the side), drop non-diagnostic
  evidence, judge by disconfirmation — the winner is the hypothesis with the least evidence
  against it — sensitivity-check the load-bearing items, report the relative likelihood of
  every hypothesis, and name the future observations that would change the answer. Use when
  several plausible causes compete: a reconciliation break that resists the standard pass, an
  incident with multiple suspects, any analysis at risk of confirmation bias. Triggers:
  competing hypotheses, hypothesis matrix, which explanation fits the evidence, diagnostic
  evidence, rule out causes, weigh rival explanations, why is this break really happening.
---

# Competing-hypotheses analysis (the hypothesis matrix)

Richards Heuer's structured method, developed for CIA analysts in the 1970s–80s and published in
*Psychology of Intelligence Analysis*, chapter 8 (a free CIA publication). When several explanations
could account for the same evidence, weigh them **against each other** in one matrix and judge by
disconfirmation — the answer is the hypothesis that best survives attack, not the first one that
felt right.

**Naming rule for this library:** never shorten this method to its usual three-letter initialism.
In this library that letter sequence means Automated Clearing House (the banking and NACHA skills
own it). Write "competing hypotheses" or "the hypothesis matrix" — in prose, headings, and output.

## When to use
- An unexplained result with a natural set of rival causes. Canonical examples: a
  reconciliation break that resists the standard pass — timing difference vs. duplicate statement
  line vs. matching-rule gap vs. bank error vs. keying error — or a works-in-test-fails-in-prod
  production mystery.
- Any analysis at risk of confirmation bias: an incident with multiple suspects, rival readings of
  a prompt during a `coding-agent-skills:master-prompt-architect` audit, or generalizing the
  disconfirmation pass of `deep-research-skills:medical-research-detective` beyond medicine.
- Deciding what evidence to gather next — the matrix shows which observation would actually
  discriminate between the surviving rivals.
- Not for: drilling a single causal chain from symptom to root →
  `continuous-improvement-skills:root-cause-analysis`. Five-Whys assumes ONE chain and asks "how
  deep"; this method weighs RIVAL chains and asks "which one". Use that skill once the matrix has
  picked the chain worth drilling. Medical literature questions →
  `deep-research-skills:medical-research-detective`.

## Do it
Work all eight steps; the full procedure with a worked reconciliation-break matrix is in
`references/hypothesis-matrix-method.md`.

1. **Brainstorm the FULL hypothesis set.** Include the unlikely ones and at least one deception
   hypothesis (an actor benefits from the evidence looking this way). Aim for 4–8. Generating the
   set is where the assistant adds the most — it proposes the rivals the analyst anchors past.
2. **List the significant evidence and arguments.** Include the absence of expected evidence (the
   dog that didn't bark) and the assumptions you are treating as facts.
3. **Build the matrix.** Hypotheses across the top, evidence down the side. Mark each cell
   consistent (C), inconsistent (I), or neutral/not-applicable (N). Fill **one evidence row at a
   time** — ask "how does this item sit with EACH hypothesis?", never "what supports my favorite?".
4. **Refine: drop non-diagnostic evidence.** An item consistent with every hypothesis
   distinguishes nothing — it is worthless for this decision however impressive it looks. What
   remains is the diagnostic core; note how small it usually is.
5. **Judge by disconfirmation.** The tentative winner is the hypothesis with the LEAST evidence
   against it — count the I marks, not the C marks. Consistency is cheap; inconsistency eliminates.
6. **Sensitivity check.** Identify the few load-bearing items whose I marks drive the ranking. For
   each, ask: what if it is wrong, misdated, or deliberately misleading? Verify those specific
   items against the most primary source available before trusting the ranking.
7. **Report the relative likelihood of ALL hypotheses** — never just the winner. The decision
   changes if the runner-up is close, and the reader deserves to see what was rejected and why.
8. **Name future observations that would change the answer** — what to watch for, and which
   hypothesis each observation would promote or kill.

**Division of labor (the human gate).** The matrix died in manual practice of cell-filling tedium;
the assistant fills evidence-by-hypothesis cells instantly, generates the hypothesis set, and
replays sensitivity checks for free. The human supplies the **evidence credibility judgments**
(which sources to trust, which items could be shaped) and **owns the call**. Anti-sycophancy
discipline: before ranking, the assistant must argue AGAINST its own preferred hypothesis — state
the strongest case for the runner-up in full, then let the matrix decide.

## Why / learn
The failure this method counters is **satisficing**: pick the first plausible explanation, search
for support, stop. With any real evidence pool something supports almost every story, so counting
support cannot separate rivals — Heuer's central observation, and the reason the method judges by
disconfirmation instead. It is the structured countermeasure to confirmation bias [snippet-only].

**Diagnosticity is the pivot.** Evidence earns its keep by discriminating between hypotheses. A
fever "consistent with" a dozen diseases diagnoses none of them; a break amount consistent with
timing, duplicate, and keying error tells you nothing about which. Step 4 usually reveals that most
of the file is non-diagnostic and the whole case turns on two or three items — which is exactly why
step 6 stress-tests those items, and why a single solid inconsistency outweighs ten consistencies:
consistency can never confirm, but inconsistency can eliminate.

**Why a matrix at all?** Working memory holds one favored story; the matrix externalizes the whole
rival set so evidence gets applied to every hypothesis, not just the one in mind. That is also why
deception belongs in the set: a deception hypothesis is never supported by evidence at face value —
it predicts the evidence will look consistent with something innocent — so unless it is written
down as a column it is silently impossible. And it is why this method revives under an LLM: the
discipline was always sound, the tedium killed it, and the tedium is now free.

## Common mistakes
- Starting with two hypotheses (favorite plus strawman) → brainstorm the full set, unlikely and
  deception rivals included; the true cause is often the fifth column.
- Filling the matrix column-by-column (advocating for one hypothesis) → fill row-by-row,
  evidence-first.
- Counting C marks to pick a winner → judge by fewest I marks; support is cheap.
- Ranking on non-diagnostic evidence → drop it first; it inflates confidence in everything equally.
- Reporting only the winner → report all relative likelihoods; a close runner-up changes the action.
- Skipping the sensitivity check → rankings routinely hang on one misdated or misread item.
- Treating the matrix as the answer → it structures judgment; the human owns credibility calls and
  the final decision.
- Shortening the method's name to the three-letter initialism → in this library that means
  Automated Clearing House; say "the hypothesis matrix".

## Tailor to your environment
Record your recurring rival sets and evidence sources in `references/your-environment.md`: the
standing hypothesis set for each problem you diagnose repeatedly (e.g., break causes per bank
account or statement feed), where the evidence lives (statement exports, match logs, subledger
reports, access logs), your source-credibility conventions, and your escalation rule for deception
hypotheses. Keep it structural — real account numbers, amounts, or names belong in
`your-environment.private.md` (git-ignored), never in a committed file.

## References
- references/hypothesis-matrix-method.md — the eight steps in full, diagnosticity explained with a
  worked reconciliation-break matrix, deception hypotheses, and the sensitivity protocol
- references/your-environment.md — your recurring rival sets, evidence sources, and credibility conventions
