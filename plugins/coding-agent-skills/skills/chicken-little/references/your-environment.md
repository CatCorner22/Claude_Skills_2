# Your environment (fill in)

Add the system-specific facts that make Chicken Little's answers exact rather than generic.
Keep anything sensitive in `your-environment.private.md` (git-ignored). Never commit
credentials, account numbers, or client data.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it. Copy it into your own
project — `.claude/skills-env/chicken-little.private.md` works well — and point the skill at that copy.

## The systems in scope
- Primary system(s) of record, and what each one owns:
- Environments (prod / test) and how you tell them apart in output:
- Org, entity, or tenant structure and its key names:

## The record model you work in
- The main transactional objects and the level the decisive status lives at (header vs line):
- Segmentation or coding structure, in order, with labels:
- Naming conventions for identifiers you will see in extracts:

## Workflow and exceptions
- Approval workflow configuration (stages, escalation):
- Hold / exception policies and who clears which:

## Reporting access
- The reports or subject areas you actually use:
- Extract cadence and format:

## Escalation thresholds (what earns an andon pull)
- Cycle-time or aging thresholds that trigger action:
- Statuses that page a human vs. wait for the trend:
