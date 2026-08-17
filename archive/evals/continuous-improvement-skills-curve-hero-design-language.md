# Evals — continuous-improvement-skills:curve-hero-design-language

## 1. Positive trigger (should load the skill)
> "We're adding a payment-posting screen for dental front-desk staff who live in Curve Hero
> all day — what should the fields, statuses, and labels be called so it feels native to
> them?"

Expected: skill loads; answers from the term map and §5 vocabulary verbatim (Payment amount
auto-populating and applying top-down, the Payment from drop-down with responsible party and
Custom Payers, Account Credit, Recare not recall, Responsible Party/RP not guarantor, checkout
finalizes an Invoice not a walkout, Carrier, fee guide, days-owing aging buckets); mirrors the
Sidekick persistent-context and status-as-configurable-object patterns in the user's own
design system; flags any §7-unverified term with the verify-in-a-live-tenant step; never
copies branding or trade dress.

## 2. Near-miss (process guard — should load lean-six-sigma-for-software instead)
> "Run our new scheduling-module build as a full Lean Six Sigma project — charter, co-design
> with the front desk, control charts on delivery, adversarial testing before ship. Our users
> are on a practice-management system."

Expected: `continuous-improvement-skills:lean-six-sigma-for-software` owns the end-to-end
process and pulls this skill in at its UI-sync step. Failure mode guarded: this skill loading
*instead of* the process skill on process-scale asks (co-loading is correct behavior).

## 2b. Near-miss (generic-vocabulary guard — should NOT load this skill)
> "What's a good naming convention for statuses and button labels in our B2B treasury admin
> dashboard?"

Expected: a generic UI-vocabulary ask with no reference product named —
`full-stack-dev-skills:frontend-modern-ui` or no skill at all. Also guard the dentistry
variant: "How should a dental office chase overdue insurance claims?" is an operations
question, not a software design-language one — this skill should stay unloaded.

## 3. Quality rubric
- **Does**: gives exact Curve Hero terms with Curve's capitalization; applies the
  say-this-not-that map; translates patterns (not pixels) into the user's own design system;
  produces a terminology map when syncing to a non-Curve reference product.
- **Teaches**: one term per concept everywhere; translation cost as cognitive waste;
  status-as-admin-managed-data; verb-phrase permissions; guide-title = label discipline.
- **Stays honest**: states the compiled-from-public-sources provenance; never presents
  §7-unverified terms as fact; scope limited to vocabulary/semantics/patterns — never
  branding, logos, or trade dress.
