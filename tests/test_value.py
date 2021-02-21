from rpidiag.value import Value, Temperature


def test_value_get_avg():
    value = Value(Temperature.get)  # any getter is fine
    value.all = [10, 20]
    assert value.get_avg() == 15


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
