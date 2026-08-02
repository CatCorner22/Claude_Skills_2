# Dental Notes Standardizer

An auxiliary web app for standardizing dental clinical notes, benchmarked against **Curve Hero** templated notes workflows.

## Features

- **Visit-type-first navigation** with color-coded templates (Fillings, Crown, Hygiene, Lab Case)
- **Favorites and recently used** templates (localStorage)
- **Reusable blocks**: Anesthesia, Provider(s), Patient Behavior
- **Form engine** supporting dropdowns, multi-select, yes/no, clinical scales, site fields, repeaters, and conditional visibility
- **Required field validation** before note generation
- **Standardized note output** with copy-to-clipboard for EHR paste

## Quick Start

```bash
npm install
npm run dev
```

Open http://localhost:5173

## Build

```bash
npm run build
npm run preview
```

## Architecture

- `src/types/form.ts` — Field and template type definitions
- `src/data/reusableBlocks.ts` — Cross-template reusable question blocks
- `src/data/templates/` — Procedure-specific template schemas
- `src/components/FormEngine/` — Dynamic form renderer and validation
- `src/components/TemplatePicker.tsx` — Visit-type navigation with favorites
- `docs/WORKFLOW_VALIDATION.md` — Curve Hero workflow parity checklist

## Benchmark Reference

Based on Curve Dental public documentation for Curve Forms note templates, charting workflows, and the color-coded appointment-type system.
