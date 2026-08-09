# Your environment (fill in)

Real production volumes that are sensitive stay in `your-environment.private.md`
(git-ignored); sanitized magnitudes may live here.

## Standing payloads (measured, with source)
- Bank feed volumes (day-1 / peak / growth / largest historical file):
- Statement-line retention horizon (what the staging schema truly carries):
- Patient/appointment volumes for the dental app (Monday peak, biggest single record):

## House safety factors
- Well-measured, cheap-to-grow loads: <e.g. 1.5×>
- Estimated or one-way-door loads: <e.g. 3×>
- Factor floor that triggers a stop:

## Known one-way doors
- Schema/partition keys, ID formats, storage layouts that are retrofit-priced to change:

## Manifest registry
- Where signed Load Manifests live, and the re-review calendar:
