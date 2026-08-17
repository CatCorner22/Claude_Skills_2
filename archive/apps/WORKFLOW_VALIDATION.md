# Workflow Validation — Curve Hero Benchmark

This document maps the Dental Notes Standardizer implementation to documented Curve Hero workflows. Validation is based on public Curve Dental Zendesk documentation (no live Curve Hero UI access).

## Validated Workflow Parity

| Curve Hero Workflow | Our Implementation | Status |
|---------------------|-------------------|--------|
| Visit-type-first navigation via appointment tags | Template picker keyed by visit type with color badges | Implemented |
| Color-coded templates matching appointment types | Each template has a `color` property displayed on cards and form header | Implemented |
| Favorites list for common templates | localStorage-backed favorites with star toggle | Implemented |
| Recently used templates | localStorage-backed recent list (last 5) | Implemented |
| Reusable Questions (Anesthesia, Provider, Behavior) | `reusableBlocks.ts` composed into templates via `reusableBlockIds` | Implemented |
| Required field enforcement (red asterisk, block save) | Required fields marked `*`; validation blocks Generate Note | Implemented |
| Conditional field visibility | `conditional` rules on fields; hidden when trigger not met | Implemented |
| Repeater for multi-tooth entries | Repeater component on Fillings and Lab Case templates | Implemented |
| Additional notes escape hatch | Text box on every procedure template | Implemented |
| Structured output for EHR paste | Generate Note → copy to clipboard | Implemented |

## Procedure Template Schema Parity (Section 9)

| Template | Curve Hero Documented Fields | Implemented |
|----------|------------------------------|-------------|
| Fillings | Repeater (site/surface/material), Anesthesia, Provider, Behavior, Additional notes | Yes |
| Crowns | Site(s), Build up, Material, Radiographs, Replacement, Diagnosis, conditional date, cross-blocks | Yes |
| Hygiene | Performed, Home care scale, Radiographs, conditional sites, Calculus, Bleeding, Additional notes | Yes |
| Lab Case | Lab dropdown, conditional Other, Repeater (site/shade), Material, Due date, Provider | Yes |

## Form Component Toolbox Parity (Section 7)

| Curve Forms Component | Implementation |
|----------------------|----------------|
| Section Header | `section-header` |
| Short Answer | `short-answer` |
| Text box | `text-box` |
| Dropdown | `dropdown` |
| Select Boxes | `select-boxes` |
| Checkbox | `checkbox` |
| Yes, No | `yes-no` |
| Material | `material` |
| Radiographs | `radiographs` |
| Diagnosis Reason | `diagnosis-reason` |
| Excellent/Good/Fair/Poor | `scale-4` |
| Mild/Moderate/Severe | `scale-3` |
| Generalized/Localized | `distribution` |
| Repeater | `repeater` |
| Site | `site` |
| Conditional logic | `conditional` on any field |

## Known Gaps vs Curve Hero (Intentional or Out of Scope)

- No integration with Curve Hero API or charting right-click context
- No QuickText legacy support
- No AI transcript pre-fill (Curve Care+)
- Anesthesia defaults match Curve docs (agent names only); no technique/carpules/aspiration fields
- Provider names are static placeholders, not synced from practice staff
- Template builder/admin UI separate from clinical fill (Curve Forms vs Charting) — our app focuses on clinical fill only

## Sources

See plan Section 14 for primary Curve Dental documentation links.
