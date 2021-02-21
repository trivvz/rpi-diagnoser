import sys
from typing import Dict

from rpidiag.config import LOGFILE
from rpidiag.templates import OUTPUT_TEMPLATE, SUMMARY_STR_TEMPLATE


class OutputHandler:
    @staticmethod
    def gen_summary(summary_dict: Dict[str, str]) -> str:
        return SUMMARY_STR_TEMPLATE.substitute(summary_dict)

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
