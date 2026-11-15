# Pull Request: Add Task Filtering Feature

## Summary
Adds a task filtering feature to a simple task manager. Tasks can be filtered by status, due date range and a title keyword, and the result can be sorted by due date, title or id. The PR also adds helper functions to count tasks by status and to list overdue tasks.

## Changes
- Added `tasks.py` (115 lines):
  - `Task` dataclass with validation of the title and status
  - `parse_due_date()` to convert `YYYY-MM-DD` strings into dates
  - `filter_tasks()` with filters for status, `due_before`, `due_after` and `keyword`, plus sorting
  - `count_by_status()` and `overdue_tasks()` helpers
  - Small private helpers (`_matches_status`, `_matches_due_range`, `_matches_keyword`, `_sort_key`)
- Added `test_tasks.py` (130 lines) with 26 pytest tests (all passing)

## Context
- Motivation: users need to find tasks quickly, for example "unfinished tasks due this week" or "tasks that mention a report".
- Size: about 115 lines of feature code plus 130 lines of tests.
- Related issue: none (this is a standalone feature for the AI Code Review Simulator project).
- Behavior notes:
  - Filters set to `None` are ignored; all given filters must match.
  - Due date bounds are inclusive; tasks without a due date never match a due-date filter.
  - Invalid status, sort field or date range raises `ValueError`.

## Testing
Run `python -m pytest` in the `ai_code_review_simulator` folder. Result: 26 passed.
