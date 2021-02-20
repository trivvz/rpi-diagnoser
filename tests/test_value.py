from rpidiag.value import Value


def test_value_get_avg():
    def getter():
        return 0

    value = Value(getter)
    value.all = [10, 20]
    assert value.get_avg() == 15


def test_value_update_max():
    def getter():
        return 20

    value = Value(getter)
    value.max = 15
    value.min = 15
    value.update()

    assert value.min == 15
    assert value._get_summary()["min"] == 15

    assert value.max == 20
    assert value._get_summary()["max"] == 20


def test_value_update_min():
    def getter():
        return 10

    value = Value(getter)
    value.max = 15
    value.min = 15
    value.update()

    assert value.min == 10
    assert value._get_summary()["min"] == 10

    assert value.max == 15
    assert value._get_summary()["max"] == 15
