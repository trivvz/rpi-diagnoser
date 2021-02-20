from datetime import datetime
from typing import Dict

from src import throttled, utils, value
from src.constants import DEGREE_SIGN
from src.templates import OUTPUT_TEMPLATE, SUMMARY_STR_TEMPLATE


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
        return ", ".join([val for val in self._get_output_dict().values()])

    def _get_output_dict(self) -> Dict[str, str]:
        clk_align = " " if self.clock.value < 1000 else ""
        return {
            "time": utils.format_time(self.time),
            "temperature": f"{self.temperature.value}{DEGREE_SIGN}C",
            "voltage": f"{self.voltage.value:.2f}V",
            "clock": f"{clk_align}{self.clock.value} MHz",
            "throttled": self.throttled.get(),
        }
