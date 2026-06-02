#!/usr/bin/env python3
"""Personal Morning Hub — dispatches merged briefing jobs."""

from __future__ import annotations

import os
import runpy
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parent

JOBS = {
    "morning_brief": ROOT / "jobs" / "morning_brief.py",
    "ai_news": ROOT / "jobs" / "ai_news" / "main.py",
    "crypto_weekly": ROOT / "jobs" / "crypto" / "main.py",
}


def run_job(name: str) -> None:
    script = JOBS.get(name)
    if not script:
        raise SystemExit(f"Unknown job: {name}. Choose from: {', '.join(JOBS)}")

    print(f"Running job: {name}")
    if name == "morning_brief":
        os.chdir(ROOT)
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
    else:
        job_dir = str(script.parent)
        os.chdir(job_dir)
        if job_dir not in sys.path:
            sys.path.insert(0, job_dir)
    runpy.run_path(str(script), run_name="__main__")


def main() -> None:
    job = os.getenv("JOB", "").strip()
    if not job:
        raise SystemExit("Set JOB to one of: morning_brief, ai_news, crypto_weekly")
    try:
        run_job(job)
    except SystemExit:
        raise
    except Exception:
        traceback.print_exc()
        raise SystemExit(1)


if __name__ == "__main__":
    main()
