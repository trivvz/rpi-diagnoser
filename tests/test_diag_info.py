from pathlib import Path

import pytest

from rpidiag.config import LOGFILE
from rpidiag.diag_info import DiagInfo

TEST_TEMPERATURE = 45.2
TEST_VOLTAGE = 1.266
TEST_CLOCK = 1200
TEST_THROTTLED = "0b000000000000000000"  # no events
TEST_TIME = "12:34:56"

TEST_TEMPERATURE_2 = 50.5


@pytest.fixture(scope="module")
def create_testable_diag_info(module_mocker):
    mm = module_mocker
    mm.patch("rpidiag.diag_info.get_temperature", return_value=TEST_TEMPERATURE)
    mm.patch("rpidiag.diag_info.get_voltage", return_value=TEST_VOLTAGE)
    mm.patch("rpidiag.diag_info.get_clock", return_value=TEST_CLOCK)
    mm.patch("rpidiag.throttled._get_binary", return_value=TEST_THROTTLED)
    mm.patch("rpidiag.utils.get_formatted_datetime", return_value=TEST_TIME)

    diag_info = DiagInfo()
    diag_info.update()

    return diag_info


def test_diag_info(create_testable_diag_info):
    diag_info = create_testable_diag_info

    assert diag_info.temperature.all == [TEST_TEMPERATURE]
    assert diag_info.voltage.all == [TEST_VOLTAGE]
    assert diag_info.clock.all == [TEST_CLOCK]


def test_get_output(create_testable_diag_info):
    diag_info = create_testable_diag_info
    assert (
        diag_info.get_output()
        == "│ 12:34:56 │ 45.2 °C │ 1.27 V │ 1200 MHz │ 0000:0000 │"
    )


def test_get_summary(create_testable_diag_info):
    diag_info = create_testable_diag_info
    assert (
        diag_info.get_summary()
        == """
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = 45.2/45.2/45.2
    Voltage min/avg/max = 1.27/1.27/1.27
    Clock min/avg/max = 1200/1200/1200
"""
    )


def test_save_log_with_path_to_folder(tmpdir, create_testable_diag_info):
    diag_info = create_testable_diag_info
    diag_info.log(Path(tmpdir))

    assert Path(tmpdir, LOGFILE).is_file()


def test_save_log_with_path_to_file(tmpdir, create_testable_diag_info):
    test_logfile = LOGFILE + "test_as_file"
    diag_info = create_testable_diag_info
    diag_info.log(Path(tmpdir, test_logfile))

    assert Path(tmpdir, test_logfile).is_file()
