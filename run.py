#!/usr/bin/env python3
"""Personal Morning Hub — dispatches merged briefing jobs."""

from __future__ import annotations

import os
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run_job(name: str) -> None:
    jobs = {
        "morning_brief": ROOT / "jobs" / "morning_brief.py",
        "ai_news": ROOT / "jobs" / "ai_news" / "main.py",
        "crypto_weekly": ROOT / "jobs" / "crypto" / "main.py",
    }
    script = jobs.get(name)
    if not script:
        raise SystemExit(f"Unknown job: {name}. Choose from: {', '.join(jobs)}")

    print(f"Running job: {name}")
    os.chdir(script.parent if name != "morning_brief" else ROOT)
    runpy.run_path(str(script), run_name="__main__")


def main() -> None:
    job = os.getenv("JOB", "").strip()
    if not job:
        raise SystemExit("Set JOB to one of: morning_brief, ai_news, crypto_weekly")
    run_job(job)


if __name__ == "__main__":
    main()
