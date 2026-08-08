# Your environment (sanitized template)

Fill this in with your real conventions so the matrix starts from your standing rival sets instead
of a blank page. Keep it **structural**: no account numbers, no real amounts, no customer or
employee names. Anything sensitive goes in `your-environment.private.md` — that suffix is
git-ignored and never committed.

## Standing rival sets (per recurring problem)
For each problem you diagnose repeatedly, list the default hypothesis set to start the matrix from.

- **Problem:** <e.g., unexplained break on the operating account>
  - Rivals: <timing difference | duplicate statement line | matching-rule gap | bank error |
    keying error | deception>
  - Always-include deception hypothesis? <yes/no, and why>
- **Problem:** <e.g., auto-match rate drop after a statement-format change>
  - Rivals: <parse-rule regression | new bank reference format | tolerance too tight | volume mix shift>

## Evidence sources and how primary they are
Rank each source so the sensitivity protocol knows what "most primary" means for you.

- <raw statement file (BAI2/camt) — primary> → <bank portal view — primary-adjacent> →
  <system match log — derived> → <reconciliation report — derived twice>
- <subledger reports, journal exports, access/audit logs, approval trails>

## Credibility conventions
- Sources treated as reliable without re-verification: <...>
- Sources that must always be re-pulled when load-bearing: <...>
- Known innocent-error patterns in your data: <e.g., date cutoffs on the portal view,
  leading-zero loss in re-saved exports>

## Deception / escalation policy
- Who is notified when a deception hypothesis survives to the final ranking: <role, channel>
- What is never closed by the analyst alone: <...>
