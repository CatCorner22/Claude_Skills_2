# Your flat-file feeds (sanitized template)

Fill in each recurring feed. Real export files live in `references/*.local.*` (git-ignored).

Per feed:
- **Name / source system:** <e.g. daily AP payment export from ERP>
- **Encoding / delimiter / quoting:** <e.g. cp1252, pipe, no quotes>
- **Schema:** <columns in order, with types; which are IDs (string!)>
- **Known quirks:** <footer total row, European decimals, mixed date formats...>
- **Validation contract:** <expected row-count range, control total source>
- **Cadence and delivery:** <when it arrives, where it lands>
- **Owner to call when the layout changes:** <team/contact>
