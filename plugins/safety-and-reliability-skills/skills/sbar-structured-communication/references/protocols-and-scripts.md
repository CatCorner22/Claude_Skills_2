# Protocols and scripts — SBAR, I-PASS, closed loop, PACE

The four protocols in full, with worked treasury and dental examples. All examples are
synthetic and sanitized — structure only, no real payments, patients, or people.

Contents: §1 Choosing the protocol · §2 SBAR (escalation) · §3 I-PASS (work transfer) ·
§4 Closed loop (critical instructions) · §5 PACE (graded assertiveness) ·
§6 Sterile-cockpit rule · §7 Evidence base and lineage

## §1 Choosing the protocol

| The moment | Protocol | The one thing that must happen |
|---|---|---|
| Raising a problem upward | SBAR | A recommendation with a deadline |
| Transferring work to a person | I-PASS | The receiver's synthesis (read-back) |
| Giving a critical instruction | Closed loop | The sender's third-turn confirmation |
| Questioning a decision above you | PACE | Climbing the ladder instead of hinting or exploding |
| A critical phase in progress | Sterile cockpit | No non-essential interruption; park and schedule |

## §2 SBAR (escalation)

Format — four labeled parts, in order, no preamble:

- **S — Situation.** One sentence: what is happening now. If the receiver reads nothing else,
  this sentence must carry the event.
- **B — Background.** Only the facts needed to judge the situation: amounts, dates, who was
  involved, what was already tried. Pertinent, never biographical. Three to six bullets.
- **A — Assessment.** What you think is going on. Commit to a view; state uncertainty
  explicitly ("most consistent with X; I can't rule out Y"). An escalation without an
  assessment forces the receiver to redo your analysis.
- **R — Recommendation.** The action you want, from whom, by when. Include the consequence of
  no action by the deadline if there is one.

Worked treasury example — analyst → treasurer, suspected business email compromise:

> **Situation:** A $248,000 vendor payment scheduled for today's 2 PM run matches a
> banking-details change we cannot verify.
> **Background:** The remit-to account was changed 3 days ago via an emailed request; the
> "confirmation" came from a domain one letter off the vendor's; callback to the number on
> file goes to voicemail; this vendor's prior 14 payments all went to the old account.
> **Assessment:** This pattern is consistent with business email compromise. I cannot confirm
> the change is legitimate.
> **Recommendation:** Pull this payment from the 2 PM run now, and hold it until we verify the
> change by phone with our known contact. I need your decision by 1:30 PM or it releases.

Worked dental example — front desk → office manager:

> **Situation:** Mrs. [patient]'s insurance shows terminated as of the 1st, and she is in the
> chair for a crown prep with an estimated $1,400 claim.
> **Background:** Eligibility check this morning returned "coverage terminated"; her employer
> changed carriers; we have no new carrier on file; she was quoted her old copay at booking.
> **Assessment:** If we proceed on the old estimate we will likely bill her the full fee later,
> which she has not agreed to.
> **Recommendation:** Someone needs to present a revised estimate and get her signature before
> the doctor starts the prep — in the next 10 minutes.

## §3 I-PASS (work transfer)

Origin: pediatric shift handoffs. Translation for office work — "illness severity" becomes
**item criticality**. The five parts:

1. **I — Item criticality.** Open with the ranking: which items can hurt us, which are
   routine. The receiver's attention budget is spent in the first minute — spend it on the
   dangerous items.
2. **P — Problem summary.** For each item: current state in two or three sentences. What it
   is, where it stands, what's unresolved.
3. **A — Action list.** Each open action with an owner and a when. "Being handled" is not an
   owner.
4. **S — Situation awareness and contingency plans.** If-then pairs for what may happen on the
   receiver's watch: "If X happens, do Y; if Y unavailable, do Z." This is the part people
   under time pressure always omit — and the part the receiver needs most at 4:55 PM.
5. **S — Synthesis by receiver.** The receiver restates the criticality ranking, the actions
   they now own, and the contingencies. The sender corrects gaps. The transfer is complete
   here, not at the end of the sender's monologue.

Worked treasury example — vacation coverage note (condensed):

> **Criticality:** (1) Wire recall on the duplicate ACME payment — money at risk, deadline
> Friday. (2) Month-end BAI2 file loads — routine unless a load fails. (3) Everything else
> waits.
> **Problem summary (1):** Duplicate $86K payment sent Tuesday; recall request filed with the
> bank Wednesday, case #[sanitized]; bank promised status by Thursday.
> **Actions:** You: call the bank desk Thursday 10 AM if no status email (contact in the
> shared runbook). Me (on return): file the write-off if recall fails.
> **Contingencies:** If the bank confirms return, post it to the clearing account and email AP.
> If the Friday BAI2 file fails to load, rerun the interface once; if it fails twice, open a
> ticket and load the statement manually — do not leave the recon open over the weekend.
> **Receiver synthesis:** Coverage restates the two critical items, Thursday's call, and both
> if-thens; sender confirms.

Worked dental example — front desk → clinical, morning transition: criticality first ("two
premeds not yet confirmed taken — chairs 2 and 4"), then per-patient summaries, then actions
("confirm premed before seating; if not taken, doctor decides reschedule vs. dispense"), then
the assistant reads the premed list back before the first patient is seated.

## §4 Closed loop (critical instructions)

Three turns. The third turn is the loop — without it, a mishear survives silently.

1. **Sender states** the instruction, one action at a time: "Release payment batch 47, total
   $1,204,300, value date today."
2. **Receiver repeats back** in their own words, critical values verbatim: "Releasing batch
   47, one-million-two-oh-four-three-hundred, value today."
3. **Sender confirms:** "That's correct." (Or corrects, and the loop restarts.)

Use for: payment amounts and account digits (read digit by digit), cutoff times, dosage or
chart entries, anything irreversible. Dental: "Extract number 30" → "Confirming extraction,
tooth three-zero, lower right first molar" → "Correct." The receiver names the tooth in words,
not just the number — transposition is the classic wrong-site error.

## §5 PACE (graded assertiveness)

A subordinate's script for challenging a decision, escalating in four graded steps. Climb in
order; the risk sets the pace — seconds in an emergency, days for a policy concern. Skipping
straight to Emergency burns trust; staying at Probe forever is the United 173 failure.

- **P — Probe.** A question that surfaces the data: "Do we know the fuel state?" / "Did we
  verify the new bank details by callback?" Gives the senior person the chance to catch it
  themselves — the cheapest correction there is.
- **A — Alert.** State your concern as a concern: "I'm concerned that this change came by
  email only and doesn't match the vendor's history."
- **C — Challenge.** Direct disagreement with the action: "I don't think we should release
  this payment until the change is verified. I'd like us to hold it."
- **E — Emergency.** Stop language, unmistakable: "Stop this payment. Do not release it. I am
  escalating to the treasurer now." Reserved for imminent, material harm — and when used, act
  on the stated escalation.

Worked ladder — junior analyst → senior approver (suspicious approved wire):
1. "Quick check before the run — did the callback on ACME's new account details reach the
   contact we have on file, or the number in the email?"
2. "I'm not comfortable with this one: new account, email-only request, lookalike domain.
   That's the classic compromise pattern."
3. "I don't think this should go in the 2 PM run. I'm asking you to hold it until the callback
   clears."
4. "Stop the payment. I'm calling the treasurer." *(Then call — an Emergency step you don't
   act on teaches everyone the ladder is a bluff.)*

Worked ladder — dental assistant → dentist:
1. "Doctor, can we double-check the chart? I have the premed as not yet confirmed."
2. "I'm concerned about starting before we confirm she took the premed — her cardiologist's
   note requires it."
3. "I don't think we should seat her until we've confirmed it. Can we call the pharmacy?"
4. "Please stop — we cannot start this procedure. I'm getting the office manager."

Two supporting norms make PACE work: a **two-challenge rule** (if two Challenges go
unanswered, escalate past the person, without penalty), and leadership explicitly inviting the
ladder ("if you're not sure, I want the Probe") — assertiveness training fails where speaking
up is punished.

## §6 Sterile-cockpit rule

Aviation's rule that below 10,000 feet the crew discusses nothing but the flight. Transplant:
declare specific phases interruption-free — the payment-release window, a production cutover,
seating-to-numbing in a procedure. During the phase: no drop-ins, no "quick questions"; anyone
interrupting is redirected to a named time ("after the 2 PM run"). The point is not rudeness
but error rates: interruptions during high-load phases are where transposed digits and skipped
checks happen. Mark the phases visibly (calendar block, a flag at the desk) so others can
self-serve the rule.

## §7 Evidence base and lineage

- **SBAR origin:** adapted for clinical use at Kaiser Permanente by Leonard, Bonacum, and
  Graham, drawing on military and aviation briefing formats (nuclear submarine and aviation
  practice) [snippet-only].
- **I-PASS outcome trial:** Starmer et al., New England Journal of Medicine — the I-PASS
  handoff bundle across 9 pediatric residency sites, 10,740 admissions: medical errors fell
  23%, preventable adverse events fell 30%, with no increase in handoff duration or workflow
  cost [snippet-only]. The strongest outcome evidence behind any protocol in this skill.
- **Team training mortality evidence:** Neily et al., Journal of the American Medical
  Association — VA facilities with medical team training showed an 18% decline in surgical
  mortality versus 7% in untrained facilities, with a dose-response relationship (more
  training, larger decline) [snippet-only].
- **PACE / closed-loop lineage:** aviation crew resource management (spelled out; the
  abbreviation is reserved for customer relationship management in this library), which grew
  from a NASA workshop on flight-deck human factors and the airline training programs that
  followed — prompted by the United 173 fuel-exhaustion crash, in which the flight engineer's
  unchallenged deference to the captain proved fatal [snippet-only].
- **Honesty note:** these effects came from enacted protocols with training and verification —
  the read-back, the invited challenge. Studies of artifacts adopted without their mechanism
  (checklists distributed without enactment) show null results; expect the same here if the
  templates are pasted but never spoken.
