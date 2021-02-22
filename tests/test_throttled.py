from rpidiag.throttled import Throttled
from tests.utils import utils


def test_get(mocker):
    assert 0x2C009 == 0b101100000000001001
    utils.mock_cmd_output("0x2C009", mocker)
    throttled = Throttled()
    assert throttled.get() == "1011:1001"


def test_get_summary(mocker):
    assert 0x2C000 == 0b101100000000000000
    utils.mock_cmd_output("0x2C000", mocker)
    throttled = Throttled()
    assert throttled.get_summary() == {0: 1, 1: 0, 2: 1, 3: 1}


def test_get_summary_list(mocker):
    assert 0x2C000 == 0b101100000000000000
    utils.mock_cmd_output("0x2C000", mocker)
    throttled = Throttled()
    assert throttled.get_summary_list() == [0, 2, 3]


def mock_throttled_cmd_output(returned, mocker):
    mocker.patch("rpidiag.utils.call_cmd", return_value=returned)
