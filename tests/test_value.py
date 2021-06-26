import pytest

from rpidiag.value import Value, get_clock, get_temperature, get_voltage
from tests import utils


def test_get_temperature(mocker):
    utils.mock_cmd_output("58.9'C", mocker)
    assert pytest.approx(get_temperature(), abs=0.001) == 58.9


def test_get_voltage(mocker):
    utils.mock_cmd_output("0.8438V", mocker)
    assert pytest.approx(get_voltage(), abs=0.0001) == 0.8438


def test_get_clock(mocker):
    utils.mock_cmd_output("600117184", mocker)
    assert get_clock() == 600


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([10, 20], 15.0),
        ([52.6, 53.9, 54.1], 53.533),
        ([0.001, 0], 0.0),
    ],
)
def test_value_get_avg(mocker, test_input, expected):
    utils.mock_cmd_output("58.9'C", mocker)
    value = Value(getter_mock)  # any getter is fine
    value.all = test_input
    assert pytest.approx(sum(value.all) / len(value.all), abs=0.001) == expected


def test_get_summary(mocker):
    mocker.patch(
        "rpidiag.value.Value.get_summary",
        return_value={"min": 5.0, "avg": 7.5125, "max": 100},
    )
    value = Value(getter_mock)
    assert value.get_summary() == {
        "min": 5.0,
        "avg": 7.5125,
        "max": 100,
    }


def getter_mock():
    return 0
