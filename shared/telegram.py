"""Shared Telegram helpers for morning hub jobs."""

from __future__ import annotations

import os
import urllib.parse
import urllib.request


def token() -> str:
    return os.getenv("TELEGRAM_BOT_TOKEN") or os.getenv("TELEGRAM_TOKEN", "")


def chat_id() -> str:
    return os.getenv("TELEGRAM_CHAT_ID") or os.getenv("CHAT_ID", "")


def send_message(text: str, *, parse_mode: str | None = None) -> None:
    bot_token = token()
    chat = chat_id()
    if not bot_token or not chat:
        raise RuntimeError("Missing TELEGRAM_BOT_TOKEN/TELEGRAM_CHAT_ID")

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat,
        "text": text,
        "disable_web_page_preview": "true",
    }
    if parse_mode:
        payload["parse_mode"] = parse_mode

    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        if resp.status != 200:
            body = resp.read().decode("utf-8")
            raise RuntimeError(f"Telegram error: {resp.status} {body}")


def send_chunks(parts: list[str]) -> None:
    for part in parts:
        send_message(part)
