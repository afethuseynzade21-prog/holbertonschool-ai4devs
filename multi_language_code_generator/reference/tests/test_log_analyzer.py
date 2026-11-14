"""Tests for the reference LogAnalyzer. Run with: pytest multi_language_code_generator/reference/tests"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from log_analyzer import LogAnalyzer, compute_error_rate  # noqa: E402


def line(ip="192.168.1.1", status=200, size="2326"):
    return f'{ip} - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" {status} {size}'


analyzer = LogAnalyzer()

# ---- The 7 test cases defined in cross_language_spec.md ----

SPEC_CASES = [
    # (name, lines, expected)
    (
        "TC1 empty input",
        [],
        {"total_requests": 0, "unique_visitors": 0, "error_requests": 0,
         "error_rate": 0.0, "malformed_lines": 0},
    ),
    (
        "TC2 single valid request, bytes is '-'",
        [line("192.168.1.1", 200, "-")],
        {"total_requests": 1, "unique_visitors": 1, "error_requests": 0,
         "error_rate": 0.0, "malformed_lines": 0},
    ),
    (
        "TC3 mixed statuses and repeated visitors",
        [line("10.0.0.1", 200), line("10.0.0.2", 404), line("10.0.0.1", 500),
         line("10.0.0.3", 301), line("10.0.0.2", 200)],
        {"total_requests": 5, "unique_visitors": 3, "error_requests": 2,
         "error_rate": 40.0, "malformed_lines": 0},
    ),
    (
        "TC4 malformed and blank lines",
        [line("10.0.0.1", 200), "this is not a log line", "", line("10.0.0.1", 503),
         '10.0.0.9 - - [10/Oct/2023:13:55:36 +0000] "GET / HTTP/1.1"'],
        {"total_requests": 2, "unique_visitors": 1, "error_requests": 1,
         "error_rate": 50.0, "malformed_lines": 2},
    ),
    (
        "TC5 all requests are errors",
        [line("10.0.0.1", 400), line("10.0.0.2", 404), line("10.0.0.1", 500)],
        {"total_requests": 3, "unique_visitors": 2, "error_requests": 3,
         "error_rate": 100.0, "malformed_lines": 0},
    ),
    (
        "TC6 rounding down (1 of 3)",
        [line("10.0.0.1", 200), line("10.0.0.2", 200), line("10.0.0.3", 500)],
        {"total_requests": 3, "unique_visitors": 3, "error_requests": 1,
         "error_rate": 33.33, "malformed_lines": 0},
    ),
    (
        "TC7 rounding up (2 of 3)",
        [line("10.0.0.1", 200), line("10.0.0.2", 404), line("10.0.0.3", 500)],
        {"total_requests": 3, "unique_visitors": 3, "error_requests": 2,
         "error_rate": 66.67, "malformed_lines": 0},
    ),
]


@pytest.mark.parametrize("name,lines,expected", SPEC_CASES, ids=[c[0] for c in SPEC_CASES])
def test_spec_cases(name, lines, expected):
    assert analyzer.analyze(lines) == expected


# ---- Additional unit tests ----

def test_parse_valid_line():
    assert analyzer.parse_line(line("8.8.8.8", 404)) == {"ip": "8.8.8.8", "status": 404}


def test_parse_line_with_dash_bytes():
    assert analyzer.parse_line(line("8.8.8.8", 200, "-")) == {"ip": "8.8.8.8", "status": 200}


def test_parse_malformed_line_returns_none():
    assert analyzer.parse_line("not a log line") is None


def test_parse_line_with_non_numeric_status_is_malformed():
    bad = '8.8.8.8 - - [10/Oct/2023:13:55:36 +0000] "GET / HTTP/1.1" abc 12'
    assert analyzer.parse_line(bad) is None


def test_status_399_is_not_error_and_400_is_error():
    result = analyzer.analyze([line(status=399), line(status=400)])
    assert result["error_requests"] == 1
    assert result["total_requests"] == 2


def test_redirects_are_not_errors():
    result = analyzer.analyze([line(status=301), line(status=302), line(status=304)])
    assert result["error_requests"] == 0
    assert result["error_rate"] == 0.0


def test_lines_with_newline_characters_are_accepted():
    result = analyzer.analyze([line() + "\n", line("10.0.0.2", 500) + "\r\n"])
    assert result["total_requests"] == 2
    assert result["error_requests"] == 1


def test_result_has_exactly_the_specified_keys():
    result = analyzer.analyze([])
    assert set(result) == {"total_requests", "unique_visitors", "error_requests",
                           "error_rate", "malformed_lines"}


def test_analyze_file(tmp_path):
    f = tmp_path / "access.log"
    f.write_text("\n".join([line("10.0.0.1", 200), line("10.0.0.2", 500)]) + "\n", encoding="utf-8")
    result = analyzer.analyze_file(str(f))
    assert result["total_requests"] == 2
    assert result["error_rate"] == 50.0


def test_analyze_empty_file(tmp_path):
    f = tmp_path / "empty.log"
    f.write_text("", encoding="utf-8")
    assert analyzer.analyze_file(str(f))["total_requests"] == 0


@pytest.mark.parametrize("errors,total,expected", [
    (0, 0, 0.0), (1, 3, 33.33), (2, 3, 66.67), (1, 8, 12.5), (1, 32, 3.13), (20, 100, 20.0),
])
def test_compute_error_rate_rounds_half_up(errors, total, expected):
    assert compute_error_rate(errors, total) == expected
