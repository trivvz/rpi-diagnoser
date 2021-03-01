from unittest.mock import patch

import pytest

from rpidiag.constants import OCCURRED_EVENTS
from rpidiag.output_handler import LogSavePermissionError, OutputHandler


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([0], OCCURRED_EVENTS + "soft temperature limit"),
        ([1, 3], OCCURRED_EVENTS + "throttling, under-voltage"),
        ([], ""),
    ],
)
@patch("rpidiag.templates.SUMMARY_TEMPLATE.substitute", return_value="")
def test_gen_summary(mock_substitute, test_input, expected):
    # patch("rpidiag.templates.SUMMARY_TEMPLATE.substitute", return_value="")
    assert OutputHandler.get_summary({}, test_input) == expected


def test_prepare_events():
    test_events = ["throttling", "under-voltage"]
    test_output = OutputHandler._get_events(test_events)
    expected = OCCURRED_EVENTS + "throttling, under-voltage"
    assert test_output == expected


@patch("builtins.open")
def test_save_log(mock_open):
    patch("rpidiag.output_handler.LOGFILE", "./rpidiag.log")
    OutputHandler.save_log("")


@patch("builtins.open")
def test_save_log_except(mock_open):
    mock_open.side_effect = PermissionError
    with pytest.raises(LogSavePermissionError):
        OutputHandler.save_log("")


@patch("builtins.open")
def test_check_save_permissions(mock_open):
    patch("rpidiag.output_handler.LOGFILE", "./rpidiag.log")
    OutputHandler.check_save_permissions()


@patch("builtins.open")
def test_check_save_permissions_except(mock_open):
    mock_open.side_effect = PermissionError
    with pytest.raises(SystemExit):
        OutputHandler.check_save_permissions()
