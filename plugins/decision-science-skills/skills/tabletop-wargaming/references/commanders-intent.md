# Commander's intent (format, test, and briefing-an-agent application)

Commander's intent is the part of an order written so that people two levels down can
act without further orders when the plan breaks. It is not a summary of the plan; it is
what survives the plan's contact with reality.

## The format: purpose / key tasks / end state

- **Purpose** — *why* the operation exists, one sentence, stated so it remains true even
  if every specific step changes. "Ensure employees are paid on time and no fraudulent
  payment releases" — not "transmit the payroll file by 10:00."
- **Key tasks** — the few things that must happen (or must not), in any workable order,
  for the purpose to hold. Conditions, not steps: "payroll settles by end of day,"
  "no payment released without out-of-band verification," "the bank is informed before
  we retransmit anything."
- **End state** — what "done" looks like for people, systems, and information when the
  dust settles: "payroll settled once and only once; fraud attempt documented and
  reported; contingency channel exercised and re-secured."

Keep the whole intent short enough to recall under stress — a few sentences. If it needs
a page, it is a plan wearing intent's clothes.

## The violate-the-plan test

Ask: **could someone achieve the intent while violating the plan's specifics?**

- If yes — the intent is real. A blue player who abandons the scripted transmission
  channel, phones the bank, and settles payroll through the portal has *violated the
  plan* and *achieved the intent*. In the exercise, white cell should score that as
  success.
- If no — you have written a task list, and people will freeze (or comply into failure)
  the moment step 3 becomes impossible. Rewrite: strip steps out of the intent and move
  them back into the plan where they belong.

The test doubles as an exercise instrument: when a tabletop turn breaks the plan, watch
whether players reach for the intent or for the broken step. Players quoting step
numbers at a dead system is a finding about the intent, not about the players.

## Writing it for an exercise (white/blue setup)

1. Draft purpose / key tasks / end state with the process owner before play.
2. Run the violate-the-plan test; rewrite until it passes.
3. Brief blue on the intent AND hand them the plan. Red never sees the intent draft
   process — red targets the plan's specifics, which is exactly the point.
4. In the debrief, compare decisions against the intent, not just the plan: a plan
   deviation that served the intent is a sustain item, not a violation.

## The briefing-an-agent application

The same structure is the right way to brief an autonomous agent (or a colleague, or a
contractor) on a task where you will not be available for follow-up questions:

- **Purpose**: what the work is *for* — so the agent can resolve ambiguity in your
  favor instead of guessing ("this report exists so the treasurer can decide X").
- **Key tasks / constraints**: the must-happen and must-not-happen conditions — data
  that may not leave the machine, formats that must round-trip, approvals that gate
  irreversible steps.
- **End state**: what a finished, verifiable deliverable looks like — including how the
  agent should prove it ("all reconciliation IDs preserved as text; validator passes").

Then apply the same test: if the agent could satisfy your instructions while defeating
your purpose, the briefing is a task list, and an agent — like a stressed blue player —
will follow it off the cliff. Intent is what makes delegation safe when the plan meets
the real world.
