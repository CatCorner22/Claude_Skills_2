# Your data-cleaning environment (sanitized template)

Wire in your current role here — the recipes are deliberately domain-neutral and attach to
whatever extracts you clean wherever you work next: an analyst's revenue pull, an attorney's
matter export, an ops manager's ticket dump, a developer's event log. Fill this in with your
real setup; if any value is sensitive (real category mappings, client keys, sample rows),
keep it in `your-environment.private.md` instead — that suffix is git-ignored. Commit only
sanitized, structural examples.

- **Common source formats & quirks:** <CSV export encoding, Excel merged headers, API paging, etc.>
- **Tools you clean with:** <SQL, pandas, Power Query, dbt, Alteryx>
- **Key definitions per table:** <table → unique key columns>
- **Canonical category lookups:** <where the state / product / entity mapping tables live>
- **Standard missing-value policy:** <per-column defaults; when to flag vs. drop vs. impute>
- **Dedup survivor rule:** <e.g. keep latest updated_at; tie-break by source priority>
- **Validation / control totals:** <which sums or counts must tie, and to what source>
- **Non-destructive workflow:** <where raw lands, where clean lands, how re-runs work — see
  data-tools-skills:data-file-hygiene for the folder conventions>
