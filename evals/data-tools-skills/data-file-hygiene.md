# Evals — data-tools-skills:data-file-hygiene

## 1. Positive trigger (should load the skill)
> "My analysis folder is a mess of final_v2_FINAL(3).xlsx files, and I need to share an example
> workbook externally but it's built from real customer account data. Sort me out."

Expected: skill loads; sets up dated immutable naming and raw/processed/output flow; classifies
the workbook as sensitive; sanitizes structurally (consistent shape-preserving fakes, rebuilt
workbook — not hidden columns) with the Excel scrub checklist (hidden sheets, pivot caches,
metadata).

## 2. Near-miss (should NOT load this skill)
> "This dataset has duplicates and missing values — clean it up before I run the analysis."

Expected: content cleaning — `data-analytics-bi-skills:data-cleaning`. If this skill loads,
sharpen the files/organization/sharing framing.

## 3. Quality rubric
A good response:
- **Does the task:** delivers a concrete naming convention, folder skeleton with the
  regenerate-from-raw invariant, and a properly sanitized shareable file.
- **Teaches:** files-carry-their-provenance as the unifying idea; why hand-editing processed
  files breaks reproducibility; how leaks actually happen (pivot caches, hidden tabs, "quick
  examples").
- **Safe:** treats git history as forever; sanitization is structural rebuild, not cosmetic
  hiding; aligns with the repo's `*.private.md` / `*.local.*` guardrails.
