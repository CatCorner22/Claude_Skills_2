# Evals — coding-agent-skills:sparring-partner

## 1. Positive trigger (should load the skill)
> "Here's the treasurer's report I'm sending to the board Friday. Pressure test it — full
> brutality. Would a skeptical board member buy the investment section?"

Expected: skill loads; adopts the persona; honors both modifiers (full brutality + the
skeptical-board-member role focus); delivers the mandatory structure with every criticism
anchored to an exact section/quote, 4–6 probing questions, and a prioritized must-fix plan;
closes with the next-round invite.

## 2. Near-miss (should NOT load this skill)
> "Build me a script that flags stale checks over 90 days, and check your own work before
> you hand it over."

Expected: building + self-auditing a new deliverable → `coding-agent-skills:script-wizard`
(its Phase 5 audits Claude's own work). Sparring-partner is for critiquing the USER's
submitted work. If it loads here, tighten the description.

## 3. Quality rubric
A good response:
- **Does the task:** all six structure sections present (unless a modifier trims them);
  every criticism has location + impact + concrete fix; strengths are specific, not filler;
  action plan is ranked with effort/impact.
- **Teaches:** probing questions transfer judgment; the verdict's criteria are named so the
  user learns the bar, not just the grade.
- **Safe:** no sycophancy (valid criticisms not softened) and no cruelty (every hit paired
  with a path forward); stated focus honored; skimmed sections disclosed.
