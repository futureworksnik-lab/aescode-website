# AesCode Co. — Build System Master Document

**Product Requirements · UX Flows · Technical Architecture · Database Design · Risk Log · Execution Guidelines**  
Prepared for: Stitch MCP + Google Antigravity | Version 1.0 | April 2026

---

## DESIGN SYSTEM RULES — ENFORCE ON EVERY PAGE

> Copy this block into every Antigravity prompt that generates UI.

```
DESIGN SYSTEM RULES — ENFORCE STRICTLY:
• Background: #FCF9F8 (warm white). NEVER pure white on page body.
• Primary color: #021934 (deep navy). Buttons, active states, key headings only.
• Body text: #1C1B1B. Muted/label text: #707785.
• Headlines: Newsreader (Google Fonts), serif.
• Body + labels + nav: Public Sans (Google Fonts).
• Border-radius: maximum 4px. NEVER pill/rounded buttons.
• NO gradients. NO box-shadows above 4px blur. NO glassmorphism. NO blurs.
• Section separation: background shifts or whitespace ONLY. NO 1px divider lines.
• Nav: text labels only, all-caps, Public Sans. NO icons.
• Dot-grid overlay: CSS pseudo-element on surface layer, opacity: 0.03, pointer-events: none, z-index: 0.
• Input fields: underline-only (0.5px #C4C6CE). Focus state: 1.5px #021934. No glowing halos.
• Cards: surface-container-lowest (#FFFFFF), 2px border-radius, separated by grid not borders.
• All label text: all-caps, Public Sans, letter-spacing +0.05em, color #707785.
```

---

## Design Token Reference

| Token | Value | Usage |
|---|---|---|
| `--surface` | `#FCF9F8` | Page background |
| `--primary` | `#021934` | Buttons, active nav, headings |
| `--on-surface` | `#1C1B1B` | Body text |
| `--secondary` | `#707785` | Labels, metadata, muted text |
| `--surface-container-lowest` | `#FFFFFF` | Cards, interactive elements |
| `--surface-dim` | `#DCD9D9` | Subtle structural shifts |
| `--outline-variant` | `#C4C6CE` | Hairlines (0.5px), input borders |
| `--font-serif` | `Newsreader` | Display, headlines, pullquotes |
| `--font-sans` | `Public Sans` | Body, labels, navigation, buttons |

---

---

# SECTION 1 — Product Requirements Document (PRD)

---

## 1.1 Product Vision

AesCode Co. is a MedTech research platform that accelerates the translation of clinical insights into deployable, evidence-based technological solutions. The website is the primary institutional surface — its primary audiences are institutional partners and sponsors, investors, press, and research participants.

The site must communicate academic authority, not startup energy. Every page should feel like a peer-reviewed monograph rendered in digital form. The creative north star is **"The Digital Monograph"** — white canvas editorial aesthetic referencing Nature, Medium, and Stripe Docs.

---

## 1.2 Site Map (Final State)

| Route | Page Name | Status | Nav Position |
|---|---|---|---|
| `/` | Home | Existing — updated | HOME |
| `/about` | About | Existing — updated | ABOUT |
| `/cohort-1` | Cohort 1 | Existing — expanded | COHORT 1 |
| `/ai-ethics` | AI Ethics | New page | AI ETHICS |
| `/contact` | Contact | Existing — unchanged | CONTACT |
| `/team` | Meet the Team | New page | Footer link only |
| `/thanks` | Special Thanks | New page | Footer link only |

**REMOVED:** `/problems` as a standalone nav item. Problems content migrated into `/cohort-1`.

---

## 1.3 Navigation Bar — Final Spec

| Tab Label | Route | Action |
|---|---|---|
| HOME | `/` | Keep — no change |
| ABOUT | `/about` | Keep — no change |
| COHORT 1 | `/cohort-1` | Keep — expand content |
| AI ETHICS | `/ai-ethics` | ADD — new page |
| CONTACT | `/contact` | Keep — no change |
| PROBLEMS | N/A | REMOVE from nav — content moves into Cohort 1 |

**Nav style:** Text labels only. All-caps. Public Sans. Letter-spacing `+0.05em`. Active state: 1px underline in `#021934`. No icons. No dropdowns.

---

## 1.4 User Personas

### Persona A — Institutional Partner / Sponsor
- Arrives via LinkedIn, press, or direct referral
- Wants to evaluate credibility, institutional backing, and research quality
- Key pages: Home, About, Cohort 1, AI Ethics
- Conversion goal: Email inquiry via Contact page

### Persona B — Research Participant / Applicant
- Student or early-career researcher considering applying to future cohorts
- Wants to understand problem statements, timeline, prizes, mentors, judges
- Key pages: Cohort 1, Contact
- Conversion goal: Newsletter subscription (email capture)

### Persona C — Investor / Press
- Evaluating platform legitimacy and proof of scale
- Wants to see team, institutional partners, cohort outcomes
- Key pages: Home, About, Meet the Team, Special Thanks
- Conversion goal: Contact or media inquiry

---

## 1.5 Cohort 1 Page — Section Order

| # | Section Name | Source | Content Notes |
|---|---|---|---|
| 01 | Hero / Overview | Existing — keep | Title, venue, dates, tagline quote |
| 02 | Timeline | Existing — keep | Six specific dated entries |
| 03 | Prize Structure | Existing — keep | ₹1.5L overall, ₹10K per category |
| 04 | Problem Statements | MOVED FROM /problems | Expandable accordion cards — all 5 problems |
| 05 | Judges | Existing — keep | 4 judges with photos, bios, focus/affiliation tags |
| 06 | Mentors | Existing — keep | 4 KCDH IIT Bombay researchers with bios |
| 07 | Coming Soon / Cohort 2 | Existing — keep | Collapsed dark panel |

**Internal anchor nav** (sticky, below page hero): Overview · Problems · Judges · Mentors

---

## 1.6 Newsletter Section — Full Spec

**Placement:** Standalone section on Home page (above footer) AND as a persistent component in the global footer across all pages.

| Element | Spec |
|---|---|
| Section label | `STAY INFORMED` — all-caps, Public Sans, letter-spacing +0.05em, color #707785 |
| Headline | "Research updates, directly to your inbox." — Newsreader serif, 2.5rem |
| Sub-copy | "Weekly dispatches on MedTech research, cohort updates, and institutional announcements." |
| Input field | Placeholder: "Email address" — underline-only style, placeholder text #707785 |
| CTA button | `SUBSCRIBE` — primary navy button (#021934), white text, 4px radius, Public Sans |
| Success state | Inline: "You're on the list." — replaces button, no page reload |
| Duplicate state | Inline: "You're already subscribed." — no error crash |
| Invalid state | Inline: "Please enter a valid email." — color #707785, below input |
| Backend | Supabase — inserts row into `newsletter_subscribers` table |

---

## 1.7 Meet the Team Page — Full Spec

**Route:** `/team` | **Linked from:** Footer | **Not in main navbar**

| Section | Content |
|---|---|
| Hero | Label: `OUR FOUNDATION`. Headline: "Meet the Team." — Newsreader italic serif, large. Sub: "The people who built AesCode Cohort 1.0 from the ground up." |
| Founder & CEO | Nikhil Gour — large portrait, role label FOUNDER & CEO, bio. Asymmetric layout: portrait left, text right. |
| Co-Lead | Janushi Bhatia — portrait right, text left (alternating) |
| Operations + Finance | Shruti Deshpande (Operations Head) + Sahil Kankariya (Finance Head) — 2-column grid row |
| Organising Secretariat | 4-up grid: Siddharta Kakani, Saurabh Sharma, Anshika Gupta, Srishti Jain — label `ORGANISING SECRETARIAT` |
| Closing Quote | Large italic serif pullquote: "We are not just building software; we are cultivating the next generation of intellectual architects who understand the poetry in the code." — attributed: THE COLLECTIVE MISSION OF AESCODE CO. |

---

## 1.8 Special Thanks Page — Full Spec

**Route:** `/thanks` | **Linked from:** Footer | **Not in main navbar**

**Hero:** Headline "Special Thanks." — Newsreader italic. Sub: "AesCode Co. stands on the foundations of clinical excellence and rigorous research. We extend our gratitude to the leadership whose mentorship and institutional support have guided our technical evolution."

**Layout per honoree:** Illustrated B&W portrait + numbered category tag + long bio + 2–3 tagged links. Alternating image-left / image-right.

| # | Honoree | Category Label | Bio Summary |
|---|---|---|---|
| 01 | Dr. (Brig) S.P. Gorthi | CLINICAL LEADERSHIP | Distinguished neurologist, 40+ years, AIIMS, Bharati Vidyapeeth Head of Neurology, Pune. Awards: ML Soni, Best Research Paper IANeurology 2001, Stinfer Patel Award. |
| 02 | Dr. Raghavendran Lakshminarayan | SCIENTIFIC STRATEGY | Data Analyst & Bioinformatics SME, Operations Lead & Senior Program Officer. AI/ML for complex healthcare challenges. George-August University Göttingen. |
| 03 | Dr. Kshitij Jadhav | CURRICULUM DESIGN | Assistant Professor, KCDH IIT Bombay. MBBS + MD Pharmacology (Lausanne). Postdoc Cambridge UK. Multimodal data integration, high-dimensional data analysis. |
| 04 | Dr. Varsha Vaidya | ECOSYSTEM PARTNERSHIP | Professor of Medicine, Bharati Vidyapeeth since 1980. MBBS + DPH (Grant Medical) + PhD (Mumbai) + MD (Bharati). 150 total citations, h-index 6. |

**Closing line:** "And to our contributors who wish to remain anonymous." — Newsreader italic, centered. Sub: YOUR SILENCE IS AS VALUED AS YOUR SPEECH.

---

## 1.9 AI Ethics Page — Full Spec

**Route:** `/ai-ethics` | **In main navbar**

| Section | Content |
|---|---|
| Hero | Label: `FOUNDATIONAL FRAMEWORK`. Headline: "AI Ethics" — Newsreader italic, large. Sub: "Aescode Co. operates at the frontier of healthcare artificial intelligence, where technical capability must be matched by a rigorous moral architecture." Meta tag: VERSION 2.4 / REGULATORY COMPLIANCE |
| Why AI Ethics Matters | Left: serif heading "Why AI Ethics Matters in MedTech". Right: body text + image. "Artificial intelligence in healthcare is not a neutral tool. It is a decision-support mechanism that interacts directly with patient outcomes." |
| Our Ethical Principles | Label: `THE FIVE OPERATIONAL PILLARS OF AESCODE AI`. 5-column numbered grid: (01) Clinical Safety First · (02) Transparent Algorithmic Reasoning · (03) Data Governance and Privacy · (04) Human-in-the-Loop Medical Oversight · (05) Responsible Deployment Frameworks |
| Governance Philosophy | Left column serif italic heading + body: "Aescode approaches AI governance as a systems problem, not a checklist. We integrate ethical checkpoints directly into the CI/CD pipeline." |
| Research and Policy Alignment | Right column serif italic heading + body: "The governance of medical AI does not exist in a vacuum. We actively collaborate with global regulatory bodies and academic institutions." |
| Closing Statement | Large Newsreader italic: "Aescode Co. is committed to building a medtech innovation ecosystem where ethical governance is not an afterthought — it is architecture." |
| CTA | `EXPLORE OUR RESEARCH INITIATIVES →` — tertiary text link |

---

## 1.10 Global Footer — Standardized Spec

> This exact footer renders on every page without exception. Build as a single reusable component.

**Three-column layout (12-column grid):**

| Column | Content |
|---|---|
| Left (col 1–4) | Brand mark: **AESCODE CO.** in bold Public Sans, all-caps. Tagline: *MedTech Research. Clinically Grounded. Institutionally Anchored.* in Newsreader italic. |
| Center (col 5–8) | Label: `LEGAL & DOCUMENTATION`. Links: Privacy Policy · Terms of Service · Archive · RSS |
| Right (col 9–12) | Label: `CONNECT`. Links: Meet the Team · Special Thanks. Copyright: © 2026 AESCODE CO. Version: V1.1.0-RELEASE |

**Footer rules:**
- Background: `#FCF9F8` (same as surface — no border-top)
- Separation from page content: 80px+ vertical whitespace only
- All link text: Public Sans, label-sm, all-caps, color #707785
- Social icons: optional — LinkedIn + X only, right-aligned below copyright

---

## 1.11 Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | Newsletter email capture submits to Supabase `newsletter_subscribers` table | P0 |
| FR-02 | Success/error states display inline without page reload | P0 |
| FR-03 | Cohort 1 Problem Statements render as expandable accordion cards | P0 |
| FR-04 | All pages render the standardized footer component | P0 |
| FR-05 | Navigation reflects updated tabs: AI Ethics added, Problems removed | P0 |
| FR-06 | AI Ethics page accessible at `/ai-ethics` | P0 |
| FR-07 | Meet the Team page accessible at `/team`, linked from footer | P1 |
| FR-08 | Special Thanks page accessible at `/thanks`, linked from footer | P1 |
| FR-09 | Cohort 1 sections ordered: Overview → Timeline → Prizes → Problems → Judges → Mentors | P1 |
| FR-10 | Dot-grid background overlay present at opacity 0.03 on all pages | P2 |
| FR-11 | All newsletter submissions timestamped with `created_at` | P1 |
| FR-12 | Duplicate email submission handled gracefully — no crash, friendly message | P1 |

---

## 1.12 Non-Functional Requirements

| Category | Requirement |
|---|---|
| Performance | LCP < 2.5s on desktop. Images served as WebP. |
| Accessibility | WCAG 2.1 AA. All images have alt text. Color contrast ratios met. |
| Responsiveness | Mobile-first. Breakpoints: 375px, 768px, 1280px, 1440px. |
| SEO | Meta title + description on every page. OG tags for social sharing. |
| Security | Supabase RLS: anon key = insert-only on newsletter table. No admin panel public-facing. |
| Uptime | Vercel or Netlify — 99.9% SLA. |
| Design Fidelity | Zero gradients. Zero glassmorphism. Zero border-radius > 4px. Strict DESIGN.md adherence. |

---

---

# SECTION 2 — UX Flow Documentation

---

## 2.1 User Journey — First-Time Institutional Visitor

| Step | Page | Action | Outcome |
|---|---|---|---|
| 1 | Home | Reads hero headline + gap section | Understands mission and positioning |
| 2 | Home | Scrolls to stats (250+, 100+, 20, 5, ₹1.5L+) + partner logos | Establishes scale and institutional credibility |
| 3 | About | Reads origin story, platform pillars | Understands research-first positioning |
| 4 | Cohort 1 | Reviews timeline, problem statements, judges | Evaluates program quality |
| 5 | AI Ethics | Reviews governance principles | Assesses institutional seriousness |
| 6 | Contact | Copies email | Sends inquiry |

---

## 2.2 User Journey — Research Participant / Applicant

| Step | Page | Action | Outcome |
|---|---|---|---|
| 1 | Home | Lands via event link. Sees CTA: EXPLORE COHORT 1. | Clicks through |
| 2 | Cohort 1 | Reviews overview, timeline, prize structure | Determines eligibility and interest |
| 3 | Cohort 1 | Expands Problem Statement accordion cards. Reads problem context + dataset links. | Selects preferred problem |
| 4 | Cohort 1 | Reviews judges and mentors bios | Assesses program quality |
| 5 | Home / Footer | Finds newsletter section | Subscribes with email |
| 6 | Contact | If questions remain | Emails inquiry |

---

## 2.3 User Journey — Newsletter Subscriber

| Step | Element | Interaction | System Response |
|---|---|---|---|
| 1 | Newsletter input | Types email | Border transitions to navy #021934 at 1.5px |
| 2 | Subscribe button | Clicks SUBSCRIBE or presses Enter | Button: opacity 0.6, cursor not-allowed (loading) |
| 3a — Success | Inline | Email saved to Supabase | "You're on the list." replaces button |
| 3b — Duplicate | Inline | Supabase unique violation | "You're already subscribed." |
| 3c — Invalid | Inline | Client-side validation | "Please enter a valid email." — below input |

---

## 2.4 Interaction States — Component Level

| Component | State | Visual Treatment |
|---|---|---|
| Nav link | Default | Public Sans, all-caps, #707785, no underline |
| Nav link | Hover | Color → #021934 |
| Nav link | Active | #021934 + 1px underline below text |
| Primary button | Default | Background #021934, text #FFFFFF, 4px radius |
| Primary button | Hover | Opacity 0.88 |
| Primary button | Loading | Opacity 0.6, cursor not-allowed |
| Primary button | Disabled | Opacity 0.4 |
| Email input | Default | Underline only — 0.5px #C4C6CE |
| Email input | Focus | Underline → 1.5px, color #021934 |
| Problem accordion | Collapsed | Category label + title + summary + "+" icon right-aligned |
| Problem accordion | Expanded | Full context + ML task + dataset link + "−" icon |
| Partner logo | Default | Grayscale / monochrome |
| Partner logo | Hover | Full color treatment |

---

---

# SECTION 3 — Technical Architecture

---

## 3.1 Frontend Component Hierarchy

### Global Components (every page)
- `NavBar` — logo, nav links, active state logic
- `Footer` — 3-column standardized layout
- `DotGridBackground` — CSS pseudo-element, opacity 0.03, z-index 0, pointer-events none
- `NewsletterBlock` — reusable email capture (Home section + Footer variant)

### Page Components
- `HomePage` — Hero, GapSection, MissionColumns, StatsBar, PartnersSection, NewsletterSection, Cohort2Teaser
- `AboutPage` — ManifestoHero, OriginStory, PlatformPillars, FeaturedQuote, Cohort2ComingSoon
- `Cohort1Page` — CohortHero, Philosophy, Timeline, Prizes, **ProblemsAccordion**, Judges, Mentors, Cohort2Panel
- `AIEthicsPage` — EthicsHero, WhyEthicsMatters, PrinciplesGrid, GovernanceSection, ClosingStatement
- `ContactPage` — ContactHero, EmailDisplay
- `TeamPage` — TeamHero, FounderSection, LeadsSection, SecretariatGrid, ClosingQuote
- `ThanksPage` — ThanksHero, HonoreeList, AnonymousClosing

### Shared UI Primitives
- `HeroBlock(label, headline, subtext, meta)` — standardized page hero
- `PersonCard(name, role, bio, focus, affiliation, imageUrl)` — Judges, Mentors, Team, Thanks
- `AccordionCard(category, title, summary, mlTask, expectedOutput, datasetUrl)` — Problem Statements
- `StatItem(value, label)` — Stats bar
- `PartnerLogo(src, alt, colorOnHover)` — Institutional partner logos

---

## 3.2 Backend — Supabase Setup

- **Auth:** No user authentication required. Public-facing site only.
- **Public key:** Supabase anon key used for newsletter insert only.
- **API calls:** Direct REST via `supabase-js` v2 client from frontend.
- **Env vars:** `SUPABASE_URL` and `SUPABASE_ANON_KEY` in `.env.local`. Never commit to repo.
- **Admin access:** Subscriber list accessed only via Supabase Studio with service role key.

---

## 3.3 Newsletter Data Flow

```
1. User types email
   → Client-side regex validation
   → If invalid: show inline error, STOP

2. If valid:
   → supabase.from('newsletter_subscribers').insert({ email, source, created_at })

3. Supabase checks UNIQUE constraint on email

4a. HTTP 201 (success)
    → setState('subscribed')
    → Render: "You're on the list."

4b. HTTP 409 (unique violation)
    → Render: "You're already subscribed."

4c. Other error
    → Render: "Something went wrong. Try again."
```

---

## 3.4 Deployment Stack

| Service | Provider | Notes |
|---|---|---|
| Hosting | Vercel (recommended) | Free tier. Auto-deploy from GitHub `main`. |
| Domain | aescode.nexus (GoDaddy) | Add CNAME in GoDaddy → Vercel deployment URL |
| Database | Supabase | Free tier — 500MB, sufficient for launch |
| Fonts | Google Fonts CDN | Newsreader + Public Sans. Preload in `<head>`. |
| Images | `/public/images/` in repo | All portraits as WebP, < 200KB each |
| Env vars | Vercel Environment Variables | `SUPABASE_URL`, `SUPABASE_ANON_KEY` only |

---

---

# SECTION 4 — Database Design (Supabase)

---

## 4.1 Table: `newsletter_subscribers`

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | `uuid` | PRIMARY KEY, DEFAULT `gen_random_uuid()` | Auto-generated |
| `email` | `text` | NOT NULL, UNIQUE | Lowercase enforced via trigger |
| `created_at` | `timestamptz` | NOT NULL, DEFAULT `now()` | UTC timestamp |
| `source` | `text` | DEFAULT `'website'` | Track origin: `'home'`, `'footer'`, `'cohort1'` |
| `is_active` | `boolean` | DEFAULT `true` | For future unsubscribe handling |

---

## 4.2 Table: `cohorts` (scaffolded for Cohort 2+)

| Column | Type | Notes |
|---|---|---|
| `id` | `uuid` | PRIMARY KEY |
| `slug` | `text` | UNIQUE — e.g. `cohort-1` |
| `title` | `text` | Display name |
| `status` | `text` | `active` / `archived` / `coming_soon` |
| `venue` | `text` | Location string |
| `start_date` | `date` | |
| `end_date` | `date` | |
| `prize_total` | `text` | e.g. `₹1,50,000` |
| `created_at` | `timestamptz` | DEFAULT `now()` |

---

## 4.3 Table: `problem_statements` (scaffolded for future CMS)

| Column | Type | Notes |
|---|---|---|
| `id` | `uuid` | PRIMARY KEY |
| `cohort_id` | `uuid` | FK → `cohorts.id` |
| `category_label` | `text` | e.g. `DIABETIC CARE` |
| `title` | `text` | Full problem title |
| `summary` | `text` | One-line description |
| `ml_task` | `text` | |
| `expected_output` | `text` | |
| `dataset_url` | `text` | Kaggle or external link |
| `sort_order` | `integer` | DEFAULT 0 |

---

## 4.4 Row-Level Security Policies

| Table | Policy Name | Permission | Role |
|---|---|---|---|
| `newsletter_subscribers` | `allow_public_insert` | INSERT only | `anon` |
| `newsletter_subscribers` | `block_public_select` | NO SELECT | `anon` |
| `newsletter_subscribers` | `admin_full_access` | ALL | `service_role` |
| `cohorts` | `allow_public_read` | SELECT only | `anon` |
| `problem_statements` | `allow_public_read` | SELECT only | `anon` |

---

## 4.5 SQL — Run in Supabase Studio

```sql
-- Newsletter subscribers table
CREATE TABLE newsletter_subscribers (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  email text NOT NULL UNIQUE,
  created_at timestamptz NOT NULL DEFAULT now(),
  source text DEFAULT 'website',
  is_active boolean DEFAULT true
);

-- Normalize email to lowercase on insert
CREATE OR REPLACE FUNCTION lowercase_email()
RETURNS trigger AS $$
BEGIN
  NEW.email = lower(NEW.email);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER lowercase_email_trigger
BEFORE INSERT ON newsletter_subscribers
FOR EACH ROW EXECUTE FUNCTION lowercase_email();

-- Enable RLS
ALTER TABLE newsletter_subscribers ENABLE ROW LEVEL SECURITY;

-- Anon can insert only
CREATE POLICY allow_public_insert ON newsletter_subscribers
  FOR INSERT TO anon WITH CHECK (true);

-- Anon cannot read
CREATE POLICY block_public_select ON newsletter_subscribers
  FOR SELECT TO anon USING (false);
```

---

---

# SECTION 5 — Risk & Assumptions Log

---

## 5.1 Technical Risks

| Risk | Severity | Mitigation |
|---|---|---|
| Supabase anon key exposed in frontend JS bundle | HIGH | Acceptable for insert-only. RLS blocks all reads. Never use service_role key in frontend. |
| Email field not normalized — case duplicates | MEDIUM | Lowercase trigger (SQL in Section 4.5 handles this) |
| Accordion breaks on mobile if problem text is very long | MEDIUM | Test on 375px. Use `overflow: hidden` + proper `max-height` transition. |
| Google Fonts CDN blocked in some regions | LOW | Add `font-display: swap`. Fallback: `Georgia, serif` / `system-ui, sans-serif` |
| Portrait images too large → slow LCP | MEDIUM | Convert all to WebP < 200KB. Lazy load below-fold portraits. |
| Footer inconsistency across pages | HIGH | Build Footer as single component. Import identically on every page. Never inline. |

---

## 5.2 UX Risks

| Risk | Severity | Mitigation |
|---|---|---|
| `/team` and `/thanks` not discoverable — footer-only links | MEDIUM | Add "Meet the Team" CTA on About page as well |
| Problem accordion cards may not signal interactivity in editorial aesthetic | MEDIUM | Use `+` icon right-aligned. Ghost border on card hover (background → #FFFFFF). |
| Newsletter section feels like marketing on academic site | LOW | Label as "Research Updates" not "Newsletter". Frame as dispatch. |
| Cohort 1 page becomes too long with added sections | MEDIUM | Add sticky internal anchor nav: Overview · Problems · Judges · Mentors |

---

## 5.3 Antigravity-Specific Failure Modes

| Failure Mode | Prevention |
|---|---|
| Antigravity applies SaaS defaults (rounded corners, gradients, shadows) | In every prompt: explicitly forbid border-radius > 4px, gradients, glassmorphism. Paste the Design System Rules block. |
| Antigravity generates icon-based navigation | Explicit instruction: text-only nav labels, all-caps, Public Sans. No icons. |
| Antigravity stacks components symmetrically by default | Cite asymmetric grid requirement. Specify column offsets per section. |
| Supabase integration generated with service_role key | In every DB prompt: use anon key only. Specify RLS policy explicitly. |
| Footer differs between pages | Build footer as standalone component first. Reference in every page prompt by component name. |
| Typography drifts — system fonts used instead of specified fonts | Every prompt: specify Newsreader (serif) for headlines, Public Sans for body. Include Google Fonts import. |

---

## 5.4 Assumptions

- Domain `aescode.nexus` is owned and DNS is accessible for CNAME configuration
- Portrait images for all team members, judges, and Special Thanks honorees are available in high-res
- Problem statement content is final as per `Problem_Statements_v2.docx`
- Cohort 1 is complete — the page is an archive, not a live application portal
- No user authentication, participant submission portal, or judging interface is required at launch
- Newsletter is one-way — no automated email sending required at launch (manual export from Supabase Studio)
- Cohort 2 section remains collapsed as "Coming Soon" with email capture as the only CTA

---

---

# SECTION 6 — Execution Guidelines for Antigravity

---

## 6.1 Build Order — Step by Step

| Phase | Step | Task | Dependency |
|---|---|---|---|
| 1 — Foundation | 1 | Set CSS design tokens (Section 3.1) | None |
| 1 — Foundation | 2 | Build NavBar component (updated tabs) | Design tokens |
| 1 — Foundation | 3 | Build Footer component (standardized spec) | Design tokens |
| 1 — Foundation | 4 | Build DotGridBackground component | Design tokens |
| 1 — Foundation | 5 | Build NewsletterBlock — UI only, no backend | Design tokens |
| 2 — Supabase | 6 | Create Supabase project. Run SQL (Section 4.5) | None |
| 2 — Supabase | 7 | Connect NewsletterBlock to Supabase — wire insert + all states | Steps 5, 6 |
| 3 — Pages | 8 | Build Home page | Steps 1–7 |
| 3 — Pages | 9 | Build About page | Steps 1–4 |
| 3 — Pages | 10 | Build Cohort 1 page with ProblemsAccordion | Steps 1–4 |
| 3 — Pages | 11 | Build AI Ethics page | Steps 1–4 |
| 3 — Pages | 12 | Build Meet the Team page | Steps 1–4 |
| 3 — Pages | 13 | Build Special Thanks page | Steps 1–4 |
| 3 — Pages | 14 | Build Contact page | Steps 1–4 |
| 4 — QA | 15 | Cross-page footer consistency check | All pages |
| 4 — QA | 16 | Mobile responsiveness check (375px, 768px, 1280px) | All pages |
| 4 — QA | 17 | Newsletter end-to-end test (success, duplicate, invalid) | Step 7 |
| 5 — Deploy | 18 | Deploy to Vercel. Configure domain in Vercel + GoDaddy. | Steps 15–17 |

---

## 6.2 Component Priority Matrix

| Priority | Component | Rationale |
|---|---|---|
| P0 — Build first | NavBar, Footer, Design Tokens | Errors here multiply across all pages |
| P0 — Build first | NewsletterBlock + Supabase connection | Core new feature — validate early |
| P1 — Build second | Home page, About page | Primary landing surfaces |
| P1 — Build second | Cohort 1 with ProblemsAccordion | Longest page — most complex assembly |
| P2 — Build third | AI Ethics page | New page — relatively self-contained |
| P2 — Build third | Meet the Team, Special Thanks | Content-heavy but structurally simple |
| P3 — Build last | Contact page | Simplest page — email display only |

---

## 6.3 Stitch Prompt Template

> Use this structure for every Stitch execution prompt.

```
PAGE: [Page Name]
ROUTE: [/route]

DELETE:
- [Exact section or element to remove]
- [Exact section or element to remove]

ADD:
- [New section/element with full content]
- [New section/element with full content]

UPDATE:
- [Element]: "[Old copy]" → "[New copy]"

CONTENT:
[Full content blocks in order, labeled by section]

TYPOGRAPHY:
- [Element]: [Font], [size], [weight], [color]

COLOR:
- [Section background]: [hex]
- [Text]: [hex]

DO NOT CHANGE:
- [Element that must remain exactly as-is]
- [Element that must remain exactly as-is]

DESIGN RULES: [Paste the Design System Rules block from the top of this document]
```

---

## 6.4 Critical Failure Points — How to Avoid

| Failure Mode | How to Avoid |
|---|---|
| Footer differs between pages | Build Footer as a single reusable component. Import identically. Never inline footer HTML on any page. |
| Newsletter form causes full page reload | Use `preventDefault()` on submit handler. Manage all response state at component level. |
| Problem accordion — all cards open simultaneously | Implement single-open logic: `state = activeIndex`. Closing previously open card when new one opens. |
| Newsreader font not loading | Add `<link rel="preload">` for Newsreader in `<head>`. Import weights: 400, 400italic, 700. |
| Supabase CORS error in development | Add `localhost:3000` to Supabase → Authentication → URL Configuration → Allowed Origins. |
| Portrait images cause layout shift | Set explicit `width` and `height` attributes. Use `aspect-ratio` CSS to reserve space before load. |
| Mobile nav breaks editorial grid | At mobile breakpoint: hamburger or stacked list. Maintain all-caps, Public Sans, navy active state. |
| Dot-grid overlay blocks interaction | `z-index: 0` on overlay. `z-index: 1` on all content containers. `pointer-events: none` on overlay. |

---

## 6.5 Deployment Checklist

- [ ] All images converted to WebP, optimized < 200KB per image
- [ ] Google Fonts preloaded in `<head>` for Newsreader and Public Sans
- [ ] `SUPABASE_URL` and `SUPABASE_ANON_KEY` set as env vars in Vercel
- [ ] Supabase RLS verified: anon can INSERT but NOT SELECT on `newsletter_subscribers`
- [ ] Custom domain CNAME configured in GoDaddy → Vercel deployment URL
- [ ] SSL auto-provisioned by Vercel (Let's Encrypt)
- [ ] Meta title + OG description set on every page
- [ ] Footer version tag: `V1.1.0-RELEASE`
- [ ] Copyright year: `© 2026 AESCODE CO.`
- [ ] Newsletter flow tested end-to-end on production domain
- [ ] Accordion cards tested on 375px mobile and 1440px desktop
- [ ] Dot-grid overlay visible but not obstructing any content or interaction
- [ ] Internal anchor nav on Cohort 1 page working and sticky

---

---

## Problem Statements — Content Reference (for Cohort 1 Accordion)

> Hardcode these directly into the `ProblemsAccordion` component.

### PS-01 — AI-Based Prediction of High-Risk Plantar Pressure Zones
- **Category:** DIABETIC CARE
- **Summary:** Identifying high-pressure areas in diabetic patients to prevent ulceration through early biomechanical intervention.
- **ML Task:** Supervised ML — Classification / Risk Prediction. Time-series forecasting / Heatmap Regression.
- **Expected Output:** Pressure hotspot detection map · Ulcer risk score for foot regions · Plantar pressure distribution visualization
- **Dataset:** [kaggle.com/datasets/khalidsiddiqui2003/dfu-dataset-annotated-into-4-classes](https://www.kaggle.com/datasets/khalidsiddiqui2003/dfu-dataset-annotated-into-4-classes)

### PS-02 — AI-Based Early Warning System for Patient Physiological Deterioration
- **Category:** PATIENT MONITORING
- **Summary:** Detecting subtle patterns in vital signs that precede clinical decompensation in acute care settings.
- **ML Task:** Time-Series Prediction / Binary Classification. Anomaly Detection / Multi-modal sequence modelling.
- **Expected Output:** Real-time risk score with clinical reasoning flags · Dashboard visualization of patient vitals
- **Dataset:** [kaggle.com/datasets/tarekmasryo/hospital-deterioration-dataset](https://www.kaggle.com/datasets/tarekmasryo/hospital-deterioration-dataset)

### PS-03 — AI-Based Osteoporosis Risk Screening from Routine X-Ray Radiographs
- **Category:** BONE HEALTH
- **Summary:** Analyzing opportunistic imaging data to screen for low bone density in asymptomatic populations.
- **ML Task:** Computer Vision — Image Classification. Computer Vision / Feature Extraction.
- **Expected Output:** Probabilistic fracture risk index · Binary or multi-class classification (Normal / Osteopenia / Osteoporosis)
- **Dataset:** [kaggle.com/datasets/kmader/rsna-bone-age](https://www.kaggle.com/datasets/kmader/rsna-bone-age)

### PS-04 — AI-Based Detection of Incorrect Exercise Form Using Human Pose Estimation
- **Category:** REHABILITATION
- **Summary:** Providing real-time feedback on kinetic alignment to ensure safe and effective home-based physical therapy.
- **ML Task:** Computer Vision + Classification. Pose Estimation / Temporal Action Localization.
- **Expected Output:** Correction vectors and form quality score · Classification: Correct / Incorrect (with optional error categories: knee valgus, asymmetrical squat, forward trunk lean)
- **Dataset:** [kaggle.com/datasets/matthewjansen/ucf101-action-recognition](https://www.kaggle.com/datasets/matthewjansen/ucf101-action-recognition)

### PS-05 — AI-Based Infarct Volume Estimation from Non-Contrast CT for Acute Anterior Circulation Stroke
- **Category:** STROKE
- **Summary:** Automating the precise measurement of ischemic core and penumbra to guide urgent thrombectomy decisions.
- **ML Task:** Medical Image Segmentation + Regression. 3D Image Segmentation.
- **Expected Output:** Quantified volume in mL and vascular territory map · Infarct segmentation overlay on CT slices · Optional severity classification: Small (<30mL) / Medium (30–70mL) / Large (>70mL)
- **Dataset:** [kaggle.com/datasets/orvile/cpaisd-acute-ischemic-stroke-dataset](http://www.kaggle.com/datasets/orvile/cpaisd-acute-ischemic-stroke-dataset)

---

*AesCode Co. — Build System Master Document | Version 1.0 | April 2026*
