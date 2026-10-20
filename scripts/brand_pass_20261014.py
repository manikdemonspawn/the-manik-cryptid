#!/usr/bin/env python3
"""Brand palette pass + Huntington Gothic book records (2026-10-14).
Kreator directive: the site is built around her brand palette —
BLACK #000000, BURGUNDY #800020, DEEP PURPLE #5A2D82, HOT PINK #FF69B4.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- 1. Brand palette CSS (appended to phase2.css, which loads after site.css) ----
p = os.path.join(ROOT, "assets/css/phase2.css")
css = open(p, encoding="utf-8").read()
brand_css = """
/* THE MANIK CRYPTID BRAND PALETTE — Kreator-locked 2026-10-14.
   BLACK #000000 • BURGUNDY #800020 • DEEP PURPLE #5A2D82 • HOT PINK #FF69B4 */
:root{
  --brand-black:#000000;
  --brand-burgundy:#800020;
  --brand-purple:#5A2D82;
  --brand-pink:#FF69B4;
}
.brand-strip{height:6px;border:0;background:linear-gradient(90deg,#000 0 25%,#800020 25% 50%,#5A2D82 50% 75%,#FF69B4 75% 100%);}
.hero h1{background:linear-gradient(115deg,#f7ecf4 15%,#FF69B4 52%,#5A2D82 88%);-webkit-background-clip:text;background-clip:text;color:transparent;}
.section h2::after{content:"";display:block;width:4.5rem;height:3px;margin-top:.45rem;background:linear-gradient(90deg,#800020,#5A2D82,#FF69B4);border-radius:2px;}
a:hover{color:var(--brand-pink);}
.status-chip{border-color:var(--brand-purple);color:#dccbf5;}
.btn{background:linear-gradient(135deg,#2b0a12,#241239);border-color:var(--brand-burgundy);color:#f3e7f5;}
.btn:hover{border-color:var(--brand-pink);filter:brightness(1.2);}
.catalog-modal-cover{display:block;max-width:220px;width:100%;height:auto;margin:0 auto 1rem;border-radius:.4rem;border:1px solid #3a3450;box-shadow:0 8px 28px rgba(0,0,0,.5);}
"""
if "--brand-pink" not in css:
    open(p, "w", encoding="utf-8").write(css.rstrip() + "\n" + brand_css)
    print("phase2.css: brand palette appended")
else:
    print("phase2.css: brand palette already present")

# ---- 2. Brand strip on the Nexus (right under the construction ribbon) ----
p = os.path.join(ROOT, "index.html")
h = open(p, encoding="utf-8").read()
old = '<div class="construction-ribbon">'
if "brand-strip" not in h and old in h:
    h = h.replace(old, '<div class="brand-strip" aria-hidden="true"></div>\n  ' + old, 1)
    open(p, "w", encoding="utf-8").write(h)
    print("index.html: brand strip added")
else:
    print("index.html: brand strip already present or ribbon not found")

# ---- 3. Palette card in the Guildhall ----
p = os.path.join(ROOT, "realms/guildhall/index.html")
h = open(p, encoding="utf-8").read()
card = '''<article class="worktable"><h3>Brand Palette</h3><img src="../../assets/images/brand/manik-cryptid-brand-palette.jpg" alt="The Manik Cryptid brand palette: black, burgundy, deep purple, hot pink"><p>Black #000000 &bull; Burgundy #800020 &bull; Deep purple #5A2D82 &bull; Hot pink #FF69B4. The whole site wears these colors.</p></article>'''
if "manik-cryptid-brand-palette" not in h:
    anchor = '<article class="worktable"><h3>Hands-On Crafts</h3>'
    assert anchor in h
    h = h.replace(anchor, card + anchor, 1)
    open(p, "w", encoding="utf-8").write(h)
    print("guildhall: brand palette card added")
else:
    print("guildhall: palette card already present")

# ---- 4. Modal cover art ----
p = os.path.join(ROOT, "assets/js/library-catalog.js")
js = open(p, encoding="utf-8").read()
old = '''    modalBody.appendChild(make("h3", "catalog-modal-title", record.title || "Untitled record"));'''
new = '''    modalBody.appendChild(make("h3", "catalog-modal-title", record.title || "Untitled record"));
    const coverSrc = record.media && (record.media.hero_image || record.media.thumbnail);
    if (coverSrc) {
      const coverImg = document.createElement("img");
      coverImg.src = coverSrc;
      coverImg.alt = "Cover art: " + (record.title || "artifact");
      coverImg.className = "catalog-modal-cover";
      modalBody.appendChild(coverImg);
    }'''
if "catalog-modal-cover" not in js:
    assert old in js
    js = js.replace(old, new, 1)
    open(p, "w", encoding="utf-8").write(js)
    print("catalog js: modal cover art")
else:
    print("catalog js: modal cover already present")

# ---- 5. The two Huntington Gothic book records ----
p = os.path.join(ROOT, "data/library.json")
d = json.load(open(p, encoding="utf-8"))
ids = {r["record_id"] for r in d["records"]}
books = [
    {
        "record_id": "LIB-BOOK-002",
        "title": "Huntington Gothic: The Odyssey",
        "Kanonikal_title": "Huntington Gothic: The Odyssey",
        "category": "fiction", "realm": "library", "creator": "The Manik Cryptid",
        "type": "book", "status": "IN_PROGRESS", "Kanon_status": "KREATOR-APPROVED",
        "archive_status": "NOT_ARCHIVED", "creation_date": None, "version": None,
        "description": "Book 1 of the Huntington Gothic series. 16 parts, 43,583 words. Cover art final; KDP edition in progress.",
        "notes": "Manuscript complete (restructured 2026-10-01). KDP EPUB built; upload is the Kreator's tap, still pending.",
        "source": None, "access": None,
        "media": {"audio_embed": None, "hero_image": "/assets/images/books/huntington-gothic-odyssey-cover.jpg",
                  "thumbnail": "/assets/images/books/huntington-gothic-odyssey-cover.jpg", "video_embed": None},
        "related_artifacts": [],
    },
    {
        "record_id": "LIB-BOOK-003",
        "title": "Huntington Gothic: The Manor House",
        "Kanonikal_title": "Huntington Gothic: The Manor House",
        "category": "fiction", "realm": "library", "creator": "The Manik Cryptid",
        "type": "book", "status": "IN_PROGRESS", "Kanon_status": "KREATOR-APPROVED",
        "archive_status": "NOT_ARCHIVED", "creation_date": None, "version": None,
        "description": "Book 2 of the Huntington Gothic series. Cover art final; manuscript in progress.",
        "notes": "Front-matter dedication (Kreator's words): \u201cHe was perfect for his imperfections.\u201d",
        "source": None, "access": None,
        "media": {"audio_embed": None, "hero_image": "/assets/images/books/huntington-gothic-manor-house-cover.jpg",
                  "thumbnail": "/assets/images/books/huntington-gothic-manor-house-cover.jpg", "video_embed": None},
        "related_artifacts": [],
    },
]
added = 0
for b in books:
    if b["record_id"] not in ids:
        d["records"].append(b)
        added += 1
json.dump(d, open(p, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"library.json: added {added} book records; total {len(d['records'])}")
