# The result contains exactly the keys defined in the specification
def test_result_has_exactly_the_specified_keys(analyzer):
    result = analyzer.analyze([])
    assert set(result) == {
        "total_requests",
        "unique_visitors",
        "error_requests",
        "error_rate",
        "malformed_lines",
    }


def test_counts_are_integers_and_rate_is_a_number(analyzer, make_line):
    result = analyzer.analyze([make_line(status=500)])
    assert isinstance(result["total_requests"], int)
    assert isinstance(result["error_rate"], float)
