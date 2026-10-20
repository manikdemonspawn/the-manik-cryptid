# Webflow Designer — resource notes (2026-10-11)

Source: https://webflow.com/feature/design

## Core idea
The main workspace: visual canvas that generates production-ready HTML/CSS/JS
as you design. Not a mockup tool — what you draw IS the website.

## Key capabilities
- **Canvas**: drag-and-drop HTML elements, flexbox + CSS grid layouts,
  pixel-level styling control.
- **Design systems**: reusable components (nav, footer, forms), CSS classes,
  variables (colors, spacing, typography), component variants managed in one
  place, Shared Libraries across sites.
- **Figma import**: Figma to Webflow plugin converts components/layouts/styles
  into editable Webflow elements (see 02-figma-to-webflow.md).
- **AI**: site builder (generate a site from a prompt), section generation
  from the existing design system, copy generation, CMS item generation,
  code components (React, edited visually).
- **Launch**: one-click publish to Webflow hosting, or export clean
  HTML/CSS/JS/images on paid plans.

## Why it matters for the-manik-cryptid build
- This is where the Forest gets built: the canvas + grid + interactions.
- Components = the book cards, chapter headers, nav — build once, reuse.
- Variables = the Gothic palette (black, burgundy, plum, crimson) defined once,
  applied everywhere.
- AI site builder could scaffold the first draft of pages; Manik refines.
