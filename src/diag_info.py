from datetime import datetime

from src import utils, value, throttled
from src.constants import DEGREE_SIGN, VERTICAL_SPLIT


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
        # TODO: get rid of \t in output
        output = [
            utils.format_time(self.time),
            f"t = {self.temperature.value}{DEGREE_SIGN}C",
            f"v = {self.voltage.value:.2f}V",
            f"clk = {self.clock.value} MHz\t",
            self.throttled.get(),
        ]
        return f" {VERTICAL_SPLIT} ".join(output)

    def gen_summary(self) -> str:
        return (
            "\n--- Raspberry Pi diagnostic statistics ---"
            f"\nTemperature min/avg/max = {self.temperature.min}/{self.temperature.get_avg():.1f}/{self.temperature.max}"
            f"\n    Voltage min/avg/max = {self.voltage.min:.2f}/{self.voltage.get_avg():.2f}/{self.voltage.max:.2f}"
            f"\n      Clock min/avg/max = {self.clock.min}/{self.clock.get_avg()}/{self.clock.max}"
        )

    def gen_log(self, logfile: str) -> None:
        with open(logfile, "a+") as file:
            file.write(self.gen_output() + "\n")

    def __str__(self) -> str:
        print(self.gen_output())
        return super().__str__()
