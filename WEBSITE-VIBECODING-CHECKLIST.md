# Vibecoding Checklist — Things to Take Care Of On Your Next Website

A pre-flight checklist distilled from real PageSpeed/Lighthouse failures. Paste it into your repo (or your AI agent's context) and tick boxes before you ship. Ordered by impact: **images and fonts cause ~90% of performance pain.**

> **Golden rule:** vibecoding produces working-but-heavy output fast. The failure mode is never "it doesn't work" — it's "it works but ships 9 MB and blocks render." Catch that here, not in production.

---

## 0. Set up the guardrails first (before writing features)

- [ ] Run **Lighthouse / PageSpeed Insights on both Mobile and Desktop** after the first deploy, not at the end. Mobile is throttled (Slow 4G) and always scores worse — design for it.
- [ ] Add a **performance budget**: total page weight < 1 MB, LCP < 2.5 s, CLS < 0.1, TBT < 200 ms. Treat a breach as a build failure, not a nice-to-have.
- [ ] Tell your AI agent the constraints up front: *"every image must be WebP/AVIF and sized to display dimensions; no render-blocking third-party scripts in `<head>`; explicit width+height on all images."* It will not do this unless asked.

---

## 1. Images — the #1 killer

- [ ] **Never ship raw camera/export JPEGs or PNGs.** A 4 MB hero photo is the single most common cause of bad LCP. Convert everything to **WebP or AVIF**.
- [ ] **Resize to actual display size** (× ~2 for retina). Don't serve a 4080×2297 image into a 568×428 slot, or a 720×1280 logo into a 39×70 box. The browser downloads the full file regardless of CSS sizing.
- [ ] Use your framework's image pipeline so this is automatic:
  - Astro → `astro:assets` `<Image>` / `<Picture>` (images live in `src/assets/`, **not** `public/`).
  - Next.js → `next/image`. Nuxt → `<NuxtImg>`. Plain HTML → `<picture>` with `<source type="image/avif">` + `srcset`, pre-built with `sharp`/Squoosh.
- [ ] **Always set explicit `width` and `height`** (or `aspect-ratio`) on every `<img>` — both, not just one. Prevents layout shift (CLS). Avoid `width: auto` in inline styles.
- [ ] Mark the **above-the-fold hero image** `loading="eager"` + `fetchpriority="high"` + `decoding="async"`. Mark **everything below the fold** `loading="lazy"`.
- [ ] Optimise logos too — a "small" logo exported at full resolution is still hundreds of KB.

## 2. Fonts — the silent #2 killer

- [ ] **Never load fonts via CSS `@import`.** It creates a chained, render-blocking request (CSS must download before the font is even discovered). It's the slowest possible method.
- [ ] Prefer **self-hosting** woff2 in your project over hotlinking Google Fonts — removes two third-party origins from the critical path.
- [ ] If self-hosting, `<link rel="preload" as="font" type="font/woff2" crossorigin>` the 1–2 fonts used above the fold.
- [ ] Set `font-display: optional` (no layout shift) or `swap` + a **metrics-matched fallback** (`size-adjust` / `ascent-override`) to kill font-swap CLS.
- [ ] Only load the **weights and styles you actually use.** Don't pull 7 weights for 2.

## 3. JavaScript & third-party scripts

- [ ] **No synchronous third-party `<script>` in `<head>`.** It blocks the parser and first paint. Move to end of `<body>` with `defer`, or load on demand.
- [ ] **Lazy-load heavy SDKs** (auth, analytics, payment, DB clients) only when needed. A DB client for a below-the-fold newsletter form should `import()` on submit, not load on every page.
- [ ] For a single API call, **skip the whole SDK** — a `fetch()` to the REST endpoint is often 50 KiB lighter.
- [ ] Bundle dependencies through your build tool (tree-shaken) instead of pulling full UMD bundles from a CDN — smaller and cached on your own origin.
- [ ] Keep scroll/animation scripts cheap: defer init with `requestIdleCallback`, use `IntersectionObserver` (not manual `offsetTop`/`offsetWidth` reads), and **separate DOM reads from writes** to avoid forced reflow / layout thrashing.

## 4. CSS & render path

- [ ] **Minimise render-blocking CSS.** Let the framework inline critical CSS (e.g. Astro `build.inlineStylesheets: 'auto'`); don't ship 5 separate blocking `<link>` stylesheets.
- [ ] Don't load **page-specific CSS on every page** (check a shared import isn't dragging an `about.css` onto the homepage).
- [ ] Keep the DOM shallow and lean — deep nesting and huge element counts slow style/layout. (Stay well under ~800 elements.)

## 5. Core Web Vitals — the metrics that get scored

- [ ] **LCP element:** identify it (often the hero image *or* a hero text/number). If it's an **animated counter** that starts at 0, render the final value in HTML and animate as enhancement — otherwise the paint waits on JS (pure render delay).
- [ ] **CLS:** reserve space for images, ads, embeds, and fonts. Anything that loads late and pushes content down costs you.
- [ ] **TBT:** keep main-thread tasks short; defer non-critical JS.
- [ ] Add `preconnect` hints **only** for origins you actually fetch from early — and remove them when you stop using that origin (dead preconnects waste connections). Max ~4.

## 6. Caching & delivery

- [ ] Serve static assets from **your own origin** behind a CDN with long cache lifetimes (`max-age=31536000, immutable` for hashed assets).
- [ ] Avoid relying on third-party CDNs with short TTLs for things you re-download every visit.

## 7. Accessibility — don't let the AI skip it (it scores too)

- [ ] **Don't `aria-hidden="true"` a container that still has focusable children** (closed menus/modals). Use `inert` + `hidden` when closed so keyboard/screen-reader users can't tab into invisible links. This is a real bug, not cosmetic.
- [ ] **Heading order must be sequential** — no jumping h2 → h4. Footer/section headings should be the right *level*; control size with CSS classes, not by picking a smaller tag.
- [ ] **Colour contrast ≥ 4.5:1** for body text (≥ 3:1 for large text). Muted-grey-on-dark footers fail constantly — check with a contrast tool.
- [ ] Every `<img>` has meaningful `alt`. Every form input has an associated `<label>`.
- [ ] Buttons are `<button>`, links are `<a>` — not `<div onclick>`. Keyboard focus must be visible.

## 8. SEO & metadata (cheap, high-value)

- [ ] Unique `<title>` + meta description per page; canonical URL; `robots` meta.
- [ ] Open Graph + Twitter card tags with a real OG image.
- [ ] Valid JSON-LD structured data (Organization / WebSite at minimum).
- [ ] `sitemap.xml` + `robots.txt` generated and submitted.

## 9. Security headers (set once at the edge)

- [ ] `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`
- [ ] `X-Frame-Options: DENY` (or CSP `frame-ancestors 'none'`) — anti-clickjacking.
- [ ] `Cross-Origin-Opener-Policy: same-origin`.
- [ ] A `Content-Security-Policy` allowlisting only the origins you use. **Roll out in `-Report-Only` first** so you don't silently break fonts/DB/analytics calls.
- [ ] Keep secrets server-side. Only the public/anon keys belong in client JS.

## 10. Pre-ship verification loop

- [ ] Re-run **PageSpeed Insights (Mobile + Desktop)** — aim ≥ 90 Performance, 100 A11y/BP/SEO.
- [ ] Open DevTools **Network tab, throttled to Slow 4G** — confirm no single asset > ~300 KB and total < 1 MB.
- [ ] Tab through the whole page with the **keyboard only** — nothing hidden should be focusable; focus is always visible.
- [ ] Test on a **real mobile device**, not just the responsive emulator.
- [ ] Diff the final build: every asset traces to something actually rendered (no orphaned CSS/JS/images).

---

### The 5 mistakes that caused most of the damage last time

1. **Multi-MB raw images** served at a fraction of their size → killed LCP + payload.
2. **Fonts via CSS `@import`** → chained render-blocking request.
3. **DB SDK loaded synchronously in `<head>`** for a below-fold form → blocked render + 48 KiB unused JS.
4. **Images with no `width`/`height`** → layout shift.
5. **`aria-hidden` on a menu with focusable links** + bad heading order + low-contrast footer → avoidable accessibility failures.

Fix these five reflexively and you start every new site at ~90+ instead of clawing back from 68.
