# The hypothesis-matrix method (Heuer's eight steps, in full)

Source method: Richards J. Heuer Jr., *Psychology of Intelligence Analysis*, chapter 8 — a free
CIA publication. Framing as a countermeasure to confirmation bias and satisficing [snippet-only].
Naming rule: never shorten the method's name to its three-letter initialism — in this library that
letter sequence means Automated Clearing House.

## Contents
- [The eight steps](#the-eight-steps)
- [Diagnosticity, explained](#diagnosticity-explained)
- [Worked example: a reconciliation-break matrix](#worked-example-a-reconciliation-break-matrix)
- [Deception hypotheses](#deception-hypotheses)
- [The sensitivity protocol](#the-sensitivity-protocol)
- [Reporting format](#reporting-format)

## The eight steps

1. **Identify the full set of hypotheses.** Brainstorm wide before judging — include hypotheses
   you consider unlikely, and at least one deception hypothesis when any actor could benefit from
   the evidence looking the way it does. A hypothesis left off the matrix can never win, however
   true it is. Group-generate if possible (or have the assistant generate; different minds anchor
   on different favorites). Target 4–8 mutually distinct rivals; merge duplicates, keep genuinely
   different causal stories separate.
2. **List the significant evidence and arguments.** "Evidence" is broad: observed facts, absence
   of expected facts, assumptions being treated as facts, and arguments (e.g., "the vendor had no
   access"). Date each item and note its source. Absence matters: if a hypothesis predicts
   something you should see and you do not see it, that is evidence — write it down.
3. **Build the matrix.** Hypotheses across the top, evidence down the side. For each cell ask:
   *if this hypothesis were true, would I expect to see this evidence?* Mark **C** (consistent),
   **I** (inconsistent), or **N** (neutral / not applicable). Work row by row — take one evidence
   item and score it against every hypothesis before moving on. Row-wise filling is the mechanical
   trick that forces evidence to confront the whole rival set instead of decorating a favorite.
4. **Refine the matrix: drop non-diagnostic evidence.** Any row that reads C (or N) across the
   board discriminates between nothing and should be removed from the judgment (keep it listed —
   it may become diagnostic if the hypothesis set changes). Also reword hypotheses that the
   evidence suggests splitting or merging. What survives is the *diagnostic core* — typically a
   small fraction of the original file.
5. **Draw tentative conclusions by disconfirmation.** Rank hypotheses by **fewest I marks**. Do
   not rank by most C marks: consistency accumulates for every halfway-plausible story, but a
   solid inconsistency eliminates. Proceeding this way inverts the analyst's instinct, which is
   exactly the point.
6. **Sensitivity analysis.** The ranking usually hangs on a handful of I marks. Identify those
   load-bearing items and interrogate each one (see [the sensitivity protocol](#the-sensitivity-protocol)).
   If a load-bearing item could plausibly be wrong or shaped, verify it against the most primary
   source available *before* publishing the conclusion.
7. **Report conclusions about ALL hypotheses.** Give the relative likelihood of every rival, not
   just the winner — the reader's decision depends on how close the runner-up is and on what was
   rejected. State which evidence drove each elimination.
8. **Identify milestones for future observation.** Name the concrete observations that would
   change the answer, and which hypothesis each would promote or kill. This converts the analysis
   from a one-time verdict into a monitored position.

## Diagnosticity, explained

An evidence item's value is its power to *discriminate* among the rivals — not its vividness,
volume, or cost of collection. The classic illustration: a high fever is genuinely informative
about whether a patient is ill, yet nearly worthless for deciding *which* illness, because it is
consistent with dozens. In a reconciliation break, "the amount is material" and "it appeared near
month-end" feel weighty but are consistent with every rival cause — non-diagnostic. Diagnosticity
is relative to the hypothesis set: add a new rival and a dead row can come alive. That is why the
matrix is refined (step 4) rather than filled once.

## Worked example: a reconciliation-break matrix

Setting: an operating account shows an unexplained **$12,480.00 credit-side break** — the
statement carries a lockbox credit the ledger cannot pair. The standard reconciliation pass
did not clear it.

**Hypotheses**
- **H1 Timing** — the ledger receipt exists but posts in the next period.
- **H2 Duplicate statement line** — the statement feed loaded the same credit twice.
- **H3 Matching-rule gap** — both sides exist and are open, but the auto-match rule cannot pair
  them (reference or date mismatch).
- **H4 Bank error** — the credit belongs to another account.
- **H5 Keying error** — the ledger entry was keyed with transposed digits, so no exact match exists.
- **H6 Deception** — the credit is genuine but engineered to mask an unauthorized movement elsewhere.

**Evidence** (dated, sourced)
- E1: The break equals one open statement credit exactly (a $12,480.00 lockbox line).
- E2: The loaded feed contains **two** lines with identical amount, date, and bank reference number.
- E3: The bank's own portal shows only **one** such credit that day.
- E4: The auto-match log shows the first line matched a ledger receipt; the second found **no
  candidate within tolerance** (no near-miss).
- E5: No unposted or next-day ledger receipt of $12,480.00 exists.
- E6: Month-end close is three days away; volumes are high.
- E7: Access logs show no unusual user activity and no new payee in the period.

**Matrix** (C consistent / I inconsistent / N neutral)

| Evidence | H1 timing | H2 duplicate | H3 rule gap | H4 bank error | H5 keying | H6 deception |
|---|---|---|---|---|---|---|
| E1 exact open line | C | C | C | C | C | C |
| E2 two identical feed lines | I | C | I | N | I | N |
| E3 portal shows one credit | N | C | N | I | N | N |
| E4 no near-miss candidate | N | C | I | N | I | N |
| E5 no next-period receipt | I | N | N | N | N | N |
| E6 month-end pressure | C | C | C | C | C | C |
| E7 access logs clean | N | N | N | N | N | I (weak) |

**Refine (step 4):** E1 and E6 are consistent with everything — non-diagnostic, dropped. Note how
the "impressive" facts (materiality, month-end) contributed nothing.

**Judge by disconfirmation (step 5):** I-counts — H1: 2, H2: 0, H3: 2, H4: 1, H5: 2, H6: 1 (weak).
Tentative winner **H2 (feed duplicate)** with zero inconsistencies. H4 and H6 trail; H1/H3/H5 (the
ledger-side stories) each carry two solid inconsistencies.

**Sensitivity (step 6):** the ranking hangs on **E2** and **E3**. If the two feed lines actually
differ in reference (E2 misread — check the raw statement file, not the report over it), the case
collapses. If the portal view was date-filtered (E3), H4 revives. H6 is only *weakly* disconfirmed
— absence-of-evidence — so name its test: examine the raw feed file at record level. The same
record duplicated is a load artifact (confirms H2); a second line with distinct origination detail
is not, and escalates.

**Report (steps 7–8):** all six likelihoods with the driving evidence, then the milestones —
tomorrow's feed line count for the same reference, and whether reloading the corrected feed clears
the break. If the duplicate reproduces, the diagnosis moves from this matrix into production
troubleshooting of the statement-feed import.

## Deception hypotheses

Heuer's warning: analysts discount deception because they have rarely seen it, and deception is
designed to look like the innocent explanation — at face value the evidence will always be
"consistent" with something routine. Consequences for the matrix:

- A deception hypothesis is rarely disconfirmed by ordinary consistency checks; expect mostly N
  marks. Its I marks come from *absence* evidence (clean access logs, intact approvals) and from
  verifying load-bearing items at a source the potential deceiver could not shape.
- Include one whenever an actor has **means, motive, and opportunity** to shape what you are
  seeing — in payments work, business-email compromise and mandate fraud are engineered precisely
  so the evidence reads as routine (`safety-and-reliability-skills:bowtie-barrier-analysis` maps
  the barriers such schemes are built to defeat).
- Weak disconfirmation is not clearance. If a deception hypothesis survives to the final ranking,
  say so plainly and route it to escalation/verification, never to quiet closure.

## The sensitivity protocol

For each load-bearing item (any item whose I marks move the ranking):
1. **Source reliability** — who produced it, from what system, how far from the primary record?
2. **Innocent error** — could it be wrong by accident (filtered view, stale export, misread
   reference, timezone/date cutoff)?
3. **Shaped evidence** — could anyone benefit from it being misleading, and did they have access?
4. **Verify** — re-pull the item from the most primary source available (raw file over report,
   bank portal over feed, original document over summary). Record what was checked.
5. **Replay** — flip the item (assume it wrong) and re-rank the matrix. If the winner changes, the
   conclusion is provisional until the item is verified; say so in the report.

## Reporting format

- One line per hypothesis: relative likelihood (e.g., likely / plausible / unlikely / eliminated),
  the evidence that drove it there, and what would change it.
- The diagnostic core: the 2–4 items the conclusion actually rests on, each with its verification
  status from the sensitivity protocol.
- Milestones: future observations, each mapped to the hypothesis it would promote or kill.
- Never present the winner alone, and never present a ranking whose load-bearing evidence went
  unverified without flagging it.
