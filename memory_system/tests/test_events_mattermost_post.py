"""Unit tests for the Mattermost-webhook briefing poster.

Pure-Python — uses ``unittest.mock`` to intercept ``urlopen`` so no
real HTTP traffic happens. Covers the URL resolution waterfall, the
chunk splitter (single-post / paragraph-split / hard-split), the
dry-run path, and POST failure handling.
"""
from __future__ import annotations

import io
import json
from unittest.mock import patch

import pytest

from memory_system.events.mattermost_post import (
    DEFAULT_MAX_CHARS,
    PostResult,
    WebhookPostError,
    post_briefing,
    post_text,
    resolve_webhook_url,
    split_for_mattermost,
)


# --------------------------------------------------------------------------
# resolve_webhook_url
# --------------------------------------------------------------------------


class TestResolveWebhookUrl:
    def test_explicit_arg_wins(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("MATTERMOST_WEBHOOK_URL", "http://env.example/x")
        assert resolve_webhook_url("http://explicit/y") == "http://explicit/y"

    def test_briefing_specific_env_wins_over_generic(
        self, monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setenv("MATTERMOST_WEBHOOK_URL", "http://generic")
        monkeypatch.setenv("MATTERMOST_BRIEFING_WEBHOOK_URL", "http://briefing")
        assert resolve_webhook_url(None) == "http://briefing"

    def test_falls_back_to_generic_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("MATTERMOST_BRIEFING_WEBHOOK_URL", raising=False)
        monkeypatch.setenv("MATTERMOST_WEBHOOK_URL", "http://generic")
        assert resolve_webhook_url(None) == "http://generic"

    def test_no_url_raises(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("MATTERMOST_BRIEFING_WEBHOOK_URL", raising=False)
        monkeypatch.delenv("MATTERMOST_WEBHOOK_URL", raising=False)
        with pytest.raises(WebhookPostError, match="no Mattermost webhook URL"):
            resolve_webhook_url(None)


# --------------------------------------------------------------------------
# split_for_mattermost
# --------------------------------------------------------------------------


class TestSplitForMattermost:
    def test_empty_input_yields_empty_list(self) -> None:
        assert split_for_mattermost("") == []

    def test_small_text_returns_single_chunk(self) -> None:
        text = "# Briefing\n\nLine 1.\n\nLine 2.\n"
        assert split_for_mattermost(text) == [text]

    def test_splits_on_blank_line_boundaries(self) -> None:
        para = "x" * 6000
        # Two paragraphs of 6000 chars + a tiny one — should split when
        # joined length would exceed 8000
        text = "\n\n".join([para, para, "tail"])
        chunks = split_for_mattermost(text, max_chars=8000)
        assert len(chunks) >= 2
        # All chunks fit
        for c in chunks:
            assert len(c) <= 8000
        # Continuation prefix on chunk 2+
        assert chunks[0].startswith("x")
        for c in chunks[1:]:
            assert c.startswith("_(continued ")

    def test_hard_splits_a_giant_paragraph(self) -> None:
        para = "x" * 20000
        chunks = split_for_mattermost(para, max_chars=8000)
        assert len(chunks) >= 3
        for c in chunks:
            assert len(c) <= 8000 + 30  # +30 for continuation marker

    def test_continuation_marker_format(self) -> None:
        text = "p1\n\n" + ("x" * 5000) + "\n\n" + ("y" * 5000)
        chunks = split_for_mattermost(text, max_chars=6000)
        assert len(chunks) >= 2
        assert "(continued 2/" in chunks[1]


# --------------------------------------------------------------------------
# post_text — mocked urlopen
# --------------------------------------------------------------------------


class _FakeResponse:
    def __init__(self, status: int = 200) -> None:
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class TestPostText:
    def test_posts_json_body_with_required_fields(self) -> None:
        captured: dict = {}

        def fake_urlopen(req, timeout):
            captured["url"] = req.full_url
            captured["body"] = json.loads(req.data)
            captured["headers"] = dict(req.headers)
            captured["method"] = req.method
            return _FakeResponse(200)

        with patch("memory_system.events.mattermost_post.urllib.request.urlopen",
                   side_effect=fake_urlopen):
            status = post_text(
                "hello",
                webhook_url="http://wh/",
                channel="town-square",
                username="Briefing Bot",
                icon_emoji=":calendar:",
            )
        assert status == 200
        assert captured["url"] == "http://wh/"
        assert captured["method"] == "POST"
        assert captured["body"]["text"] == "hello"
        assert captured["body"]["channel"] == "town-square"
        assert captured["body"]["username"] == "Briefing Bot"
        assert captured["body"]["icon_emoji"] == ":calendar:"
        # Content-Type header (urllib lowercases header keys)
        assert captured["headers"].get("Content-type") == "application/json"

    def test_optional_fields_omitted_from_body_when_none(self) -> None:
        captured: dict = {}

        def fake_urlopen(req, timeout):
            captured["body"] = json.loads(req.data)
            return _FakeResponse(200)

        with patch("memory_system.events.mattermost_post.urllib.request.urlopen",
                   side_effect=fake_urlopen):
            post_text("hi", webhook_url="http://wh/")
        assert "channel" not in captured["body"]
        assert "username" not in captured["body"]
        assert "icon_emoji" not in captured["body"]

    def test_non_2xx_raises(self) -> None:
        with patch("memory_system.events.mattermost_post.urllib.request.urlopen",
                   return_value=_FakeResponse(503)):
            with pytest.raises(WebhookPostError, match="HTTP 503"):
                post_text("x", webhook_url="http://wh/")

    def test_url_error_wrapped(self) -> None:
        import urllib.error as ue
        with patch(
            "memory_system.events.mattermost_post.urllib.request.urlopen",
            side_effect=ue.URLError("network down"),
        ):
            with pytest.raises(WebhookPostError, match="failed to POST"):
                post_text("x", webhook_url="http://wh/")


# --------------------------------------------------------------------------
# post_briefing — orchestrates split + per-chunk post
# --------------------------------------------------------------------------


class TestPostBriefing:
    def test_empty_text_returns_skipped(self) -> None:
        r = post_briefing("", webhook_url="http://wh/")
        assert r.posted == 0
        assert r.skipped is True
        assert r.chunks == ()

    def test_dry_run_does_not_post(self) -> None:
        with patch("memory_system.events.mattermost_post.urllib.request.urlopen") as up:
            r = post_briefing(
                "# Briefing\n\nbody\n",
                webhook_url="http://wh/",
                dry_run=True,
            )
        assert up.call_count == 0
        assert r.skipped is True
        assert len(r.chunks) == 1

    def test_short_text_posts_once(self) -> None:
        with patch(
            "memory_system.events.mattermost_post.urllib.request.urlopen",
            return_value=_FakeResponse(200),
        ) as up:
            r = post_briefing(
                "# Briefing\n\nbody\n",
                webhook_url="http://wh/",
            )
        assert up.call_count == 1
        assert r.posted == 1
        assert r.skipped is False

    def test_long_text_posts_multiple_chunks(self) -> None:
        para = "x" * 6000
        text = "\n\n".join([para] * 4)  # ~24k chars

        with patch(
            "memory_system.events.mattermost_post.urllib.request.urlopen",
            return_value=_FakeResponse(200),
        ) as up:
            r = post_briefing(
                text,
                webhook_url="http://wh/",
                max_chars=8000,
            )
        assert r.posted >= 2
        assert up.call_count == r.posted

    def test_post_failure_propagates(self) -> None:
        with patch(
            "memory_system.events.mattermost_post.urllib.request.urlopen",
            return_value=_FakeResponse(500),
        ):
            with pytest.raises(WebhookPostError):
                post_briefing("x", webhook_url="http://wh/")

    def test_default_username_and_emoji(self) -> None:
        captured: list = []

        def fake_urlopen(req, timeout):
            captured.append(json.loads(req.data))
            return _FakeResponse(200)

        with patch(
            "memory_system.events.mattermost_post.urllib.request.urlopen",
            side_effect=fake_urlopen,
        ):
            post_briefing("body", webhook_url="http://wh/")
        assert captured[0]["username"] == "Briefing Bot"
        assert captured[0]["icon_emoji"] == ":calendar:"
