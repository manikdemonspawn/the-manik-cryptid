# Webflow CMS — resource notes (2026-10-11)

Source: https://webflow.com/feature/cms

## Core idea
Webflow's CMS is visual + composable: collections hold structured content, one template layout renders every item automatically.

## Why it matters for the-manik-cryptid build
- **Blog/interludes library**: perfect CMS use — write once, the Collection page template does the design.
- **Dynamic lists**: "all stories," "all episodes," etc. via CMS list blocks with filters/sort.
- **Reference fields**: link collections together (e.g., a "book" entry pointing at its "chapters").
- **Bulk import via CSV**: if Gremmy's blueprint content lives in a spreadsheet, it can be bulk-loaded.

## Headless / API angle
MACH-certified headless CMS APIs — content can be pushed/pulled programmatically, served to other channels (app, Discord bot, newsletter). Relevant later for the SaypheSpayse app / Phase 2 software work.

## Collaboration bits
- On-canvas editing: editors change text right on the page.
- Commenting, real-time co-editing, branching/staging/approvals for publishing.

## AI hooks
- AI site builder, AI-generated CMS Collection items (beta), AI copy generation, SEO/AEO audits.

## Gotchas
- Enterprise plans needed for very large item counts (hundreds of thousands); fine at our scale.
- SEO + AEO built in — aligns with the AEO guide filed separately.
