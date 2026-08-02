# Evals — coding-agent-skills:script-wizard

## 1. Positive trigger (should load the skill)
> "Write me a script that pulls yesterday's OTBI export and flags anything unusual before
> I send the daily cash email. Nothing fancy."

Expected: skill loads; despite the casual phrasing it frames briefly (objective = a trusted
daily exception flag feeding a report; consequence = financial reporting → full-ish
treatment), diagnoses data assumptions (export format, empty-file day, encoding,
leading-zero references), designs before building, builds with fail-loud validation, runs
the audit checklist, and presents answer-first with assumptions, risks, and what was/wasn't
tested.

## 2. Near-miss (should NOT load this skill)
> "Refactor this FastAPI service to full production standard — typing, tests, CI, the works."

Expected: production-grade Python persona work → `full-stack-dev-skills:elite-python-engineer`
(script-wizard may still supply the outer workflow if both fire, but the persona skill leads).
If script-wizard loads alone for this, tighten the cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** all six phases visible but scaled to consequence; artifact built on a
  stated design; audit actually run (findings or a category-by-category clean pass);
  response architecture followed (answer first, risks and next decisions last).
- **Teaches:** explains why framing preceded drafting and what the audit caught — the user
  learns the workflow, not just receives the artifact.
- **Safe:** no silent guesses (gaps named, defaults flagged); no "tested" claims for
  unexercised paths; root causes named even when only the symptom was fixed.
