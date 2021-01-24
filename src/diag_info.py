from datetime import datetime

from src import utils, value, throttled
from src.templates import (
    SUMMARY_STR_TEMPLATE,
    OUTPUT_TEMPLATE,
)


class DiagInfo:
    """Contains and processes the basic RPi diagnostic info."""

    def __init__(self) -> None:
        self.temperature = value.Temperature()
        self.voltage = value.Voltage()
        self.clock = value.Clock()
        self.throttled = throttled.Throttled()
        self.time = datetime.now()

    def update(self) -> None:
        self.time = datetime.now()
        self.temperature.update()
        self.voltage.update()
        self.clock.update()

    def gen_output(self) -> str:
        clk_align = " " if self.clock.value < 1000 else ""
        return OUTPUT_TEMPLATE.substitute(
            time=utils.format_time(self.time),
            temperature=self.temperature.value,
            voltage=f"{self.voltage.value:.2f}V",
            clock=f"{clk_align}{self.clock.value}",
            throttled=self.throttled.get(),
        )

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

    def gen_log(self, logfile: str) -> None:
        with open(logfile, "a+") as file:
            file.write(self.gen_output() + "\n")

    def __str__(self) -> str:
        print(self.gen_output())
        return super().__str__()
