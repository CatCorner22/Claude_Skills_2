---
name: bowtie-barrier-analysis
description: >-
  Maps the defenses around a standing hazard as a bowtie: names the top event where control is lost,
  generates threat lines by running HAZOP guidewords (no, more, less, reverse, as well as, part of,
  other than) over the process, places independent preventive barriers on each threat line and
  mitigative/recovery barriers on each consequence, attaches escalation factors that degrade
  barriers, and gives every barrier an owner plus an assurance test — policing the policy-as-barrier
  error throughout. Use when mapping what stands between a hazard and a loss (unauthorized payment
  released, fraudulent instruction accepted, clinical harm), turning a flat control list into a
  defense architecture, or auditing whether a claimed control is a real barrier. Triggers: bowtie,
  barrier analysis, top event, lines of defense, what stops this from happening, escalation factor,
  HAZOP, guideword.
metadata:
  version: "1.1.0"
---

# Bowtie barrier analysis

## When to use
- Mapping the defenses around a *standing* hazard before anything goes wrong — payment fraud, BEC,
  release of an unauthorized payment, a clinical safety event.
- Turning a flat list of controls into an architecture: which threat does each control block, where
  are the unguarded lines, what degrades each barrier.
- Auditing controls: an audit finding is a missing or failed barrier — place it on the diagram.
- **Not for:** a one-off cause hunt after an incident → see
  `continuous-improvement-skills:root-cause-analysis`. Scoring failure modes of a process design
  with severity/occurrence/detection → see `continuous-improvement-skills:fmea`. Adversarial review
  of a plan or project → see `continuous-improvement-skills:project-command-center`.

## Do it
1. **Name the hazard and the top event.** The hazard is the standing activity with harm potential
   ("we move money on instruction"); the **top event** is the single moment control is lost — e.g.
   "fraudulent payment instruction accepted as genuine". One top event per bowtie; if you have two,
   draw two bowties.
2. **Generate threat lines with HAZOP guidewords.** Walk the guidewords over a plain description of
   the process and keep every credible deviation that could cause the top event: **NO** (no approval
   obtained), **MORE** (duplicate file transmitted), **LESS** (partial approval, short verification),
   **REVERSE** (credit-return posting treated as receipts), **AS WELL AS** (extra payee appended),
   **PART OF** (truncated addenda), **OTHER THAN** (wrong beneficiary, wrong account). Full
   guideword × parameter matrix in `references/bowtie-and-hazop-method.md`.
3. **Place preventive barriers on each threat line.** A barrier must be a real, independent control
   that can *by itself* stop that threat: dual approval enforced in the bank platform, callback to a
   number from the vendor master, positive pay, an ACH filter. "Training", "policy", and "culture"
   are never barriers — at best they support a barrier or control an escalation factor. Barrier
   quality tests (independent / effective / auditable) in the reference.
4. **Draw the right side: consequences and mitigative barriers.** If the top event happens anyway,
   what limits the loss and recovers? Recall/return request on the rail, the KYC/AML detection
   chain at the receiving bank, insurance, incident response and disclosure.
5. **Attach escalation factors.** For each barrier ask what degrades it: "approver on vacation →
   delegate rubber-stamps", "positive pay exception queue defaults to pay", "callback list stale".
   Add controls on the escalation factors themselves.
6. **Assign every barrier an owner and an assurance test — the human gate.** A model can draft the
   full bowtie from a plain process description in minutes and police the policy-as-barrier error,
   but people must correct the threat lines against how work really happens, *own* each barrier, and
   run its assurance test on a cadence. An untested barrier is scenery — the same doctrine as the
   failover rule elsewhere in this library: a backup you have never exercised is not a backup.
   **The deliverable is two things:** the diagram, and a barrier register with one row per barrier —
   which line it sits on, owner (a named role), assurance test, cadence, last test result. A diagram
   without the register is a picture; the register is what gets audited.

## Why / learn
Barrier thinking has an engineering lineage: bowtie-style diagrams trace to ICI hazard-analysis
course notes (1979); after Piper Alpha and the Cullen inquiry, Shell adopted the bowtie as a group
standard in the early 1990s, and CCPS / the Energy Institute later standardized the method ("Bow
Ties in Risk Management"). The HAZOP front end is older still — ICI in the late 1960s (Trevor
Kletz), codified in IEC 61882. Provenance-marked evidence notes in the reference.

Why the shape works: incident thinking is single-threaded — one cause, one fix. A bowtie forces you
to see *every* threat converging on one loss of control, and both sides of it: prevention on the
left, recovery on the right. The guidewords defeat the imagination limit — you don't brainstorm
threats (which yields the threats you already fear), you systematically deviate every step of the
process and let the deviations propose the threats. And the barrier-quality discipline is where most
value lives: most control registers are lists of wishes ("staff are trained", "policy requires"),
and the bowtie's demand that each barrier be independent, effective on its own, and auditable is
what converts a wish list into a defense architecture.

Honesty note: in financial services (fraud, cyber, operational risk) bowtie adoption is strong, but
controlled measurement of outcomes is thin — unlike the surgical-checklist literature there is no
clean before/after trial. Present it as a structuring discipline with an engineering pedigree, not
as a proven effect size.

Why this skill pairs well with a model: a classical bowtie workshop needs a trained facilitator and
a cross-functional team for one to two days *per hazard*, which is why most teams never run one. A
model drafts the complete bowtie — threat lines, barriers, escalation factors — from a plain process
description in minutes, and flags every soft barrier as it goes. The human work moves to the gate:
correcting threats against reality, naming owners, and running assurance tests.

## Common mistakes
- Policy or training listed as a barrier → not independent, not effective alone. Demote it to
  escalation-factor support and find the real control.
- Several top events in one diagram → mush nobody can act on. One moment of lost control per bowtie.
- Barriers with no owner or no test → scenery. Every barrier gets both, or gets deleted.
- Skipping escalation factors → the diagram looks safe until vacation season. Ask what degrades
  each barrier and when.
- Counting two barriers that share a failure mode (same person, same system, same data) as two →
  they are one barrier drawn twice.
- Using the bowtie as post-incident cause analysis → that is RCA's job; the bowtie is for standing
  hazards and their defenses.
- Left side only → prevention without recovery. The right side (mitigation) is half the diagram.

## Tailor to your environment
Record your hazards, top events, barrier owners, and assurance-test cadence in
`references/your-environment.md`; anything naming real people, accounts, or incidents goes in
`your-environment.private.md` (git-ignored). Known mounts: a flat cash-controls catalog (SOD, dual
approval, positive pay, BEC controls) becomes the barrier set for top event "unauthorized payment
released" — bring your own control catalog, since this library does not carry a finance one;
counterparty KYC/AML detection supplies the mitigative chain on the right side of a fraud bowtie;
an audit-findings catalog
from your own assurance function maps one-to-one onto missing or failed barriers — record where
yours lives here.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/bowtie-barrier-analysis.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/bowtie-and-hazop-method.md — guideword × parameter matrix, barrier quality tests
  (independent / effective / auditable), escalation-factor catalog, assurance-test patterns, the
  worked BEC treasury bowtie, and lineage/evidence notes with provenance
- references/your-environment.md — your hazards, top events, barrier owners, and assurance tests
