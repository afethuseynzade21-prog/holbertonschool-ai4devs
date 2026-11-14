# analyze_file reads a log file from disk
def test_analyze_file(tmp_path, analyzer, make_line):
    f = tmp_path / "access.log"
    f.write_text("\n".join([make_line("10.0.0.1", 200), make_line("10.0.0.2", 500)]) + "\n", encoding="utf-8")
    result = analyzer.analyze_file(str(f))
    assert result["total_requests"] == 2
    assert result["error_rate"] == 50.0


def test_analyze_empty_file(tmp_path, analyzer):
    f = tmp_path / "empty.log"
    f.write_text("", encoding="utf-8")
    assert analyzer.analyze_file(str(f))["total_requests"] == 0
