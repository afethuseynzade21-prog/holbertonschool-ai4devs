# TC5: all requests are errors
def test_all_requests_are_errors(analyzer, make_line):
    lines = [make_line("10.0.0.1", 400), make_line("10.0.0.2", 404), make_line("10.0.0.1", 500)]
    assert analyzer.analyze(lines) == {
        "total_requests": 3,
        "unique_visitors": 2,
        "error_requests": 3,
        "error_rate": 100.0,
        "malformed_lines": 0,
    }
