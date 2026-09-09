"""
Run this BEFORE class (not part of the student notebook) to pre-scrape a
fallback dataset zip. Hand it out over AirDrop/USB/shared drive if live
DuckDuckGo scraping is flaky or slow on the classroom network.

Usage:
    python3 -m venv .venv && source .venv/bin/activate
    pip install ddgs pillow requests
    python3 instructor_backup_scrape.py
"""
import io
import shutil
import zipfile
from pathlib import Path

import requests
from PIL import Image
from ddgs import DDGS

HEADERS = {"User-Agent": "Mozilla/5.0"}

CLASSES = {
    "golden_retriever": "golden retriever dog photo",
    "poodle": "poodle dog photo",
}
IMAGES_PER_CLASS = 100
OUT_DIR = Path("backup_dataset")
ZIP_PATH = Path("backup_dataset.zip")


def scrape_class(query, out_dir, n):
    out_dir.mkdir(parents=True, exist_ok=True)
    with DDGS() as ddgs:
        results = list(ddgs.images(query, max_results=n))
    saved = 0
    for r in results:
        url = r.get("image")
        if not url:
            continue
        try:
            resp = requests.get(url, headers=HEADERS, timeout=6)
            img = Image.open(io.BytesIO(resp.content)).convert("RGB")
            img.save(out_dir / f"{saved:03d}.jpg", "JPEG", quality=90)
            saved += 1
        except Exception:
            continue
    return saved


if __name__ == "__main__":
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)

    for folder_name, query in CLASSES.items():
        n = scrape_class(query, OUT_DIR / folder_name, IMAGES_PER_CLASS)
        print(f"{folder_name}: {n} images saved")

    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in OUT_DIR.rglob("*.jpg"):
            zf.write(f, f.relative_to(OUT_DIR.parent))

    print(f"\nWrote {ZIP_PATH} ({ZIP_PATH.stat().st_size / 1024:.0f} KB)")
    print("If live scraping fails in class: students upload this zip to Colab")
    print('and run: !unzip -q backup_dataset.zip -d data  (skip the Step 2 scrape cell)')
