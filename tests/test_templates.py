from rpidiag import templates as t


def test_build_header():
    assert t.build_header() == """
┌──────────┬─────────┬────────┬──────────┬───────────┐
│   TIME   │  TEMP   │ VOLTS  │  CLOCK   │ THROTTLED │
├──────────┼─────────┼────────┼──────────┼───────────┤
    """.strip()
