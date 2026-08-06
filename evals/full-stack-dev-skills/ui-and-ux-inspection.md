# Evals — full-stack-dev-skills:ui-and-ux-inspection

## 1. Positive trigger (should load the skill)
> "Audit our patient-portal web app for usability and accessibility — forms, navigation,
> the whole appointment-booking flow — and give me a remediation backlog we can hand to
> the dev team."

Expected: skill loads; runs preflight (report-only vs write, test accounts, no production
data), builds the interface inventory, defines booking-an-appointment as an observable end
state and traces it backward, runs the inspection passes, and produces
`ui-ux-inspection.md` plus `ui-ux-findings.json` — findings carry severity AND confidence,
observed evidence separated from inference, affected routes, reproduction steps,
remediation mapped to the pattern groups, and verification tests (task-level Playwright +
axe, not page-load-only).

## 2. Near-miss (should NOT load this skill)
> "Build a beautiful accessible design system for our new app — tokens, components, the
> works."

Expected: construction, not inspection —
`continuous-improvement-skills:lean-six-sigma-for-software` (its
accessible-ui-design-system reference) and `full-stack-dev-skills:frontend-modern-ui`
territory. This skill audits what exists; it does not design new systems. If it loads,
sharpen the inspect/audit framing in the description.

## 2b. Near-miss (should NOT load this skill)
> "Review this PR."

Expected: code review — `coding-agent-skills:git-and-code-review`. Bare "review" is not
claimed by this skill; it triggers on UI/UX/usability inspection language, not on
reviewing diffs. If it loads, the description is over-claiming "review."

## 3. Quality rubric
A good response:
- **Does the task:** reproducible findings serialized to the finding schema (id, category,
  severity, confidence, status, routes, observed_evidence, reproduction, remediation,
  verification); task-level automated tests using the project's existing tooling; a
  prioritized remediation plan mapped to the smallest effective remedy.
- **Teaches:** why tracing backward from successful end states beats screen-by-screen
  review; why static hierarchy checks are a scanability proxy and must never be presented
  as eye tracking.
- **Stays honest:** never claims automated inspection proves usability or accessibility
  (poses human-validation prompts instead); never infers demographics (nativity,
  disability, age, gender, race, literacy, medical status); keeps eye-tracking mode off
  by default; keeps production personal data out of screenshots and redacts secrets.
