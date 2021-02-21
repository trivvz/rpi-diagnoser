import pytest

from rpidiag.value import Value, Temperature


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([10, 20], 15.0),
        ([52.6, 53.9, 54.1], 53.533),
        ([0.001, 0], 0.0),
    ],
)
def test_value_get_avg(test_input, expected):
    value = Value(Temperature.get)  # any getter is fine
    value.all = test_input
    assert pytest.approx(value.get_avg(), abs=0.001) == expected


def test_value_update_max(mocker):
    mocker.patch("rpidiag.value.Temperature.get", return_value=20)
    value = Value(Temperature.get)
    value.max = 15
    value.min = 15
    value.update()

    assert value.min == 15
    assert value._get_summary()["min"] == 15

    assert value.max == 20
    assert value._get_summary()["max"] == 20


def test_value_update_min(mocker):
    mocker.patch("rpidiag.value.Temperature.get", return_value=10)
    value = Value(Temperature.get)
    value.max = 15
    value.min = 15
    value.update()

    assert value.min == 10
    assert value._get_summary()["min"] == 10

    assert value.max == 15
    assert value._get_summary()["max"] == 15
