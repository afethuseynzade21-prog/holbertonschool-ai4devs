# TC7: 2 errors out of 3 requests gives 66.67
def test_rounding_up(analyzer, make_line):
    lines = [make_line("10.0.0.1", 200), make_line("10.0.0.2", 404), make_line("10.0.0.3", 500)]
    assert analyzer.analyze(lines) == {
        "total_requests": 3,
        "unique_visitors": 3,
        "error_requests": 2,
        "error_rate": 66.67,
        "malformed_lines": 0,
    }
