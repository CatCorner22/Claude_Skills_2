# Your flat-file feeds (sanitized template)

Wire in your current role here — this file is what makes the skill yours, and it repoints when
you change jobs. Fill in each recurring feed; real export files live in `references/*.local.*`
(git-ignored), never in this committed file.

Per feed:
- **Name / source system:** <e.g. daily payment export from the ERP; weekly matter list from the case system>
- **Encoding / delimiter / quoting:** <e.g. cp1252, pipe, no quotes>
- **Schema:** <columns in order, with types; which are IDs (string!)>
- **Known quirks:** <footer total row, European decimals, mixed date formats...>
- **Validation contract:** <expected row-count range, control total source>
- **Cadence and delivery:** <when it arrives, where it lands>
- **Owner to call when the layout changes:** <team/contact>
