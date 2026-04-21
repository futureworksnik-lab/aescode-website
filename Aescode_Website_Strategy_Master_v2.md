# AESCODE CO. — WEBSITE STRATEGY MASTER DOCUMENT
### Website Audit · Revised IA · Full Page Content · Antigravity Execution Prompts · QA Framework

**Prepared:** April 2026  
**Source of Truth:** Aescode Founder Blueprint (April 2026), AesCode Build System v1.0, DESIGN.md, live site audit of aescode.nexus  
**Design Constraint:** Visual identity, design system, and aesthetic are FROZEN. Zero changes to typography, color tokens, spacing, or component logic.  
**Aristotle Cross-Check Applied Throughout:** Every recommendation maps to an irreducible component of the platform. No speculation without evidence from the live site or the Blueprint.

---

## ARISTOTLE FIRST-PRINCIPLES BASELINE

Before any recommendation is made, the following irreducible truths (drawn directly from the Founder Blueprint) govern every decision in this document:

| Truth | Implication for Website |
|---|---|
| Clinical AI will not be deployed without trust | Every page must reinforce trust infrastructure, not innovation theater |
| Patient data cannot move to engineers; federated learning is the only architecturally sound path | The platform narrative must explain federated learning clearly, not bury it |
| Institutional credibility is earned through co-creation, not co-branding | Bharati Hospital is a co-builder, not a logo — language must reflect this |
| The 250+ research abstracts are a dataset, not a participation metric | They must be framed as intellectual output and proof of demand |
| IIT Bombay MoU has ended; the association is historical | Every reference to IIT Bombay must be past-tense or individual-faculty-specific |
| Speed is the only real competitive advantage in this 18–24 month window | Website execution must be deterministic and fast — no scope creep |

---

---

# SECTION A — WEBSITE AUDIT

---

## A.1 — Page-by-Page Audit

### PAGE 01: Home (`/index.html`)

**Current State:**
- Hero: "A New Paradigm in Translational Tech" / "Advancing Clinical Research Through Engineering"
- Two CTAs: `Explore Cohort 1` and `Get Involved`
- Section: "The Gap" — explains mission to close clinical-engineering divide
- Primary Mission + Secondary Mission (startup incubation)
- Scrolling marquee stats: 250+ abstracts, 100+ teams, 20 finalists, 5 problems, 14 days, ₹1.5L+
- Pullquote: "We are not just building software; we are cultivating..."
- Newsletter section (email capture)

**Audit:**

| Element | Verdict | Rationale |
|---|---|---|
| Hero headline | **REWRITE** | "A New Paradigm in Translational Tech" is vague and forgettable. The Blueprint's one-sentence positioning is far more powerful. |
| Hero subheadline | **REWRITE** | "MedTech research platform" framing is correct but current copy is generic. |
| CTA 1: "Explore Cohort 1" | **RETAIN** | Correct primary CTA for proof-of-work visitors |
| CTA 2: "Get Involved" | **REWRITE to "Partner With Us"** | "Get Involved" implies volunteering. "Partner With Us" signals institutional intent. |
| "The Gap" section | **REWRITE** | Good framing but doesn't use the Blueprint's sharp language around ABDM, trust as the bottleneck, or the federated learning architecture. |
| Primary/Secondary Mission | **RESTRUCTURE** | Secondary mission (incubation) should not appear on Home. It dilutes the research infrastructure positioning. Move to About page. |
| Marquee stats | **RETAIN + ADD CONTEXT** | Stats are credibility anchors. Add a one-line caption under each stat to explain what it means. |
| Pullquote | **RETAIN** | Strong voice. On-brand. Keep exactly as-is. |
| Newsletter section | **RETAIN** | Functional. Retain positioning above footer. |
| Partner logos section | **ADD** | Critical gap. No partner/institutional logos visible on Home. Bharati Hospital and KCDH IIT Bombay (historical) logos must appear. |
| "Why Now" section | **ADD** | The three convergences from the Blueprint (ABDM at 834M, regulation hardening, Apollo deploying certified AI) make a powerful first-principles case. Must appear on Home. |

**Structural Weaknesses:**
- No institutional anchoring above the fold — a first-time visitor has no signal of credibility until they scroll
- The homepage reads like a hackathon event, not infrastructure
- No explicit mention of Bharati Hospital until deep scroll
- No explanation of what makes Aescode different from other MedTech hackathons
- Missing "Why Now" argument — the window argument is the strongest investor/partner hook

---

### PAGE 02: About (`/about.html`)

**Current State:**
- Origin story anchored to Nexus 3.0 + KCDH IIT Bombay + Bharati Vidyapeeth
- Key partners listed: KCDH IIT Bombay, Bharati Vidyapeeth
- 4 platform pillars: Primary Mission, Research Methodology, Secondary Function, Institutional Grounding
- Attribution to KCDH IIT Bombay and Bharati Vidyapeeth as ongoing institutional framework
- "Cohort 2 Coming Soon" CTA at bottom

**Audit:**

| Element | Verdict | Rationale |
|---|---|---|
| Origin story | **REWRITE** | Currently presents IIT Bombay MoU as ongoing. Blueprint is explicit: MoU has ended. Must be corrected to avoid misrepresentation. Historical framing: "in partnership with" → "co-hosted with" |
| Key Partners callout | **REWRITE** | Must not list KCDH IIT Bombay as a current partner. Bharati Hospital is the current primary anchor. |
| 4 platform pillars | **RETAIN + EXPAND** | Good structure. Add a 5th pillar: Federated Learning Infrastructure, which is the architectural differentiator. |
| "KCDH provides institutional foundation" | **REWRITE** | Too close to misrepresentation. Rephrase as historical contribution to Cohort 1. |
| Closing pullquote | **RETAIN** | Strong. On-brand. |
| "Cohort 2 Coming Soon" | **RETAIN** | Signals forward motion |
| Three-layer architecture (Layer 0/1/2) | **ADD** | The Talent Engine → Federated Data → Certification flywheel is the platform's most defensible IP. It must appear on About, visually. |
| Incubation / Secondary Mission | **MOVE HERE from Home** | About is the right place for the secondary function explanation |

**Structural Weaknesses:**
- No mention of federated learning or what makes the research methodology architecturally unique
- Overstates IIT Bombay relationship — legal/credibility risk
- Missing the ABDM alignment story which is the government partnership hook
- Platform vision is described in abstract terms; needs the 3-layer flywheel diagram or description

---

### PAGE 03: Cohort 1 (`/cohort1.html`)

**Current State:**
- Hero: "The Inaugural Cohort 1" with tagline and venue
- Timeline: 6 dated entries from Feb 15 to Apr 4
- Prizes: ₹1L first prize, ₹10K x5 category awards
- 5 Problem Statements (accordion expandable cards)
- 4 Judges: Dr. Dhane (IIT Kharagpur), Bhavik Kanekar (KCDH), Buddhadev Goswami (KCDH), Dr. Dulari Gupta (Neurologist)
- 3 Mentors: Viraj Gaur, Dr. Subham Ghosh, Shayantan Banerjee (all KCDH IIT Bombay)
- Testimonials placeholder ("Coming Soon")
- Archive image placeholder
- "Cohort 2 Coming Soon" CTA

**Audit:**

| Element | Verdict | Rationale |
|---|---|---|
| Hero section | **RETAIN — minor copy adjustment** | Strong. Archive framing is good. |
| Timeline | **RETAIN** | Specific, credible, well-structured |
| Prize structure | **RETAIN** | Clear |
| Problem Statements (all 5) | **RETAIN IN FULL** | Mission-critical. These 5 problems are the proof that Aescode works with real clinical problems. Do not compress or hide. |
| Judges section | **RETAIN IN FULL** | Strong credibility anchors. All 4 bios are detailed and valuable. |
| Mentors section | **RETAIN IN FULL** | All 3 KCDH researchers provide academic credibility. Keep full bios. |
| Testimonials placeholder | **REPLACE or REMOVE** | "Coming Soon" placeholder damages credibility. Replace with a structural insight from Cohort 1 (aggregated abstract analysis, key themes) until real testimonials arrive. |
| Archive placeholder | **ADD REAL CONTENT** | Empty image slot looks abandoned. Add 1-2 real cohort photos or remove the section entirely until photos are ready. |
| "What They Built" section | **REWRITE** | Frame this as "Cohort 1 Outcomes" — summarize the 5 problem domains and what the top teams produced, even in brief. |
| Abstract dataset insight | **ADD** | The Blueprint notes 250+ abstracts are the most underused asset. Add a brief "What 250 Engineers Told Us" section — top themes, problem clusters, key insight. This turns participation into intellectual output. |
| Internal anchor nav | **ADD** | Long page needs sticky anchor nav: Overview · Timeline · Problems · Judges · Mentors |

**Structural Weaknesses:**
- No cohort outcomes — what happened after the hackathon? Where are the top teams?
- No "What We Learned" signal — positions Aescode as an events company, not a research platform
- Testimonials placeholder actively hurts credibility
- Missing connection to Cohort 2 — the "Coming Soon" panel is visually heavy but strategically vague

---

### PAGE 04: AI Ethics (`/ai_ethics.html`)

**Current State:**
- Label: "GOVERNANCE PROTOCOL"
- Hero: "AI Ethics & Integrity" + version tag (v2.4 / DPDP & ICMR ALIGNMENT)
- "Necessity of Rigor in Indian MedTech" section
- 5 operational pillars: Non-Maleficence, Glass-Box Interpretability, Synthetic Data Sovereignty, Augmented Human Oversight, Staged Socio-Technical Rollouts
- "Governance as Code" and "Bridging Regulatory Gaps" subsections
- Closing pullquote
- CTA: "REVIEW OUR POLICY WHITEPAPER →" (broken link — leads to `/policy-whitepaper` which doesn't exist)

**Audit:**

| Element | Verdict | Rationale |
|---|---|---|
| Label "GOVERNANCE PROTOCOL" | **RETAIN** | Precise and authoritative |
| Hero headline | **RETAIN** | Clean and direct |
| Version tag (v2.4) | **RETAIN** | Signals living document, institutional process |
| "Necessity of Rigor" section | **REWRITE + STRENGTHEN** | Good intent but doesn't cite the specific Indian regulatory context clearly enough. Must explicitly reference DPDP Act 2023, ICMR 2023 guidelines, CDSCO SaMD. |
| 5 operational pillars | **RETAIN + RENAME PILLAR 3** | "Synthetic Data Sovereignty" is correct for Cohort 1 but contradicts the federated learning vision. Rename to "Privacy-Preserving Data Architecture" — covers both synthetic validation AND federated learning. |
| "Governance as Code" | **RETAIN** | Technically credible. Strong positioning. |
| "Bridging Regulatory Gaps" | **RETAIN + EXPAND** | Add ABDM consent framework reference and CDSCO SaMD pathway explicitly. |
| Closing pullquote | **RETAIN** | Strong institutional voice |
| CTA → broken link | **FIX IMMEDIATELY** | `/policy-whitepaper` returns 404. Either create the page or change CTA to Contact. This is a credibility-damaging error. |
| AI Ethics Framework as published document | **ADD** | Blueprint explicitly recommends publishing the framework as a co-authored document. Even a structured page version counts. |

**Structural Weaknesses:**
- Broken CTA link — top priority fix
- Pillar 3 creates internal contradiction with federated learning vision
- Missing explicit connection to Cohort evaluation process ("Every model submitted to Aescode is evaluated against this framework")
- No mention of ABDM alignment

---

### PAGE 05: Contact (`/contact.html`)

**Current State:**
- Headline: "Get in Touch."
- Single email address: aescode.nexus@gmail.com

**Audit:**

| Element | Verdict | Rationale |
|---|---|---|
| Gmail address | **UPGRADE** | A Gmail address is a trust signal failure for institutional visitors. Should be hi@aescode.nexus or partnerships@aescode.nexus |
| Single contact option | **EXPAND** | Add differentiated contact types: General Inquiries / Partnership & Institutional / Press & Media |
| Contact form | **ADD** | No form exists. For institutional partners, a form is more trustworthy than a bare email. Minimum: Name, Organization, Role, Message type, Message. |
| Social links | **ADD** | LinkedIn minimum. Provides alternate verification path. |
| FAQ or "Before You Write" section | **ADD** | Brief pre-contact section addressing common questions (When is Cohort 2? How do I apply? How do I partner?) saves both sides' time |

---

### PAGE 06: Meet the Team (`/meet_the_team.html`)

**Current State:**
- Full team displayed: Nikhil Gour (Founder & CEO), Janushi Bhatia (Co-Lead), Shruti Deshpande (Operations), Sahil Kankariya (Finance), 4 Organising Secretariat members
- Good photo quality and bio depth for senior members
- Closing pullquote

**Audit:**

| Element | Verdict | Rationale |
|---|---|---|
| Core team profiles | **RETAIN IN FULL** | Strong. Photos, roles, bios are appropriate |
| Organising secretariat grid | **RETAIN** | Signals organizational depth |
| Closing pullquote | **RETAIN** | On-brand |
| Advisory board section | **ADD** | Blueprint calls for 3 advisors with real equity. Even aspirationally framing an "Advisory Board — Forming" section signals institutional intent |
| Role titles | **REVIEW** | "Co-Lead" is vague for institutional visitors. Consider "Research Lead" or "Clinical Liaison Lead" |
| LinkedIn links per person | **ADD** | Standard professional practice. Increases credibility for institutional visitors doing due diligence |

---

### PAGE 07: Special Thanks (`/special_thanks.html`)

**Current State:**
- 4 honorees: Dr. Gorthi (Bharati Vidyapeeth), Dr. Raghavendran (KCDH), Dr. Kshitij Jadhav (KCDH), Dr. Varsha Vaidya (Bharati Vidyapeeth)
- Strong bios, category labels, alternating layout
- Institutional acknowledgment: Bharati Vidyapeeth × KCDH IIT Bombay

**Audit:**

| Element | Verdict | Rationale |
|---|---|---|
| All 4 honoree profiles | **RETAIN IN FULL** | High credibility content. Bios are appropriately detailed. |
| Category labels (Clinical Leadership, Scientific Strategy, etc.) | **RETAIN** | Precise and organized |
| Institutional acknowledgment at bottom | **REWRITE** | Currently frames both institutions as co-equal ongoing partners. Bharati Vidyapeeth is the primary active anchor. KCDH IIT Bombay contribution was for Cohort 1. Language must distinguish. |
| Page overall | **RETAIN** | One of the strongest credibility pages on the site. Do not compress. |

---

## A.2 — Global Structural Gaps (Cross-Site)

| Gap | Impact | Fix |
|---|---|---|
| No partner/logo strip anywhere on the site | High — institutional visitors see no third-party credibility | Add Bharati Hospital + KCDH IIT Bombay (Cohort 1 historical) logos to Home and About |
| No "Why Now" or market context on any page | High — investors and partners need the macro argument | Add to Home and About |
| No federated learning explanation anywhere | High — this is the architectural differentiator, completely absent | Add to About and/or a dedicated Infrastructure page |
| Broken `/policy-whitepaper` link on AI Ethics | Critical — damages trust | Fix immediately |
| Gmail contact address | Medium-High — appears unprofessional to institutional visitors | Migrate to domain email |
| No cohort outcomes section | High — site reads as events, not platform | Add to Cohort 1 page |
| No LinkedIn/social links in nav or footer | Medium | Add to footer |
| IIT Bombay ongoing partnership language | Legal/credibility risk | Reframe to historical throughout |
| "Cohort 2 Coming Soon" — vague, no timeline | Medium | Add a hint of Cohort 2 framing from the Blueprint |

---

---

# SECTION B — REVISED WEBSITE INFORMATION ARCHITECTURE

---

## B.1 — Updated Sitemap

```
aescode.nexus/
│
├── / (Home)                          [PRIMARY — INSTITUTIONAL ENTRY POINT]
│   ├── Hero + One-Sentence Platform Positioning
│   ├── Platform Architecture (3-Layer)
│   ├── Why Now (3 Convergences)
│   ├── Stats Marquee (with captions)
│   ├── Partner Logo Strip
│   ├── Pullquote
│   └── Newsletter Capture
│
├── /about (About)                    [SECONDARY — NARRATIVE & ARCHITECTURE]
│   ├── Origin Story (corrected)
│   ├── The 3-Layer Platform Architecture
│   ├── 5 Platform Pillars (expanded)
│   ├── Incubation Function (moved from Home)
│   └── Cohort 2 Signal
│
├── /cohort1 (Cohort 1)              [PROOF OF WORK — MISSION CRITICAL]
│   ├── [Sticky Anchor Nav]
│   ├── Hero / Overview
│   ├── Timeline
│   ├── Prize Structure
│   ├── "What 250 Engineers Told Us" (Abstract Insight)
│   ├── Problem Statements (5 × Accordion)
│   ├── Cohort 1 Outcomes Summary
│   ├── Evaluation Committee (Judges)
│   ├── Research Mentors
│   └── Cohort 2 Signal
│
├── /ai-ethics (AI Ethics)            [INSTITUTIONAL DIFFERENTIATOR]
│   ├── Hero + Version Tag
│   ├── Why Rigor Matters in India (with regulatory refs)
│   ├── 5 Operational Pillars (revised)
│   ├── Governance as Code
│   ├── Regulatory Alignment (DPDP, ICMR, CDSCO, ABDM)
│   ├── Ethics in Evaluation (connection to cohort process)
│   └── Framework Download CTA (or Contact CTA)
│
├── /contact (Contact)                [CONVERSION]
│   ├── Differentiated Contact Types
│   ├── Contact Form
│   └── FAQ / Before You Write
│
├── /meet-the-team (Team)            [FOOTER ONLY]
│   ├── Core Leadership
│   ├── Organising Secretariat
│   ├── Advisory Board (Forming)
│   └── Closing Pullquote
│
└── /special-thanks (Special Thanks) [FOOTER ONLY]
    ├── 4 Honoree Profiles
    └── Institutional Acknowledgment (corrected language)
```

---

## B.2 — Navigation Flow

**Primary Nav (top bar):** HOME · ABOUT · COHORT 1 · AI ETHICS · CONTACT  
**Footer Nav:** Meet the Team · Special Thanks · Privacy Policy · Terms of Service

**CTA Hierarchy Per Page:**

| Page | Primary CTA | Secondary CTA |
|---|---|---|
| Home | Explore Cohort 1 | Partner With Us |
| About | Explore Cohort 1 | View AI Ethics Framework |
| Cohort 1 | Subscribe (newsletter) | Contact |
| AI Ethics | Contact (fixed) | View Cohort 1 |
| Contact | Send message | — |

---

## B.3 — Section Ordering Logic (First Principles)

Each page's section order follows a single rule: **establish credibility before asking for action.**

```
EVERY PAGE: Label → Headline → Context/Proof → Architecture/Detail → CTA
```

Home flows: What we are → Why it exists → Proof it works → Partner with us  
About flows: Where we came from → What we built → How it works → What's next  
Cohort 1 flows: What happened → When → What was built → Who judged → Who mentored → Subscribe  
AI Ethics flows: Why this matters → What we believe → How we enforce it → Talk to us  

---

## B.4 — Cross-Page Consistency Rules

| Element | Standard |
|---|---|
| IIT Bombay references | All past-tense or "Cohort 1 partner" framing |
| Bharati Hospital references | "Primary clinical anchor" and "founding clinical partner" |
| Stats (250+, 100+, 20, 5) | Must appear consistently on Home and Cohort 1. Never inflated. |
| Platform description | One sentence used consistently: "India's clinical AI validation infrastructure — the federated data layer and certification standard that makes ABDM deployable" |
| Cohort 2 signal | Appears on About, Cohort 1, and optionally Home. Always framed as forward motion, never as current offering. |

---

## B.5 — SEO Structure Overview

| Page | Target Keyword Intent |
|---|---|
| Home | "MedTech research platform India", "clinical AI validation India", "ABDM AI infrastructure" |
| About | "clinical AI certification India", "federated learning healthcare India" |
| Cohort 1 | "MedTech hackathon India", "clinical AI research program India", "IIT Bombay MedTech" |
| AI Ethics | "clinical AI ethics India", "ICMR AI guidelines", "CDSCO AI regulation India" |
| Contact | "MedTech partnership India", "clinical AI collaboration" |

---

---

# SECTION C — FINAL PAGE-WISE CONTENT

---

## C.1 — HOME (`/`)

**SEO Title:** `Aescode Co. — India's Clinical AI Validation Infrastructure`  
**Meta Description:** `Aescode Co. connects engineering teams to real clinical problems, trains AI on hospital data without moving it, and certifies the tools hospitals can trust. Built with Bharati Hospital. Grounded in research.`  
**Keywords:** clinical AI validation India, MedTech research platform, federated learning healthcare India, ABDM AI infrastructure

---

### [HERO SECTION]

**Label:** `MEDTECH RESEARCH PLATFORM · FOUNDED 2026`

**H1:** India's Clinical AI Validation Infrastructure.

**Subheadline:**  
Aescode Co. connects engineering teams to real clinical problems, trains AI on hospital data without moving it, and certifies the tools hospitals can trust.

**CTA 1:** `Explore Cohort 1`  
**CTA 2:** `Partner With Us`

---

### [THE STRUCTURAL GAP]

**Label:** `THE PROBLEM`

**H2:** The gap is not ambition. It is infrastructure.

**Body:**  
India has 834 million ABHA digital health IDs and 438,000 registered health facilities. The data infrastructure exists. The engineering talent exists. Clinical AI adoption is blocked by one thing: trust.

Hospital procurement teams will not deploy software that has not been independently validated against Indian patient populations. AI trained on US or European datasets performs differently — sometimes dangerously differently — on Indian patients. And there is no Indian institution that benchmarks and certifies clinical AI tools.

Aescode builds that institution.

---

### [PLATFORM ARCHITECTURE — 3 LAYERS]

**Label:** `THE PLATFORM`

**H2:** Three layers. One flywheel.

**Layer 0 — Talent Engine**  
Recurring cohorts surface engineering teams working on real clinical problems from Bharati Hospital. The best teams advance to the next layer.

**Layer 1 — Federated Learning Infrastructure**  
Selected teams train AI on real hospital data — without that data ever leaving the hospital. The model goes to the data. Not the other way around.

**Layer 2 — Certification & Benchmarking**  
An independent evaluation process tests whether a clinical AI tool is accurate, safe, and fit for Indian clinical deployment. Pass = certification. Fail = structured feedback.

**Connecting line:**  
Each layer feeds the next. Each cohort produces new models. Each certified model builds the benchmark. The system compounds.

---

### [WHY NOW — THREE CONVERGENCES]

**Label:** `THE TIMING`

**H2:** Three things converged at once.

**01 — Infrastructure is ready.**  
ABDM reached 834 million citizens in 2025. India's National Federated Learning Platform MoU was signed in October 2024. The rails exist. The application layer is missing.

**02 — Regulation is hardening.**  
CDSCO is drafting SaMD regulations. ICMR published AI ethics guidelines in 2023. Draft DPDP rules were released January 2025. Every clinical AI tool will eventually require validation. First-mover in certification becomes institutional moat.

**03 — Hospitals are ready to buy — but only certified tools.**  
Apollo deployed 20 certified AI tools in 2024. The Indian hospital market is not waiting for AI. It is waiting for trusted AI. That is the bottleneck Aescode resolves.

---

### [STATS MARQUEE — WITH CAPTIONS]

`250+` Research Abstracts — problem statements submitted by engineers nationwide  
`100+` Competing Teams — interdisciplinary teams across disciplines  
`20` Finalists — selected through jury review  
`5` Clinical Problems — sourced directly from Bharati Hospital clinicians  
`14` Days — structured competition window  
`₹1.5L+` Prize Pool — awarded to top research outcomes  

---

### [INSTITUTIONAL ANCHORS]

**Label:** `OUR CLINICAL ANCHOR`

**Copy:**  
Bharati Hospital, Pune — one of India's largest teaching hospitals — is the founding clinical partner of Aescode Co. Every problem statement we work on is sourced from their clinicians. Every certified tool we produce is offered to them first.

`[Bharati Hospital Logo]` `[KCDH IIT Bombay Logo — Cohort 1]`

**Caption under KCDH logo:** *Research partner for Cohort 1*

---

### [PULLQUOTE]

> "We are not just building software; we are cultivating the next generation of intellectual architects who understand the poetry in the code."

— The Collective Mission of Aescode Co.

---

### [NEWSLETTER]

**Label:** `STAY INFORMED`

**H2:** Research updates, directly to your inbox.

**Sub:** Weekly dispatches on MedTech research, cohort updates, and institutional announcements.

`[Email input]` `[SUBSCRIBE]`

---

## C.2 — ABOUT (`/about.html`)

**SEO Title:** `About Aescode Co. — Clinical AI Research Infrastructure, India`  
**Meta Description:** `Aescode Co. was built to close the gap between clinical problems and engineering solutions. Built with Bharati Hospital, Pune. Learn about our 3-layer research platform.`  
**Keywords:** clinical AI research platform India, federated learning hospital India, MedTech infrastructure India

---

### [HERO]

**Label:** `ABOUT · 01`

**H1:** The Origin.

**Sub:** `AESCODE CO. · RESEARCH PLATFORM · FOUNDED 2026`

---

### [ORIGIN STORY — CORRECTED]

**H2:** Origin Story

**Key Partners — Cohort 1:**
- Koita Centre for Digital Health (KCDH), IIT Bombay *(Research partner, Cohort 1)*
- Bharati Vidyapeeth Medical College & Bharati Hospital, Pune *(Founding clinical anchor)*

**Body:**

Aescode Co. emerged from Nexus 3.0 — the annual undergraduate research conference at Bharati Vidyapeeth Medical College, Pune — co-hosted in partnership with the Koita Centre for Digital Health at IIT Bombay for its inaugural cohort.

The founding premise was simple: meaningful progress at the intersection of medicine and technology requires structure — clinical rigour on one side, engineering capability on the other, and a shared problem to hold them together.

India's MedTech innovation landscape was fragmented. Events were isolated. Prototypes were built without clinical grounding. Research findings rarely translated into deployable solutions. The gap was not one of ambition — it was one of infrastructure.

Aescode was built to close that gap. Our programs are designed around one constraint: every problem we work on must be both medically significant and technically tractable. We begin with clinical need and work backward toward the most rigorous technical response.

---

### [PLATFORM ARCHITECTURE]

**Label:** `THE PLATFORM`

**H2:** A MedTech Research Ecosystem.

**01. TALENT ENGINE (Layer 0)**  
Recurring hackathons surface engineering teams working on clinically sourced problems. 250+ research abstracts from Cohort 1 are the first documented output of this layer.

**02. FEDERATED LEARNING INFRASTRUCTURE (Layer 1)**  
Selected teams train AI models on real hospital data without that data leaving the hospital. Instead of sending data to the engineer, the AI model is sent to the data. Model weights — not patient records — are returned. Privacy-preserving by architecture, not by policy.

**03. CERTIFICATION & BENCHMARKING (Layer 2)**  
An independent evaluation process tests clinical AI tools against India-specific benchmarks. Certified tools can be deployed with institutional confidence. This is the layer no Indian platform currently provides.

**04. RESEARCH METHODOLOGY**  
Every program begins with clinical observation. Solutions are held against three standards before development begins: reproducibility, clinical relevance, and deployment feasibility.

**05. INSTITUTIONAL GROUNDING**  
Bharati Hospital is the founding clinical partner providing problem statements, data access pathways, and deployment context. Every initiative is held to peer-reviewed research standards.

---

### [SECONDARY FUNCTION — INCUBATION]

**H3:** Incubation follows validation — not the inverse.

**Body:**  
Where research outcomes demonstrate commercial viability, Aescode provides structured pathways toward startup formation and institutional support. This is a deliberate ordering: research first, commercialization second. We do not lower the research bar to accelerate the startup timeline.

---

### [CLOSING PULLQUOTE]

> "The most consequential medical technologies are not born from speed or ambition alone. They emerge from the disciplined convergence of clinical truth and engineering precision — built slowly, validated rigorously, and deployed only when the evidence demands it."

`AESCODE CO. · RESEARCH PLATFORM · FOUNDED 2026`

---

### [COHORT 2 SIGNAL]

**Label:** `COHORT 2`  
**Text:** Coming Soon.

---

## C.3 — COHORT 1 (`/cohort1.html`)

**SEO Title:** `Cohort 1 — The Inaugural Aescode MedTech Research Program`  
**Meta Description:** `Aescode Cohort 1: 250+ research abstracts, 5 clinically sourced AI problems, 20 finalists, judged by KCDH IIT Bombay researchers and clinical specialists. Full documentation.`  
**Keywords:** MedTech hackathon India 2026, clinical AI research India, IIT Bombay KCDH hackathon

---

### [STICKY ANCHOR NAV]
`OVERVIEW · ABSTRACTS · PROBLEMS · JUDGES · MENTORS`

---

### [HERO]

**Label:** `ARCHIVE · 001`

**H1:** The Inaugural Cohort 1

**Sub:** A two-week MedTech research program structured around clinically sourced problem statements and interdisciplinary research teams.

**Venue:** Bharati Vidyapeeth Medical College, Pune — with research mentorship from KCDH, IIT Bombay

---

### [PHILOSOPHY]

**H3:** We didn't write the problem statements. We collected them from the field.

---

### [TIMELINE — RETAIN AS-IS]

*(All 6 dated entries are accurate and credible — retain without change)*

---

### [PRIZES — RETAIN AS-IS]

---

### [ABSTRACT INSIGHT — NEW SECTION]

**Label:** `COHORT 1 INTELLIGENCE`

**H2:** What 250 Engineers Told Us.

**Body:**  
Before any team competed, 250+ engineers from institutions across India submitted structured research abstracts — their own analysis of real, unresolved clinical problems. This was not a registration form. It was a diagnostic.

The submission pool revealed five dominant clinical problem clusters: diabetic complications, acute patient monitoring, bone health screening, rehabilitation technology, and neurological imaging. Each cluster was independently confirmed by Bharati Hospital's clinical staff as a genuine operational gap.

The 250+ abstracts from Cohort 1 are not a participation metric. They are a dataset — structured evidence of how India's engineering graduates understand and frame clinical challenges. Aescode treats them as such.

*(Future: A structured analysis and publication of this dataset is in preparation.)*

---

### [PROBLEM STATEMENTS — RETAIN IN FULL]

*(All 5 problem statements retained exactly as-is. The problem documentation is mission-critical.)*

---

### [COHORT 1 OUTCOMES]

**Label:** `RESEARCH OUTCOMES`

**H2:** What Cohort 1 Produced.

**Body:**  
Twenty finalist teams presented research frameworks and prototype architectures across five clinical AI domains. The evaluation committee — comprising KCDH IIT Bombay researchers and clinical specialists — assessed submissions against three criteria: research methodology, clinical relevance, and deployment feasibility.

Top teams produced documented AI architectures for: plantar pressure mapping in diabetic patients, early warning systems for physiological deterioration, opportunistic osteoporosis screening from routine X-rays, pose-based rehabilitation feedback, and ischemic volume estimation from CT imaging.

Full winner documentation and testimonials are being compiled for the Cohort 1 archive. Contact us at partnerships@aescode.nexus for access.

---

### [JUDGES — RETAIN IN FULL]

*(All 4 judge profiles retained. These are strong credibility anchors. Do not compress.)*

---

### [MENTORS — RETAIN IN FULL]

*(All 3 KCDH mentor profiles retained.)*

---

### [COHORT 2 SIGNAL]

**Label:** `COHORT 2`  
**Text:** Coming Soon.

---

## C.4 — AI ETHICS (`/ai_ethics.html`)

**SEO Title:** `AI Ethics & Governance — Aescode Co. Clinical AI Framework`  
**Meta Description:** `Aescode Co.'s AI Ethics framework governs every clinical AI model evaluated through our platform. Aligned with DPDP Act 2023, ICMR guidelines, and CDSCO SaMD pathways.`  
**Keywords:** clinical AI ethics India, ICMR AI guidelines compliance, CDSCO SaMD AI, DPDP clinical AI

---

### [HERO]

**Label:** `GOVERNANCE PROTOCOL`

**H1:** AI Ethics & Integrity

**Sub:** In the Indian healthcare ecosystem, technical innovation is secondary to clinical trust. Aescode Co. builds the ethical infrastructure required to move AI from the lab to the bedside.

**Tag:** `v2.4 / DPDP ACT 2023 · ICMR 2023 · CDSCO SaMD ALIGNMENT`

---

### [NECESSITY OF RIGOR]

**H2:** The Necessity of Rigor in Indian MedTech

**Body:**  
India's healthcare landscape is defined by extreme scale, diverse patient demographics, and a regulatory environment that is actively evolving. Here, an unmonitored algorithm does not just "fail" — it risks codifying systemic biases and eroding patient autonomy across populations of hundreds of millions.

Three regulatory frameworks now govern this space explicitly:

- **Digital Personal Data Protection (DPDP) Act, 2023** — requires consent, data minimization, and purpose limitation. Federated learning is designed for compliance with this architecture.
- **ICMR Ethical Guidelines for AI in Healthcare, 2023** — mandate privacy-by-design, algorithmic transparency, and clinical validation before deployment.
- **CDSCO SaMD Regulation** — AI diagnostic tools require regulatory approval. Aescode certification is positioned as a pre-submission validation standard.

At Aescode, we recognize that while regulation is still evolving, the responsibility of the builder is absolute. We do not wait for policy to mandate safety. We architect for it.

---

### [5 OPERATIONAL PILLARS — REVISED]

**Label:** `OPERATIONAL PILLARS — NON-NEGOTIABLE STANDARDS`

**01 — Clinical Non-Maleficence**  
Safety is not a feature; it is the baseline. Every model evaluated through Aescode is validated against local clinical gold standards before any performance claim is made.

**02 — Glass-Box Interpretability**  
Black-box models have no place in medicine. Our evaluation rubric requires clear, interpretable evidence for every clinical suggestion. A clinician must be able to understand why the AI made its recommendation.

**03 — Privacy-Preserving Data Architecture**  
No live patient data leaves the hospital in any Aescode program. For prototype validation, we utilize high-fidelity synthetic datasets. For model training, we use federated learning — the model trains at the hospital; only what it learned returns, never the data itself.

**04 — Augmented Human Oversight**  
AI is a tool for the clinician. Final clinical authority remains strictly with certified medical professionals. Aescode does not certify AI tools that position themselves as autonomous clinical decision-makers.

**05 — Staged Socio-Technical Rollouts**  
We evaluate deployments for their impact on existing hospital workflows and provider workloads. A tool that creates more clinical burden than it resolves fails the deployment standard regardless of its technical performance.

---

### [GOVERNANCE AS CODE — RETAIN]

**H3:** Governance as Code

**Body:** At Aescode, ethics is a systems problem. We integrate ethical checkpoints directly into our evaluation pipelines. If a submitted model fails a safety constraint, a bias check, or an interpretability review, it does not receive certification — regardless of performance metrics.

---

### [REGULATORY ALIGNMENT — EXPANDED]

**H3:** Regulatory Alignment

**Body:** We actively engage with India's evolving regulatory landscape — including the DPDP Act, ICMR guidelines, and the CDSCO SaMD pathway — and align our evaluation standards with ABDM's consent-first architecture. This means Aescode-certified tools are positioned for regulatory recognition, not just academic validation.

---

### [ETHICS IN EVALUATION]

**H3:** Ethics Is Part of Every Cohort Evaluation

**Body:** Every team that participates in an Aescode cohort is evaluated not only on technical performance but on the ethical architecture of their solution. Problem framing, data handling, model interpretability, and deployment assumptions are all assessed. This is what distinguishes Aescode evaluation from a standard hackathon jury process.

---

### [CLOSING PULLQUOTE]

> "We are building an ecosystem where responsible AI is the default, ensuring that innovation never comes at the cost of medical integrity."

---

### [CTA — FIXED]

`CONTACT US TO DISCUSS INSTITUTIONAL PARTNERSHIP →` → links to `/contact.html`

*(Note: Remove the broken `/policy-whitepaper` link entirely until the whitepaper page is built.)*

---

## C.5 — CONTACT (`/contact.html`)

**SEO Title:** `Contact Aescode Co. — Institutional Partnerships & Research Inquiries`  
**Meta Description:** `Partner with Aescode Co. on clinical AI research, institutional programs, or sponsorship. Reach the team directly.`

---

### [HERO]

**H1:** Get in Touch.

---

### [CONTACT TYPES]

**General Inquiries**  
`hi@aescode.nexus`

**Partnership & Institutional**  
`partnerships@aescode.nexus`

**Press & Media**  
`press@aescode.nexus`

*(Note: All three can forward to the same inbox initially. The differentiation signals institutional seriousness to each visitor type.)*

---

### [CONTACT FORM]

Fields: Full Name · Organization · Role · Inquiry Type (dropdown: General / Partnership / Press / Research / Other) · Message  
CTA: `SEND MESSAGE`  
Success state: "Your message has been received. We aim to respond within 48 hours."

---

### [FAQ / BEFORE YOU WRITE]

**Before you write, some quick answers:**

**When is Cohort 2?** — Cohort 2 details are being finalized. Subscribe to our newsletter for the announcement.

**How do I apply to participate?** — Applications open with each cohort announcement. Subscribe for updates.

**How do I partner with Aescode?** — Email partnerships@aescode.nexus with your organization name and area of interest.

---

---

# SECTION D — EXECUTION PROMPTS FOR ANTIGRAVITY

---

## D.0 — Workflow Strategy

**Model assignment:**
- All planning, architecture decisions, and first-pass content generation: **Claude Opus 4.6 (Thinking)**
- All implementation, HTML edits, and copy refinements: **Claude Sonnet** (lower cost, sufficient for execution)

**Execution principle:** Every prompt below is deterministic. Antigravity is the execution engine. You have done the strategic thinking. Do not allow Antigravity to make structural decisions.

**Design system block to prepend to EVERY prompt:**

```
DESIGN SYSTEM — ENFORCE STRICTLY ON EVERY OUTPUT:
• Background: #FCF9F8 (warm white). NEVER pure white on page body.
• Primary: #021934 (deep navy). Buttons, active states, headings only.
• Body text: #1C1B1B. Muted/label text: #707785.
• Headlines: Newsreader (Google Fonts), serif.
• Body + labels + nav: Public Sans (Google Fonts).
• Border-radius: 4px maximum. NO pill buttons. NO rounded buttons.
• NO gradients. NO box-shadows > 4px blur. NO glassmorphism. NO blurs.
• Section separation: background shifts or whitespace only. NO 1px dividers.
• Nav: text labels only, all-caps, Public Sans. NO icons. NO dropdowns.
• Dot-grid overlay: body::before pseudo-element, opacity 0.03, pointer-events: none, z-index: 0.
• Input fields: underline-only 0.5px #C4C6CE. Focus: 1.5px #021934. No halos.
• Cards: #FFFFFF background, 2px radius, separated by grid spacing not borders.
• Label text: all-caps, Public Sans, letter-spacing +0.05em, color #707785.
DO NOT change any of these rules. If in doubt, do not add styling.
```

---

## D.1 — CRITICAL FIX (Execute First, Before Any Content Work)

**Objective:** Fix the broken `/policy-whitepaper` link on AI Ethics page.

**Prompt:**
```
In ai_ethics.html, find the CTA element that links to "/policy-whitepaper".

Replace the entire CTA element with:
<a href="contact.html" class="btn-tertiary">CONTACT US TO DISCUSS INSTITUTIONAL PARTNERSHIP →</a>

Do not change any other element on the page.
Do not change any styling.
```

**Expected output:** Single line change. CTA now routes to contact.html.

**Verification checklist:**
- [ ] Link goes to contact.html, not /policy-whitepaper
- [ ] Button class is btn-tertiary (tertiary style per design system)
- [ ] No other element on the page was modified
- [ ] Page still renders in correct design system style

**Fallback correction prompt:**
```
The CTA change was not applied correctly. Revert to the previous state and re-apply only this change: Find the anchor tag with href="/policy-whitepaper". Replace only the href with "contact.html" and the visible text with "CONTACT US TO DISCUSS INSTITUTIONAL PARTNERSHIP →". Touch nothing else.
```

---

## D.2 — HOME PAGE UPDATE

**Objective:** Rewrite homepage hero, add "Why Now" section, add institutional anchor section, update CTA copy. Preserve all existing sections not explicitly mentioned.

**Prompt:**
```
[PREPEND DESIGN SYSTEM BLOCK]

You are editing index.html. Make the following changes exactly as specified. Do not change anything not listed below.

CHANGE 1 — Hero label:
Find the label text "A New Paradigm in Translational Tech".
Replace with: "MEDTECH RESEARCH PLATFORM · FOUNDED 2026"
Style: all-caps, Public Sans, letter-spacing +0.05em, color #707785.

CHANGE 2 — H1:
Find the H1 element "Advancing Clinical Research Through Engineering".
Replace with: "India's Clinical AI Validation Infrastructure."

CHANGE 3 — Hero subheadline:
Find the subheadline paragraph beginning "AesCode Co. is a MedTech research platform dedicated to accelerating..."
Replace with: "Aescode Co. connects engineering teams to real clinical problems, trains AI on hospital data without moving it, and certifies the tools hospitals can trust."

CHANGE 4 — CTA 2:
Find the button with text "Get Involved".
Replace text with: "Partner With Us"
Do not change any button styling, class, or href.

CHANGE 5 — Add "Why Now" section:
After the stats marquee section and before the newsletter section, insert the following new section block with the same background and spacing as the existing sections. Use the existing card component style for the three sub-points:

Label: THE TIMING
H2: Three things converged at once.

Card 01:
Label: 01
H3: Infrastructure is ready.
Body: ABDM reached 834 million citizens in 2025. India's National Federated Learning Platform MoU was signed in October 2024. The rails exist. The application layer is missing.

Card 02:
Label: 02
H3: Regulation is hardening.
Body: CDSCO is drafting SaMD regulations. ICMR published AI ethics guidelines in 2023. Draft DPDP rules were released January 2025. Every clinical AI tool will eventually require validation.

Card 03:
Label: 03
H3: Hospitals are ready — but only for certified tools.
Body: Apollo deployed 20 certified AI tools in 2024. The Indian hospital market is not waiting for AI. It is waiting for trusted AI. That is the bottleneck Aescode resolves.

CHANGE 6 — "The Gap" section body text:
Find the paragraph beginning "Medical knowledge and engineering capability have advanced in parallel..."
Replace with:
"India has 834 million ABHA digital health IDs and 438,000 registered health facilities. The data infrastructure exists. The engineering talent exists. Clinical AI adoption is blocked by one thing: trust.

Hospital procurement teams will not deploy software that has not been independently validated against Indian patient populations. And there is no Indian institution that benchmarks and certifies clinical AI tools. Aescode builds that institution."

CHANGE 7 — Remove "Secondary Mission" block from homepage:
Find the section labeled "Secondary Mission" and the text "Startup Incubation — Post-Research".
Remove this entire block. The "Primary Mission" block should remain.
```

**Expected output:** Updated index.html with 7 targeted changes. All existing sections preserved.

**Verification checklist:**
- [ ] H1 reads "India's Clinical AI Validation Infrastructure."
- [ ] "Why Now" section with 3 cards inserted between marquee and newsletter
- [ ] "Partner With Us" CTA in place of "Get Involved"
- [ ] "Secondary Mission" block removed
- [ ] Stats marquee unchanged
- [ ] Newsletter section unchanged
- [ ] Footer unchanged
- [ ] Design system tokens not altered
- [ ] Dot-grid overlay still present

**Fallback correction prompt:**
```
One or more changes were not applied cleanly. Identify which of the 7 changes was missed or incorrectly applied. Apply only that change. List which change you are re-applying and show the before/after diff.
```

---

## D.3 — ABOUT PAGE UPDATE

**Objective:** Correct IIT Bombay language, add 3-layer architecture description, move incubation content from homepage.

**Prompt:**
```
[PREPEND DESIGN SYSTEM BLOCK]

You are editing about.html. Make the following targeted changes. Do not change anything not listed.

CHANGE 1 — Key Partners label:
Find "Key Partners" section.
Change "Koita Centre for Digital Health (KCDH), IIT Bombay" to: "Koita Centre for Digital Health (KCDH), IIT Bombay (Research partner, Cohort 1)"
Change "Bharati Vidyapeeth" to: "Bharati Vidyapeeth Medical College & Bharati Hospital, Pune (Founding clinical anchor)"

CHANGE 2 — Origin story — IIT Bombay framing:
Find the sentence: "AesCode Co. emerged from within the academic framework of Nexus 3.0 — the annual undergraduate research conference at Bharati Vidyapeeth Medical College, Pune — in institutional partnership with the Koita Centre for Digital Health at IIT Bombay."
Replace with: "AesCode Co. emerged from Nexus 3.0 — the annual undergraduate research conference at Bharati Vidyapeeth Medical College, Pune — co-hosted for its inaugural cohort in partnership with the Koita Centre for Digital Health at IIT Bombay."

CHANGE 3 — Final paragraph — IIT Bombay language:
Find: "Bharati Vidyapeeth Medical College and KCDH IIT Bombay provide the institutional foundation that makes this approach possible — combining clinical depth with the computational standards that serious research demands."
Replace with: "Bharati Hospital, Pune provides the clinical foundation — a continuous source of real, documented clinical problems and a deployment context for validated tools. KCDH IIT Bombay's researchers served as research mentors and evaluation committee members for Cohort 1, contributing the computational standards the program demanded."

CHANGE 4 — Add federated learning pillar:
In the numbered platform section (01, 02, 03, 04), after item 04 "INSTITUTIONAL GROUNDING", add a new item:

Label: 05.
H3: FEDERATED LEARNING INFRASTRUCTURE
Body: Selected teams train AI models on real hospital data without that data leaving the hospital. The model goes to the data — not the other way around. Model weights, not patient records, are the only thing that moves. This is privacy-preserving by architecture, not by policy.

Use the same structural markup and styling as items 01–04.
```

**Expected output:** Updated about.html with 4 targeted changes.

**Verification checklist:**
- [ ] IIT Bombay listed as "Cohort 1" partner only, not ongoing
- [ ] Bharati Hospital listed as "Founding clinical anchor"
- [ ] Origin story uses "co-hosted for its inaugural cohort" not "institutional partnership"
- [ ] Federated learning pillar appears as item 05 in the numbered list
- [ ] Design system unchanged
- [ ] All existing sections preserved

---

## D.4 — AI ETHICS PAGE UPDATE

**Objective:** Revise pillar 3, expand regulatory section, add evaluation connection, fix broken link (already done in D.1).

**Prompt:**
```
[PREPEND DESIGN SYSTEM BLOCK]

You are editing ai_ethics.html. Make the following targeted changes.

CHANGE 1 — Pillar 03 rename and rewrite:
Find pillar 03 labeled "Synthetic Data Sovereignty".
Replace the label with: "Privacy-Preserving Data Architecture"
Replace the body text with: "No live patient data leaves the hospital in any Aescode program. For prototype validation, we utilize high-fidelity synthetic datasets. For model training, we use federated learning — the model trains at the hospital; only what it learned returns, never the data itself."

CHANGE 2 — Expand the "Bridging Regulatory Gaps" section:
Find the paragraph beginning "We actively engage with Indian regulatory frameworks, including the Digital Personal Data Protection (DPDP) Act and ICMR guidelines..."
Replace with: "We align with three active regulatory frameworks: the Digital Personal Data Protection (DPDP) Act 2023, ICMR Ethical Guidelines for AI in Healthcare 2023, and the CDSCO SaMD regulatory pathway for AI diagnostic tools. We additionally align with ABDM's consent-first architecture to ensure Aescode-certified tools are positioned for regulatory recognition, not just academic validation."

CHANGE 3 — Add new section "Ethics in Evaluation":
After the "Bridging Regulatory Gaps" section, before the closing pullquote, insert a new subsection:

H3: Ethics Is Part of Every Cohort Evaluation
Body: Every team that participates in an Aescode cohort is evaluated not only on technical performance but on the ethical architecture of their solution. Problem framing, data handling, model interpretability, and deployment assumptions are all assessed against a published rubric. This is what distinguishes Aescode evaluation from a standard hackathon jury process.

Use the same paragraph style as existing body text.
```

**Expected output:** Updated ai_ethics.html with 3 targeted changes (plus D.1 already applied).

**Verification checklist:**
- [ ] Pillar 03 is now "Privacy-Preserving Data Architecture"
- [ ] Regulatory section references DPDP 2023, ICMR 2023, CDSCO SaMD, and ABDM
- [ ] "Ethics in Evaluation" section appears before closing pullquote
- [ ] Broken link already fixed (from D.1)
- [ ] Design system tokens unchanged

---

## D.5 — COHORT 1 PAGE UPDATE

**Objective:** Add abstract insight section, add cohort outcomes section, remove testimonial placeholder.

**Prompt:**
```
[PREPEND DESIGN SYSTEM BLOCK]

You are editing cohort1.html. Make the following targeted changes.

CHANGE 1 — Remove testimonial placeholder:
Find the section "FROM THE COHORT" containing the text "Testimonials, winner stories, and documentation from Cohort 1 participants will appear here."
Replace the body of this section (the placeholder text only) with the following:

H2: Cohort 1 Outcomes.
Body: Twenty finalist teams presented research frameworks and AI prototype architectures across five clinical domains. Top teams produced documented solutions for: plantar pressure mapping in diabetic patients, early warning systems for physiological deterioration, opportunistic osteoporosis screening from routine X-rays, pose-based rehabilitation feedback, and ischemic volume estimation from CT imaging.

Full winner documentation is being compiled for the Cohort 1 archive. For access or media inquiries, contact partnerships@aescode.nexus.

Retain the section heading "FROM THE COHORT" or replace with "COHORT 1 OUTCOMES" — use the same label style as other section labels on this page.

CHANGE 2 — Add abstract insight section:
Before the PROBLEMS section, insert a new section:

Label: COHORT 1 INTELLIGENCE
H2: What 250 Engineers Told Us.
Body: Before any team competed, 250+ engineers from institutions across India submitted structured research abstracts — their analysis of real, unresolved clinical problems. The submission pool revealed five dominant clinical problem clusters, each independently confirmed by Bharati Hospital's clinical staff as a genuine operational gap.

The 250+ abstracts from Cohort 1 are not a participation metric. They are a dataset — structured evidence of how India's engineering graduates understand and frame clinical challenges. A structured analysis of this dataset is in preparation.

Use the same section structure and spacing as existing sections on this page.

CHANGE 3 — Add sticky internal anchor navigation:
At the top of the page content (below the nav bar, above the hero), add a sticky horizontal anchor navigation bar with the following links:
- OVERVIEW → links to the hero section
- PROBLEMS → links to the PROBLEMS section
- JUDGES → links to the EVALUATION COMMITTEE section
- MENTORS → links to the RESEARCH MENTORS section

Style: Public Sans, all-caps, letter-spacing +0.05em, color #707785. Active/hover: #021934. 0.5px bottom border. Sticky on scroll. Background #FCF9F8.
```

**Expected output:** Updated cohort1.html with 3 targeted changes.

**Verification checklist:**
- [ ] Testimonial placeholder ("Coming Soon") removed
- [ ] Cohort 1 Outcomes section present with contact email
- [ ] "What 250 Engineers Told Us" section added before Problems
- [ ] Sticky anchor nav bar present and links to correct sections
- [ ] All 5 problem statements retained unchanged
- [ ] All 4 judges retained unchanged
- [ ] All 3 mentors retained unchanged
- [ ] Design system unchanged

---

## D.6 — CONTACT PAGE REBUILD

**Objective:** Upgrade contact page from bare email to structured contact experience.

**Prompt:**
```
[PREPEND DESIGN SYSTEM BLOCK]

You are rebuilding contact.html. The current page has only a headline "Get in Touch." and a single Gmail address.

Retain the headline "Get in Touch." and the page hero structure.

Below the headline, add the following:

SECTION 1 — Contact types (three columns or a clean list):

Column/Item 1:
Label: GENERAL INQUIRIES
Email: hi@aescode.nexus

Column/Item 2:
Label: PARTNERSHIP & INSTITUTIONAL
Email: partnerships@aescode.nexus

Column/Item 3:
Label: PRESS & MEDIA
Email: press@aescode.nexus

All email addresses styled as plain text links (color #021934, no underline default, underline on hover). Label style: all-caps, Public Sans, #707785.

SECTION 2 — Contact form:
Below the three contact columns, add a form with the following fields, all styled as underline-only inputs per design system:

- Full Name (text input, placeholder "Full name")
- Organization (text input, placeholder "Organization")
- Role (text input, placeholder "Your role")
- Inquiry Type (select dropdown with options: General · Partnership · Press · Research · Other)
- Message (textarea, placeholder "Your message", min-height 120px, same underline style)
- Submit button: class="btn-primary", text "SEND MESSAGE"

The form should NOT use a <form> HTML tag — use a div with id="contact-form" and handle submission with JavaScript fetch.

SECTION 3 — FAQ (below the form):
Add a simple text block:

Label: BEFORE YOU WRITE

Three short FAQ items in plain body text:
Q: When is Cohort 2? — Cohort 2 details are being finalized. Subscribe to our newsletter for the announcement.
Q: How do I apply to participate? — Applications open with each cohort announcement. Subscribe for updates.
Q: How do I partner with Aescode? — Email partnerships@aescode.nexus with your organization name and area of interest.

Use the existing footer, nav, and page background unchanged.
```

**Expected output:** Rebuilt contact.html with contact types, form, and FAQ.

**Verification checklist:**
- [ ] Three differentiated contact types visible
- [ ] No Gmail address visible (old address removed)
- [ ] Form uses div not `<form>` tag
- [ ] All inputs are underline-only style
- [ ] Submit button is btn-primary class
- [ ] FAQ section present
- [ ] Nav and footer unchanged
- [ ] Design system tokens unchanged

---

---

# SECTION E — QUALITY ASSURANCE + VERIFICATION FRAMEWORK

---

## E.1 — Pre-Execution Checklist (Run Before First Antigravity Call)

| Check | Standard | Status |
|---|---|---|
| Source of truth confirmed | Founder Blueprint April 2026 + AesCode Build System v1.0 + DESIGN.md | ✓ |
| IIT Bombay language audit complete | All references to be past-tense or Cohort 1-specific | ✓ |
| Broken link documented | /policy-whitepaper → Fix in D.1 | ✓ |
| Gmail address to replace | aescode.nexus@gmail.com → domain emails | ✓ |
| Design tokens frozen | #FCF9F8, #021934, Newsreader, Public Sans — no changes | ✓ |
| Content changes scoped | 6 pages × targeted changes only — no full rewrites | ✓ |

---

## E.2 — Post-Execution Verification (Run After Every Antigravity Call)

**For every page update:**

**Design System Integrity:**
- [ ] Background is #FCF9F8, not pure white
- [ ] No gradients anywhere on the page
- [ ] No border-radius > 4px on any button or card
- [ ] Newsreader used only for H1, H2, H3, pullquotes
- [ ] Public Sans used for all labels, nav, body, buttons
- [ ] Dot-grid overlay present (body::before, opacity 0.03)
- [ ] All label text is all-caps, #707785, letter-spacing +0.05em
- [ ] No 1px divider lines used for section separation

**Content Integrity:**
- [ ] IIT Bombay not referred to as ongoing partner on any page
- [ ] Bharati Hospital referred to as "founding clinical partner" or "primary clinical anchor"
- [ ] 250+ figure used consistently — not inflated
- [ ] Broken /policy-whitepaper link does not appear on any page
- [ ] Gmail address does not appear on contact page

**Navigation Integrity:**
- [ ] All 5 nav tabs present: HOME · ABOUT · COHORT 1 · AI ETHICS · CONTACT
- [ ] Footer links present: Meet the Team · Special Thanks
- [ ] Active nav state applies 1px #021934 underline to current page

**SEO Integrity:**
- [ ] Every page has a unique `<title>` tag
- [ ] Every page has a `<meta name="description">` tag
- [ ] No two pages have the same meta description
- [ ] H1 appears once per page
- [ ] Images have alt text

**Functional Integrity:**
- [ ] Newsletter form submits without page reload
- [ ] Newsletter form shows inline success/error states
- [ ] Cohort 1 accordion cards expand on click
- [ ] Contact form does not use `<form>` HTML tag
- [ ] Contact email links are mailto: links
- [ ] All internal links resolve correctly (no 404s)

---

## E.3 — Hallucination Prevention Checks

These checks prevent Antigravity from inventing content not in the source documents.

| Risk | Prevention |
|---|---|
| Inventing statistics | Only use: 250+, 100+, 20, 5, 14 days, ₹1.5L+, ₹1L, ₹10K×5 — all verified from live site |
| Inventing partner claims | Only partners: Bharati Vidyapeeth/Bharati Hospital (active), KCDH IIT Bombay (Cohort 1 historical) |
| Inventing regulatory claims | Only cite: DPDP Act 2023, ICMR AI guidelines 2023, CDSCO SaMD, ABDM — all verified from Blueprint |
| Inventing market figures | Only cite: 834M ABHA IDs, 438,000 facilities, Apollo 20 certified tools — all from Blueprint |
| Inventing team members | Only use names from meet_the_team.html — do not add or invent new team members |
| Inventing cohort outcomes | Frame outcomes as "documented architectures" not "deployed products" |

---

## E.4 — Messaging Consistency Matrix

This table is the single source of truth for how Aescode should be described across all pages.

| Topic | Correct Language | Prohibited Language |
|---|---|---|
| What Aescode is | "Clinical AI validation infrastructure" / "MedTech research platform" | "Hackathon company" / "startup accelerator" / "innovation platform" |
| Bharati Hospital | "Founding clinical partner" / "primary clinical anchor" | "Sponsor" / "participant" / "supporter" |
| IIT Bombay KCDH | "Research partner for Cohort 1" / "Cohort 1 collaboration" | "Institutional partner" / "ongoing partner" / any present-tense framing |
| Federated learning | "AI model goes to the data" / "data never leaves the hospital" | "Secure data sharing" / "encrypted transfer" |
| 250+ abstracts | "Dataset" / "structured research output" | "Submissions" / "entries" / "participation count" |
| Cohort 2 | "Coming soon" / "in preparation" | "Launching soon" / "registrations open" / any specific date not confirmed |
| Certification | "AI tools hospitals can trust" / "India-specific clinical benchmarks" | "ISO certification" / any reference to formal regulatory certification not yet obtained |

---

## E.5 — Visual Consistency Checks (Post-Render)

After each page is rendered, perform a visual scan:

- [ ] Page feels like "ink on paper" — not a SaaS product
- [ ] Negative space is generous — not compressed
- [ ] No element feels "rounded" or "soft"
- [ ] Typography hierarchy is clear: large serif headline → muted all-caps label → body text
- [ ] Section breaks feel like page turns, not dividers
- [ ] Color usage is restrained — navy (#021934) appears only on primary interactive elements
- [ ] Dot-grid is barely perceptible — a texture, not a pattern

---

## E.6 — Execution Sequence (Recommended Order)

```
PRIORITY ORDER:

Step 1  →  D.1  (CRITICAL: Fix broken /policy-whitepaper link)
Step 2  →  D.6  (Contact page rebuild — quick trust upgrade)
Step 3  →  D.2  (Home page update — highest traffic page)
Step 4  →  D.3  (About page — corrects IIT Bombay risk)
Step 5  →  D.4  (AI Ethics — regulatory expansion)
Step 6  →  D.5  (Cohort 1 — abstract insight + outcomes)
```

**Rationale for this order:**
- Step 1 is a credibility-damaging bug. Fix in < 5 minutes before anything else.
- Step 2 upgrades first contact infrastructure — institutional visitors arriving from any page end up at Contact.
- Steps 3 and 4 fix the two pages with the highest institutional visitor traffic.
- Steps 5 and 6 are content enrichment — important but not credibility-damaging if deferred slightly.

---

*AESCODE CO. · aescode.nexus · MedTech Research. Clinically Grounded. Institutionally Anchored.*  
*CONFIDENTIAL — FOUNDER USE ONLY · APRIL 2026*
