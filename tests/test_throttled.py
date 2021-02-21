from rpidiag.throttled import Throttled


def test_get_occurred_part():
    raw_output = "0b101100000000001001"
    throttled = Throttled()
    assert throttled._get_occurred_part(raw_output) == "1011"


def test_get_active_part():
    raw_output = "0b101100000000001001"
    throttled = Throttled()
    assert throttled._get_active_part(raw_output) == "1001"
