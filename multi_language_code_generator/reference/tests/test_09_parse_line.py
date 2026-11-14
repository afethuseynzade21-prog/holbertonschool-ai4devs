# parse_line: valid lines return ip and status, malformed lines return None
def test_parse_valid_line(analyzer, make_line):
    assert analyzer.parse_line(make_line("8.8.8.8", 404)) == {"ip": "8.8.8.8", "status": 404}


def test_parse_line_with_dash_bytes(analyzer, make_line):
    assert analyzer.parse_line(make_line("8.8.8.8", 200, "-")) == {"ip": "8.8.8.8", "status": 200}


def test_parse_malformed_line_returns_none(analyzer):
    assert analyzer.parse_line("not a log line") is None


def test_parse_non_numeric_status_returns_none(analyzer):
    line = '8.8.8.8 - - [10/Oct/2023:13:55:36 +0000] "GET / HTTP/1.1" abc 12'
    assert analyzer.parse_line(line) is None


def test_parse_two_digit_status_returns_none(analyzer):
    line = '8.8.8.8 - - [10/Oct/2023:13:55:36 +0000] "GET / HTTP/1.1" 20 12'
    assert analyzer.parse_line(line) is None
