# Checklist Fold-In — 2026-10-11

Manik downloaded 5 Webflow University checklists tonight. They are Webflow-product
docs, but the underlying craft applies to our hand-built static site on
Cloudflare Pages. This file folds what's useful into the build plan, mapped
against what already exists. Nothing here invents Kanon. Kreator decisions
1 and 3–12 remain PENDING KREATOR APPROVAL; decision 2 (keep each Realm's
visual style as designed) stays resolved.

Source files (her downloads): `~/workspace/user/files/`
- design-system-checklist_2_dnez.md
- seo-checklist_4_wixs.md
- pre-launch-checklist_1_ta60.md
- optimize-checklist_0_nr3g.md
- optimize-checklist-for-non-webflow-sites_3_msaf.md

(Copies already live under `resources/webflow-guides/` from an earlier pass.)

Key translation note: this site is NOT Webflow. Anything naming a Webflow
panel, CMS, Library, or the Optimize product does not directly apply. The
principle underneath usually does — those are marked ADAPTED below.

## 1. Design system (from design-system-checklist)

| Checklist item | Status in this build |
|---|---|
| Define design system goals | DONE — goals are Kanon-driven: 8 Realm portals in Kanon order, each Realm keeps its designed visual style (Kreator decision 2, resolved) |
| Organize components/styles | DONE — `assets/css/` per-concern stylesheets, `templates/` for reusable page types, `data/` for machine-readable content |
| Naming rules, documented | DONE — Kanon spellings locked (Krypt not Crypt, Kurio Shoppe, Apothekary, Katakombs, etc.); legacy paths kept as noindex redirects, not active nav |
| Style guide page/site | OPEN — no living style-guide page exists yet. ADAPTED task: build an internal (noindex) style-guide page showing Realm color/type/spacing tokens for consistency checks |
| Accessibility built into the system | PARTIAL — reduced-motion + keyboard-focus support exist. ADAPTED tasks still open: color-contrast pass per Realm palette, heading-level discipline, alt text from final imagery (already in LAUNCH_CHECKLIST) |
| Design tokens / variables | PARTIAL — CSS exists per concern; ADAPTED task: formalize shared tokens (Realm colors, spacing scale, type scale) as CSS custom properties so a Realm re-skin touches one place |
| Global styles, components, variants, slots | ADAPTED — our equivalents are `templates/` + `assets/css/` hooks. No new invention; keep extending the existing pattern |
| Motion system, kept consistent | OPEN — ADAPTED task: document the one motion language (durations, easing, what animates) so Realm pages don't each invent their own; respect reduced-motion throughout |
| Document the system | OPEN — this file + STRUCTURE.md + ART_ASSET_CONTRACT.md are the start; the style-guide page becomes the living reference |

## 2. SEO (from seo-checklist)

| Checklist item | Status in this build |
|---|---|
| Clear shallow site structure + nav | DONE — Nexus → 8 Realm portals, max 2 clicks; Katakombs as legal/admin only, not a 9th Realm |
| Responsive for desktop + mobile | OPEN — must verify on narrow screens (already in LAUNCH_CHECKLIST); Realm visual styles must survive small viewports |
| Keyword research | DEFERRED — Kreator call; her brand terms are Kanon ("The Manik Cryptid", "Resurrection Artifact Universe"), not SEO-invented |
| Logical H1–H6 hierarchy, one H1 per page | OPEN — audit pass needed across all Realm pages |
| HTML5 semantic tags | OPEN — verify header/nav/main/section/footer usage per page |
| Clean descriptive URLs | DONE — Kanon paths; legacy spellings preserved as noindex notices |
| Meta title + meta description per page | OPEN — not yet written; unique per Realm page, titles ≤60 chars, descriptions ≤160 |
| Open Graph per page (social previews) | OPEN — not yet set; each Realm page gets its own OG title/description/image |
| Descriptive alt text | OPEN — already in LAUNCH_CHECKLIST; write from FINAL imagery only, ≤125 chars, no "image of" |
| Quality content (E-E-A-T) | KANON — her voice, her stories; no invented authority copy |
| SSL / HTTPS | DONE via Cloudflare Pages (auto) |
| Google Search Console + sitemap submit | DEFERRED to launch readiness — preview stays noindex until she approves public launch |
| Analytics | DEFERRED — "chosen with privacy in mind" per LAUNCH_CHECKLIST; no tracking on preview |
| Staging subdomain noindex | DONE — `_headers` sets `X-Robots-Tag: noindex, nofollow, noarchive` on the construction preview |
| Custom 404 with useful nav | DONE — `404.html` exists; OPEN: verify it's styled to the Universe and links back to Nexus |
| Minify CSS/JS/HTML | OPEN — enable at publish; remove unused classes/interactions first |
| Compress images (WebP/AVIF) | PARTIAL — forest panorama already WebP; OPEN: sweep remaining JPG/PNG assets |
| 301 redirects | DONE in spirit — legacy paths are noindex notices pointing at Kanonikal paths |
| Canonical tags | OPEN — set when custom domain goes live, not before |
| Schema markup, featured snippets, AI-search optimization | DEFERRED — post-launch nice-to-haves, Kreator call |
| Regular site audits | DONE in tooling — `scripts/site_audit.py` exists; OPEN: run it as a pre-publish gate |

## 3. Pre-launch (from pre-launch-checklist)

Folded into the existing LAUNCH_CHECKLIST.md rather than duplicated. New items
this checklist adds that weren't already there:

- [ ] Favicon exists and shows in browser tabs (not previously listed — ADD)
- [ ] Social preview image uploaded for OG sharing (pairs with OG task above)
- [ ] Mobile tap targets ≥44px with spacing (ADD to the mobile check)
- [ ] No leftover placeholder / lorem ipsum copy anywhere (ADD — proofread pass)
- [ ] Third-party embeds/scripts verified at all breakpoints, unused ones removed (ADD)
- [ ] Forms tested IF any exist at launch (none currently; conditional)

Everything else on the pre-launch list (layout consistency, responsiveness,
proofread, link audit, animations, custom code, headings, alt text, titles,
meta, asset weight, minification, accessibility, SEO pass, staging test,
domain, SSL/indexing) is already covered between LAUNCH_CHECKLIST.md and
sections 1–2 above.

## 4. Optimize checklists (both — Webflow Optimize product)

NOT APPLICABLE as product: Webflow Optimize / the Optimize JS snippet are
Webflow products; this is a static hand-built site. No snippet gets installed.

The one transferable principle, kept: define 2–3 conversion goals BEFORE
launch so post-launch iteration has a signal (e.g. Realm portal clicks,
artifact registry engagement, mailing-list signup IF she ever adds one).
Goals are Kreator-defined, not invented. Post-launch only — no tracking on
the construction preview.

## Build order (checklist-derived, Kanon-safe)

1. Tokens + style-guide page (internal, noindex) — §1
2. Semantic HTML + heading hierarchy sweep — §1/§2
3. Alt text from final imagery — §2 (needs final art first)
4. Meta titles/descriptions + OG tags + favicon + social preview image — §2/§3
5. Image compression sweep (WebP/AVIF) + minify + dead-code removal — §2/§3
6. 404 styling verification + tap-target + placeholder-copy sweeps — §3
7. `site_audit.py` as pre-publish gate, every time — §2
8. Launch-flip runbook: canonical tags, sitemap, Search Console, robots/indexing
   switch — written now, executed only on her explicit launch approval — §2/§3
9. Post-launch: Kreator-defined goals, privacy-minded analytics, schema — §4

## What this does NOT change

- No Kanon invented, no Realm renamed, no lore filled in.
- Kreator decisions 1, 3–12 still pending. Nothing here answers them.
- Preview stays noindex. No custom domain. No launch without her word.
- 17 commits still ahead of origin — push waits on her GitHub auth.
