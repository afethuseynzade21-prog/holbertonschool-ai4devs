"""Reference implementation of the Log Analyzer (Python).

Follows cross_language_spec.md. Parses Apache Common Log Format lines and computes:
total requests, unique visitors, error requests, error rate and malformed lines.
"""
import re
from typing import Iterable, Optional

# IP ident user [timestamp] "request" status bytes
LOG_PATTERN = re.compile(r'^(\S+) \S+ \S+ \[[^\]]+\] "[^"]*" (\d{3}) (?:\d+|-)$')


def compute_error_rate(error_requests: int, total_requests: int) -> float:
    """Percentage of error requests, rounded half up to 2 decimals.

    Uses integer arithmetic only, so every language can reproduce the exact same result.
    """
    if total_requests == 0:
        return 0.0
    hundredths = (2 * error_requests * 10000 + total_requests) // (2 * total_requests)
    return hundredths / 100


class LogAnalyzer:
    def parse_line(self, line: str) -> Optional[dict]:
        """Return {"ip": str, "status": int} for a valid line, or None if malformed."""
        match = LOG_PATTERN.match(line.rstrip("\r\n"))
        if match is None:
            return None
        return {"ip": match.group(1), "status": int(match.group(2))}

    def analyze(self, lines: Iterable[str]) -> dict:
        total_requests = 0
        error_requests = 0
        malformed_lines = 0
        visitors = set()

        for line in lines:
            if line.strip() == "":
                continue  # blank lines are ignored (not counted as malformed)
            entry = self.parse_line(line)
            if entry is None:
                malformed_lines += 1
                continue
            total_requests += 1
            visitors.add(entry["ip"])
            if entry["status"] >= 400:
                error_requests += 1

        return {
            "total_requests": total_requests,
            "unique_visitors": len(visitors),
            "error_requests": error_requests,
            "error_rate": compute_error_rate(error_requests, total_requests),
            "malformed_lines": malformed_lines,
        }

    def analyze_file(self, path: str) -> dict:
        with open(path, encoding="utf-8") as f:
            return self.analyze(f)
