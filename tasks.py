"""Task filtering feature for a simple task manager."""
from dataclasses import dataclass
from datetime import date
from typing import Dict, Iterable, List, Optional

VALID_STATUSES = ("todo", "in_progress", "done")
VALID_SORT_FIELDS = ("due_date", "title", "id")


@dataclass(frozen=True)
class Task:
    """A single task with a status and an optional due date."""

    id: int
    title: str
    status: str = "todo"
    due_date: Optional[date] = None

    def __post_init__(self) -> None:
        if not self.title or not self.title.strip():
            raise ValueError("Task title must not be empty")
        if self.status not in VALID_STATUSES:
            raise ValueError(
                f"Invalid status '{self.status}'. Allowed: {', '.join(VALID_STATUSES)}"
            )


def parse_due_date(value: str) -> date:
    """Convert an ISO date string (YYYY-MM-DD) into a date object."""
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid date '{value}'. Expected format: YYYY-MM-DD")


def _matches_status(task: Task, status: Optional[str]) -> bool:
    return status is None or task.status == status


def _matches_due_range(
    task: Task, due_before: Optional[date], due_after: Optional[date]
) -> bool:
    if due_before is None and due_after is None:
        return True
    if task.due_date is None:
        return False
    if due_before is not None and task.due_date > due_before:
        return False
    if due_after is not None and task.due_date < due_after:
        return False
    return True


def _matches_keyword(task: Task, keyword: Optional[str]) -> bool:
    if not keyword:
        return True
    return keyword.strip().lower() in task.title.lower()


def _sort_key(sort_by: str):
    if sort_by == "due_date":
        # Tasks without a due date go last.
        return lambda t: (t.due_date is None, t.due_date or date.max, t.id)
    if sort_by == "title":
        return lambda t: (t.title.lower(), t.id)
    return lambda t: t.id


def filter_tasks(
    tasks: Iterable[Task],
    status: Optional[str] = None,
    due_before: Optional[date] = None,
    due_after: Optional[date] = None,
    keyword: Optional[str] = None,
    sort_by: str = "due_date",
) -> List[Task]:
    """Return tasks that match all given filters, sorted by `sort_by`.

    Filters that are None are ignored. Due-date bounds are inclusive and
    tasks without a due date never match a due-date filter.
    """
    if status is not None and status not in VALID_STATUSES:
        raise ValueError(
            f"Invalid status '{status}'. Allowed: {', '.join(VALID_STATUSES)}"
        )
    if sort_by not in VALID_SORT_FIELDS:
        raise ValueError(
            f"Invalid sort field '{sort_by}'. Allowed: {', '.join(VALID_SORT_FIELDS)}"
        )
    if due_before and due_after and due_after > due_before:
        raise ValueError("due_after must not be later than due_before")

    matching = [
        task
        for task in tasks
        if _matches_status(task, status)
        and _matches_due_range(task, due_before, due_after)
        and _matches_keyword(task, keyword)
    ]
    return sorted(matching, key=_sort_key(sort_by))


def count_by_status(tasks: Iterable[Task]) -> Dict[str, int]:
    """Return how many tasks exist for each valid status."""
    counts = {status: 0 for status in VALID_STATUSES}
    for task in tasks:
        counts[task.status] += 1
    return counts


def overdue_tasks(tasks: Iterable[Task], today: Optional[date] = None) -> List[Task]:
    """Return unfinished tasks whose due date is before `today`."""
    today = today or date.today()
    unfinished = filter_tasks(tasks, due_before=today, sort_by="due_date")
    return [t for t in unfinished if t.status != "done" and t.due_date < today]
