# Your CM environment (sanitized template)

Fill in structural facts only. Anything sensitive (account numbers, real statement data)
belongs in `your-environment.private.md`, which is git-ignored.

- **Instances / pods:** <e.g. DASH; TEST/PROD names> and current release
- **Bank accounts (structural names) and their assigned rule sets:** <account → rule set>
- **Statement formats by bank:** <bank → BAI2 / CAMT.053 / MT940>
- **Known profile-option settings:** <name → value, as configured>
- **Migration path:** <how config moves test → prod; export/import method>
- **Recurring failure history:** <what has broken before, and what fixed it>
- **Who runs what:** <who owns imports, AutoReconciliation schedule, period close>
