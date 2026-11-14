# TC1 (cross_language_spec.md): empty input
def test_empty_input_returns_zeros(analyzer):
    assert analyzer.analyze([]) == {
        "total_requests": 0,
        "unique_visitors": 0,
        "error_requests": 0,
        "error_rate": 0.0,
        "malformed_lines": 0,
    }
