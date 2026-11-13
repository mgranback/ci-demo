from count import count_errors


def test_count_errors():
    assert count_errors(["INFO", "WARNING", "INFO", "ERROR"]) == 1