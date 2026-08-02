# Your git and review conventions (sanitized template)

Fill in your team's real workflow. Keep anything sensitive — private repo hosts, tokens, reviewer
names/emails, internal URLs — in `your-environment.private.md` (git-ignored). Commit only sanitized
structure here.

- **Default branch name:** <e.g. main | master | trunk>
- **Branch naming convention:** <e.g. `type/short-desc` — feat/ fix/ chore/; ticket prefix?>
- **Commit message style:** <e.g. Conventional Commits `type(scope): subject`, or plain imperative>
- **Update strategy:** <merge main into branch | rebase onto main | squash-merge PRs>
- **PR requirements:** <template location, required approvals, required status checks (CI, lint, tests)>
- **Who reviews what:** <CODEOWNERS? area experts? — describe structurally, no personal data here>
- **Protected-branch rules:** <e.g. no direct pushes to main, linear history required>
- **CI commands a reviewer expects to pass:** <e.g. `make test`, `npm run lint`>
- **Merge etiquette:** <who merges, when, and how the branch is cleaned up>
