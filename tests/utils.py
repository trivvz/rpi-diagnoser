def mock_cmd_output(return_value, mocker):
    mocker.patch("rpidiag.utils.call_cmd", return_value=return_value)


def getter_mock():
    return 0
