import sys
from pathlib import Path
from typing import Dict, Set, Union

from rpidiag.config import LOGFILE
from rpidiag.constants import OCCURRED_EVENTS
from rpidiag.templates import build_summary


def get_summary(
    summary: Dict[str, Union[Dict[str, int], Dict[str, float]]],
    occurred_events: Set[str],
) -> str:
    return build_summary(summary) + _get_events(occurred_events)


def check_save_permissions(logfile: Path) -> None:
    try:
        if logfile.is_dir():
            # If dir path is given, use default filename
            logfile = Path(logfile, LOGFILE)

        with open(logfile, "a+"):
            pass

    except PermissionError:
        print(
            f"Not allowed to save the log file to: {logfile}."
            "\nChange the log path or use sudo."
        )
        sys.exit()


def save_log(output: str, logfile: Path) -> None:
    if logfile.is_dir():
        logfile = Path(logfile, LOGFILE)
    with open(logfile, "a+") as file:
        file.write(output + "\n")


def _get_events(events: Set[str]) -> str:
    if events:
        return OCCURRED_EVENTS + ", ".join(sorted(events))
    return ""
