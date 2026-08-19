# The split-record method: halves, anchors, rejoining, and the second keeper

Method lineage: the English Exchequer's split tally sticks (12th century–1826) as
documented by the Science Museum Group's medieval Exchequer tallies, Wikipedia's tally-stick
and Burning of Parliament articles, and Christie's sale records [snippet-only]; the
independent-parallel-derivation section rests on Garcilaso de la Vega's account of khipu
keepers and Gary Urton's identification of surviving duplicate khipu (Cambridge, *Latin
American Antiquity*) [snippet-only]. Source list at the end of this file.

## Contents
- [The Exchequer mechanics, told properly](#the-exchequer-mechanics-told-properly)
- [The risk-inventory protocol](#the-risk-inventory-protocol)
- [Split-design patterns by medium](#split-design-patterns-by-medium)
- [Worked example — contractor deliverable acceptance](#worked-example--contractor-deliverable-acceptance)
- [The rejoining ritual](#the-rejoining-ritual)
- [The alteration test](#the-alteration-test)
- [The second keeper — independent parallel derivation](#the-second-keeper--independent-parallel-derivation)
- [Sources](#sources)

## The Exchequer mechanics, told properly

A debt was recorded by cutting notches into a willow stick — notch width and style encoded
the amount — and then splitting the stick lengthwise through the notches. The creditor kept
the longer half, the **stock**; the debtor kept the shorter, the **foil**. Settlement or
audit meant producing both halves and rejoining them: the notches had to line up, and —
decisive — the **wood grain had to match across the fracture**, a pattern no forger could
reproduce because refitting a fracture is harder than any signature. Each party held the
half the *other* party would want altered, so each policed the record at no institutional
cost. The system served the Exchequer for roughly 650 years, from the 12th century until
its abolition in 1826 [snippet-only: Science Museum Group, Wikipedia, Christie's].

Three properties did the work, and each must survive translation to any modern medium:

1. **Halved between adverse parties.** Neither side can alter the record alone; the party
   holding the other half is exactly the party motivated to catch alteration.
2. **Tamper-evidence from the medium.** The grain authenticates the pair by physics, not by
   procedure. No custodian, however privileged, can override a fracture.
3. **Verification is rejoining.** The check is a physical operation with a binary outcome —
   the halves fit or they don't — not a judgment about whose ledger seems more credible.

The coda: in 1834, two cartloads of retired tallies were burned in the furnaces beneath the
House of Lords; the flues overheated and the fire destroyed the Palace of Westminster
(16 October 1834) [snippet-only]. Six centuries of tamper-evident records, and the one
undesigned step — disposal — took down Parliament. Retirement is part of the flow.

## The risk-inventory protocol

1. **List the record flows that matter.** Wherever value, obligation, or blame will later
   depend on "what was agreed / delivered / decided / approved, and when": agreements and
   amendments, acceptance of work, decision logs, approvals, timesheets, filings, evidence
   for a potential dispute.
2. **For each flow, name the single-custody risk.** Who holds the only authoritative copy?
   Could that holder — including you — alter it after the fact without anyone being able to
   prove the alteration? (An honest "yes, we could" is the finding, not an accusation.)
3. **Name the adverse party.** Who would be harmed by an alteration in each direction? That
   party is the natural holder of the other half. No adverse party with an interest in the
   record's integrity → a split cannot work there; use a third-party anchor instead.
4. **Score by stakes:** what a successful alteration would cost (money, liability, a lost
   dispute), and how likely a dispute is over the flow's lifetime.
5. **Split the top of the list; leave the bottom alone.** Splits cost upkeep and
   counterpart goodwill. Ordinary records with ordinary stakes keep ordinary copies.

## Split-design patterns by medium

For each pattern: what each side holds, and what mismatch alteration produces.

| Pattern | Our half | Their half | Alteration shows as |
|---|---|---|---|
| **Counterpart confirmation** | The record | Their own written statement of the same terms, kept by them | The two statements no longer agree on terms neither side can re-edit alone |
| **Hash anchor** | The record (editable by us) | The record's hash, held/published where we cannot edit | Recomputed hash ≠ anchored hash |
| **Third-party anchor** | The record | Timestamped copy lodged with a neutral holder | Our copy diverges from the lodged one |
| **Signed receipt** | The delivered item | Their signed acknowledgment of exactly what was received, when | Receipt describes something other than the disputed item |
| **Append-only log + external anchor** | The running log | Periodic hash of the log-so-far, sent outside our control | Any rewrite of history breaks every subsequent anchor |
| **Dual custody** | Half the authority to change (e.g., one of two keys/signatures) | The other half | No change exists without both parties' marks on it |

Design rules that make any of these a real split:

- **The halves must interlock, not resemble.** A confirmation restates the terms; a receipt
  names the deliverable and the date; a hash is recomputable. "We also kept a copy" fails,
  because each side can claim the other's copy is the altered one — nothing fits.
- **The anchor must sit outside the record-holder's reach.** A hash in the same folder as
  the record is stock and foil in the same drawer.
- **Cheap beats perfect.** An emailed one-paragraph confirmation the counterpart keeps is a
  weaker grain than a cryptographic anchor — and infinitely stronger than the unsplit
  record it replaces. Match the medium to the stakes from the inventory.
- **Time-stamp the split, not just the record.** The half's value is that it existed
  *before* the dispute; make the halving event itself dated and provable (send, don't
  just save).

## Worked example — contractor deliverable acceptance

Domain-neutral on purpose: "contractor" here is any outside party delivering work — a
freelance developer, an expert preparing a work product for an attorney, a vendor delivering
equipment to an operations manager, an agency delivering a dataset to an analyst.

**The unsplit flow (the risk).** The contractor uploads deliverables to the client's shared
drive; the client pays against them. Every record of what was delivered, in what version,
and when lives in a store one party controls. If a defect dispute arises a year later,
either side could have altered the files or their timestamps, and neither can prove
otherwise — the classic single-custody flow, maximally editable exactly where stakes are
highest.

**The split design, by the numbered method:**

1. *Risk inventory:* the flow ranks high — payment and liability both hang on "what was
   delivered when," and the dispute window (warranty/engagement term) is long.
2. *The split:* the receiving side must hold something the delivering side cannot alter,
   and vice versa — acceptance must fit delivery.
3. *Medium:* on each delivery, the contractor sends with the files a manifest: file list,
   version, date, and a hash of each file. The client replies with a dated acceptance
   note — "received manifest M, hashes verified, accepted for review" — which the
   contractor keeps. Now the contractor holds the acceptance (the client cannot deny
   receipt or swap files without the hash mismatch showing); the client holds the manifest
   (the contractor cannot later substitute a "fixed" version and claim it was the
   original). Each side holds the half the other would want altered.
4. *Rejoining ritual:* at each payment milestone — and at engagement end — hashes are
   recomputed against the manifest and the acceptance chain is read back. Result recorded
   in one line each time.
5. *Alteration test (run once at design time, on a copy — see
   [The alteration test](#the-alteration-test)):* silently replace one delivered file with
   an edited version, then run the ritual. The recomputed hash must fail against both
   halves. If anyone can swap the file and pass, the design is broken — e.g., the manifest
   was stored only on the shared drive both parties can edit.
6. *Second keeper (if the deliverable is a computed number — a valuation, a dataset's
   summary statistics):* someone on the receiving side re-derives the headline figures
   from the raw inputs before acceptance, blind to the contractor's figures.
7. *Retirement:* both sides keep their halves for the engagement term plus the dispute
   window stated in the agreement, then confirm disposal to each other in writing —
   **subject to the hold rail below, which overrides the schedule in every case.**

## The hold rail (step 7's mandatory companion)

Step 7 is the only step in this skill that destroys evidence, and it does so on a schedule
both parties signed. That makes the hold rail structural, not optional.

**The trigger is foreseeability, not filing.** A schedule suspends the moment litigation, a
claim, an audit, or a regulatory inquiry becomes *reasonably anticipated*. Concretely, any
of these should trip it: a demand or preservation letter, a threat to sue however informal,
a serious internal complaint, a regulator's inquiry or subpoena, an insurer's notice, a
counterpart's lawyer appearing on a thread, or your own decision to bring a claim. Waiting
for a filed complaint means the deletions that mattered already ran.

**What the rail contains**

| Element | Test it passes |
|---|---|
| Named trigger owner + backstop | Someone can trip the hold today, and someone else can when they are on leave |
| Written suspension notice | Sent to every holder of every half — **including the counterpart**, who cannot honor a hold nobody told them about |
| Scope statement | Names the flows, anchors, and logs frozen, so "did this cover the ritual log?" has a written answer |
| Automation confirmation | Retention policies, log rotation, mailbox purges, expiring links, and storage lifecycle rules verified **off**, not merely requested off |
| Release condition | Disposal resumes only on a written release from a named person, dated and logged like any rejoining result |

**Scope reaches the whole apparatus.** The primary half is the obvious target and the
easiest to freeze. The parts that quietly expire are the anchors, the third-party
lodgements, the append-only log's rotation window, the rejoining ritual's result log, and
the second keeper's working papers. A frozen document whose timestamp log rotated away is a
file you can no longer authenticate — you preserved the evidence and destroyed the proof it
is the evidence.

**Log the hold like a rejoining.** Date the trigger, the notice, the automation
confirmation, and the release, in the same log the ritual writes to. If the destruction is
ever questioned, that log is the difference between a documented good-faith suspension and
a schedule that ran on autopilot.

**Scope and limits.** U.S. Federal Rule of Civil Procedure 37(e) governs lost
electronically stored information in federal civil cases: curative measures on a finding of
prejudice, and the severe sanctions — adverse-inference instruction, dismissal, default —
only on a finding that the party acted with intent to deprive another party of the
information's use. [rule text, FRCP 37(e) as amended 2015; the "reasonably anticipated"
trigger is the *Zubulake* line — canon attribution, not re-verified here.] State courts and
other jurisdictions differ, and criminal, tax, employment, healthcare, and securities
regimes carry their own, sometimes stricter, preservation duties. Nothing here is legal
advice for a specific matter: a live preservation question goes to counsel immediately,
because the cost of asking late is the thing that is already gone.

Total cost: a manifest, a reply email, and a one-line log — the tally stick was never
expensive either. The point is not the tooling; it is that after the split, **neither party
can alter history without the mismatch showing at rejoining.**

## The rejoining ritual

Tamper-evidence only pays when someone looks. The ritual is the looking, on a schedule:

- **When:** before reliance, always — payment, renewal, filing, escalation — plus a fixed
  cadence for long-lived flows (quarterly or at period end). Never first at the dispute.
- **What:** the literal fit test per medium — recompute hashes against anchors; read terms
  against the counterpart confirmation; walk the append-only log's anchor chain; confirm
  receipts match deliverables.
- **Record:** one line per rejoining — date, flow, halves checked, fit or mismatch,
  checker. This log is itself worth anchoring (pattern: append-only log + external
  anchor). A dated history of "the halves fit" is what makes the record trustworthy *for
  the whole period*, not merely at the moment of checking.
- **On mismatch:** stop reliance first (pause the payment, the filing, the renewal), then
  investigate which half moved — the halves tell you *that* history changed, and the
  custody trail tells you *where*. Whose account of events to believe is a different
  question; if it comes to reconciling people's conflicting recollections, that is
  `decision-science-skills:rashomon-effect` territory.

## The alteration test

**Run it on a copy. Never on live records.** This test asks you to forge a record, and the
records in scope are, by construction, the ones that matter — client files, accounting
entries, clinical notes, the evidence chain itself. Falsifying a live one is not a test, it
is the thing the skill exists to prevent, and a covert alteration of a real record you
"meant to undo" is indistinguishable afterwards from one you did not. Three rules, before
step 1:

- **Test against a copy of the store, a sandbox instance, or a purpose-made synthetic record
  set** that mirrors the real structure. If the design can only be tested against production,
  that is itself a finding about the design.
- **Label every test artifact as a test at the moment it is created** — in the filename, in
  the record body, and in the log — so it can never later be mistaken for, or presented as,
  a genuine record. An unlabelled forged record is a liability you manufactured.
- **Where the test touches a counterparty's systems, get written authorisation from both
  sides first.** "Silently" applies to the *operator* being tested, not to the organisations
  whose systems you are probing. Unauthorised alteration of someone else's records is not a
  methodology question.

With that in place, every split gets tested by playing the forger — once at design time, and
again whenever the medium or custody changes:

1. **Enumerate the attackers honestly:** each party (including you), plus anyone with admin
   rights over the stores involved. The test is about capability, not suspicion.
2. **For each, attempt the alteration that would profit them:** change the amount, swap the
   file, backdate the entry, delete the inconvenient item, rewrite the log.
3. **Run the rejoining ritual.** The design passes only if every attempted alteration
   produces a visible mismatch — and fails if any attacker can also reach the other half
   (the admin who can edit both the record and its anchor is one party holding both
   halves, whatever the org chart says).
4. **Fix the split, not the procedure.** If alteration can pass, the answer is a better
   half or a further anchor — not a policy asking people to behave. The tally never asked.

## The second keeper — independent parallel derivation

The Inka ran imperial bookkeeping on khipu — knotted-cord decimal records — and did not
trust a single keeper: Garcilaso de la Vega reports a minimum of four khipu keepers per
community maintaining the same accounts, and Gary Urton's work identifies surviving
matching/duplicate khipu pairs and triples — physical evidence of parallel redundant
encoding, checked record-against-record [snippet-only].

This is the sibling of the split, for records that are **computations rather than
exchanges.** A split proves what passed between parties; it cannot catch a number that is
wrong identically in both halves — a miscalculated total is faithfully preserved by every
hash. For the few numbers where an error is expensive (the figure a payment, filing, or
decision rests on):

- A **second keeper** — a person, or an independently written script — re-derives the
  number from the raw source.
- **Blind:** the second derivation happens without sight of the first result; a checker who
  knows the target number finds the target number.
- **Independent path:** different person, and ideally different tools or method, so the two
  derivations do not share the same mistake.
- **Agreement is checked result-against-result,** and a disagreement is investigated before
  the number is used — the whole point is that this happens *before* reliance.

Use it sparingly: N-version bookkeeping for everything is the double work it looks like.
The khipu empire paid four keepers for the accounts that ran the state; you fund a second
keeper for the handful of numbers that would fund a dispute.

## Sources

All marks [snippet-only]: claims cross-checked across independent WebSearch results; direct
fetches were egress-blocked in the research sandbox. Per the library's research dossier
(docs/research/epic-wave-held-research.md, Lane 1, entries 2 and 8):

- Split tally sticks — Science Museum Group (medieval Exchequer tally sticks); Wikipedia;
  Christie's [snippet-only]
- Burning of Parliament, 16 October 1834 — Wikipedia [snippet-only]
- Khipu duplicate accounts — Gary Urton, "Khipu Archives, Duplicate Accounts, and Identity
  Labels in the Inka Knotted String Records," *Latin American Antiquity* (Cambridge);
  Garcilaso de la Vega via Harvard Library and Britannica coverage [snippet-only]
