from rpidiag import templates as t


def test_build_output():
    values = {
        "time": "12:34:56",
        "temperature": "49.4 °C",
        "voltage": "1.34 V",
        "clock": "1400 MHz",
        "throttled": "0000:0000",
    }
    assert (
        t.build_output(values)
        == "│ 12:34:56 │ 49.4 °C │ 1.34 V │ 1400 MHz │ 0000:0000 │"
    )


def test_build_summary():
    summary = {
        "temp": {
            "min": 49.99,
            "avg": 52.123,
            "max": 55.01,
        },
        "voltage": {
            "min": 1.23,
            "avg": 1.346,
            "max": 1.405,
        },
        "clock": {
            "min": 600,
            "avg": 1000,
            "max": 1400,
        },
    }
    # type is ignored because of mypy bug
    # https://github.com/python/mypy/issues/7835
    assert (
        t.build_summary(summary)  # type: ignore
        == """
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = 50.0/52.1/55.0
    Voltage min/avg/max = 1.23/1.35/1.41
    Clock min/avg/max = 600/1000/1400
    """
    )
