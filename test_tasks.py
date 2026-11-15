from datetime import date

import pytest

from tasks import (
    Task,
    count_by_status,
    filter_tasks,
    overdue_tasks,
    parse_due_date,
)


@pytest.fixture
def tasks():
    return [
        Task(1, "Write report", "todo", date(2026, 11, 20)),
        Task(2, "Review code", "in_progress", date(2026, 11, 10)),
        Task(3, "Deploy app", "done", date(2026, 11, 5)),
        Task(4, "Plan sprint", "todo"),
        Task(5, "Fix report bug", "todo", date(2026, 11, 15)),
    ]


def ids(result):
    return [t.id for t in result]


def test_task_rejects_empty_title():
    with pytest.raises(ValueError):
        Task(1, "   ")


def test_task_rejects_invalid_status():
    with pytest.raises(ValueError):
        Task(1, "A", "blocked")


def test_parse_due_date_valid():
    assert parse_due_date("2026-11-20") == date(2026, 11, 20)


@pytest.mark.parametrize("value", ["20-11-2026", "", "abc", None])
def test_parse_due_date_invalid(value):
    with pytest.raises(ValueError):
        parse_due_date(value)


def test_no_filters_returns_all_sorted_by_due_date(tasks):
    assert ids(filter_tasks(tasks)) == [3, 2, 5, 1, 4]


def test_filter_by_status(tasks):
    assert ids(filter_tasks(tasks, status="todo")) == [5, 1, 4]


def test_filter_by_invalid_status_raises(tasks):
    with pytest.raises(ValueError):
        filter_tasks(tasks, status="blocked")


def test_due_before_is_inclusive_and_skips_missing_dates(tasks):
    assert ids(filter_tasks(tasks, due_before=date(2026, 11, 10))) == [3, 2]


def test_due_after_is_inclusive(tasks):
    assert ids(filter_tasks(tasks, due_after=date(2026, 11, 15))) == [5, 1]


def test_due_range(tasks):
    result = filter_tasks(tasks, due_after=date(2026, 11, 6), due_before=date(2026, 11, 15))
    assert ids(result) == [2, 5]


def test_invalid_range_raises(tasks):
    with pytest.raises(ValueError):
        filter_tasks(tasks, due_after=date(2026, 12, 1), due_before=date(2026, 11, 1))


def test_keyword_is_case_insensitive(tasks):
    assert ids(filter_tasks(tasks, keyword="REPORT")) == [5, 1]


def test_combined_filters(tasks):
    result = filter_tasks(tasks, status="todo", keyword="report", due_before=date(2026, 11, 16))
    assert ids(result) == [5]


def test_no_match_returns_empty_list(tasks):
    assert filter_tasks(tasks, keyword="zzz") == []


def test_empty_input():
    assert filter_tasks([]) == []


def test_sort_by_title(tasks):
    assert ids(filter_tasks(tasks, sort_by="title")) == [3, 5, 4, 2, 1]


def test_sort_by_id(tasks):
    assert ids(filter_tasks(tasks, sort_by="id")) == [1, 2, 3, 4, 5]


def test_invalid_sort_field_raises(tasks):
    with pytest.raises(ValueError):
        filter_tasks(tasks, sort_by="priority")


def test_input_list_is_not_modified(tasks):
    original = list(tasks)
    filter_tasks(tasks, status="todo")
    assert tasks == original


def test_count_by_status(tasks):
    assert count_by_status(tasks) == {"todo": 3, "in_progress": 1, "done": 1}


def test_count_by_status_empty():
    assert count_by_status([]) == {"todo": 0, "in_progress": 0, "done": 0}


def test_overdue_tasks_excludes_done_and_future(tasks):
    result = overdue_tasks(tasks, today=date(2026, 11, 12))
    assert ids(result) == [2]


def test_overdue_tasks_ignores_tasks_without_due_date(tasks):
    assert 4 not in ids(overdue_tasks(tasks, today=date(2030, 1, 1)))
