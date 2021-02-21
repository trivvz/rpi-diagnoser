import sys
from typing import Dict, List

from rpidiag.config import LOGFILE
from rpidiag.constants import THROTTLED_OCCURRED_MAPPING
from rpidiag.templates import OUTPUT_TEMPLATE, SUMMARY_STR_TEMPLATE


class OutputHandler:
    @classmethod
    def gen_summary(cls,
        summary_dict: Dict[str, str], occurred_keys: List[int]
    ) -> str:
        events = [THROTTLED_OCCURRED_MAPPING[key] for key in occurred_keys]
        return SUMMARY_STR_TEMPLATE.substitute(summary_dict) + cls._prepare_events(events)

    @staticmethod
    def _prepare_events(events: List[str]) -> str:
        if events:
            return "Occurred events: " + ", ".join(events)
        return ""

    @staticmethod
    def gen_output(output_dict: Dict[str, str]) -> str:
        return OUTPUT_TEMPLATE.substitute(output_dict)

    @staticmethod
    def save_log(output: str) -> None:
        try:
            with open(LOGFILE, "a+") as file:
                file.write(output + "\n")
        except PermissionError:
            print(
                f"Not allowed to save the log file to: {LOGFILE}."
                "\nChange log path or use sudo."
            )
            sys.exit()
