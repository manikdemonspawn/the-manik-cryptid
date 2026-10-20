#!/usr/bin/env python3
"""File the 9-image batch (2026-10-14). Filing only — nothing wired into pages.
Also: demon image to its own story folder; LIB-BOOK-004 (Court of Ash and Blood NSFW)."""
import json, os, shutil
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = os.path.expanduser("~/workspace/user/files")

FILING = [
    ("45903dc4-393e-465a-9261-943ac5a0f4c0-1_all_910_18_mu5a.jpg",  "assets/images/museum/sertifikate-ai-befuddlement.jpg"),
    ("45903dc4-393e-465a-9261-943ac5a0f4c0-1_all_1107_19_vvxg.png", "assets/images/books/mothers-day-miracle-ward-of-hicks-holler.png"),
    ("45903dc4-393e-465a-9261-943ac5a0f4c0-1_all_1246_20_84qy.jpg", "docs/reference/fairy-forest-nexus-dev-board.jpg"),
    ("45903dc4-393e-465a-9261-943ac5a0f4c0-1_all_1247_21_xuvb.jpg", "docs/reference/cryptids-dark-nexus-build-status.jpg"),
    ("45903dc4-393e-465a-9261-943ac5a0f4c0-1_all_1562_22_p2xf.jpg", "assets/images/kurio-shoppe/curio-shop-banner-v2.jpg"),
    ("45903dc4-393e-465a-9261-943ac5a0f4c0-1_all_1601_23_bcau.jpg", "assets/images/books/mothers-day-miracle-cover.jpg"),
    ("45903dc4-393e-465a-9261-943ac5a0f4c0-1_all_1602_24_xcuk.jpg", "assets/images/forest/fairy-daddys-girl-full.jpg"),
    ("45903dc4-393e-465a-9261-943ac5a0f4c0-1_all_1600_25_71sk.jpg", "assets/images/brand/manik-cryptid-font-comparison.jpg"),
    ("45903dc4-393e-465a-9261-943ac5a0f4c0-1_all_483_26_r74p.jpg",  "assets/images/forest/fairy-daddys-girl-portrait.jpg"),
]

os.makedirs(os.path.join(ROOT, "docs/reference"), exist_ok=True)
pushed = []
for src, dst in FILING:
    s = os.path.join(U, src)
    d = os.path.join(ROOT, dst)
    shutil.copy(s, d)
    # web-optimized twin for the API push (128KB argv limit)
    im = Image.open(d)
    if max(im.size) > 500:
        r = 500 / max(im.size)
        im = im.resize((int(im.width * r), int(im.height * r)), Image.LANCZOS)
    w = os.path.splitext(d)[0] + ".webp"
    im.save(w, "WEBP", quality=75)
    pushed.append(w)
    print(f"filed {dst} ({os.path.getsize(w)//1024}KB web)")

# Demon image -> its own story folder (NOT the website)
story_dir = os.path.expanduser("~/workspace/your_files/chaos-demon")
os.makedirs(story_dir, exist_ok=True)
shutil.copy(os.path.join(U, "1792020227908_7_st19.jpeg"),
            os.path.join(story_dir, "chaos-demon-cam03.jpeg"))
print("demon image -> ~/workspace/your_files/chaos-demon/")

# LIB-BOOK-004: Court of Ash and Blood (NSFW Edition) — cover per Kreator 2026-10-14
p = os.path.join(ROOT, "data/library.json")
d = json.load(open(p, encoding="utf-8"))
ids = {r["record_id"] for r in d["records"]}
if "LIB-BOOK-004" not in ids:
    d["records"].append({
        "record_id": "LIB-BOOK-004",
        "title": "Court of Ash and Blood (The Original Story)",
        "Kanonikal_title": "Court of Ash and Blood (The Original Story) — NSFW Edition, Book 1",
        "category": "fiction", "realm": "library", "creator": "The Manik Cryptid",
        "type": "book", "status": "IN_PROGRESS", "Kanon_status": "KREATOR-APPROVED",
        "archive_status": "NOT_ARCHIVED", "creation_date": None, "version": None,
        "description": "Court of Ash and Blood, the original story — NSFW edition, Book 1. Chapters publishing on Patreon.",
        "notes": "Cover art is the NSFW-edition cover (Kreator identification 2026-10-14); regular-edition cover pending. NSFW chapters live on Patreon behind its membership gate.",
        "source": None, "access": None,
        "media": {"audio_embed": None, "hero_image": "/assets/images/books/court-of-ash-and-blood-nsfw-cover.webp",
                  "thumbnail": "/assets/images/books/court-of-ash-and-blood-nsfw-cover.webp", "video_embed": None},
        "related_artifacts": [],
    })
    print("LIB-BOOK-004 added")
json.dump(d, open(p, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"total records: {len(d['records'])}")
print("WEBPUSH:" + "\nWEBPUSH:".join(w.replace(ROOT + "/", "") for w in pushed))
