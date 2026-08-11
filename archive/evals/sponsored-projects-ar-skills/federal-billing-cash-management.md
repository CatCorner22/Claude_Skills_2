# Evals — sponsored-projects-ar-skills:federal-billing-cash-management

## 1. Positive trigger (should load the skill)
> "Our federal AR aging looks weirdly empty but PPM shows $6M of costs on HHS awards — most of
> them are on letter of credit. What should we actually be measuring, and are we leaving cash
> on the table?"

Expected: skill loads; identifies LOC/PMS awards as draw-based (no invoices is normal);
replaces invoice aging with the expenditure-to-draw lag worksheet; computes undrawn balance
and its age; checks the overdraw side (§200.346); recommends draw cadence against policy and
the audit-defense package per draw.

## 2. Near-miss (should NOT load this skill)
> "Is entertainment allowable on a federal grant, and what's the current Single Audit
> threshold?"

Expected: the compliance frame — `sponsored-projects-ar-skills:uniform-guidance-federal-core`.
If this skill loads instead, sharpen the mechanics-vs-frame split.

## 3. Quality rubric
A good response:
- **Does the task:** segments awards by payment method, computes the lag correctly, reads
  reimbursement aging from the proper-request 30-day clock, ties cash application to the draw
  schedule.
- **Teaches:** the pull-system inversion (process risk over counterparty risk), the two-sided
  draw corridor, and why federal losses can't hit the award (§200.426) so prevention is the
  game.
- **Safe:** never applies invoice aging to draw-based awards, never suggests drawing ahead of
  expenditures, keeps award/draw specifics out of committed files.
