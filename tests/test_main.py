import pytest

from rpidiag.main import main

TEST_TEMPERATURE = 45.2
TEST_VOLTAGE = 1.266
TEST_CLOCK = 1200
TEST_THROTTLED = "0b000000000000000000"  # no events
TEST_TIME = "12:34:56"


def test_main_help(mocker, capsys):
    mocker.patch("rpidiag.diag_info.get_temperature", return_value=TEST_TEMPERATURE)
    mocker.patch("rpidiag.diag_info.get_voltage", return_value=TEST_VOLTAGE)
    mocker.patch("rpidiag.diag_info.get_clock", return_value=TEST_CLOCK)
    mocker.patch("rpidiag.throttled._get_binary", return_value=TEST_THROTTLED)
    mocker.patch("rpidiag.utils.get_formatted_datetime", return_value=TEST_TIME)

    with pytest.raises(SystemExit):
        main(["-h"])

    out, err = capsys.readouterr()

    assert out.startswith("usage: rpidiag")
    assert err == ""
