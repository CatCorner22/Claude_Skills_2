---
name: sbar-structured-communication
description: >-
  Structures high-stakes workplace communication with the protocols high-hazard industries run
  on: SBAR for escalations (Situation, Background, Assessment, Recommendation with a deadline),
  I-PASS for transferring work (criticality, problem summary, action list, if-then contingencies,
  receiver read-back), closed-loop confirmation for critical instructions, and PACE graded
  assertiveness (Probe, Alert, Challenge, Emergency) for questioning a decision upward — drafting
  phrase ladders for the specific relationship and roleplaying the hard conversation first. Use
  when escalating an issue to a manager, partner, or executive, transitioning work for coverage or shift
  change, giving instructions that must not be misheard, or preparing to challenge a superior's
  call such as a suspicious approved payment. Triggers: SBAR, escalate this to, structured
  handoff, transition this work, coverage notes, read-back, closed-loop communication, graded
  assertiveness, PACE, speak up to the boss.
metadata:
  version: "1.2.0"
---

# SBAR structured communication

## When to use
- Escalating a problem upward so it lands in one read — an analyst flagging a payment to the
  treasurer, a front-desk team member raising a concern to the office manager or dentist.
- Transferring work between people: coverage or vacation notes, shift change, transitioning a
  task, or the process-owner handoff that closes a DMAIC Control phase
  (`continuous-improvement-skills:dmaic-problem-solving` names that deliverable with no format —
  this skill supplies the format).
- Giving or receiving an instruction where a mishear is expensive: a payment amount, bank
  details, a chart entry.
- Preparing to question a decision made above you — a suspicious approved wire, an off-policy
  instruction — without either silence or insubordination.
- Not for: tightening general professional prose → see `writing-skills:adams-smart-brevity`
  (that is a writing register; this is a communication protocol). Processing a correction of
  your own work → see `metacognition-skills:reflective-learner`. Getting a decision out of a
  written page — the one-pager with costed options and a signable ask → see
  `collaboration-skills:executive-briefing`; SBAR is the urgent, usually spoken escalation that
  must land in one read, and that skill owns the page a reader signs.

## Do it
1. **Pick the protocol by the moment.** Escalation → SBAR (step 2). Transferring work to another
   person → I-PASS (step 3). Critical instruction → closed loop (step 4). Challenging a decision
   upward → PACE (step 5). One moment, one protocol.
2. **Escalation = SBAR.** (a) **Situation** — one sentence: the problem, now. (b) **Background** —
   only the facts the receiver needs to judge it; pertinent, never biographical. (c) **Assessment** —
   what you think is going on; commit to a view, with stated uncertainty if needed ("I can't rule
   out X"). (d) **Recommendation** — what you want the receiver to do **and by when**. A
   recommendation without a deadline is a status update, not an escalation.
3. **Work transfer = I-PASS.** (a) Severity, translated for office work as **item criticality** —
   lead with what can hurt us; (b) **problem summary** per item; (c) **action list** — each action
   with owner and when; (d) **situation awareness and contingency plans** as if-then pairs ("if the
   confirmation doesn't arrive by noon, call the bank's desk"); (e) **synthesis by receiver** — the
   receiver restates the plan back and the sender corrects gaps. The handoff is complete at the
   read-back, not when the sender stops talking.
4. **Critical instructions = closed loop.** Sender states → receiver repeats it back → sender
   confirms ("that's correct"). Three turns — the sender's confirmation is the loop. Amounts,
   account digits, names, and doses are repeated item by item.
   - **The loop verifies transmission, not correctness.** It catches a mishear — 30 heard as
     13 — and nothing else. If the sender means the wrong thing, the readback confirms the
     wrong thing in two voices and *adds* confidence to the error. So a closed loop is not a
     wrong-site, wrong-patient, or wrong-account control: those need verification of the plan
     against the source (chart, consent, imaging; the vendor's file and a phone-back on a
     changed payee) and a stop point immediately before acting at which anyone may halt it.
     Run both. A team that believes the readback covers wrong-site has swapped a control for
     a slogan. `safety-and-reliability-skills:checklist-design` owns the pause-point structure.
5. **Challenging upward = PACE graded assertiveness.** Climb in order: **Probe** ("do we know the
   fuel state?" / "did we verify the new bank details by phone?") → **Alert** ("I'm concerned
   this doesn't match the vendor's history") → **Challenge** ("I don't think we should release
   this until it's verified") → **Emergency** ("Stop this payment."). Draft the phrase ladder for
   the specific relationship in advance (junior analyst → senior approver; dental assistant →
   dentist) — worked ladders are in `references/protocols-and-scripts.md`.
6. **Protect critical phases (sterile-cockpit discipline).** During a payment release, a cutover,
   or a clinical procedure, permit no non-essential interruption; park other topics explicitly
   for afterward, and say when they'll be heard.
7. **Draft with the model; enact with the humans.** Paste the rambling situation dump and have it
   restructured into SBAR; generate the if-then contingency list a tired person forgets; have the
   PACE ladder phrased for the real relationship; roleplay the uncomfortable conversation before
   having it. The receiver's read-back and the decision itself are human acts — the protocol only
   works enacted, never merely written.

## Why / learn
Two failure modes destroy communication under pressure: information dies at transitions, and
deference silences warnings under an authority gradient. The second one crashed United 173 — the
flight engineer knew fuel was critically low, hinted instead of challenging, and the aircraft ran
out of fuel while the captain troubleshot a landing-gear light [snippet-only]. That accident is
why aviation began training crews in crew resource management, from which PACE and
closed-loop descend; SBAR came the other way, adapted at Kaiser Permanente by Leonard, Bonacum,
and Graham from military and aviation briefing formats into clinical escalation. Each protocol
attacks one failure mode structurally: SBAR forces the sender to commit to an assessment and a
timed request instead of dumping data and hoping the listener infers urgency; I-PASS converts a
one-way broadcast into a verified transfer, because the receiver's synthesis is the only moment
the sender learns what actually arrived; closed loop makes a mishear detectable in the third
turn; PACE gives a subordinate a legitimate, graded script so the challenge doesn't require
heroism. The evidence is unusually strong for a communication intervention: the I-PASS handoff
bundle across 9 hospitals and 10,740 admissions cut medical errors 23% and preventable adverse
events 30% with no increase in handoff time [snippet-only], and VA team training showed an 18%
surgical mortality decline in trained facilities versus 7% in untrained, with a dose-response
relationship [snippet-only]. In any approval chain, PACE is the human barrier on the
business-email-compromise bowtie (see `safety-and-reliability-skills:bowtie-barrier-analysis`):
the junior analyst who challenges the suspicious approved wire is a control, and the ladder is
what makes that control fire. One caution the evidence also teaches: copying the form without
the mechanism nulls the result — a pasted SBAR nobody reads back is scenery.

## Common mistakes
- Background becomes a biography → include only what changes the receiver's judgment; cut the rest.
- Recommendation without a deadline → nothing happens; state the action and the by-when.
- Handoff with no receiver synthesis → a broadcast, not a transfer; require the read-back.
- Closing the loop in two turns → the mishear survives; the sender's final confirmation is the loop.
- Starting at Emergency, or never leaving Probe → climb the ladder in order, at the pace the risk demands.
- Treating the written template as the intervention → enactment is the active ingredient; unread ladders and skipped read-backs deliver nothing.

## Tailor to your environment
Record your real communication paths in `references/your-environment.md`: who escalates to whom
(analyst → treasurer; front desk → office manager → dentist), your coverage-notes template, the
phases you treat as sterile-cockpit (payment release windows, procedures), and PACE ladders tuned
to the actual relationships. If it names real people, accounts, or incidents, put it in
`your-environment.private.md` (git-ignored) instead. Never commit real payment or patient details.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/sbar-structured-communication.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/protocols-and-scripts.md — the four protocols in full, with worked treasury and dental examples, PACE phrase ladders, the sterile-cockpit rule, and the evidence base
- references/your-environment.md — your escalation paths, ladders, and templates (add when supplied)
