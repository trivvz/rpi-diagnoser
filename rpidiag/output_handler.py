import sys

from typing import Dict, List
from pathlib import Path

from rpidiag.constants import EVENTS_MAPPING, OCCURRED_EVENTS
from rpidiag.templates import HEADER, OUTPUT_TEMPLATE, SUMMARY_TEMPLATE


def get_summary(summary: Dict[str, str], occurred_keys: List[int]) -> str:
    events = [EVENTS_MAPPING[key] for key in occurred_keys]
    return SUMMARY_TEMPLATE.substitute(summary) + _get_events(events)


def print_header() -> None:
    print(HEADER)


def check_save_permissions(logfile: Path) -> None:
    try:
        with open(logfile, "a+"):
            pass
    except PermissionError:
        print(
            f"Not allowed to save the log file to: {logfile}."
            "\nChange the log path or use sudo."
        )
        sys.exit()


def save_log(output: str, logfile: Path) -> None:
    with open(logfile, "a+") as file:
        file.write(output + "\n")


def get_output(output_dict: Dict[str, str]) -> str:
    return OUTPUT_TEMPLATE.substitute(output_dict)


def _get_events(events: List[str]) -> str:
    if events:
        return OCCURRED_EVENTS + ", ".join(events)
    return ""
