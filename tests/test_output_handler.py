from pathlib import Path
from unittest.mock import patch

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


@pytest.mark.parametrize("test_input", ["rpidiag.log", ""])
def test_save_log(tmpdir, test_input):
    try:
        oh.save_log("", Path(tmpdir, test_input))
    except Exception as ex:
        assert False, f"test_save_log() raised {ex}"


@patch("builtins.open")
def test_save_log_except(mock_open):
    mock_open.side_effect = PermissionError
    with pytest.raises(PermissionError):
        oh.save_log("", Path("./rpidiag.log"))


@pytest.mark.parametrize("test_input", ["rpidiag.log", ""])
def test_check_save_permissions(tmpdir, test_input):
    try:
        oh.check_save_permissions(Path(tmpdir, test_input))
    except Exception as ex:
        assert False, f"test_check_save_permissions() raised {ex}"


@patch("builtins.open")
def test_check_save_permissions_except(mock_open):
    mock_open.side_effect = PermissionError
    with pytest.raises(SystemExit):
        oh.check_save_permissions(Path("./rpidiag.log"))
