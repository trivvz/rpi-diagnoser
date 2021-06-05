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
        "temp_min": "10",
        "temp_avg": "11",
        "temp_max": "12",
        "voltage_min": "13",
        "voltage_avg": "14",
        "voltage_max": "15",
        "clock_min": "16",
        "clock_avg": "17",
        "clock_max": "18",
    }
    assert t.build_summary(summary) == """
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = 10/11/12
    Voltage min/avg/max = 13/14/15
    Clock min/avg/max = 16/17/18
    """
