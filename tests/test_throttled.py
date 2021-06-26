from pytest_mock import MockFixture

from rpidiag import throttled
from tests import utils


def test_get(mocker: MockFixture) -> None:
    assert 0x2C009 == 0b101100000000001001
    utils.mock_cmd_output("0x2C009", mocker)
    assert throttled.get() == "1011:1001"


def test_get_summary(mocker: MockFixture) -> None:
    assert 0x2C000 == 0b101100000000000000
    utils.mock_cmd_output("0x2C000", mocker)

    # sets are equal even regardless of the order
    assert throttled.get_summary() == {
        "under-voltage",
        "arm frequency capped",
        "soft temperature limit",
    }
