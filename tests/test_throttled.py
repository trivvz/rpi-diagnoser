from rpidiag.throttled import Throttled


def test_get_occurred_part():
    raw_output = "0b101100000000001001"
    throttled = Throttled()
    assert throttled._get_occurred_part(raw_output) == "1011"


def test_get_active_part():
    raw_output = "0b101100000000001001"
    throttled = Throttled()
    assert throttled._get_active_part(raw_output) == "1001"


def test_get_binary(mocker):
    raw_output = "0b000000000000000000"
    mocker.patch("rpidiag.utils.call_cmd", return_value="0x0")
    throttled = Throttled()
    assert throttled._get_binary() == raw_output


def test_get_raw_value(mocker):
    mocker.patch("rpidiag.utils.call_cmd", return_value="0x0")
    throttled = Throttled()
    assert throttled._get_raw_value() == 0


def test_get_summary(mocker):
    occurred_part = "1011"
    mocker.patch(
        "rpidiag.throttled.Throttled._get_occurred_part",
        return_value=occurred_part,
    )
    throttled = Throttled()
    assert throttled.get_summary() == {0: 1, 1: 0, 2: 1, 3: 1}
