from datetime import datetime

import pytest

from rpidiag import utils
from rpidiag.constants import FULL_DATETIME, HOUR_MIN_SEC


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (b"throttled=0x0\n", "0x0"),
        (b"volt=0.8438V\n", "0.8438V"),
        (b"frequency(48)=600117184\n", "600117184"),
        (b"temp=58.9'C\n", "58.9'C"),
    ],
)
def test_call_cmd(test_input, expected, mocker):
    mocker.patch("subprocess.check_output", return_value=test_input)
    assert utils.call_cmd("") == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [(HOUR_MIN_SEC, "21:37:33"), (FULL_DATETIME, "2012-12-21 21:37:33")],
)
def test_get_formatted_datetime(test_input, expected):
    test_datetime = datetime(2012, 12, 21, 21, 37, 33)
    output = utils.get_formatted_datetime(test_datetime, test_input)
    assert output == expected
