from datetime import datetime

from src import utils
from src.constants import (
    DEGREE_SIGN,
    GET_THROTTLED,
    THROTTLED_VAL_0,
    THROTTLED_VAL_3,
    THROTTLED_VAL_16,
    THROTTLED_SEP,
    VERTICAL_SPLIT,
)
from src.value import Clock, Temperature, Voltage


class DiagInfo:
    """Contains and processes the basic RPi diagnostic info."""

    def __init__(self) -> None:
        self.temperature = Temperature()
        self.voltage = Voltage()
        self.clock = Clock()
        self.throttled = self.get_throttled()
        self.time = datetime.now()

    @staticmethod
    def get_throttled() -> str:
        throttled_val = int(utils.call_cmd(GET_THROTTLED), 0)
        throttled_str = f"{throttled_val:#020b}"
        return (
            f"{throttled_str[THROTTLED_VAL_0:THROTTLED_VAL_3]}"
            f"{THROTTLED_SEP}"
            f"{throttled_str[THROTTLED_VAL_16:]}"
        )

    def update(self) -> None:
        self.time = datetime.now()
        self.temperature.update()
        self.voltage.update()
        self.clock.update()
        self.throttled = self.get_throttled()

    def gen_output(self) -> str:
        # TODO: get rid of \t in output
        output = [
            utils.format_time(self.time),
            f"t = {self.temperature.value}{DEGREE_SIGN}C",
            f"v = {self.voltage.value:.2f}V",
            f"clk = {self.clock.value} MHz\t",
            self.throttled,
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
