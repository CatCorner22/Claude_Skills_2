# Exercise design (scenarios, injects, adjudication, escalation safety)

## Contents
- Scenario library — three high-yield starters
- Scenario library — additional patterns
- Inject templates
- Adaptive-inject rules
- Adjudication rules (white cell)
- Escalation-safety discipline for LLM red/white play
- Turn log template

## Scenario library — three high-yield starters

**1. BEC payment-fraud drill** (pairs with `safety-and-reliability-skills:bowtie-barrier-analysis` — the barrier map is the drill's test plan)
- Setup: a supplier "bank-change" email chain, followed by an urgent wire request that
  impersonates an executive, timed against an approver's known absence.
- Blue objective: the fraudulent payment never releases; the genuine payment run is not
  paralyzed.
- Red's levers: escalating urgency, spoofed reply-chains, a phone call quoting real
  invoice numbers, a second smaller "test" payment.
- What it reveals: callback discipline, out-of-band verification, dual-approval reality
  vs. paper, who can say "stop" to a name with authority on it.

**2. Bank-connectivity outage on payroll day** (pairs with `safety-and-reliability-skills:break-glass-playbooks` — the drill unseals the contingency playbook)
- Setup: the transmission channel to the disbursement bank fails the morning payroll
  files are due; the bank's status line says "investigating."
- Blue objective: payroll settles on time through a contingency channel without
  duplicate files.
- Red/environment levers: partial acknowledgments (files maybe received), portal limits
  below payroll size, cutoff times approaching, a second bank asking for setup lead time.
- What it reveals: contingency payment paths, duplicate-release controls, bank contact
  tree currency, decision authority for changing rails under deadline.

**3. Ransomware during month-end close**
- Setup: file shares and the ERP integration layer encrypt mid-close; email is suspect;
  the close calendar has statutory deadlines.
- Blue objective: protect cash operations (payments, positions) first, then complete a
  defensible close with degraded systems.
- Red's levers: spreading encryption, a ransom deadline, an offer of "proof" decryption,
  rumors reaching leadership before facts.
- What it reveals: what treasury can do from a clean device, paper/portal fallbacks,
  communication when email is untrusted, close-deadline triage authority.

## Scenario library — additional patterns
- Cutover weekend meets hostile Monday: new Oracle config live, bank file format rejects.
- Key-person outage: the one analyst who runs the recon engine is unreachable during a
  break investigation.
- Regulator/auditor arrives mid-incident: evidence preservation vs. operational speed.

## Inject templates

Pre-scripted injects are written before play, with delivery times; each states its
purpose. Format:

> **Inject #** · T+<minutes> · via <email/phone/alert/news> · to <role>
> **Content:** <the artifact players see — write it as the artifact, not a summary>
> **Purpose:** <the decision or gap this inject is meant to expose>
> **Expected branch:** <what blue plausibly does; what red does next in each branch>

Examples (sanitize before use; model on your real formats):
- Spoofed executive email: reply-chain quoting a real (sanitized) invoice, new IBAN,
  "board meeting, cannot talk, confirm by 3 pm."
- Bank alert: "File acknowledgment delayed. Do not retransmit." — arriving after blue
  has already discussed retransmitting.
- News item: local outlet reports "payment issues" at the organization — tests the
  communication plan, not the payment plan.
- Phone script for red: caller ID matches the bank's number; caller asks blue to "verify"
  credentials.

## Adaptive-inject rules
- Adaptive injects respond to what players actually chose; they are drafted by red/white
  during play and MUST stay inside the scenario's scripted bounds (below).
- Each adaptive inject still gets a one-line purpose before delivery — an inject without
  a target decision is noise.
- If blue solves the scenario early, escalate depth (consequences of their fix), not
  scope (a second unrelated disaster).

## Adjudication rules (white cell)
- Adjudicate after each action/reaction/counteraction exchange, before the next turn.
- Rule on plausibility, not preference: "would this action work in our real environment,
  with our real banks and systems, in this timeframe?" Cite the process document or the
  person in the room who owns that step.
- Track state visibly: what is down, what is pending, what each side knows, the clock.
- When uncertain, ask the process owner present; when no one knows, log it — "nobody
  could say whether X" is a primary finding.
- Consequential outcomes (fraud succeeded or not, payroll settled or not, data lost or
  not) are ruled by the human white cell only.

## Escalation-safety discipline for LLM red/white play
- The LLM is a scenario generator in both seats: it drafts red moves, injects, and
  adjudication *options with rationale*; humans select and rule.
- Provenance for the caution: studies placing LLMs in wargame roles report sudden
  escalation dynamics [snippet-only], and default sycophancy erodes adversary play into
  agreement with the user's plan.
- Anti-agreement prompt for red (adapt): "You are the adversary. Do not soften, do not
  concede a turn because blue sounds confident, do not praise blue's choices. Stay within
  the scenario bounds below. If blue's action would plausibly defeat your move, say so
  plainly and try the next-best adversary option."
- Scripted bounds: before play, write what red may and may not do (e.g. may spoof email
  and phone; may not invent nation-state capabilities, physical threats, or a second
  simultaneous disaster). The LLM never exceeds them, even "for realism."
- Ground truth: every inject cites which real process document, format, or system it is
  modeled on. An inject that can't be grounded is cut.

## Turn log template

| Turn | Blue action | Red reaction | Counteraction | White ruling (human) | Authority invoked | Gap exposed |
|------|-------------|--------------|---------------|----------------------|-------------------|-------------|

Hand the completed log to `decision-science-skills:after-action-review` for the debrief.
