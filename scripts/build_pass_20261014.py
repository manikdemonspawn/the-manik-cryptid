#!/usr/bin/env python3
"""Build pass 2026-10-14 — blanket Kreator OK.
1. Inject meta descriptions + OG tags (18 pages) per docs/META_DRAFTS.md.
   og:image = brand banner (forest-panorama-fused-v1.webp), decided 2026-10-14.
   og:url   = construction preview URL (no custom domain yet).
2. WebP swap: forest-variant-fairies-v1.jpg -> .webp (same art, ~100KB saved).
3. Favicon: derive 32px + 180px PNGs from fused panorama crop; link on all pages.
4. 404: wire forest-master-v1.jpg into "Lost in the Woods".
5. Yard sale: integrations declaration banner (Kreator decision 10 of 12).
6. Katakombs: Fine Print section (decision 12 placement); "Fine print" footer
   link at the bottom of every Realm incl. Nexus/Forest (decision 12).
7. Update META_DRAFTS.md status header.
Nothing here invents Kanon. No legal language is invented (decision 12 copy
remains the Kreator's to write).
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREVIEW = "https://construction.the-manik-cryptid.pages.dev"
OG_IMAGE = PREVIEW + "/assets/images/forest/forest-panorama-fused-v1.webp"

DESCRIPTIONS = {
    "index.html": "A fairy forest at the center of the Cryptid's Resurrection Artifact Universe. Eight thresholds, one haunted woods, zero ordinary geography.",
    "realm-index.html": "Don't feel like solving a haunted forest puzzle? A plain list of every realm threshold in the Resurrection Artifact Universe. Pick a door.",
    "404.html": "That path doesn't exist \u2014 the woods do that sometimes. Head back to the Nexus and pick a threshold that actually goes somewhere.",
    "realms/library/index.html": "Nobody walks into a Vatican-scale collection with muddy boots. The Library is the archive: writing, audio, soundscapes, apps, art.",
    "realms/library/archive/index.html": "Not a bookshelf \u2014 an institution. Writing, audio, soundscapes, apps, artwork, multimedia, and the platforms where artifacts live.",
    "realms/library/forbidden/index.html": "The black door means it. Mature collections live behind it, and the gate doesn't take your word for it. Adults only, no exceptions.",
    "realms/museum/index.html": "Stonehenge is the door. Lineage, family lore, milestones, credentials, and the artifacts that explain what made the Cryptid.",
    "realms/krypt/index.html": "Guarded memory, protected truth, honored dead. The vault for what belongs to remembrance \u2014 coffin optional, reverence required.",
    "realms/guildhall/index.html": "Disciplines, work samples, crafts, and the things the Cryptid can actually do. Castle door. Flat out.",
    "realms/morgue/index.html": "Dead projects get preserved here, paperwork and all. Resurrection never erases the death record \u2014 even necromancy has administration.",
    "realms/kurio-shop/index.html": "A crooked round-door storefront. What the Cryptid made stays separate from what she found and recommends. Manik-made goods live here.",
    "realms/kurio-shop/yard-sale/index.html": "Stuff the Cryptid found, uses, likes, or recommends \u2014 not the same as Manik-made goods. Practical picks, grouped by what they help with.",
    "realms/apothecary/index.html": "Upstairs in the Kurio Shoppe, behind a rope. Under konstruction \u2014 contents still under lock.",
    "realms/forge/index.html": "The Forge exists. The blueprint is still under lock. Under konstruction \u2014 come back when the Kreator says so.",
    "realms/katakombs/index.html": "The cellar door to the legalese realm: policies, permissions, administration, infrastructure. Boring, necessary, deliberately separate.",
    "realms/mausoleum/index.html": "The Kreator is alive, so this is not a memorial. The Mausoleum stays sealed until it's actually needed. No active portal.",
    "realms/semmaterry/index.html": "The burial ground for absolutely dead artifacts. The Morgue records the death; the Semmaterry keeps the grave. Permanent on the record.",
    "registry-preview.html": "Konstruction-only diagnostic proving artifacts can load from structured data. Not lore navigation \u2014 stays noindex.",
}

report = []

def rel_to(page, target):
    return os.path.relpath(target, os.path.dirname(page)).replace(os.sep, "/")

def page_url(page):
    if page == "index.html":
        return PREVIEW + "/"
    if page.endswith("/index.html"):
        return PREVIEW + "/" + page[:-len("index.html")]
    return PREVIEW + "/" + page

for page, desc in DESCRIPTIONS.items():
    p = os.path.join(ROOT, page)
    html = open(p, encoding="utf-8").read()
    orig = html

    # --- meta description ---
    if '<meta name="description"' in html:
        report.append(f"{page}: description already present, skipped")
    else:
        m = re.search(r"<title>(.*?)</title>", html, re.S)
        title = m.group(1) if m else page
        block = [f'  <meta name="description" content="{desc}">']
        if page != "registry-preview.html":
            block += [
                f'  <meta property="og:title" content="{title}">',
                f'  <meta property="og:description" content="{desc}">',
                '  <meta property="og:type" content="website">',
                f'  <meta property="og:url" content="{page_url(page)}">',
                f'  <meta property="og:image" content="{OG_IMAGE}">',
            ]
        # favicon links (relative per page depth)
        fav = rel_to(page, "assets/images/forest/favicon-32x32.png")
        ati = rel_to(page, "assets/images/forest/apple-touch-icon.png")
        if "favicon-32x32.png" not in html:
            block += [
                f'  <link rel="icon" type="image/png" sizes="32x32" href="{fav}">',
                f'  <link rel="apple-touch-icon" href="{ati}">',
            ]
        html = html.replace("</title>", "</title>\n" + "\n".join(block), 1)
        report.append(f"{page}: meta/OG/favicon injected")

    # --- fine-print footer link (decision 12): bottom of every Realm + Nexus ---
    if '<nav aria-label="Way out">' in html and "fine-print" not in html.split('<nav aria-label="Way out">')[-1].split("</nav>")[0]:
        fp = rel_to(page, "realms/katakombs/index.html") + "#fine-print"
        html = html.replace(
            '<nav aria-label="Way out">',
            '<nav aria-label="Way out">', 1)
        # insert before the closing </nav> of the way-out nav
        head, sep, tail = html.partition('<nav aria-label="Way out">')
        nav_close = tail.find("</nav>")
        tail = tail[:nav_close] + f'<a href="{fp}">Fine print</a>\n' + tail[nav_close:]
        html = head + sep + tail
        report.append(f"{page}: fine-print footer link added")
    elif "Fine print" in html or "#fine-print" in html:
        pass
    else:
        report.append(f"{page}: NO way-out nav found, fine-print link skipped")

    if html != orig:
        open(p, "w", encoding="utf-8").write(html)

# --- WebP swap: fairies jpg -> webp (same art) ---
p = os.path.join(ROOT, "index.html")
html = open(p, encoding="utf-8").read()
if "forest-variant-fairies-v1.jpg" in html:
    html = html.replace("forest-variant-fairies-v1.jpg", "forest-variant-fairies-v1.webp")
    open(p, "w", encoding="utf-8").write(html)
    report.append("index.html: fairies jpg -> webp swapped")

# --- 404: wire the forest master ---
p = os.path.join(ROOT, "404.html")
html = open(p, encoding="utf-8").read()
if "forest-master-v1.jpg" not in html:
    fig = '''    <figure class="lost-woods-art">
      <img src="assets/images/forest/forest-master-v1.jpg" alt="Dark forest at night with a hand-painted wooden sign nailed to a tree reading 'LEAVE ME ALONE'">
    </figure>
'''
    html = html.replace("    </section>\n  </main>", "    </section>\n" + fig + "  </main>", 1)
    open(p, "w", encoding="utf-8").write(html)
    report.append("404.html: forest-master wired into Lost in the Woods")

# --- Yard sale: integrations declaration banner (decision 10 of 12) ---
p = os.path.join(ROOT, "realms/kurio-shop/yard-sale/index.html")
html = open(p, encoding="utf-8").read()
if "integrations-banner" not in html:
    banner = '''    <aside class="integrations-banner" aria-label="External integrations declaration">
      <strong>EXTERNAL INTEGRATIONS &mdash; DECLARED</strong><br>
      Legal bit: this site currently runs no analytics, no email list, no tracking pixels, and no third-party integrations. If any are ever added, they get declared here, in plain talk, before they go live.<br>
      Personal bit, from the Kreator: &ldquo;You&rsquo;re a guest in my woods, not a product on my shelf. I don&rsquo;t want your data &mdash; I want you to have a good time and maybe take home something weird.&rdquo;
    </aside>

'''
    anchor = '<div class="yard-exit" aria-hidden="true"><strong>YOU HAVE STEPPED OUT THE BACK DOOR.</strong></div>\n'
    html = html.replace(anchor, anchor + "\n" + banner, 1)
    open(p, "w", encoding="utf-8").write(html)
    report.append("yard-sale: integrations declaration banner added (decision 10)")

# --- Katakombs: Fine Print section (decision 12 placement; copy still hers) ---
p = os.path.join(ROOT, "realms/katakombs/index.html")
html = open(p, encoding="utf-8").read()
if 'id="fine-print"' not in html:
    section = '''    <section class="section site-shell" id="fine-print">
      <h2>Fine Print</h2>
      <p>The full legal language &mdash; privacy, terms, disclaimers &mdash; is still being written by the Kreator. Her standing requirement: it must be thorough and detailed enough to actually protect her. Until that language is finished and verified, this section is a placeholder, not a policy. Nothing here is the final word.</p>
      <p class="wayfinding-note">Linked from the bottom of every Realm, per Kreator decision 12 of 12.</p>
    </section>

'''
    html = html.replace("  </main>", section + "  </main>", 1)
    open(p, "w", encoding="utf-8").write(html)
    report.append("katakombs: fine-print section added (decision 12)")

# --- META_DRAFTS.md status ---
p = os.path.join(ROOT, "docs/META_DRAFTS.md")
md = open(p, encoding="utf-8").read()
md = md.replace(
    "**STATUS: DRAFT \u2014 NEEDS HER APPROVAL. NOTHING BELOW IS INJECTED INTO ANY PAGE.**",
    "**STATUS: INJECTED 2026-10-14 under blanket Kreator OK.** Descriptions live on all 18 pages as drafted. Flag any page for a rewrite anytime.")
md = md.replace(
    "2. Which image is the OG share image? (Forest master is the candidate \u2014 her pick.)",
    "2. RESOLVED 2026-10-14: OG share image = forest-panorama-fused-v1.webp (brand banner).")
md = md.replace(
    "3. What's the canonical domain for `og:url`? (Undecided \u2014 no OG injection until this is answered.)",
    "3. og:url uses the construction preview URL until a custom domain is chosen.")
open(p, "w", encoding="utf-8").write(md)
report.append("docs/META_DRAFTS.md: status updated")

print("\n".join(report))
