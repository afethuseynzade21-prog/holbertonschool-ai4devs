# compute_error_rate: integer-only arithmetic, rounded half up to 2 decimals
import pytest

from log_analyzer import compute_error_rate


@pytest.mark.parametrize(
    "errors,total,expected",
    [(0, 0, 0.0), (1, 3, 33.33), (2, 3, 66.67), (1, 8, 12.5), (1, 32, 3.13), (20, 100, 20.0)],
)
def test_compute_error_rate_rounds_half_up(errors, total, expected):
    assert compute_error_rate(errors, total) == expected
