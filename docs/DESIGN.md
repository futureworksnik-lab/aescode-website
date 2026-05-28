```markdown
# Design System Strategy: The Academic Modernist

## 1. Overview & Creative North Star
The Creative North Star for this design system is **"The Digital Monograph."** 

We are moving away from the "SaaS-template" aesthetic to embrace the quiet authority of a high-end academic journal blended with the surgical precision of a technical platform. This system celebrates the "white canvas"—using negative space not just as a container, but as a structural element. 

To break the "standard" UI feel, we utilize a **Strict Editorial Grid**. While most digital products favor centered, symmetrical stacks, this system thrives on intentional asymmetry. Large serif headlines should often sit "off-axis," balanced by wide margins and meticulous hairline details. The atmosphere is elevated by a persistent, low-opacity animated dot grid, suggesting a blueprint or a mathematical substrate beneath the intellectual content.

---

## 2. Colors & Surface Philosophy
The palette is rooted in high-contrast neutrality. It is designed to feel expensive through restraint.

### Color Logic
- **Background (`surface`):** #FCF9F8. A slightly "warm" white that prevents eye strain and feels like archival paper.
- **Primary (`primary`):** #021934 (Deep Navy). Used for key brand moments and heavy-weight interactions.
- **Surface Tiers:** We use `surface-container-lowest` (#FFFFFF) for interactive elements and `surface-dim` (#DCD9D9) for subtle structural shifts.

### The "No-Line" Sectioning Rule
In this system, we prohibit 1px solid borders for sectioning large areas of content. Boundaries must be defined through:
1.  **Background Shifts:** Use `surface-container-low` to set off a secondary content block from the main `surface`.
2.  **Negative Space:** Use the 12-column grid to create "voids" that act as natural separators.
3.  **Hairline Accents:** Only use `outline-variant` (#C4C6CE) at 0.5px for decorative hairlines or to define very small UI primitives (like input fields).

### Surface Hierarchy & Nesting
Treat the UI as a physical desk. The `surface` is your desk. A `surface-container-lowest` card is a sheet of paper placed upon it. To create depth without shadows, nest a `surface-container-high` element inside a `surface-container-low` block. This "tonal stacking" creates a sophisticated, flat depth that feels integrated rather than "floating."

---

## 3. Typography: The Editorial Voice
Typography is the primary driver of credibility. We pair a high-contrast serif for intellectual weight with a neutral grotesque for technical clarity.

- **Display & Headlines (Newsreader):** These are our "Editorial Hooks." Use `display-lg` (3.5rem) with tight tracking (-0.02em) to create a sharp, authoritative presence. Headlines should feel like title pages of a thesis.
- **Body & Titles (Public Sans):** This is our "Precision Engine." Public Sans provides a neutral, grotesque clarity that balances the serif’s romanticism. Use `body-md` (0.875rem) for technical documentation to maximize information density without sacrificing legibility.
- **Labels (Public Sans):** All-caps with increased letter spacing (+0.05em) should be used for metadata and labels to evoke the feel of a museum placard.

---

## 4. Elevation & Depth
We reject the "soft-bubble" aesthetic of modern web design. Depth is achieved through **Tonal Layering** and **Structural Hairlines.**

- **The Layering Principle:** Depth is signaled by value changes. A sidebar in `surface-container-low` sitting next to a main body in `surface` provides all the hierarchy needed.
- **Ambient Shadows:** Shadows are a last resort. When required for floating modals, use an "Atmospheric Shadow": `0px 20px 40px rgba(15, 15, 15, 0.04)`. It should be nearly invisible, felt rather than seen.
- **The "Ghost Border":** For internal component containment, use a hairline border of `outline-variant` at 20% opacity. It should act as a subtle guide for the eye, not a heavy fence.
- **Atmosphere Overlay:** A global `dot-grid` overlay (opacity: 0.03) must be present on the `surface` layer, providing a "technical texture" that breaks the sterility of pure white.

---

## 5. Components

### Buttons
- **Primary:** `primary` (#021934) background with `on-primary` (#FFFFFF) text. Rectangular with a 4px radius (`md`). 
- **Secondary:** `surface-container-highest` background. No border.
- **Tertiary:** Text-only in `primary` with a 1px hairline underline on hover.

### Input Fields
- **Style:** Underline-only or 4-sided hairline using `outline-variant`. 
- **States:** Focus state moves the hairline color to `primary` (#021934) and thickens it to 1.5px. No glowing "halos."

### Cards & Lists
- **Rule:** Forbid the use of divider lines between list items. Use `body-sm` vertical padding (12px-16px) to create separation.
- **Cards:** Use `surface-container-lowest` (#FFFFFF) with a `none` or `sm` (2px) border radius. Separate cards via the grid, not borders.

### The "Monograph" Data Table
- Data tables should use `label-sm` for headers (all-caps).
- Alternate rows using `surface-container-low` instead of horizontal lines. This maintains the "White Canvas" aesthetic while ensuring row-tracking legibility.

---

## 6. Do’s and Don’ts

### Do
- **Do** use asymmetrical layouts (e.g., a 4-column empty "gutter" on the left of a 8-column text block).
- **Do** use 0.5px hairlines for technical accents.
- **Do** lean into extreme vertical white space between sections.
- **Do** ensure all serif typography is set to `optical-sizing: auto` for maximum sharpness.

### Don’t
- **Don't** use border-radius above 4px. Round "pill" buttons are strictly prohibited.
- **Don't** use gradients, blurs, or glassmorphism. This system is about the "ink on paper" honesty.
- **Don't** use icons as primary navigation elements; use text labels (`label-md`) to maintain the academic tone.
- **Don't** use pure black (#000). Always use `on-surface` (#1C1B1B) to keep the contrast high but sophisticated.