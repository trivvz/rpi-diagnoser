import sys
from typing import Dict, List

from rpidiag.config import LOGFILE
from rpidiag.constants import EVENTS_MAPPING, OCCURRED_EVENTS
from rpidiag.templates import HEADER, OUTPUT_TEMPLATE, SUMMARY_TEMPLATE


def get_summary(summary: Dict[str, str], occurred_keys: List[int]) -> str:
    events = [EVENTS_MAPPING[key] for key in occurred_keys]
    return SUMMARY_TEMPLATE.substitute(summary) + _get_events(events)


def print_header() -> None:
    print(HEADER)


def check_save_permissions() -> None:
    try:
        with open(LOGFILE, "a+"):
            pass
    except PermissionError:
        print(
            f"Not allowed to save the log file to: {LOGFILE}."
            "\nChange the log path or use sudo."
        )
        sys.exit()


def save_log(output: str) -> None:
    with open(LOGFILE, "a+") as file:
        file.write(output + "\n")


def get_output(output_dict: Dict[str, str]) -> str:
    return OUTPUT_TEMPLATE.substitute(output_dict)


def _get_events(events: List[str]) -> str:
    if events:
        return OCCURRED_EVENTS + ", ".join(events)
    return ""
