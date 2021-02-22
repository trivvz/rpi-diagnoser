from rpidiag.throttled import Throttled


def test_get_occurred_part():
    throttled = Throttled()
    assert throttled._get_occurred_part("0b101100000000001001") == "1011"


def test_get_active_part():
    throttled = Throttled()
    assert throttled._get_active_part("0b101100000000001001") == "1001"


def test_get_binary(mocker):
    mocker.patch("rpidiag.utils.call_cmd", return_value="0x0")
    throttled = Throttled()
    assert throttled._get_binary() == "0b000000000000000000"


def test_get_raw_value(mocker):
    mocker.patch("rpidiag.utils.call_cmd", return_value="0x0")
    throttled = Throttled()
    assert throttled._get_raw_value() == 0


def test_get_summary(mocker):
    mock_get_ocurred_part(mocker)
    throttled = Throttled()
    assert throttled.get_summary() == {0: 1, 1: 0, 2: 1, 3: 1}


def test_get_summary_list(mocker):
    mock_get_ocurred_part(mocker)
    throttled = Throttled()
    assert throttled.get_summary_list() == [0, 2, 3]


def mock_get_ocurred_part(mocker):
    occurred_part = "1011"
    mocker.patch(
        "rpidiag.throttled.Throttled._get_occurred_part",
        return_value=occurred_part,
    )
