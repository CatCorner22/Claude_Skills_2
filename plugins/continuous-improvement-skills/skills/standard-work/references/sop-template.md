# Standard work / SOP: template, TWI breakdown, worked example

Method lineage: Toyota's standardized work — takt time, working sequence, and standard
in-process stock, described in Taiichi Ohno's *Toyota Production System* — combined with the
Training Within Industry (TWI) Job Instruction breakdown (important steps / key points /
reasons), a WWII-era US industrial training program later carried to Japan and absorbed into
Toyota's training practice. The worked example's numbers are illustrative, not research
findings.

## Contents
- [The three elements of standard work](#the-three-elements-of-standard-work)
- [The TWI Job Instruction breakdown](#the-twi-job-instruction-breakdown)
- [The fillable template](#the-fillable-template)
- [Worked example — the weekly status snapshot](#worked-example--the-weekly-status-snapshot)
- [Training to the standard: the four-step method](#training-to-the-standard-the-four-step-method)
- [Visual management options](#visual-management-options)
- [Review cadence and the improvement path](#review-cadence-and-the-improvement-path)
- [Canon and terminology notes](#canon-and-terminology-notes)

## The three elements of standard work

Toyota's standardized work fixes three things; everything else in the document supports them.

1. **Takt time** — the pace demand sets: available working time ÷ demand. A demand-paced
   task must fit its takt. Office work is often volume-paced rather than strictly
   takt-paced; record the honest equivalent ("about 30 of these per week, so roughly one
   per working hour") so the timing context isn't lost.
2. **Working sequence** — the steps in the order they are actually performed. One sequence,
   not a menu of variants.
3. **Standard in-process stock (standard WIP)** — the minimum on hand for the cycle to run:
   files, data, approvals, access, open tickets. If starting without one of these causes
   rework, it belongs on the list.

## The TWI Job Instruction breakdown

For each step, three columns — this is what makes a standard teachable:

- **Important step (what):** the action, in sequence. A logical segment of the operation
  that advances the work.
- **Key point (how it comes out right):** the detail that makes or breaks the step — a
  check, a setting, an order, a "hard to describe but easy to show" knack. TWI's selection
  tests: would missing it injure the worker, ruin the work, or make the job harder?
- **Reason (why):** what goes wrong without the key point. The reason is the anti-rot agent:
  people keep steps they understand and silently drop steps they don't; and when the reason
  no longer holds, the step can be retired deliberately instead of cargo-culted forever.

## The fillable template

Keep the whole standard to a page or two; push detail into linked visuals.

### Header
- **Task / standard name:** <…>
- **Trigger (starts when):** <event> · **Ends when:** <done condition>
- **Owner / author:** <…> · **Version / date:** <v_ / yyyy-mm-dd> · **Next review:** <date>
- **Takt or volume context:** <available time ÷ demand = takt, if demand-paced; else typical volume>
- **Standard inputs / WIP to start:** <files, approvals, data, access that must be on hand>

### Step table
| # | Step (what) | Cycle time | Key point (the detail that makes it right) | Reason (why it matters) |
|---|-------------|-----------|--------------------------------------------|-------------------------|
| 1 | <action>    | <min>     | <quality/accuracy/ease point>              | <what goes wrong without it> |
| 2 | <action>    | <min>     | <…>                                        | <…> |
| 3 | <action>    | <min>     | <…>                                        | <…> |

### Footer
- **Visual management:** <the one-page visual instruction, controls, and flags — see below>
- **Training record:** <who trained whom, verification date — see the four-step method>
- **Deviation / idea path:** <how an exception or a better idea gets surfaced, to whom>

## Worked example — the weekly status snapshot

Domain-neutral on purpose: the "snapshot" below could be an analyst's weekly metrics
summary, an attorney's matter-status report, an ops manager's operations rollup, or a
developer's release notes. **All times are illustrative.**

- **Task:** Produce and send the weekly status snapshot.
- **Trigger:** Friday 09:00 · **Ends when:** snapshot sent to the distribution list and
  filed in the archive folder.
- **Volume context:** 1 per week; must be out before the 13:00 review meeting, so the
  ~75-minute cycle has a hard window.
- **Standard inputs:** source-system export access; last week's snapshot; the open-items
  list; the distribution list (owned, versioned — not retyped from memory).

| # | Step | CT | Key point | Reason |
|---|------|----|-----------|--------|
| 1 | Pull the source export | 10 min | Pull *after* the overnight refresh completes; check the run-date stamp on the export | A pre-refresh pull silently reports last week's numbers as this week's |
| 2 | Update the summary table | 15 min | Paste values only, into the labeled input range | Pasting formats breaks the sheet's formulas; edits outside the range aren't picked up |
| 3 | Reconcile to last week | 10 min | Explain every change larger than the stated threshold before writing commentary | Unexplained swings are the #1 reader question; catching an error here costs minutes, downstream it costs credibility |
| 4 | Write the three-line commentary | 15 min | Lead with what changed and why, not what the report is | Readers act on the delta; boilerplate trains them to stop reading |
| 5 | Peer glance | 10 min | A second person checks totals and the change-explanations, not grammar | The author can no longer see their own numbers fresh |
| 6 | Send and file | 5 min | Use the versioned distribution list; file with the yyyy-mm-dd name pattern | Ad-hoc recipient lists miss stakeholders; consistent names make the archive searchable |

- **Visual management:** a six-box done/not-done strip at the top of the working file, one
  box per step; the send step is blocked visually until the peer-glance box is checked.
- **Training verified:** new owner produced two consecutive snapshots solo, explaining each
  key point while working; verified by the outgoing owner.
- **Deviation path:** any week a step can't be followed as written, note it in the
  exceptions log; three notes on the same step trigger a review of that step.

Note what the format did: the six reasons carry the tribal knowledge (refresh timing, the
paste trap, the threshold habit) that previously lived in one person's head.

## Training to the standard: the four-step method

TWI Job Instruction's four steps, still the cleanest training loop for standard work:

1. **Prepare the learner.** Put them at ease, find out what they already know, state why
   the task matters and where it fits.
2. **Present the operation.** Do the task while naming each step, then again stressing key
   points, then again giving reasons. One idea at a time.
3. **Try-out performance.** The learner does the task while *explaining* steps, key points,
   and reasons back. Correct errors as they happen. Repeat until the explanation is as
   solid as the execution.
4. **Follow up.** Leave them to work with a named person to call on; check in at a
   declining frequency; taper off as competence shows.

The verification bar is both halves of step 3: can **do** the task unaided, can **explain**
the key points and reasons. Either alone fails — doing without understanding drops steps
under pressure; explaining without doing is theory.

## Visual management options

The goal: the correct state is obvious, and a deviation is visible at a glance, to anyone.

- One-page visual work instruction with screenshots/photos of the key points.
- Checklists for the steps people demonstrably skip (design them properly —
  `safety-and-reliability-skills:checklist-design` — a checklist is killer items, not the
  whole SOP restated).
- Done/not-done boards or status strips; color-coding; exception flags; tolerance markers
  ("green between these values, investigate outside them").
- Sequence made physical or digital-structural: numbered folders, a template whose sections
  are the steps, a form that won't submit with a blank required field.

## Review cadence and the improvement path

- **Next-review date and owner live in the header.** A standard without a review date is
  already going stale; a stale binder misleads worse than no binder.
- **Every accepted improvement updates the standard and bumps the version.** The standard is
  the *current best-known* method — when a kaizen finds better
  (`continuous-improvement-skills:kaizen-and-codesign`), the new method becomes the
  standard, and the old version number is the audit trail of learning.
- **Deviations are data.** An exception log that people actually use tells you which steps
  fight reality; hiding deviations hides the next improvement.

## Canon and terminology notes

- **"Standardized work" (Toyota)** is specifically the takt/sequence/standard-WIP trio for
  cyclical work. Office SOPs borrow the spirit and the TWI breakdown even where takt is
  approximated by volume — say which you're writing, so precision claims stay honest.
- **TWI's J-programs** (Job Instruction, Job Methods, Job Relations) were developed for US
  wartime industry and later introduced to Japan during the postwar rebuilding, where they
  fed into what became famous as lean training practice. The steps/key-points/reasons format
  is Job Instruction's breakdown sheet, essentially unchanged.
- **"Without a standard there can be no improvement"** is widely attributed to Taiichi Ohno,
  but a primary source is elusive. Use the logic (a standard is the baseline that makes
  improvement measurable), not the attribution.
