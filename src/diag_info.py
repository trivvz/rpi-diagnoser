from datetime import datetime
from typing import Dict

from src import throttled, utils, value
from src.templates import OUTPUT_TEMPLATE, SUMMARY_STR_TEMPLATE, DEGREE_SIGN


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
        return SUMMARY_STR_TEMPLATE.substitute(
            temp_min=self.temperature.min,
            temp_avg=f"{self.temperature.get_avg():.1f}",
            temp_max=self.temperature.max,
            voltage_min=f"{self.voltage.min:.2f}",
            voltage_avg=f"{self.voltage.get_avg():.2f}",
            voltage_max=f"{self.voltage.max:.2f}",
            clock_min=self.clock.min,
            clock_avg=self.clock.get_avg(),
            clock_max=self.clock.max,
        )

    def gen_output(self) -> str:
        return OUTPUT_TEMPLATE.substitute(self._get_output_dict())

    def gen_log(self, logfile: str) -> None:
        with open(logfile, "a+") as file:
            file.write(self._format_log_output() + "\n")

    def _format_log_output(self) -> str:
        return "  ".join([val for val in self._get_output_dict().values()])

    def _get_output_dict(self) -> Dict[str, str]:
        clk_align = " " if self.clock.value < 1000 else ""
        return {
            "time": utils.format_time(self.time),
            "temperature": f"{self.temperature.value}{DEGREE_SIGN}C",
            "voltage": f"{self.voltage.value:.2f}V",
            "clock": f"{clk_align}{self.clock.value} MHz",
            "throttled": self.throttled.get(),
        }
