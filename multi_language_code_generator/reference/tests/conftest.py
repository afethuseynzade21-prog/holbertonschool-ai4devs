import sys
from pathlib import Path

import pytest

# Make log_analyzer.py (one folder up) importable from every test file
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from log_analyzer import LogAnalyzer  # noqa: E402


@pytest.fixture
def analyzer():
    return LogAnalyzer()


@pytest.fixture
def make_line():
    def _make_line(ip="192.168.1.1", status=200, size="2326"):
        return f'{ip} - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" {status} {size}'

    return _make_line
