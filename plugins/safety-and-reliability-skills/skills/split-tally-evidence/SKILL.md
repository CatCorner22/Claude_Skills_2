---
name: split-tally-evidence
description: >-
  Designs tamper-evident records on the split tally-stick principle (English Exchequer,
  ~650 years): notched stick split lengthwise into stock and foil, wood grain self-
  authenticating. Halves each record between adverse parties so verification is rejoining
  two halves neither can alter alone. Inventories records one party could rewrite,
  designs the split for each (counterpart-held confirmations, hash-anchored exports,
  signed receipts, append-only logs with external anchors), schedules verification as
  rejoining ritual, proves by attempted alteration, adds second keeper who independently
  re-derives critical numbers, and suspends disposal schedules under legal hold. Use when
  records must survive disputes or when evidence needs designing rather than hoping.
  Triggers: tally stick, split tally, tamper-evident, who holds the other copy, could
  someone alter this after the fact, does our half fit their half, hash anchor, dual
  custody, evidence design, litigation hold, legal hold, spoliation, duty to preserve.
metadata:
  version: "1.3.0"
  source: >-
    Built from the library's operational-wisdom research dossier
    (docs/research/epic-wave-held-research.md, Lane 1 entry 2: split tally sticks, English
    Exchequer, 12th c.–1826), with the khipu independent-parallel-derivation angle folded in
    per the same dossier's verdict. All external claims carry their provenance marks
    ([snippet-only] = cross-checked search snippets).
---

# Split-tally evidence (the record halved between adverse parties)

For roughly 650 years — the 12th century to 1826 — the English Exchequer recorded debts on
willow sticks notched for the amount and split lengthwise. The creditor kept the longer half
(the "stock"), the debtor the shorter (the "foil"), and the unique wood grain made the pair
self-authenticating: forging a half meant refitting a fracture. Verification was not
comparing two ledgers; it was physically rejoining two artifacts neither party could alter
alone [snippet-only: Science Museum Group, Wikipedia, Christie's]. The system's afterlife is
history's best records-management cautionary tale: in 1834 the retired sticks were
carelessly incinerated in the Palace of Westminster's furnaces, and the fire burned down
Parliament (16 October 1834) [snippet-only]. Both lessons hold — the control worked for six
centuries because the medium itself was the control, and even a retired record deserves a
designed disposal.

## When to use
- A record matters and one party could quietly alter it after the fact: agreement terms,
  approvals, deliverable acceptance, a decision log, a timesheet, a chain of evidence for a
  future dispute.
- "Who holds the other copy?" has no good answer — the only history of an important exchange
  lives in one side's editable system.
- Designing evidence *before* a dispute exists — for an analyst documenting sign-offs, an
  attorney building an evidence chain, an operations manager accepting vendor work, a
  developer proving what was delivered when.
- After a dispute exposed that a record could not be trusted, and the flow needs a split so
  it cannot happen again.
- A retention or disposal schedule exists (or is being written) and needs the hold rail that
  suspends it once litigation, a claim, an audit, or a regulatory inquiry becomes reasonably
  anticipated — step 7. This skill designs the rail; it does not replace counsel on a live
  preservation question.
- Not for: reconciling two systems' outputs against each other — statement-to-ledger matching and
  the account-reconciliation craft are finance-domain work this library does not carry; this skill
  designs what each side should hold so later comparison is even possible.
- Not for: assembling the audit file and responding to auditor requests — audit-readiness / PBC
  work, also outside this library.
- Not for: reconciling conflicting good-faith human recollections of one event →
  `decision-science-skills:rashomon-effect`; this skill exists so the record never depends
  on recollection.

## Do it
The risk-inventory protocol, split-design patterns by medium, worked example, rejoining
ritual, alteration test, and the second-keeper section are in
`references/split-record-method.md`.

1. **Run the risk inventory.** List the record flows where one party — including you —
   could alter history unilaterally: anything kept in a single editable store (a document
   one side hosts, a log its owner can rewrite, an agreement that lives only in one inbox).
   For each: who would want it changed, and what would a change cost the other side?
   Rank by stakes; split the top of the list.
2. **Design the split.** For each flow, answer the tally question: what does the OTHER side
   hold, such that our half must still fit theirs? A split is real only when alteration by
   either side produces a visible mismatch at rejoining. A copy both parties can edit is
   not a split; a copy only one party holds is not one either.
3. **Choose the modern medium.** The grain comes in several forms — pick per flow:
   a **counterpart confirmation** (the other side states the terms back in writing they
   keep); a **hash anchor** (a cryptographic hash of the record published somewhere the
   record-holder cannot edit — sent to the counterpart, posted in a third-party system);
   a **third-party anchor** (a timestamped copy lodged with a neutral holder);
   an **append-only log with external anchors**; a **signed receipt** at each handover.
4. **Make verification a rejoining ritual, not a hope.** Schedule it: at each milestone, at
   each period end, or before reliance (renewal, payment, filing). The ritual is literal —
   recompute the hash against the anchor, read the terms against the counterpart's
   confirmation — and its result is recorded. A split that is never rejoined is decoration.
5. **Test the split by attempting alteration — on a copy, never on live records.** Play the
   forger against your own design: change the record, then run the ritual. If any party can
   change the record without the mismatch showing at rejoining, the design failed — fix the
   split, not the procedure around it. **The forging is done against a copy of the store, a
   sandbox, or a synthetic record set**, every test artifact is labelled as a test when it is
   created, and any test reaching a counterparty's systems needs written authorisation from
   both sides first. "Silently" describes what the operator under test is not told; it does
   not describe altering real client, accounting, or clinical records, which is the act this
   whole skill exists to make detectable.
6. **For critical numbers, add a second keeper (the khipu pattern).** Independent parallel
   derivation: a second person or process re-derives the number from raw source, without
   seeing the first result, and agreement is checked result-against-result. The Inka ran
   accounts this way — multiple khipu keepers per community encoding the same events
   separately, with surviving duplicate khipu as physical evidence of the practice
   [snippet-only]. The sibling of the split: use it for records that are computations
   rather than exchanges.
7. **Design the retirement — and the hold that suspends it.** State how long each half is
   kept, by whom, and how disposal is confirmed on both sides. The Exchequer's control
   outlived its empire's memory of why it mattered; the disposal was improvised, and
   Parliament burned [snippet-only]. Half of record-keeping discipline is end-of-life
   discipline.
   - **No retirement schedule ships without a hold rail, and the hold rail gets the same
     weight as the alteration test in step 5.** Every schedule is suspended the moment
     litigation, a claim, an audit, or a regulatory inquiry becomes *reasonably
     anticipated* — not when it is filed, served, or docketed. That earlier trigger is the
     whole point: by the time a complaint arrives, the routine deletion that ran last month
     has already happened.
   - **Why this skill in particular needs the rail.** Everything above is built to make
     records survive a dispute, so step 7 is the one step that destroys evidence on a
     timer — and it destroys it *by mutual written agreement, on a documented schedule,
     with the adverse party holding proof of exactly when your half died.* Ordinary
     housekeeping destruction is arguable. Destruction under a scheduled, countersigned,
     jointly-logged protocol is the best exhibit an opponent could ask for on the question
     of whether it was deliberate. The artifacts this skill produces to prove good faith
     become the record of the disposal.
   - **The stakes, stated plainly.** Under U.S. Federal Rule of Civil Procedure 37(e),
     where electronically stored information that should have been preserved in the
     anticipation or conduct of litigation is lost because a party failed to take
     reasonable steps to preserve it and it cannot be restored or replaced, a court may
     order curative measures on a finding of prejudice — and **only on a finding that the
     party acted with the intent to deprive another party of the information's use** may it
     presume the lost information was unfavorable, so instruct the jury, or dismiss the
     action or enter default judgment. The intent finding is the cliff, and a documented
     schedule is evidence that speaks to it. [rule text — FRCP 37(e) as amended 2015. The
     "reasonably anticipated" trigger is the *Zubulake* line of authority (canon
     attribution, not re-verified here). U.S. federal civil only: state courts, other
     jurisdictions, and criminal, tax, employment, healthcare, and securities regimes carry
     their own and sometimes stricter obligations. This is orientation, not legal advice
     for your matter — a live preservation question goes to counsel, now, not after the
     next scheduled purge.]
   - **What a working rail contains:** a named person who can trigger a hold and a named
     backstop when they are unreachable; a written suspension notice to every holder of
     every half — **including the counterpart**, who cannot honor a hold they were never
     told about; a scope statement naming the flows frozen; and a rule that disposal does
     not resume until the hold is lifted in writing by whoever can lift it.
   - **The hold reaches the whole apparatus, not just the primary half.** Anchors,
     third-party lodgements, append-only logs and their rotation, the rejoining ritual's
     result log, and the second keeper's working papers from step 6 are all part of the
     record. Freezing the document while the log that timestamps it rotates away leaves you
     holding an unauthenticatable file.
   - **A hold fails through automation, almost every time.** Retention policies,
     auto-expiring messages, log rotation, mailbox purges, and short-TTL storage lifecycle
     rules delete on schedule while everyone honestly believes they stopped deleting.
     Suspending a schedule means turning the automation off and confirming it is off — not
     circulating a request that people refrain.

**Division of labor.** The assistant runs the risk inventory from a description of the
record flows, proposes the split and medium per flow, drafts confirmation and receipt
language, and scripts the rejoining ritual and alteration test. The human owns the stakes
ranking and the counterpart relationships — asking the other side to hold a half is a
relationship move, and it is theirs to make.

## Why / learn
The design insight is that the Exchequer never trusted a ledger where it could trust a
fracture. Every anti-tampering scheme needs something that cannot be quietly rewritten;
most schemes buy it with procedure (permissions, sign-offs, retention policies) that the
record's custodian can ultimately override. The tally bought it from physics: split wood
along the grain and the fracture surface is unique, so the record's integrity is a property
of the medium, not of anyone's good behavior. The modern equivalents keep that shape — a
hash is a grain pattern (any alteration changes it), an anchor is the other half (the
alteration shows only if the hash lives where the record-holder cannot reach), and that is
why a hash stored beside the record protects nothing.

The deeper move is choosing your verifier by interest, not by office. The debtor holds the
foil precisely because the debtor *wants* to catch an inflated stock — each side polices
the half it would be harmed by. Adverse interest is the cheapest, most attentive control
ever designed: it needs no salary, no sampling plan, and no reminder. That is also why the
split must run between genuinely adverse parties — two halves inside one team is redundancy
against loss, not evidence against tampering.

Rejoining on a schedule is what turns an artifact into a control. Tamper-*evidence* is
worthless unless someone looks at the evidence, and disputes arrive years after the
exchange, when memory has hardened into position — the ritual dates each "the halves fit"
result, so the record's integrity has its own documented history. The khipu pattern
answers the remaining gap: a split protects a record of *what was exchanged*, but a
computed number can be wrong identically in both halves — only independent re-derivation
from raw source catches that, which is why the Inka paid four keepers instead of one
[snippet-only]. And the Parliament fire teaches the last lesson with unmatched economy:
records outlive their designers, so a flow without a designed retirement ends in an
improvised one.

## Common mistakes
- Both "halves" in one party's custody → that is a backup, not a split; the other half
  must sit with a party who would be harmed by alteration.
- A copy instead of an interlocking half → if the counterpart's copy can be disputed as
  "not what we sent," it fails; use signed/confirmed forms or a hash so the halves must
  *fit*, not merely resemble.
- Hash anchored where the record-holder can edit → the same drawer holds stock and foil;
  publish the hash to the counterpart or a store outside the holder's reach.
- Rejoining "as needed" (meaning never) → schedule the ritual and record its results; the
  first rejoining should not happen at the dispute.
- Skipping the alteration test → an untested split is a hoped-for one; play the forger
  before relying on it.
- Running the alteration test on live records → you have forged a real record to prove you
  could; use a copy or synthetic set, label every test artifact as a test at creation, and get
  written authorisation before touching a counterparty's systems.
- Splitting everything → splits cost relationship and upkeep; the risk inventory ranks by
  stakes, and low-stakes flows keep ordinary records.
- Treating the second keeper as double bookkeeping → it is for the few critical computed
  numbers only, and the second derivation must be blind (no peeking at the first result).
- No designed disposal → retired halves accumulate until someone improvises; Parliament
  is the cautionary tale [snippet-only].
- A disposal schedule with no hold rail → the one step in this skill that destroys evidence
  runs straight through the moment a dispute becomes foreseeable, and it does so on a
  documented, countersigned timetable that reads as deliberate. Build the rail in step 7
  before the schedule goes live, not after the demand letter.
- Treating "reasonably anticipated" as "filed" → the duty attaches at foreseeability, which
  is usually months earlier; the deletions that hurt are the ones that already ran.
- Suspending a schedule by announcement while the automation keeps running → confirm the
  policies, rotations, and expiries are actually off; belief is not suspension.

## Tailor to your environment
Wire in your current role here — the pattern is domain-neutral and attaches to whatever
record flows matter in the job you hold now. In `references/your-environment.md`, record:
your high-stakes record flows and who the adverse party is in each, the split and medium
chosen per flow, where anchors live, the rejoining ritual's schedule and log, and the
retirement rule per flow. Keep the committed file structural. Real counterpart names,
agreement contents, live hashes, and anything client- or employer-identifying belong in
`your-environment.private.md`, which is git-ignored and never committed.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/split-tally-evidence.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/split-record-method.md — the Exchequer mechanics and the Parliament fire
  (provenance-marked), the risk-inventory protocol, split-design patterns by medium with a
  worked contractor deliverable-acceptance example, the rejoining ritual, the alteration
  test, and the second-keeper (khipu) section
- references/your-environment.md — your record flows, splits, anchors, ritual schedule,
  and retirement rules (sanitized stub; live detail goes in the `.private.md` twin)
