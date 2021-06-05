from pathlib import Path
from unittest.mock import patch, call

import pytest

import rpidiag.output_handler as oh
from rpidiag.constants import OCCURRED_EVENTS


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ({"some_event"}, OCCURRED_EVENTS + "some_event"),
        ({"z", "a", "b"}, OCCURRED_EVENTS + "a, b, z"),  # check sorting
        ({}, ""),
    ],
)
@patch("rpidiag.output_handler.build_summary", return_value="")
def test_gen_summary(mock_substitute, test_input, expected):
    assert oh.get_summary({}, test_input) == expected


@patch("builtins.open")
def test_save_log(mock_open):
    oh.save_log("", Path("./rpidiag.log"))


@patch("builtins.open")
def test_save_log_dir(mock_open):
    oh.save_log("", Path("."))


@patch("builtins.open")
def test_save_log_except(mock_open):
    mock_open.side_effect = PermissionError
    with pytest.raises(PermissionError):
        oh.save_log("", Path("./rpidiag.log"))


@patch("builtins.open")
def test_check_save_permissions(mock_open):
    oh.check_save_permissions(Path("./rpidiag.log"))


@patch("builtins.open")
def test_check_save_permissions_dir(mock_open):
    mock_open.side_effect = IsADirectoryError

    with pytest.raises(IsADirectoryError):
        oh.check_save_permissions(Path("."))

    assert mock_open.call_count == 2

    calls = [call(Path("."), "a+"), call(Path(".", "rpidiag.log"), "a+")]
    mock_open.assert_has_calls(calls)


@patch("builtins.open")
def test_check_save_permissions_except(mock_open):
    mock_open.side_effect = PermissionError
    with pytest.raises(SystemExit):
        oh.check_save_permissions(Path("./rpidiag.log"))
