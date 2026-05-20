"""POST a briefing (or any text payload) to a Mattermost incoming webhook.

Pure stdlib — uses urllib so the dependency footprint stays at zero. A
Mattermost "incoming webhook" is a long-lived URL configured per
channel; the POST body is JSON of the shape:

    {"text": "...markdown...", "channel": "town-square",
     "username": "Briefing Bot", "icon_emoji": ":calendar:"}

Channel and username are optional (the webhook config carries defaults).
We split payloads longer than ``max_chars`` into multiple posts so a
busy-week briefing doesn't get silently truncated by Mattermost's
~16k message ceiling.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Iterable


# Mattermost's documented post-text limit is 16383 chars. We use a
# slightly smaller chunk size so headers + continuation markers fit.
DEFAULT_MAX_CHARS = 15000


class WebhookPostError(RuntimeError):
    """Raised when the webhook POST fails (network or non-2xx response)."""


@dataclass(frozen=True)
class PostResult:
    """Outcome of a webhook post attempt."""

    posted: int       # number of chunks successfully posted
    skipped: bool     # True if dry_run / empty text
    chunks: tuple[str, ...]


def resolve_webhook_url(explicit: str | None = None) -> str:
    """Resolve the webhook URL from explicit arg or env.

    Order:
      1. ``explicit`` (typically from --webhook-url)
      2. ``MATTERMOST_WEBHOOK_URL`` env
      3. ``MATTERMOST_BRIEFING_WEBHOOK_URL`` env (more specific)
    Raises ``WebhookPostError`` if none set.
    """
    candidates = [
        explicit,
        os.environ.get("MATTERMOST_BRIEFING_WEBHOOK_URL"),
        os.environ.get("MATTERMOST_WEBHOOK_URL"),
    ]
    for c in candidates:
        if c:
            return c
    raise WebhookPostError(
        "no Mattermost webhook URL: pass --webhook-url or set "
        "MATTERMOST_WEBHOOK_URL / MATTERMOST_BRIEFING_WEBHOOK_URL",
    )


def split_for_mattermost(text: str, *, max_chars: int = DEFAULT_MAX_CHARS) -> list[str]:
    """Split ``text`` into chunks that fit one Mattermost post each.

    Splits on blank-line boundaries first, then on single newlines if a
    paragraph itself exceeds the limit. Each chunk after the first is
    prefixed with ``(continued N/M)``.
    """
    if not text:
        return []
    if len(text) <= max_chars:
        return [text]

    # Soft split on blank lines (preserves markdown structure)
    paragraphs = text.split("\n\n")
    chunks: list[str] = []
    buf: list[str] = []
    buf_len = 0
    for p in paragraphs:
        # Each paragraph + the joining "\n\n" we'll add back
        add = len(p) + (2 if buf else 0)
        if buf_len + add > max_chars and buf:
            chunks.append("\n\n".join(buf))
            buf = [p]
            buf_len = len(p)
        else:
            buf.append(p)
            buf_len += add
    if buf:
        chunks.append("\n\n".join(buf))

    # Hard-split any single chunk that's still too big (e.g. one giant
    # paragraph). Rare but possible.
    out: list[str] = []
    for c in chunks:
        if len(c) <= max_chars:
            out.append(c)
        else:
            for i in range(0, len(c), max_chars):
                out.append(c[i : i + max_chars])

    total = len(out)
    if total <= 1:
        return out
    return [
        f"_(continued {i + 1}/{total})_\n\n{c}" if i > 0 else c
        for i, c in enumerate(out)
    ]


def post_text(
    text: str,
    *,
    webhook_url: str,
    channel: str | None = None,
    username: str | None = None,
    icon_emoji: str | None = None,
    timeout: float = 10.0,
) -> int:
    """POST one text payload to a Mattermost incoming webhook.

    Returns the HTTP status code. Raises ``WebhookPostError`` on
    network failure or non-2xx response.
    """
    body: dict = {"text": text}
    if channel:
        body["channel"] = channel
    if username:
        body["username"] = username
    if icon_emoji:
        body["icon_emoji"] = icon_emoji

    req = urllib.request.Request(
        webhook_url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = resp.status
            if status < 200 or status >= 300:
                raise WebhookPostError(
                    f"Mattermost webhook returned HTTP {status}",
                )
            return status
    except urllib.error.URLError as exc:
        raise WebhookPostError(
            f"failed to POST to Mattermost webhook: {exc}",
        ) from exc


def post_briefing(
    text: str,
    *,
    webhook_url: str,
    channel: str | None = None,
    username: str | None = "Briefing Bot",
    icon_emoji: str | None = ":calendar:",
    max_chars: int = DEFAULT_MAX_CHARS,
    dry_run: bool = False,
    timeout: float = 10.0,
) -> PostResult:
    """Split ``text`` into Mattermost-sized chunks and POST each.

    ``dry_run`` skips the actual HTTP call but still computes the
    chunks so the operator can preview what would land.
    """
    chunks = split_for_mattermost(text, max_chars=max_chars)
    if not chunks:
        return PostResult(posted=0, skipped=True, chunks=())
    if dry_run:
        return PostResult(posted=0, skipped=True, chunks=tuple(chunks))

    posted = 0
    for chunk in chunks:
        post_text(
            chunk,
            webhook_url=webhook_url,
            channel=channel,
            username=username,
            icon_emoji=icon_emoji,
            timeout=timeout,
        )
        posted += 1
    return PostResult(posted=posted, skipped=False, chunks=tuple(chunks))
