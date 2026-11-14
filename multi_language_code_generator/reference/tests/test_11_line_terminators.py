# Edge case: lines ending with \n or \r\n are parsed like lines without a terminator
def test_lines_with_newline_characters(analyzer, make_line):
    lines = [make_line() + "\n", make_line("10.0.0.2", 500) + "\r\n"]
    result = analyzer.analyze(lines)
    assert result["total_requests"] == 2
    assert result["error_requests"] == 1
    assert result["malformed_lines"] == 0
