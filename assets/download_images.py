"""
Download placeholder images for Betty Mobile Massage using Unsplash API.

Usage:
  python assets/download_images.py

Environment:
  UNSPLASH_ACCESS_KEY (optional) - if not set, falls back to provided key.
"""

import os
import pathlib
import requests

ASSET_DIR = pathlib.Path(__file__).parent
ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY", "VaweFqhg_MbRYL6IB7oxJ8Ef_AHRGcfzNCk7nbIUx4Y")

# target filenames mapped to search queries
TARGETS = {
    "hero-massage-placeholder.jpg": "professional mobile massage in home calm lighting",
    "session-1-placeholder.jpg": "massage table living room soft light",
    "session-2-placeholder.jpg": "massage tools neatly arranged spa",
    "video-poster-placeholder.jpg": "massage therapist preparing table",
    "gallery-1-placeholder.jpg": "massage therapy relaxing room warm tones",
    "gallery-2-placeholder.jpg": "aromatherapy candles spa closeup",
    "gallery-3-placeholder.jpg": "massage client relaxed calm ambiance",
    "gallery-4-placeholder.jpg": "towels and oils spa warm light",
    "gallery-5-placeholder.jpg": "soothing massage hands on back",
    "gallery-6-placeholder.jpg": "spa lighting wellness room",
    "about-hero-placeholder.jpg": "massage therapist portrait smiling professional",
    "services-hero-placeholder.jpg": "massage table setup cozy home",
    "portfolio-hero-placeholder.jpg": "spa atmosphere warm light",
    "contact-hero-placeholder.jpg": "phone and notebook spa desk",
}

SEARCH_URL = "https://api.unsplash.com/search/photos"


def fetch_image(query: str) -> bytes:
    params = {"query": query, "per_page": 1, "page": 1}
    headers = {"Authorization": f"Client-ID {ACCESS_KEY}"}
    resp = requests.get(SEARCH_URL, params=params, headers=headers, timeout=20)
    resp.raise_for_status()
    results = resp.json().get("results", [])
    if not results:
        raise ValueError(f"No results for query: {query}")
    # pick regular quality to keep size moderate
    url = results[0]["urls"]["regular"]
    img = requests.get(url, timeout=30)
    img.raise_for_status()
    return img.content


def main():
    if not ACCESS_KEY:
        raise SystemExit("Missing UNSPLASH_ACCESS_KEY.")

    ASSET_DIR.mkdir(parents=True, exist_ok=True)

    for filename, query in TARGETS.items():
        out_path = ASSET_DIR / filename
        try:
            print(f"Downloading {filename} ...")
            content = fetch_image(query)
            out_path.write_bytes(content)
        except Exception as exc:  # noqa: BLE001
            print(f"Failed {filename}: {exc}")


if __name__ == "__main__":
    main()
