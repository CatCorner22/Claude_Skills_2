# Your environment (sanitized template)

Wire in your current systems here so a contact-trace starts from your real terrain.
Keep this file **structural** — patterns and locations, not secrets. Anything sensitive
(real repo names tied to an employer, live vulnerability details, client specifics) goes
in `your-environment.private.md` — that suffix is git-ignored and never committed.

## Sweep scope (what "everywhere" means here)
- Repositories a sweep must cover: <main repo(s), sibling services, shared libraries>
- Cross-repo copies: <other codebases scaffolded from the same origins>
- Excluded from sweeps and why: <vendored code, generated artifacts — state the reason>

## Patient-zero habitats (where origins usually live)
- Templates / scaffolds / generators: <locations>
- Snippet sources people copy from: <internal wiki, example repos, pinned Q&A links>
- Known prolific-source histories: <past outbreaks' patient zeros, so new digs check them first>

## Quarantine infrastructure
- How a lint/CI rule is added in this stack: <linter, config location, CI gate>
- Where rule failure messages should point: <outbreak-report location/ID convention>
- Who approves a new blocking rule: <role>

## Outbreak reports
- Filed at: <path or system>
- ID convention: <e.g., OB-<year>-<n>>
- Open accepted-with-reason rows and their revisit dates: <tracker link>
