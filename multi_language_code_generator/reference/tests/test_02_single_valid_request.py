# TC2: single valid request, bytes field is "-"
def test_single_valid_request(analyzer, make_line):
    result = analyzer.analyze([make_line("192.168.1.1", 200, "-")])
    assert result == {
        "total_requests": 1,
        "unique_visitors": 1,
        "error_requests": 0,
        "error_rate": 0.0,
        "malformed_lines": 0,
    }
