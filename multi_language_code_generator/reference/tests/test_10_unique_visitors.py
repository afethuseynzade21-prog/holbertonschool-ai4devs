# Edge case: the same IP appearing many times is counted once
def test_same_ip_counted_once(analyzer, make_line):
    lines = [make_line("10.0.0.1", 200) for _ in range(5)]
    result = analyzer.analyze(lines)
    assert result["total_requests"] == 5
    assert result["unique_visitors"] == 1


def test_different_ips_are_counted_separately(analyzer, make_line):
    lines = [make_line("10.0.0.1"), make_line("10.0.0.2"), make_line("10.0.0.3")]
    assert analyzer.analyze(lines)["unique_visitors"] == 3
