#!/usr/bin/env python3
"""Fetch NOAA/CPC weekly relative Niño 3.4 data and update data.json.
Uses only the Python standard library.
"""
from __future__ import annotations
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen

SOURCE_URL = "https://www.cpc.ncep.noaa.gov/data/indices/rel_wksst9120.txt"
OUT = Path(__file__).resolve().parent / "data.json"
START_DATE = datetime(2026, 1, 1)
ROW_RE = re.compile(
    r"^\s*(\d{2}[A-Z]{3}\d{4})\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s*$"
)

def fetch_text() -> str:
    req = Request(SOURCE_URL, headers={"User-Agent": "Niño34-school-monitor/1.0"})
    with urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")

def parse(text: str):
    values = []
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        dt = datetime.strptime(m.group(1), "%d%b%Y")
        if dt < START_DATE:
            continue
        nino34 = float(m.group(4))
        values.append({"date": dt.strftime("%Y-%m-%d"), "value": nino34})
    if not values:
        raise RuntimeError("No 2026+ Niño 3.4 rows parsed from NOAA source")
    values.sort(key=lambda x: x["date"])
    return values

def main():
    values = parse(fetch_text())
    payload = {
        "source": "NOAA/CPC Weekly Relative OISST.v2.1 Niño 3.4",
        "source_url": SOURCE_URL,
        "base_period": "1991–2020",
        "region": "5°É–5°D, 170°Ny–120°Ny",
        "updated": values[-1]["date"],
        "values": values,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {OUT.name}: {len(values)} points, latest {values[-1]}")

if __name__ == "__main__":
    main()
