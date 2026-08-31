# Cloudflare Pages Preview Handoff

This handoff exists so the Konstruction build can be previewed without accidentally launching The Manik Cryptid’s Resurrection Artifact Universe to the public as a finished site.

## Current repo facts

- GitHub repository: `manikdemonspawn/the-manik-cryptid`
- Public / production branch: `main`
- Active technical build branch: `construction`
- Universe-facing wording: **Konstruction** / **KONSTRUCTION BUILD** / **UNDER KONSTRUCTION**
- Current site status: preview candidate only; not approved for public launch
- The future Mausoleum remains posthumous-only and must not appear as an active portal
- Restricted / adult material must remain absent until real age assurance and direct asset protection exist

## Cloudflare Pages goal

Create a Cloudflare Pages project connected to GitHub so the `construction` branch can generate preview deployments while `main` remains the production branch and remains intentionally empty / offline until creator approval.

## Recommended Cloudflare project settings

Use these settings when creating the Pages project:

| Setting | Value |
|---|---|
| Git provider | GitHub |
| Repository | `manikdemonspawn/the-manik-cryptid` |
| Project name | `the-manik-cryptid` or `the-manik-cryptid-preview` |
| Production branch | `main` |
| Framework preset | None / Static HTML / No framework |
| Build command | Leave blank / none |
| Build output directory | Leave blank if Cloudflare allows; otherwise use repo root (`/` or `.` depending on the dashboard prompt) |
| Root directory | Repository root |
| Preview branch to allow | `construction` |
| Custom domain | Do not attach yet |
| Access / password protection | Add later if needed before sharing preview links widely |

## Why production branch should stay `main`

`main` is intentionally not the active living site. Keeping `main` as the production branch helps prevent Cloudflare from treating `construction` as the public production site.

The intended flow is:

1. `main` = production placeholder / no launch
2. `construction` = preview deployments only
3. launch later requires explicit creator approval before merging or republishing

## Preview deployment behavior

Cloudflare Pages Git integration can create preview deployments for non-production branches. Keep branch controls set so `construction` is included as a preview branch. If Cloudflare defaults to deploying all non-production branches, that is acceptable for now, but the safer setting is to explicitly include only `construction` if the dashboard offers custom branch controls.

## Safety headers already added

The repo contains a root `_headers` file for Cloudflare Pages. It applies to all paths and adds:

- `X-Robots-Tag: noindex, nofollow, noarchive`
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Referrer-Policy: strict-origin-when-cross-origin`
- restrictive Permissions-Policy values

This is an extra belt-and-suspenders safeguard on top of the existing HTML `<meta name="robots" content="noindex,nofollow,noarchive">` tags.

## PC dashboard steps

1. Open Cloudflare.
2. Go to **Workers & Pages**.
3. Choose **Create application** or **Create project**.
4. Choose **Pages**.
5. Choose **Connect to Git**.
6. Authorize GitHub if prompted.
7. Select `manikdemonspawn/the-manik-cryptid`.
8. Use the settings table above.
9. Deploy.
10. After deployment, open the `construction` preview URL, not the production URL.
11. Verify the preview shows:
    - The Nexus
    - eight primary realms
    - bottom Katakombs portal
    - **KONSTRUCTION BUILD** wording
    - no active Mausoleum portal
    - Forbidden Library construction safety marker
    - no restricted/adult content

## Do not do these yet

- Do not attach a custom domain.
- Do not enable public indexing.
- Do not merge `construction` into `main`.
- Do not upload adult/restricted content.
- Do not add final cultural inscriptions until verified.
- Do not activate the Mausoleum.

## After preview exists

Record the preview URL in `docs/BUILD_STATUS.md` or a future deployment log only after it has been verified. Do not treat a successful preview deployment as launch approval.
