# Edge case: 399 is not an error, 400 is an error, redirects are not errors
def test_399_is_not_error_and_400_is_error(analyzer, make_line):
    result = analyzer.analyze([make_line(status=399), make_line(status=400)])
    assert result["total_requests"] == 2
    assert result["error_requests"] == 1
    assert result["error_rate"] == 50.0


def test_redirects_are_not_errors(analyzer, make_line):
    result = analyzer.analyze([make_line(status=301), make_line(status=302), make_line(status=304)])
    assert result["error_requests"] == 0
    assert result["error_rate"] == 0.0
