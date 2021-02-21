import pytest

from rpidiag.output_handler import OutputHandler
from rpidiag.constants import OCCURRED_EVENTS


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
