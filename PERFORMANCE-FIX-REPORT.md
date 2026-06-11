# Website Performance Fix Report

**Site:** https://www.aescode.nexus/ (homepage)
**Source reports:** PageSpeed Insights — Mobile (score 68) + Desktop (score 73), captured 11 Jun 2026, Lighthouse 13.3.0
**Stack:** Astro (static output), Cloudflare-hosted, Supabase for newsletter
**Scores:** Performance 68 (mobile) / 73 (desktop) · Accessibility 91 · Best Practices 100 · SEO 100

> **Excluded as PEF / non-actionable** (not in the table below):
> - *"Discover what your real users are experiencing — No data"* → CrUX field data not yet collected; nothing to fix in code.
> - Emulation / throttling environment notes (Moto G, Slow 4G, custom throttling) → diagnostic context, not a defect.
> - *"Structured data is valid"* (SEO manual check) → already passing; only a suggestion to run external validators.
> - Mobile **TBT 0 ms** and mobile **CLS 0** → already passing.
> - All **Passed Audits** (Perf 15, A11y 22–23, BP 13, SEO 10) and **Not Applicable** items.
> - The 10 A11y *"additional items to manually check"* → require human review, not code changes.

---

## Summary Table

| # | Issue | Severity | Category | File/URL Affected |
|---|-------|----------|----------|-------------------|
| 1 | LCP in failing range (mobile red; desktop 5.5 s) | Critical | Core Web Vitals | `src/components/Hero.astro` (hero image), `src/components/StatsBar.astro` / Hero counter |
| 2 | LCP element render delay 1,280 ms (animated stat counter) | High | Core Web Vitals | `public/scripts/scroll-reveal.js`, `data-counter` span |
| 3 | Cumulative Layout Shift from web-font swap (desktop 0.009) | Low | Core Web Vitals | `public/styles/base.css` (`@import` font), hero content |
| 4 | Render-blocking requests (mobile ~2,840 ms / desktop ~640 ms) | High | Render Blocking | `src/layouts/BaseLayout.astro` (CSS links + Supabase), `public/styles/base.css` |
| 5 | Synchronous Supabase script in `<head>` blocks render | High | Render Blocking | `src/layouts/BaseLayout.astro:96` |
| 6 | Google Fonts loaded via CSS `@import` (chained, blocking) | High | Render Blocking | `public/styles/base.css:7` |
| 7 | Oversized / unoptimised images — 5.7 MB (mobile) / 9.3 MB (desktop) savings | Critical | Images | `event_01.jpeg`, `event_03.jpeg`, `KCDH - IITB.jpeg`, `nuxus_logo.png`, `BV(DU)MC logo.png` |
| 8 | Enormous network payload (6.4 MB mobile / 9.8 MB desktop) | Critical | Images | Same image set as #7 |
| 9 | Images missing explicit `width` (only `height` set) → CLS risk | High | Images | `src/components/TrustStrip.astro`, `src/components/ClinicalPartners.astro` |
| 10 | Inefficient cache lifetimes on third-party JS | Low | Caching | `@supabase/supabase-js@2` (jsDelivr, 7d), Cloudflare `beacon.min.js` (1d) |
| 11 | Unused JavaScript — 48 KiB from Supabase UMD bundle | Medium | JavaScript | `src/layouts/BaseLayout.astro:96` / `src/components/Newsletter.astro` |
| 12 | Long main-thread tasks (mobile 152 ms + 73 ms; desktop 83 ms scroll-reveal) | Medium | JavaScript | `public/scripts/scroll-reveal.js` |
| 13 | Forced reflow — 45 ms (mobile) | Low | JavaScript | `public/scripts/scroll-reveal.js` |
| 14 | Five separate render-blocking CSS files (no critical-CSS inlining) | Medium | CSS | `src/layouts/BaseLayout.astro:87-89`, `assets/index.*.css`, `assets/about.*.css` |
| 15 | `[aria-hidden="true"]` element contains focusable descendants | High | Accessibility | `src/components/Navbar.astro:49` (`#mobile-menu`) |
| 16 | Insufficient colour contrast in footer | Medium | Accessibility | `src/components/Footer.astro` (`.footer__heading`, `.footer__copy`, `.footer__version`) |
| 17 | Heading order not sequentially descending (footer `<h4>` skips levels) | Low | Accessibility | `src/components/Footer.astro:20,29,39` |
| 18 | DOM size insight — 264 elements, depth 10 (desktop) | Low (Info) | Other | `src/pages/index.astro` and child components |
| 19 | Security headers not set (CSP, HSTS, COOP, XFO, Trusted Types) — optional | Low | Other | Cloudflare config / `public/_headers` |

---

## Issues

### Core Web Vitals

### 1. LCP in failing range
- **What:** Largest Contentful Paint is in the red on mobile and **5.5 s on desktop** (good = ≤2.5 s). The LCP element is the hero region, dominated by `event_01.jpeg` (4 MB, `loading="eager"`) and the headline/stat block.
- **Why it matters:** LCP is the heaviest-weighted Core Web Vital; >4 s reads as "slow" to Google and users, hurting both ranking and bounce.
- **Where:** `src/components/Hero.astro:53-59` — `<img src="/images/archive/event_01.jpeg" class="hero__photo" width="640" height="800" loading="eager">`.
- **Fix:** Resolve via #7 (serve a compressed, correctly-sized WebP/AVIF hero) **and** #2 (counter render delay). Keep `loading="eager"` on the hero image but add `fetchpriority="high"` and `decoding="async"`. Once the hero image is ~150–250 KB instead of 4 MB, LCP drops sharply.
- **Expected gain:** LCP image savings of ~3.4 MB (mobile) / ~3.2–3.9 MB (desktop) per the report; LCP should move from red toward green.
- **Depends on:** #7 (image optimisation) must ship first.

### 2. LCP element render delay — 1,280 ms (animated stat counter)
- **What:** Desktop LCP breakdown shows **TTFB 0 ms, Element render delay 1,280 ms**. The LCP element is the stat counter `<span class="data-lg mono" data-counter data-target="250" data-suffix="+">`, which starts at `0` and animates up via JS, so the final "250+" text paints late.
- **Why it matters:** Render delay is ~100% of LCP here — the byte loading is already fast; JS is what's holding the paint back.
- **Where:** `public/scripts/scroll-reveal.js` (`animateCounter`, ~line 27+); counter markup in the Hero/StatsBar component.
- **Fix:** Render the final value in the HTML so it paints immediately, then let JS animate from 0 only as an enhancement. E.g. set the span's text to `250+` server-side (it already has `data-target`), and in `animateCounter` skip the animation if the element is already in the viewport at load, or only animate elements that scroll into view (the hero counter is above the fold so it should paint static). Also gate the whole effect behind `requestIdleCallback` / `IntersectionObserver` so the counter is not the blocking paint.
- **Expected gain:** Removes the dominant 1,280 ms render delay from desktop LCP.

### 3. Cumulative Layout Shift from web-font swap
- **What:** Desktop CLS is **0.009** (passing but flagged). "Layout shift culprits" attributes it to the hero content reflowing when web fonts (`fonts.gstatic.com` woff2) finish loading and swap in.
- **Why it matters:** Font-swap reflow is the only remaining shift; eliminating it locks CLS near 0 and prevents regressions as content grows.
- **Where:** `public/styles/base.css:7` — the `@import` Google Fonts URL uses `display=swap`; hero text in `src/components/Hero.astro`.
- **Fix:** Self-host the three fonts (Crimson Pro, Public Sans, JetBrains Mono) as woff2 in `public/fonts/`, declare `@font-face` with `font-display: optional` (or `swap` + `size-adjust`/`ascent-override` matched to the fallback) to remove the reflow. Self-hosting also kills the `fonts.googleapis.com` round-trip (see #6).
- **Expected gain:** CLS → ~0; also removes a render-blocking origin.

---

### Render Blocking

### 4. Render-blocking requests
- **What:** Initial render is blocked by an estimated **2,840 ms (mobile) / 640 ms (desktop)**. Blockers: five CSS files (`assets/index.*.css`, `styles/utilities.css`, `styles/base.css`, `styles/tokens.css`, `assets/about.*.css`), the Google Fonts `css2` request, and the Supabase script in `<head>`.
- **Why it matters:** Everything in this list sits on the critical path before first paint, directly inflating FCP and LCP.
- **Where:** `src/layouts/BaseLayout.astro:87-96`.
- **Fix:** Combination of #5 (defer Supabase), #6 (self-host fonts), and #14 (inline critical CSS / reduce CSS file count). Add `media="print" onload="this.media='all'"` or Astro's built-in CSS bundling to drop non-critical sheets off the critical path.
- **Expected gain:** Up to ~2,840 ms (mobile) recovered on the critical path.
- **Depends on:** Resolve #5, #6, #14.

### 5. Synchronous Supabase script in `<head>`
- **What:** `<script is:inline src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>` loads synchronously in `<head>`, blocking the parser. It is only used by the newsletter form, which is below the fold.
- **Why it matters:** A 50 KiB third-party script on the critical path delays first paint for a feature most visitors never reach.
- **Where:** `src/layouts/BaseLayout.astro:96`.
- **Fix:** Remove it from `<head>`. Load Supabase lazily, only when the newsletter is needed — e.g. dynamically `import('@supabase/supabase-js')` inside `Newsletter.astro`'s submit handler, or move the tag to just before `</body>` with `defer`. Best: bundle `@supabase/supabase-js` as an npm dependency and import it in the Newsletter island so Astro tree-shakes/defers it instead of pulling the full UMD build from a CDN.
- **Expected gain:** Removes a 50 KiB blocking request from the head; feeds #4 and #11.

### 6. Google Fonts loaded via CSS `@import`
- **What:** `base.css` line 7 does `@import url('https://fonts.googleapis.com/css2?family=...')`. A CSS `@import` is discovered only after `base.css` itself downloads, creating a chained, render-blocking request to `fonts.googleapis.com` (≈261–336 ms) before any font CSS arrives — then the woff2 files load.
- **Why it matters:** `@import` is the slowest way to load fonts (serial dependency chain); it blocks render and delays text paint.
- **Where:** `public/styles/base.css:7`.
- **Fix:** Remove the `@import`. Self-host the fonts (preferred — see #3) **or**, if staying on Google Fonts, replace with a `<link rel="stylesheet" href="...css2...">` directly in `BaseLayout.astro` `<head>` plus `<link rel="preload" as="font" type="font/woff2" crossorigin>` for the two hero-weight files. The existing `preconnect` hints (lines 92-93) only help in the second case.
- **Expected gain:** Removes one chained blocking request; faster first text paint.

---

### Images

### 7. Oversized / unoptimised images
- **What:** "Improve image delivery" estimates **5,747 KiB (mobile) / 9,339 KiB (desktop)** of savings. Every offending file is a raw JPEG/PNG served at far larger dimensions than displayed:

  | File | Transfer | Intrinsic | Displayed | Used in |
  |------|----------|-----------|-----------|---------|
  | `public/images/archive/event_01.jpeg` | 4,067 KiB | 1743×3072 | 640×800 | `Hero.astro` (eager, LCP) |
  | `public/images/archive/event_03.jpeg` | 3,345 KiB | 4080×2297 | 568×428 | `ClinicalPartners.astro` (lazy) |
  | `public/images/KCDH - IITB.jpeg` | 1,843 KiB | 800×338 | ~149×63 / 85×36 | `TrustStrip.astro` + `ClinicalPartners.astro` |
  | `public/images/nuxus_logo.png` | 198 KiB | 720×1280 | 39×70 / 23×40 | `TrustStrip.astro` |
  | `public/images/BV(DU)MC logo.png` | 65 KiB | 238×241 | 83×84 / 47×48 | `TrustStrip.astro` + `ClinicalPartners.astro` |

- **Why it matters:** ~6–9 MB of images is the single biggest cause of poor LCP and the enormous payload; on Slow 4G this is multi-second delay and real data cost.
- **Where:** Files above + their `<img>` tags in `Hero.astro:53`, `ClinicalPartners.astro:27,36,50`, `TrustStrip.astro:13,27,41`.
- **Fix:** Move these images from `public/images/` into `src/assets/` and use Astro's `astro:assets` `<Image>` / `<Picture>` components to emit resized WebP/AVIF with `srcset`. Concretely:
  - **Hero (`event_01`)**: `import hero from '../assets/archive/event_01.jpeg'` then `<Picture src={hero} formats={['avif','webp']} width={640} height={800} densities={[1,2]} loading="eager" fetchpriority="high" alt="…" />`. Target ≤250 KB.
  - **`event_03`**: same pattern, `width={568} height={428}`, `loading="lazy"`.
  - **Logos (`KCDH`, `nuxus_logo`, `BV(DU)MC`)**: downscale to actual display size (~2× for retina) and convert to WebP — e.g. KCDH to ~300×128, nuxus to ~80×140, BV to ~170×170. These are tiny logos served as multi-hundred-KB assets.
  - If you cannot adopt `astro:assets`, pre-generate `.webp` + resized variants with `sharp`/`squoosh` and reference them via `<picture><source type="image/avif"><source type="image/webp"><img></picture>`.
- **Expected gain:** Up to **9.3 MB** (desktop) total; `event_01` alone ~3.4–3.9 MB; directly fixes LCP (#1) and payload (#8).
- **Prerequisite:** Adopt `astro:assets` (built into Astro, no new dependency) **before** rewriting the tags, so width/height (#9) come for free.

### 8. Enormous network payload
- **What:** Total page weight **6,443 KiB (mobile) / 9,788 KiB (desktop)**; ~96% is the five images above.
- **Why it matters:** Large payloads correlate strongly with long load times and cost users mobile data.
- **Where:** Same image set as #7.
- **Fix:** Fully resolved by #7. No separate action.
- **Expected gain:** Payload drops to well under 1 MB once images are optimised.

### 9. Images missing explicit `width`
- **What:** "Image elements do not have explicit width and height" — `nuxus_logo.png`, `KCDH - IITB.jpeg`, and `BV(DU)MC logo.png` set only `height` (e.g. `height="40"` / inline `height: 36px; width: auto`), with no intrinsic `width` attribute.
- **Why it matters:** Without both dimensions the browser cannot reserve space before the image loads, risking layout shift (CLS).
- **Where:** `src/components/TrustStrip.astro:13-46`, `src/components/ClinicalPartners.astro:27-40`.
- **Fix:** Add explicit `width` alongside `height` on each logo `<img>` (matching the intrinsic aspect ratio of the optimised asset), and avoid `width: auto` in inline styles. If you adopt `astro:assets` (#7), `<Image>` injects correct `width`/`height` automatically — fixing this for free.
- **Expected gain:** Eliminates logo-driven CLS risk; supports CLS staying ~0.

---

### Caching

### 10. Inefficient cache lifetimes on third-party JS
- **What:** "Use efficient cache lifetimes — Est savings 10 KiB." `@supabase/supabase-js@2` from jsDelivr has a **7-day** TTL; Cloudflare `beacon.min.js` has **1-day**.
- **Why it matters:** Short TTLs force re-downloads on repeat visits. Minor here (small bytes), and both are third-party so you can't set their headers directly.
- **Where:** `cdn.jsdelivr.net/npm/@supabase/supabase-js@2`, `static.cloudflareinsights.com/beacon.min.js`.
- **Fix:** Resolve by bundling Supabase locally (#5/#11) so it is served from your own origin under Cloudflare's long-cache static rules. The Cloudflare beacon is injected by Cloudflare and is not controllable — treat as accepted.
- **Expected gain:** ~10 KiB on repeat visits; main benefit is removing the third-party dependency.

---

### JavaScript

### 11. Unused JavaScript — 48 KiB
- **What:** "Reduce unused JavaScript — Est savings 48 KiB." `supabase.js@2.108.1` UMD bundle is 50.4 KiB transferred, **48.1 KiB unused** on initial load.
- **Why it matters:** The full Supabase client ships on every page but only the newsletter insert is used, and only on submit.
- **Where:** `src/layouts/BaseLayout.astro:96` → consumed in `src/components/Newsletter.astro:118`.
- **Fix:** Same as #5 — lazy-load Supabase on first interaction with the newsletter form (dynamic `import()` in the submit handler). For a single insert you can also drop the SDK entirely and POST to the Supabase REST endpoint (`/rest/v1/<table>`) with `fetch` + the anon key, removing the 50 KiB bundle completely.
- **Expected gain:** ~48 KiB removed from initial load on every page.

### 12. Long main-thread tasks
- **What:** Mobile: two long tasks (**152 ms + 73 ms**, unattributable). Desktop: `scroll-reveal.js` **83 ms** + 54 ms unattributable.
- **Why it matters:** Long tasks block input and inflate TBT; the desktop one is directly attributed to the scroll-reveal script.
- **Where:** `public/scripts/scroll-reveal.js`.
- **Fix:** Defer scroll-reveal initialisation until after first paint (wrap setup in `requestIdleCallback`), and ensure the `IntersectionObserver` callback does minimal work per frame (batch class writes, avoid per-element layout reads — see #13). The counter `requestAnimationFrame` loop should only run for in-view elements.
- **Expected gain:** Lower TBT; smoother interaction. (Mobile TBT already 0 ms — gain is mainly desktop/robustness.)

### 13. Forced reflow — 45 ms
- **What:** Mobile "Forced reflow" of 45 ms (unattributed). Typically caused by reading geometric properties (`offsetWidth`, `getBoundingClientRect`) after a DOM/style change in the same frame.
- **Why it matters:** Layout thrashing forces synchronous re-layout, wasting main-thread time.
- **Where:** `public/scripts/scroll-reveal.js` (the most likely source — counter/observer reads element geometry).
- **Fix:** Separate reads from writes: collect all measurements first, then apply class/style changes. Cache `getBoundingClientRect` results and prefer `IntersectionObserver` (which provides geometry without forcing reflow) over manual `offsetTop`/`offsetWidth` reads.
- **Expected gain:** Removes the 45 ms reflow; complements #12.

---

### CSS

### 14. Five separate render-blocking CSS files
- **What:** `tokens.css`, `base.css`, `utilities.css` plus per-route `assets/index.*.css` and `assets/about.*.css` each load as separate blocking `<link>`s before first paint.
- **Why it matters:** Each is a render-blocking round-trip on the critical path (part of the 2,840 ms mobile figure in #4).
- **Where:** `src/layouts/BaseLayout.astro:87-89`; Astro-emitted `assets/*.css`.
- **Fix:** Let Astro bundle/inline critical CSS (`build.inlineStylesheets: 'auto'` in `astro.config.mjs`) so small sheets are inlined into the head rather than fetched. Combine the three hand-authored `public/styles/*.css` into one file, or move them into Astro component `<style>` so they're bundled and scoped. Note `about.*.css` is loading on the homepage — confirm it isn't being pulled in unnecessarily by a shared import.
- **Expected gain:** Fewer blocking requests; contributes to the #4 critical-path reduction.

---

### Accessibility

### 15. `[aria-hidden="true"]` element contains focusable descendants
- **What:** The mobile menu `<div class="navbar__mobile" id="mobile-menu" role="menu" aria-hidden="true">` contains focusable `<a role="menuitem">` links. When the menu is closed, it's hidden from screen readers but its links remain keyboard-focusable — screen-reader/keyboard users can tab into "hidden" links.
- **Why it matters:** This is the only ARIA failure (drives Accessibility down from 100); it's a real keyboard/AT bug, not a cosmetic flag.
- **Where:** `src/components/Navbar.astro:49` (and child links lines ~54-55).
- **Fix:** Don't use static `aria-hidden="true"`. Toggle visibility properly: when closed, set `inert` on `#mobile-menu` (which removes it from both AT and tab order) and `hidden`/`display:none`; when opened, remove `inert`/`aria-hidden`. Update the existing open/close JS to flip `inert` + `aria-hidden` together with the `.open` class. Since `.navbar__mobile` already uses `overflow:hidden` + height for the animation, add `inert` when not `.open`.
- **Expected gain:** Resolves the ARIA audit; Accessibility toward 100.

### 16. Insufficient colour contrast in footer
- **What:** Footer text fails the WCAG AA contrast ratio — flagged elements: `.footer__heading` ("Platform/Connect/Legal"), `.footer__copy` ("© 2026 AesCode Co."), `.footer__version` ("V2.0.0-REDESIGN") against the dark footer background.
- **Why it matters:** Low-contrast text is hard/impossible to read for low-vision users; contributes to the 91 Accessibility score.
- **Where:** `src/components/Footer.astro` styles (`.footer__heading` ~line 109, `.footer__copy, .footer__version` ~line 133).
- **Fix:** Increase the foreground luminance until ratio ≥ 4.5:1 for body text (≥ 3:1 for large headings). Replace the muted grey token used for these elements with a lighter one (e.g. bump to `--color-text-secondary`/a `#b8b8b8`+ on the `#0a0a0a` footer). Verify each with a contrast checker against the actual footer background.
- **Expected gain:** Clears the contrast audit.

### 17. Heading order not sequentially descending
- **What:** Footer column headings use `<h4>` ("Platform", "Connect", "Legal") while the page's section headings are `<h1>` (Hero) → `<h2>` (Mission/WhyNow/Partners) → `<h3>` (sub-items). The footer jumps to `<h4>`, skipping a level.
- **Why it matters:** Skipped heading levels break the semantic outline for screen-reader navigation.
- **Where:** `src/components/Footer.astro:20,29,39`.
- **Fix:** Change the three `.footer__heading` elements from `<h4>` to `<h2>` (they are top-level footer sections, siblings of the other section `<h2>`s), keeping the `footer__heading` class for styling. Do not change visual size — the class controls appearance, not the tag.
- **Expected gain:** Clears the heading-order audit.

---

### SEO

No actionable SEO defects. SEO score is **100**; all 10 audits pass. The single manual item ("Structured data is valid") is already passing — excluded as non-actionable.

---

### Other

### 18. DOM size insight (desktop)
- **What:** "Optimise DOM size" reports **264 total elements, depth 10, max 10 children**. This is well within healthy limits (Lighthouse warns ~800+); listed as an informational insight, not a failure.
- **Why it matters:** Negligible today; only relevant if the homepage grows substantially.
- **Where:** `src/pages/index.astro` + child components.
- **Fix:** No action required now. Monitor if you add large repeated lists. Keep nesting shallow in `PrimaryMission.astro` (the deepest branch).
- **Expected gain:** None currently (informational).

### 19. Security headers not set (optional hardening)
- **What:** Best Practices "Trust and Safety" lists missing **CSP**, **HSTS**, **COOP**, **X-Frame-Options/CSP frame-ancestors**, and **Trusted Types**. These did **not** lower the Best Practices score (still 100) — they are surfaced as informational hardening.
- **Why it matters:** Defence-in-depth against XSS and clickjacking; good practice for a site that posts to Supabase, though not a performance issue.
- **Where:** Cloudflare (Transform Rules / Workers) or a `public/_headers` file (if using Cloudflare Pages).
- **Fix:** Add response headers: `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`, `X-Frame-Options: DENY` (or `Content-Security-Policy: frame-ancestors 'none'`), `Cross-Origin-Opener-Policy: same-origin`, and a `Content-Security-Policy` allowing `self`, `cdn.jsdelivr.net`, `fonts.googleapis.com`, `fonts.gstatic.com`, and your Supabase origin. Roll out CSP in `Content-Security-Policy-Report-Only` first to avoid breaking the Supabase/font calls. Adopt Trusted Types last (requires app changes).
- **Expected gain:** Security posture only; no score/metric change. Lowest priority.

---

## Recommended ordering & dependencies

1. **#7 Image optimisation** (adopt `astro:assets`) — biggest win; unblocks #1, #8, and #9 simultaneously.
2. **#6 Self-host fonts** + **#5/#11 defer Supabase** — clears the render-blocking critical path (#4) and unused JS, and removes the font-swap CLS (#3).
3. **#2 Counter render delay** + **#12/#13 scroll-reveal** — same file (`scroll-reveal.js`); fix together. #2 also needs the hero image (#7) done to fully land LCP.
4. **#14 CSS inlining** — config-level, low risk.
5. **#15 / #16 / #17 Accessibility** — independent, ship anytime to push A11y back to 100.
6. **#19 Security headers** — optional, last.

## Conflicts / cautions

- **`astro:assets` (#7) vs. `public/` paths:** the images currently live in `public/images/` and are referenced by absolute URL. Moving them to `src/assets/` changes the import mechanism — update every referencing component (`Hero`, `TrustStrip`, `ClinicalPartners`) in the same change, or the build will 404. Do #7 and #9 as one atomic PR.
- **Self-hosting fonts (#3/#6) vs. preconnect hints:** once fonts are self-hosted, the `preconnect` to `fonts.googleapis.com`/`fonts.gstatic.com` in `BaseLayout.astro:92-93` becomes dead and should be removed to avoid wasted connections.
- **CSP (#19) vs. current third-parties:** a strict CSP will block jsDelivr/Google Fonts/Supabase if you don't allowlist them — but if you complete #5, #6, #7 first, those external origins largely disappear, making the CSP simpler and stricter. Sequence #19 after the dependency cleanup.
- **`font-display: optional` (#3):** eliminates CLS but may show fallback text if the font is slow on first visit. If brand typography must always render, use `swap` + `size-adjust` metrics-matched fallback instead.

---

*Sources: `AesCode-PageSpeed-Insights.md` (mobile) and `PageSpeed Insights-desktop.md` (desktop), PageSpeed Insights / Lighthouse 13.3.0, 11 Jun 2026.*
