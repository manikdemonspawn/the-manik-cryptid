# Webflow Edit Mode — resource notes (2026-10-11)

Source: https://webflow.com/feature/edit-content

## Core idea
Edit Mode: change text, images, and CMS content directly on the live page —
no Designer access needed, no code, changes publish in minutes.

## What editors can do
- Edit static content (text, images, links, rich text) right on the canvas.
- Create/edit CMS Collection items (blog posts, etc.) with drafts + preview.
- Manage page-level SEO settings (meta title, description, OpenGraph).
- Manage media library assets.
- Publish options: single item immediately, staged, or full-site publish.

## Safety rails
Approvals, publishing workflows, site activity log, version control — an
editor can't silently break the live site.

## Roles
Content editor role: full editing power, zero design access. Multiple editors
can work simultaneously (last edit wins on the same element).

## Why it matters for the-manik-cryptid build
- This is how Manik will run the site day-to-day: write a post in the CMS,
  preview, publish — never touching the design.
- If anyone else ever posts (guest authors, etc.), the editor role keeps them
  out of the design.
