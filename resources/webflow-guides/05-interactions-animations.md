# Webflow Interactions & Animations — resource notes (2026-10-11)

Source: https://webflow.com/feature/interactions-animations

## Core idea
Visual animation builder powered by **GSAP** — timeline-based, no code required.

## What's available
- **Triggers**: page load, scroll into view, hover, click, mouse movement.
- **Timeline editor**: fine control of duration, easing, CSS property changes.
- **Targeting**: by id, class, custom attribute, or custom query selector.
- **Scroll animations**: parallax, progress indicators, reveal-on-scroll.
- **Presets**: save an interaction, reuse it across pages.
- **Reduced-motion support**: built-in accessibility handling.
- **Breakpoints**: tailor animations per device size.

## Integrations
Lottie (After Effects exports), Spline (3D scenes), Rive (interactive vector graphics) — all driven through Webflow Interactions.

## AI angle
Agent can build interactions from a prompt ("add a fade-in on scroll to the hero section") using the same Interactions panel.

## Why it matters for the-manik-cryptid build
- The Forest hero: scroll-triggered reveals, fog drift, parallax layers.
- Micro-interactions: button hovers, card flips on the book pages.
- Keep it tasteful: animations guide attention, not decorate. Heavy motion + reduced-motion fallback = accessibility (see accessibility guide filed).

## Gotchas
- Performance: GSAP is optimized, but use interactions strategically; presets avoid duplicated code.
