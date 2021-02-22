from tests.utils.constants import CALL_CMD


def mock_cmd_output(return_value, mocker):
    mocker.patch(CALL_CMD, return_value=return_value)
