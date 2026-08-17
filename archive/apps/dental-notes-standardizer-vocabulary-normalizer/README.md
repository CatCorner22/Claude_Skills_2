# Dental Notes Standardizer — Curve Hero Edition

A Vite + React app that normalizes dental clinical notes to
[Curve Hero](https://www.curvedental.com/)'s canonical vocabulary in real time.

## Features

- **Live two-panel editor** — raw input left, standardized output right
- **Change log** — every substitution listed with original term, Curve Hero term, and rationale
- **One-click copy** — copy the standardized text to clipboard
- **19-rule normalization engine** covering all known Curve Hero vocabulary differences
- **Zero backend** — runs entirely in the browser; no patient data leaves the machine

## Curve Hero Terms Covered

| Legacy / non-standard | → | Curve Hero |
|----------------------|---|------------|
| recall, hygiene recall | → | **Recare** |
| guarantor, account holder | → | **Responsible Party (RP)** |
| walkout, walkout statement | → | **Invoice** |
| insurance company, payer, insurer | → | **Carrier** |
| treatment room, op | → | **Operatory** |
| fee schedule, UCR fee | → | **Fee Guide** |
| days outstanding, aging bucket | → | **Days Owing** |

Full vocabulary map and benchmark methodology: [`docs/curve-hero-benchmark.md`](docs/curve-hero-benchmark.md)

## Quick Start

```bash
npm install
npm run dev        # → http://localhost:5173
npm test           # vitest unit tests
npm run build      # production build → dist/
```

## Project Structure

```
dental-notes-standardizer/
├── index.html
├── vite.config.js
├── package.json
├── src/
│   ├── main.jsx
│   ├── App.jsx
│   ├── components/
│   │   └── NotesStandardizer.jsx   # two-panel UI
│   └── lib/
│       ├── standardize.js          # normalization engine
│       └── standardize.test.js     # vitest unit tests
└── docs/
    └── curve-hero-benchmark.md     # term map + benchmark methodology
```

## Design Principle

This tool is a **design/UX reference** aligned to Curve Hero's UI language — it is not
integrated with the Curve Hero API or database. Notes standardized here can be pasted
directly into Curve Hero's clinical notes field without vocabulary inconsistencies.
