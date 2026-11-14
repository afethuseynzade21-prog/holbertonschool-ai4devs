# TC3: mixed statuses and repeated visitors
def test_mixed_statuses_and_repeated_visitors(analyzer, make_line):
    lines = [
        make_line("10.0.0.1", 200),
        make_line("10.0.0.2", 404),
        make_line("10.0.0.1", 500),
        make_line("10.0.0.3", 301),
        make_line("10.0.0.2", 200),
    ]
    assert analyzer.analyze(lines) == {
        "total_requests": 5,
        "unique_visitors": 3,
        "error_requests": 2,
        "error_rate": 40.0,
        "malformed_lines": 0,
    }
