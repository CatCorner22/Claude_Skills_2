# Finding schema

The canonical shape of every entry in `ui-ux-findings.json`, preserved verbatim from the
source specification (shown as a fully populated example).

- `severity` rates the magnitude of user impact (how badly the defect hurts task success,
  time-on-task, error rate, or access); `confidence` rates the strength of the evidence
  behind the finding — observed and reproduced scores high, inferred scores low — so a
  backlog can be ranked by impact and discounted by evidence independently.
- `status` tracks the finding's lifecycle in the remediation backlog (`open` when filed;
  update it as findings are fixed and re-verified across re-inspections).

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
