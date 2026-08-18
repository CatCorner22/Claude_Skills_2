# The sortition-review method: two controls, lot mechanics, rotation, handover, first-pass

Method lineage: Athenian euthynai — every magistrate, including the strategoi
(generals), underwent an end-of-term accounting: a financial logos before ten allotted
logistai, then a general conduct review before ten allotted euthynoi, within a month of
leaving office (Oxford Classical Dictionary; Aristotle, *Ath. Pol.*) [snippet-only] —
and the Venetian doge-election protocol of 1268: ten alternating rounds of lot and vote
(30→9→40→12→25→9→45→11→41), blind draws performed by the ballotino, family quotas, no
campaigning, used essentially unchanged until 1797 [snippet-only]. Both are selection
design, domain-neutral by construction.

## Contents
- [The two controls, kept distinct](#the-two-controls-kept-distinct)
- [Verifiable-lot mechanics](#verifiable-lot-mechanics)
- [Universality-floor design and the exemption vulnerability](#universality-floor-design-and-the-exemption-vulnerability)
- [Reviewer-rotation patterns](#reviewer-rotation-patterns)
- [The handover-review default](#the-handover-review-default)
- [The assistant-first-pass protocol](#the-assistant-first-pass-protocol)
- [Worked example: expense approvals in a small office](#worked-example-expense-approvals-in-a-small-office)
- [Sources](#sources)

## The two controls, kept distinct

They are usually conflated; they solve different failures and can be adopted
separately.

**Control (a): universal and scheduled by default.** Everything in the population is
eligible and the examination happens on a schedule, never on suspicion. What it
defeats: *trigger-gaming and stigma*. If selection follows a rule ("large items,"
"new vendors," "people the boss wonders about"), the rule is learnable and effort
migrates to its blind side; and if selection implies suspicion, every selection is a
political act, so selection becomes rare and mostly downward. Athens reviewed its most
powerful officials routinely precisely because routine implied nothing [snippet-only].

**Control (b): randomness at multiple interleaved stages.** Which items come up, and
who examines them, is drawn by lot — and where stakes are high, the lot is applied at
more than one stage. What it defeats: *capture*. A known gatekeeper is a single point
of purchase; a multi-stage lot makes steering the outcome require corrupting the whole
pool. Venice's ten alternating rounds are the exhibit: each stage multiplies the
number of people a fixer must own [snippet-only].

Design consequence: (a) sets *what is drawable* (everything); (b) sets *how the draw
happens* (unriggably). A program with (a) but not (b) has a fair scope and a riggable
selector; (b) without (a) is an unriggable draw over a gamed population.

## Verifiable-lot mechanics

The requirement: nobody — including the operator — can steer the draw, and everyone
can verify afterward that nobody could have. Mechanics, simplest first:

1. **Dice in the open.** Number the items; roll physical dice at a standing meeting
   with at least two people present; the roll indexes into the list. Verifiable by
   presence. Fits monthly draws over small populations.
2. **Pre-committed seed.** Before the period closes, the operator commits to a seed —
   writes it in a dated note, emails it, or (stronger) shares only its hash, revealing
   the seed at draw time. The seed feeds a *pinned* deterministic formula, so anyone can
   re-run it and get the same draw. The commitment must predate the population being
   final, or the operator could pick the seed after seeing the items.

   **Pin the formula, not just the seed.** "Seed the standard random generator and take
   N" is not reproducible: the same seed in the same language gives different draws under
   `shuffle`-then-slice versus `sample`, and different languages share no generator at
   all. A verifier who reaches a different answer cannot tell an honest tool difference
   from a rigged draw, which destroys exactly the property the lot was for.

   **The hash-rank draw** (reproducible in any tool with SHA-256, including a shell):

   > For each item, `rank = SHA256("<seed>|<item id>")`. Sort items ascending by `rank`.
   > The first N are the draw.

   Publish the three inputs — the seed, the item-id list, and that sentence — and the
   draw is checkable by hand:

   ```
   while read -r id; do
     printf '%s  %s\n' "$(printf '%s|%s' "$SEED" "$id" | sha256sum | cut -c1-64)" "$id"
   done < items.txt | sort | head -8
   ```

   **Stratified odds, same primitive.** To draw a class at k× the base probability, give
   each of its items k tickets — `SHA256("<seed>|<item id>|0")` … `|k-1` — rank all
   tickets together, walk the sorted list, and take an item the first time any of its
   tickets appears, stopping at N. Eligibility stays universal (every item keeps at
   least one ticket); only the odds move.
3. **External public value.** Index the list by a number nobody controls and nobody
   knows yet: the hash of tomorrow's publicly posted figure (a lottery number, a
   published closing value). Strongest against insider steering, since even the
   operator cannot know the outcome early.
4. **The ballotino move — separate the drawer from the stakes.** Venice's blind draws
   were performed by a boy with no stake in the outcome [snippet-only]. Modern form:
   the person who physically executes the draw is not the person whose work is
   drawable, and rotates.

The acceptance test for any mechanic: *could the person running the draw have chosen
the outcome, and could anyone else tell if they had?* Both halves matter — an honest
but unverifiable draw protects nobody's legitimacy, including the operator's.

## Universality-floor design and the exemption vulnerability

The floor statement is one sentence: "Every <unit> in <boundary> is eligible for the
draw, with no exemptions." Design notes:

- **Enumerability is the floor's foundation.** The draw points into a list; anything
  that can exist off-list is structurally exempt. First engineering task: make the
  population enumerable (a numbered register, a system query with a stated filter,
  a folder whose contents are the population).
- **Every exemption is a routing instruction for evasion.** "Under $50" makes $49 the
  standard price of invisibility; "senior staff excluded" makes seniority the safe
  harbor; "already approved twice" makes rubber-stamping a laundering step. If volume
  forces stratification, stratify the *odds* (small items drawn at lower probability),
  never the *eligibility* — a nonzero draw chance deters; a zero chance invites.
- **The generals test.** The floor is real only if it covers the most senior, most
  trusted, most awkward-to-examine people in scope — euthynai bound the strategoi, and
  that is why it worked [snippet-only]. When proposing the program, name this
  explicitly; the exemption requests that follow are the vulnerability map.
- **Scheduled, not discretionary.** The draw happens every period on a stated cadence.
  A draw that requires someone to decide to run it has a suspicion trigger smuggled
  back in — the decision *is* the accusation.

## Reviewer-rotation patterns

Who examines matters as much as what is examined:

- **Draw reviewers by lot from a qualified pool.** Define the pool (who is competent
  to examine this item type and has no stake in it), then draw the assignment the same
  verifiable way items are drawn.
- **Pairs beat singles where stakes allow.** Two allotted reviewers per item — the
  Athenian boards were allotted panels, not individuals [snippet-only] — halve the
  purchase value of any one relationship and give findings a second signature.
- **No permanent reviewer-reviewee pairs.** Track the pairing history; if the same
  two names recur, force a redraw. Familiarity is capture on an installment plan even
  between honest people — shared assumptions stop being examined.
- **Conflict rule, stated in advance.** A drawn reviewer with a stake in the item
  (their own work, their report's work) is replaced by the next draw — by rule, not
  by their judgment on the day.
- **Small-office compression.** With three people, the pool for any item is everyone
  who didn't touch it; with two, the second person examines the first's drawn items
  and an outside peer is borrowed periodically. The principle survives scaling: the
  examiner is not chosen by the examined, and not the same person forever.

## The handover-review default

The euthynai move, transplanted: **every role transition gets its accounting, by
default, within a stated window** — departure, promotion, rotation, contract end. Not
because transitions are suspect, but because they are the natural audit-readiness
moment (the knowledge is about to walk) and because universality is what removes the
sting: examining only *some* departures accuses those departed.

Mechanics: trigger is the transition itself (calendar-automatic, like the Athenian
one-month window [snippet-only]); scope is a standard short list (open items, held
authorities and accesses, delegated approvals, anything the role signed in its final
period, plus a lot-drawn slice of its routine output); output is a short written
record with findings adjudicated by a human and signed by both the reviewer and,
where possible, the departing person. The clean record serves the departing person —
it is their receipt, which is why universal handover accounting tends to be *popular*
once installed. Frame it that way when proposing it.

## The assistant-first-pass protocol

Random selection historically died of workload: a genuine examination of thirty drawn
items a month is a job nobody had, so real programs shrank to theater. The assistant
changes the economics — with one discipline held absolute.

Per drawn item, the assistant:
1. Pulls the item's record and the policy or standard it should satisfy.
2. Checks the item against each stated requirement, quoting the evidence for each
   check (the approval chain, the amount vs. the limit, the required attachment).
3. Drafts a finding per discrepancy — *drafts*: "item 41: approver and requester are
   the same role; policy §3 requires separation" — with the evidence attached.
4. Flags what it could not verify from the record, as explicitly unverified.

The human then adjudicates every draft finding: confirm, dismiss with a reason, or
escalate. **The assistant drafts findings; the human owns every judgment.** No
finding is reported, and no consequence attaches, on the assistant's say-so alone.
This gate is not a courtesy — the program's legitimacy rests on findings being
human-owned, and an unadjudicated machine verdict inverts the fairness the lot was
built to produce.

Sizing rule: draw as many items as the human can genuinely adjudicate, not as many as
the assistant can process. The assistant's capacity raises the ceiling; the human's
attention is still the binding limit — and the deterrent comes from every item being
*drawable*, not from any particular volume being drawn.

## Worked example: expense approvals in a small office

Setup: an eight-person office; roughly 120 expense approvals a month flow through
three approvers; the office manager wants oversight without accusing anyone.

- **Population:** every approved expense line in the calendar month, enumerated by the
  accounting system's export — the export query is written down, so the population is
  verifiable too.
- **Floor:** all lines eligible, including the approvers' own expenses and the
  director's. (The director's inclusion was the point of contention and is the point,
  full stop — the generals test.) Odds stratified, eligibility not: lines above the
  delegation limit at 3× the base probability.
- **Lot:** on the first business day, the office manager reveals a seed committed by
  email on the 25th of the prior month (before the population closed), then runs the
  published hash-rank draw over the export's line ids — three tickets per line above the
  delegation limit, one per line below it, first eight distinct lines taken. Anyone with
  the export and the seed can re-run it in a shell.
- **Reviewer rotation:** two reviewers per month drawn from the five staff who are
  not approvers, same seed, pairing history kept; a drawn reviewer never examines
  their own or their manager's lines (next-draw replacement rule).
- **First pass:** the assistant checks each of the eight lines against the expense
  policy — approval separation, limit vs. amount, receipt attached, category
  plausible — and drafts findings with quoted evidence. The two reviewers adjudicate
  in a half-hour sitting; the human gate is the meeting, and nothing leaves it
  unadjudicated.
- **Handover default:** when an approver changes roles, their final quarter's
  approvals get a 12-line draw plus the standard handover list, same mechanics, same
  no-stigma framing.
- **Published rule:** everyone knows the export query, the odds, the seed-commitment
  date, and the script. Nobody knows which lines came up until the review closes.
  After six months the office's observable change is banal in the best way: receipts
  attach the first time, and being drawn is small talk, not scandal.

## Sources

All external claims [snippet-only] — WebSearch snippets cross-checked across
independent results; see the repo's research dossier
(`docs/research/epic-wave-held-research.md`, Lane 1 entry 4) for the full provenance
notes.

- Oxford Classical Dictionary, "euthyna" — the universal end-of-term accounting;
  allotted logistai and euthynoi; the one-month window; applicability to all
  magistrates including strategoi
- Aristotle, *Ath. Pol.* — the institutional description of the boards and procedure
- Molinari's protocol analysis of the 1268 Venetian doge election — the ten
  alternating rounds (30→9→40→12→25→9→45→11→41), the ballotino's blind draws, family
  quotas, and the protocol's 529-year run
