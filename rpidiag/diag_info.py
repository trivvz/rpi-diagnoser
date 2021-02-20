from datetime import datetime
from typing import Dict

from rpidiag import throttled, utils, value
from rpidiag.constants import DEGREE_SIGN, FULL_DATETIME, HOUR_MIN_SEC
from rpidiag.templates import OUTPUT_TEMPLATE, SUMMARY_STR_TEMPLATE


class DiagInfo:
    """Contains and processes the basic RPi diagnostic info."""

    def __init__(self) -> None:
        self.temperature = value.Temperature()
        self.voltage = value.Voltage()
        self.clock = value.Clock()
        self.throttled = throttled.Throttled()
        self.time = datetime.now()

    def __str__(self) -> str:
        print(self.gen_output())
        return super().__str__()

    def update(self) -> None:
        self.time = datetime.now()
        self.temperature.update()
        self.voltage.update()
        self.clock.update()

    def gen_summary(self) -> str:
        return SUMMARY_STR_TEMPLATE.substitute(self._get_summary_dict())

    def _get_summary_dict(self) -> Dict[str, str]:
        return {
            **self.temperature.get_summary(),
            **self.voltage.get_summary(),
            **self.clock.get_summary(),
        }

    def gen_output(self) -> str:
        return OUTPUT_TEMPLATE.substitute(self._get_output_dict())

    def gen_log(self, logfile: str) -> None:
        with open(logfile, "a+") as file:
            file.write(self._format_log_output() + "\n")

    def _format_log_output(self) -> str:
        output = [val for val in self._get_output_dict(FULL_DATETIME).values()]
        return ", ".join(output)

    def _get_output_dict(
        self, time_format: str = HOUR_MIN_SEC
    ) -> Dict[str, str]:
        return {
            "time": utils.get_formatted_datetime(self.time, time_format),
            "temperature": f"{self.temperature.value}{DEGREE_SIGN}C",
            "voltage": f"{self.voltage.value:.2f}V",
            "clock": f"{self._handle_clock_align()}{self.clock.value} MHz",
            "throttled": self.throttled.get(),
        }

    def _handle_clock_align(self):
        return " " if self.clock.value < 1000 else ""
