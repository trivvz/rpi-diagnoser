from typing import Any

from pytest_mock import MockFixture

CALL_CMD = "rpidiag.utils.call_cmd"


def mock_cmd_output(return_value: Any, mocker: MockFixture) -> None:
    mocker.patch(CALL_CMD, return_value=return_value)
