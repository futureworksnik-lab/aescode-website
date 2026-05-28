# Aescode Co. Website

Astro static site for [aescode.nexus](https://www.aescode.nexus) — the public presence of Aescode Co., a medical AI research initiative.

## Setup

```bash
npm install
```

## Develop

```bash
npm run dev
# → http://localhost:4321
```

## Build

```bash
npm run build
# output → dist/
```

```bash
npm run preview
# preview the dist/ build locally
```

## Environment variables

Copy `.env.local` (never commit it) with:

```
PUBLIC_SUPABASE_URL=https://<project>.supabase.co
PUBLIC_SUPABASE_ANON_KEY=<anon-key>
```

These power the Newsletter subscription form. The Supabase anon key is public by design — it ships in client JS.

## Project structure

```
src/
  pages/       ← 7 routes (index, about, cohort1, ai-ethics, contact, meet-the-team, special-thanks)
  components/  ← 11 shared UI components (Navbar, Footer, Hero, Newsletter, …)
  layouts/     ← BaseLayout.astro (shared <head>, styles, scripts)
  data/        ← shared data constants (navLinks, etc.)
public/
  styles/      ← design tokens, base reset, utilities (loaded by BaseLayout)
  scripts/     ← scroll-reveal.js (loaded by BaseLayout)
  images/      ← canonical image and video assets
docs/          ← strategy docs, design notes, build system reference
legacy/        ← pre-Astro artifacts, quarantined 2026-05-28 (see legacy/README.md)
```

## Further reading

- Design principles and visual language → [docs/DESIGN.md](docs/DESIGN.md)
- Build system reference → [docs/AesCode_Build_System.md](docs/AesCode_Build_System.md)
- Website strategy and content plan → [docs/Aescode_Website_Strategy_Master_v2.md](docs/Aescode_Website_Strategy_Master_v2.md)
- Legacy artifact timeline → [legacy/README.md](legacy/README.md)
