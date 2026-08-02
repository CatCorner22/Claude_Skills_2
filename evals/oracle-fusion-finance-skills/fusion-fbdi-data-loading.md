# Evals — oracle-fusion-finance-skills:fusion-fbdi-data-loading

## 1. Positive trigger (should load the skill)
> "My journal import FBDI load says the interface loaded fine but no journals were created —
> the execution report shows EF03 errors on a bunch of rows. What do I do?"

Expected: skill loads; explains the file → interface table → record pipeline and why "loaded
but not imported" isn't a contradiction; reads EF-family as flexfield/combination errors; walks
the correction loop (fix file or Correct Import Errors ADFdi; delete failed interface rows
before re-loading); verifies counts and totals afterward.

## 2. Near-miss (should NOT load this skill)
> "I need to book a five-line reclass journal in Fusion — walk me through entering it."

Expected: manual/ADFdi entry — `oracle-fusion-finance-skills:fusion-gl-and-journals` should
handle it. If this skill loads, sharpen the bulk-load framing in the description.

## 3. Quality rubric
A good response:
- **Does the task:** identifies the failing validation per the execution report, fixes it, and
  re-runs both stages (loader + module import) to completion with reconciled row counts.
- **Teaches:** the staged pipeline, why template structure and lookup codes are inviolable, and
  why the Generate CSV macro (not hand-saved CSVs) is the contract with the loader.
- **Safe:** warns to purge failed interface rows before re-loading (duplicate risk) and never
  suggests editing template structure to "make it fit."
