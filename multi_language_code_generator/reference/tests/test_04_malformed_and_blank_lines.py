# TC4: malformed lines are counted, blank lines are ignored
def test_malformed_and_blank_lines(analyzer, make_line):
    lines = [
        make_line("10.0.0.1", 200),
        "this is not a log line",
        "",
        make_line("10.0.0.1", 503),
        '10.0.0.9 - - [10/Oct/2023:13:55:36 +0000] "GET / HTTP/1.1"',
    ]
    assert analyzer.analyze(lines) == {
        "total_requests": 2,
        "unique_visitors": 1,
        "error_requests": 1,
        "error_rate": 50.0,
        "malformed_lines": 2,
    }


def test_whitespace_only_line_is_ignored(analyzer, make_line):
    result = analyzer.analyze(["   ", "\t", make_line()])
    assert result["total_requests"] == 1
    assert result["malformed_lines"] == 0
