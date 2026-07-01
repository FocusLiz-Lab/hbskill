#!/usr/bin/env python3
"""Download the full atom library for this skill from GitHub."""

from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

REPO = "FocusLiz-Lab/hbskill"
ATOM_DIR = "知识库/原子库"


def package_root() -> Path:
    return Path(__file__).resolve().parents[1]


def fetch_json(url: str):
    with urllib.request.urlopen(url, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def download(url: str, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as response:
        target.write_bytes(response.read())


def main() -> int:
    encoded_dir = urllib.parse.quote(ATOM_DIR)
    api_url = f"https://api.github.com/repos/{REPO}/contents/{encoded_dir}?ref=main"
    files = [item for item in fetch_json(api_url) if item.get("type") == "file"]
    if not files:
        print("未在 GitHub 仓库中找到原子库文件。", file=sys.stderr)
        return 1

    target_dir = package_root() / ATOM_DIR
    for item in files:
        name = item["name"]
        if not (name.endswith(".jsonl") or name == "README.md"):
            continue
        print(f"下载 {name} ...")
        download(item["download_url"], target_dir / name)

    print(f"完成：{target_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
