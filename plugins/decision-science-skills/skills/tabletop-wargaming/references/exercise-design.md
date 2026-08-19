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

Each starter is stated in portable form first, then instantiated for one concrete
domain (payments operations) so the shape is visible. Re-instantiate for yours: swap
the irreversible action, the counterparty, and the deadline.

**1. The impersonated urgent instruction** (pairs with `safety-and-reliability-skills:bowtie-barrier-analysis` — the barrier map is the drill's test plan)
- Setup: an out-of-band instruction arrives from a named authority, demanding an
  irreversible action under time pressure, timed against the usual approver's known
  absence. The action is whatever your organization cannot take back: a payment
  release, a privileged access grant, a bulk data export, a public statement.
- Blue objective: the fraudulent instruction is never executed; legitimate work of the
  same kind is not paralyzed.
- Red's levers: escalating urgency, spoofed reply-chains, a phone call quoting real
  internal reference numbers, a second smaller "test" request.
- What it reveals: callback discipline, out-of-band verification, dual-approval reality
  vs. paper, who can say "stop" to a name with authority on it.
- *Payments instantiation:* a supplier "bank-change" email chain, then an urgent wire
  request impersonating an executive while the approver is travelling.

**2. Critical-vendor connectivity outage on a hard-deadline day** (pairs with `safety-and-reliability-skills:break-glass-playbooks` — the drill unseals the contingency playbook)
- Setup: the channel to a vendor you cannot substitute fails on the morning an
  externally fixed deadline lands; the vendor's status page says "investigating."
- Blue objective: the obligation is met through a contingency channel, exactly once.
- Red/environment levers: partial acknowledgments (the submission may have landed),
  contingency-channel limits below the required volume, cutoff times approaching, an
  alternative provider quoting setup lead time.
- What it reveals: contingency paths, duplicate-submission controls, currency of the
  vendor contact tree, decision authority for switching rails under deadline.
- *Payments instantiation:* the transmission channel to the disbursement bank fails the
  morning payroll files are due.

**3. Ransomware during a period-close or release freeze**
- Setup: file shares and an integration layer encrypt during a window when the calendar
  cannot move; email is suspect; the deadlines are statutory or contractual.
- Blue objective: protect the highest-consequence operations first, then complete a
  defensible close (or cut the release) with degraded systems.
- Red's levers: spreading encryption, a ransom deadline, an offer of "proof"
  decryption, rumors reaching leadership before facts.
- What it reveals: what the team can still do from a clean device, paper/portal
  fallbacks, communication when email is untrusted, deadline-triage authority.
- *Payments instantiation:* protect payments and cash positions first, then close.

## Scenario library — additional patterns
- Cutover weekend meets hostile Monday: new system config live, the downstream interface
  rejects the file format.
- Key-person outage: the one person who runs the matching/reconciliation engine is
  unreachable during an investigation.
- Regulator/auditor arrives mid-incident: evidence preservation vs. operational speed.

## Exercise control (run this before any inject reaches a person)

Blue players operate the real process with their real authorities, and the injects are spoofed
executive email, bank and vendor alerts, news items, and a phone call from someone claiming to
be the CFO. That combination is indistinguishable from an actual attack unless you make it
distinguishable on purpose. Five controls, all cheap, none optional.

**1. Every artifact carries an EXERCISE marking.** First line, last line, subject line: `**
EXERCISE EXERCISE EXERCISE — NO REAL ACTION **`. Every email, every document, every alert, and
spoken at the start and end of every phone inject. The marking is what stops a player from
actually wiring the money, and — just as important — what stops the artifact from causing a
real incident *later*, when someone finds the spoofed CFO email in a mailbox six months on and
escalates it as genuine fraud. An exercise artifact that survives without its marking has
become real evidence of a crime that did not happen.

**2. One named exercise director, with ENDEX and abort authority.** Named before start,
announced to every participant, reachable throughout. That person calls `ENDEX` (end of
exercise) and can abort instantly. State the abort phrase out loud at the briefing and make it
unambiguous and un-scriptable — **"REAL WORLD, REAL WORLD"** halts play immediately, and anyone
may call it, not just the director. Real emergencies do not wait for a scenario to finish, and
a participant who cannot stop the game to deal with one will either freeze or play through it.

**3. A no-play list, written before start.** People, systems, accounts, and counterparties the
exercise may not touch under any circumstances: production payment rails, real customer records,
the regulator, the actual bank fraud line, anyone on leave or unwell, anyone not briefed. Read
it aloud at the briefing. "We assumed nobody would actually call the bank" is the postmortem
sentence this list exists to prevent.

**4. Anything with an irreversible external effect is declared, not executed.** If a blue player
decides to freeze an account, file a report, notify a regulator, page a vendor, or send a real
message outside the exercise room, they say so to white cell and white cell adjudicates the
result. The decision is what the exercise is testing; the execution is not. Write this into the
brief in exactly those terms — players must know that *saying* it counts as *doing* it, or they
will do it to be sure it counted.

**5. Pre-notify every third party whose name, number, or brand appears in an inject.** The
executive being impersonated, the bank, the vendor whose caller ID you are matching. Two reasons:
they may otherwise trigger their own incident response against you, and impersonating a real
party without their knowledge is a decision they are entitled to make, not one you take on their
behalf. Where you cannot get that agreement, use a fictional counterparty — the exercise loses
nothing that matters. Note that spoofing caller ID is regulated in many jurisdictions and
unlawful in some; treat "match the vendor's number" as a control to clear, not a detail to
implement.

**Log the controls with the turns.** The director's name, the briefing time, the no-play list,
the ENDEX call, and every declared-not-executed action belong in the turn log
([Turn log template](#turn-log-template)). A debrief that cannot show the exercise was bounded
cannot distinguish a finding from an incident.

## Inject templates

Every template below is written *without* its EXERCISE marking so the shape is readable.
Nothing goes to a person that way — apply the marking from **Exercise control** above to each
one before it is delivered.

Pre-scripted injects are written before play, with delivery times; each states its
purpose. Format:

> **Inject #** · T+<minutes> · via <email/phone/alert/news> · to <role>
> **Content:** <the artifact players see — write it as the artifact, not a summary>
> **Purpose:** <the decision or gap this inject is meant to expose>
> **Expected branch:** <what blue plausibly does; what red does next in each branch>

Examples (sanitize before use; model on your real formats):
- Spoofed executive email: reply-chain quoting a real (sanitized) internal reference,
  new payee/endpoint details, "board meeting, cannot talk, confirm by 3 pm."
- Vendor alert: "Submission acknowledgment delayed. Do not resend." — arriving after
  blue has already discussed resending.
- News item: local outlet reports "service issues" at the organization — tests the
  communication plan, not the operational plan.
- Phone script for red: caller ID matches the vendor's number; caller asks blue to
  "verify" credentials.

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
  with our real counterparties and systems, in this timeframe?" Cite the process document
  or the person in the room who owns that step.
- Track state visibly: what is down, what is pending, what each side knows, the clock.
- When uncertain, ask the process owner present; when no one knows, log it — "nobody
  could say whether X" is a primary finding.
- Consequential outcomes (the fraud succeeded or not, the obligation was met or not,
  data was lost or not) are ruled by the human white cell only.

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
