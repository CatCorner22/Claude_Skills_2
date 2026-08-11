# Your git and review conventions (sanitized template)

Wire in your current team here — this skill is employer-neutral and re-points whenever you
change roles: fill this in per team, and the generic method above becomes *your* workflow.
Keep anything sensitive — private repo hosts, tokens, reviewer names/emails, internal URLs —
in `your-environment.private.md` (git-ignored). Commit only sanitized structure here.

- **Default branch name:** <e.g. main | master | trunk>
- **Branch naming convention:** <e.g. `type/short-desc` — feat/ fix/ chore/; ticket prefix?>
- **Commit message style:** <e.g. Conventional Commits `type(scope): subject`, or plain imperative>
- **Update strategy:** <merge main into branch | rebase onto main | squash-merge PRs>
- **Shared-branch rules:** <any branch other agents/teammates also push to, and the
  fetch-inspect-then-push discipline it requires>
- **PR requirements:** <template location, required approvals, required status checks (CI, lint, tests)>
- **Who reviews what:** <CODEOWNERS? area experts? — describe structurally, no personal data here>
- **Protected-branch rules:** <e.g. no direct pushes to main, linear history required>
- **CI commands a reviewer expects to pass:** <e.g. `make test`, `npm run lint`>
- **Merge etiquette:** <who merges, when, and how the branch is cleaned up>
- **Severity-label convention:** <e.g. blocking / should / nit / question — or your team's prefixes>

Once filled in, these conventions are themselves a rule set: run
`coding-agent-skills:rule-stress-testing` over them to find the conflicts and loopholes
before they fire mid-incident.
