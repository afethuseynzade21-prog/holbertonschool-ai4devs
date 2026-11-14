# TC6: 1 error out of 3 requests gives 33.33
def test_rounding_down(analyzer, make_line):
    lines = [make_line("10.0.0.1", 200), make_line("10.0.0.2", 200), make_line("10.0.0.3", 500)]
    assert analyzer.analyze(lines) == {
        "total_requests": 3,
        "unique_visitors": 3,
        "error_requests": 1,
        "error_rate": 33.33,
        "malformed_lines": 0,
    }
