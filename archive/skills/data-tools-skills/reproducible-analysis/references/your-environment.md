# Your environment (sanitized template)

Wire in your real reproducibility surface here so audits start from your terrain, not
generic advice. Keep this file **structural** — analyses, locations, and roles, never
real data, client or matter names, or credentials. Real specifics go in
`your-environment.private.md` — that suffix is git-ignored and never committed.

## Recurring analyses and their headline numbers
- <analysis 1 — e.g., quarterly capacity study; headline: utilization %; owner role>
- <analysis 2 — e.g., monthly variance pack; headline: net variance; owner role>

## Stack per analysis
- <analysis 1>: <tools/versions — spreadsheet, notebook, SQL engine, BI tool>
- <analysis 2>: <…>

## Lineage layout
- Raw lands at: <location; how receipt is recorded (checksum, dated folder)>
- Derived/output live at: <location>
- One-command entry point per analysis: <script/makefile/master query per analysis>
- Known unscriptable steps: <manual step, exact parameters, expected output>

## Seeds and environment records
- Where seeds are logged: <in-output footer, run log, …>
- Where the environment manifest lives: <lockfile/requirements/container spec path>

## Verification ritual
- Fresh-clone rerun: <who runs it, on what machine/profile, on what cadence>
- Second keeper roster: <role(s) who independently re-derive each headline number>
- Verification log filed at: <path or system>
