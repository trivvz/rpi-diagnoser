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
def test_gen_summary(test_input, expected, mocker):
    mocker.patch(
        "rpidiag.templates.SUMMARY_TEMPLATE.substitute", return_value=""
    )
    assert OutputHandler.get_summary({}, test_input) == expected


def test_prepare_events():
    test_events = ["throttling", "under-voltage"]
    test_output = OutputHandler._get_events(test_events)
    expected = OCCURRED_EVENTS + "throttling, under-voltage"
    assert test_output == expected


def test_save_log(mocker):
    mocker.patch("builtins.open", mocker.mock_open())
    mocker.patch("rpidiag.output_handler.LOGFILE", "./rpidiag.log")
    OutputHandler.save_log("")


def test_save_log_except(mocker):
    mocker.patch("rpidiag.output_handler.LOGFILE", "/root/rpidiag.log")
    with pytest.raises(LogSavePermissionError):
        OutputHandler.save_log("")


def test_check_save_permissions(mocker):
    mocker.patch("builtins.open", mocker.mock_open())
    mocker.patch("rpidiag.output_handler.LOGFILE", "./rpidiag.log")
    OutputHandler.check_save_permissions()


def test_check_save_permissions_except(mocker):
    mocker.patch("rpidiag.output_handler.LOGFILE", "/root/rpidiag.log")
    with pytest.raises(SystemExit):
        OutputHandler.check_save_permissions()
