"""Unit tests for the scopes SQLite store."""
from __future__ import annotations

from pathlib import Path

import pytest

from memory_system.scopes import (
    Scope,
    ScopeMember,
    ScopeTransition,
)
from memory_system.scopes.store import (
    append_transition,
    find_scopes_for_tag,
    find_transition_by_rollback,
    get_scope,
    index_all,
    list_members,
    list_scopes,
    list_transitions,
    open_db,
    upsert_member,
    upsert_scope,
)


def _ts(day: int = 16) -> str:
    return f"2026-05-{day:02d}T10:00:00+00:00"


@pytest.fixture
def db(tmp_path: Path):
    conn = open_db(tmp_path / "scopes.sqlite")
    yield conn
    conn.close()


def _make_scope(name: str = "Aurora") -> Scope:
    return Scope(
        id=f"scope-{name.lower()}-2026-05",
        name=name,
        status="provisional",
        first_seen=_ts(),
        last_seen=_ts(),
        member_tags=(f"{name.lower()}-tag-a", f"{name.lower()}-tag-b"),
    )


class TestScopeCrud:
    def test_upsert_and_get(self, db) -> None:
        s = _make_scope()
        upsert_scope(db, s)
        loaded = get_scope(db, s.id)
        assert loaded is not None
        assert loaded.name == "Aurora"
        assert loaded.status == "provisional"

    def test_get_nonexistent(self, db) -> None:
        assert get_scope(db, "scope-nope-2026-05") is None

    def test_list_scopes_empty(self, db) -> None:
        assert list_scopes(db) == []

    def test_list_with_status_filter(self, db) -> None:
        s1 = _make_scope("Aurora")
        s2 = Scope(
            id="scope-helios-2026-05", name="Helios",
            status="active", first_seen=_ts(), last_seen=_ts(),
        )
        upsert_scope(db, s1)
        upsert_scope(db, s2)
        provisionals = list_scopes(db, statuses=("provisional",))
        assert len(provisionals) == 1
        assert provisionals[0].name == "Aurora"
        actives = list_scopes(db, statuses=("active",))
        assert len(actives) == 1
        assert actives[0].name == "Helios"

    def test_upsert_overwrites_same_id(self, db) -> None:
        s = _make_scope()
        upsert_scope(db, s)
        s2 = Scope(
            id=s.id, name="Aurora v2", status="provisional",
            first_seen=_ts(), last_seen=_ts(),
        )
        upsert_scope(db, s2)
        loaded = get_scope(db, s.id)
        assert loaded.name == "Aurora v2"


class TestMembers:
    def test_upsert_and_list(self, db) -> None:
        s = _make_scope()
        upsert_scope(db, s)
        m = ScopeMember(
            scope_id=s.id, tag="aurora-tag-c",
            joined_at=_ts(), last_seen=_ts(),
        )
        upsert_member(db, m)
        members = list_members(db, s.id)
        assert len(members) == 1
        assert members[0].tag == "aurora-tag-c"

    def test_find_scopes_for_tag(self, db) -> None:
        s = _make_scope()
        upsert_scope(db, s)
        upsert_member(db, ScopeMember(
            scope_id=s.id, tag="aurora-tag-a",
            joined_at=_ts(), last_seen=_ts(),
        ))
        assert find_scopes_for_tag(db, "aurora-tag-a") == [s.id]
        assert find_scopes_for_tag(db, "unknown-tag") == []


class TestTransitions:
    def test_append_and_list(self, db) -> None:
        s = _make_scope()
        upsert_scope(db, s)
        t = ScopeTransition(
            id="trans-abcdef012345", scope_id=s.id,
            from_status=None, to_status="provisional",
            timestamp=_ts(), reason="created",
            rollback_id="rb-abcdef012345",
        )
        append_transition(db, t)
        all_t = list_transitions(db)
        assert len(all_t) == 1
        scoped = list_transitions(db, scope_id=s.id)
        assert len(scoped) == 1

    def test_find_by_rollback(self, db) -> None:
        s = _make_scope()
        upsert_scope(db, s)
        t = ScopeTransition(
            id="trans-abcdef012345", scope_id=s.id,
            from_status="provisional", to_status="active",
            timestamp=_ts(), reason="promoted",
            rollback_id="rb-abcdef012345",
        )
        append_transition(db, t)
        found = find_transition_by_rollback(db, "rb-abcdef012345")
        assert found is not None
        assert found.id == "trans-abcdef012345"

    def test_find_by_rollback_missing(self, db) -> None:
        assert find_transition_by_rollback(db, "rb-nope012345") is None


class TestIndexAll:
    def test_bulk_load(self, db) -> None:
        s1 = _make_scope("Aurora")
        s2 = _make_scope("Helios")
        m1 = ScopeMember(scope_id=s1.id, tag="aurora-tag-a",
                          joined_at=_ts(), last_seen=_ts())
        t1 = ScopeTransition(
            id="trans-aaaaaaaaaaaa", scope_id=s1.id,
            from_status=None, to_status="provisional",
            timestamp=_ts(), reason="created",
            rollback_id="rb-aaaaaaaaaaaa",
        )
        s_n, m_n, t_n = index_all(db, scopes=[s1, s2], members=[m1],
                                   transitions=[t1])
        assert (s_n, m_n, t_n) == (2, 1, 1)
        assert len(list_scopes(db)) == 2
