CALL_CMD = "rpidiag.utils.call_cmd"


def mock_cmd_output(return_value, mocker):
    mocker.patch(CALL_CMD, return_value=return_value)
