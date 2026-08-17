# Archived applications and domain tools

> **Status as of 2026-08-11: archived, not deleted.** These are standalone applications and
> tools that predate the library's re-aim to a career-portable, general-use skills
> marketplace. They lived at the repository root, where they made a skills marketplace read
> as a JavaScript app to anyone landing on the repo. Nothing in the active library references
> any of them. They are preserved here with full git history.

## What is here

### `dental-notes-standardizer-vocabulary-normalizer/`
A React (JSX) vocabulary normalizer for dental clinical notes — a ~19-rule engine that
rewrites note vocabulary toward a target practice-management system's terms. Has its own
`package.json` and a `docs/curve-hero-benchmark.md`. Formerly `tools/dental-notes-standardizer/`.

### The root Vite app — `index.html`, `src/`, `package.json`, `vite.config.ts`, `tsconfig.json`, `package-lock.json`
A **different, more complete** program from the one above, despite the similar name: a Vite +
React 19 "Dental Notes Standardizer" with a template picker, form engine, repeaters, and
conditional fields. It was the only reason `npm install` appeared anywhere in this repo.

The two dental apps were separate programs at separate paths, which made the duplication easy
to miss. They are co-located here so it is visible.

### `WORKFLOW_VALIDATION.md`
The validation record for the Vite app — Curve Hero workflow parity tables, form-component
mapping, and known gaps. Formerly `docs/WORKFLOW_VALIDATION.md`, where it sat beside the
library's generated catalogs and read as current library documentation.

### `CURVE_HERO_CLINICAL_NOTES.md`, `Curve-Hero-Clinical-Notes-Benchmark.md`
Benchmark and clinical-note reference material for the same dental work. Formerly at the
repository root.

### `fusioncash-architect/`
An Oracle-era Python tool (ingest → analyze → simulate → report) from the treasury period,
orphaned by the same re-aim that archived the nine finance/Oracle/treasury plugins. Formerly
`tools/fusioncash-architect/`.

## Also removed in this pass (deleted, not archived)

`GITHUB_SETUP.md` was deleted rather than archived: every fact in it was dead — it pointed at
a defunct repository URL, targeted a long-merged branch, and its own status line said the repo
was "not found." It had no preservation value. It did publish an `ssh-ed25519` deploy **public**
key and an expired GitHub device code; the public half discloses nothing on its own, but if
that deploy key still exists on the repository it is worth revoking in GitHub settings
independently of this cleanup.

## Restoring

```
git mv archive/apps/<thing> <destination>
```
The Vite app needs its five root files moved back together (`index.html`, `src/`,
`package.json`, `vite.config.ts`, `tsconfig.json`) plus `package-lock.json`, then
`npm install`. Neither dental app has been run or dependency-updated since archiving, so
treat their lockfiles as stale.
