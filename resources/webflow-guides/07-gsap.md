# GSAP (GreenSock Animation Platform) — resource notes (2026-10-11)

Source: https://gsap.com/

## What it is
A professional JavaScript animation library — the engine underneath Webflow's
visual Interactions panel. (Webflow acquired GSAP; the whole library, including
the former paid Club plugins, is now free.)

## Key tools
- **ScrollTrigger / scroll storytelling** — scroll-driven reveals, parallax, progress.
- **SVG plugins** — move, morph, draw SVG (great for sigils, dividers, animated logos).
- **Text effects** — SplitText-style character/word animations for headings.
- **Easings** — huge library of motion curves + custom ease builder.

## Do we need to "link" or install anything?
No. Inside Webflow, GSAP runs automatically — the Interactions panel IS GSAP with
a visual face. There is nothing to connect, no code to paste, no account needed.

## When the raw GSAP docs would matter
Only if we ever build animations by hand outside Webflow (custom code embeds,
a hand-built page, the future SaypheSpayse app). Then gsap.com/docs is the reference.

## Relevance to the-manik-cryptid build
- File-and-forget for now: every animation planned in the Interactions guide
  (05-interactions-animations.md) is GSAP-powered already.
- If a future custom embed needs fancy motion (animated Forest sigil, morphing
  divider), GSAP's SVG/text plugins are the toolkit — no new library to learn later.
