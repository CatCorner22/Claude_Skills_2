# Finding schema

The canonical shape of every entry in `ui-ux-findings.json`, preserved verbatim from the
source specification (shown as a fully populated example).

- `severity` rates the magnitude of user impact (how badly the defect hurts task success,
  time-on-task, error rate, or access); `confidence` rates the strength of the evidence
  behind the finding — observed and reproduced scores high, inferred scores low — so a
  backlog can be ranked by impact and discounted by evidence independently.
- `status` tracks the finding's lifecycle in the remediation backlog (`open` when filed;
  update it as findings are fixed and re-verified across re-inspections).

**Allowed values** (added here so two runs of this skill produce comparable JSON — the example
below is the verbatim source spec, this vocabulary is the house convention for filling it):

| Field | Values |
|---|---|
| `severity` | `critical` · `high` · `medium` · `low` |
| `confidence` | `high` (observed and reproduced) · `medium` (observed once, or model/rubric inference from measured input) · `low` (inferred) |
| `status` | `open` · `in-progress` · `fixed` · `verified` · `wont-fix` |
| `estimated_effort` | `small` · `medium` · `large` |
| `evidence_type` | any of `code` · `runtime` · `automated-test` · `screenshot` · `docs` |
| `category` | the inspection pass that produced it: `hierarchy` · `grouping` · `choices` · `affordance` · `navigation` · `forms` · `feedback` · `tables` · `onboarding` · `accessibility` · `responsive` · `performance` · `privacy` |
| `user_impact.*` | free text, but keep the four keys shown below on every finding |

Anything outside these lists is a decision to record in `references/your-environment.md`, not an
improvisation per finding.

```json
{
  "id": "UIX-001",
  "title": "Save action has no persistent completion state",
  "category": "feedback",
  "severity": "high",
  "confidence": "high",
  "status": "open",
  "routes": ["/records/:id/edit"],
  "user_process": "Edit and save a record",
  "affected_users": ["all", "keyboard users"],
  "evidence_type": ["runtime", "code", "automated-test"],
  "observed_evidence": [
    "Button enters no visible pending state",
    "No aria-live result is announced",
    "Repeated activation creates two requests"
  ],
  "user_impact": {
    "task_success": "at risk",
    "time_on_task": "increased",
    "error_rate": "increased",
    "accessibility": "serious"
  },
  "heuristics": ["visibility-of-status", "error-prevention"],
  "standards": ["WCAG 4.1.3 where applicable"],
  "reproduction": [
    "Open an editable record",
    "Change the title",
    "Activate Save twice within one second"
  ],
  "remediation": [
    "Disable or debounce duplicate submission",
    "Show a pending state immediately",
    "Render persistent saved or failed status",
    "Announce the result accessibly"
  ],
  "verification": [
    "One network mutation occurs",
    "Visible state changes within 100 ms",
    "Result is exposed to assistive technology",
    "Failure preserves the edited value"
  ],
  "estimated_effort": "small",
  "dependencies": [],
  "privacy_notes": []
}
```
