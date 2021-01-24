from datetime import datetime
from typing import List

from src import utils
from src.constants import (
    DEGREE_SIGN,
    GET_THROTTLED,
    MEASURE_CLOCK,
    MEASURE_TEMP,
    MEASURE_VOLTS,
)
from src.my_types import Clock, Temperature, Voltage


class DiagInfo:
    """Contains and processes the basic RPi diagnostic info."""

    def __init__(self) -> None:

        self.temp = self.get_temp()
        self.temp_min = self.temp
        self.temp_max = self.temp
        self.temp_list: List[Temperature] = []

        self.voltage = self.get_voltage()
        self.voltage_min = self.voltage
        self.voltage_max = self.voltage
        self.voltage_list: List[Voltage] = []

        self.clock = self.get_clock()
        self.clock_min = self.clock
        self.clock_max = self.clock
        self.clock_list: List[Clock] = []

        self.throttled = self.get_throttled()
        self.time = datetime.now()

    @staticmethod
    def get_temp() -> Temperature:
        temp_val = float(utils.call_cmd(MEASURE_TEMP).split("'")[0])
        return Temperature(temp_val)

    @staticmethod
    def get_voltage() -> Voltage:
        volts_val = float(utils.call_cmd(MEASURE_VOLTS).split("V")[0])
        return Voltage(volts_val)

    @staticmethod
    def get_clock() -> Clock:
        clock_val = int(utils.call_cmd(MEASURE_CLOCK))
        return Clock(clock_val // 1_000_000)

    @staticmethod
    def get_throttled() -> str:
        throttled_val = int(utils.call_cmd(GET_THROTTLED), 0)
        throttled_str = f"{throttled_val:#020b}"
        return f"{throttled_str[2:6]}::{throttled_str[-4:]}"

    def get_temp_avg(self) -> Temperature:
        return Temperature(sum(self.temp_list) / len(self.temp_list))

    def get_voltage_avg(self) -> Voltage:
        return Voltage(sum(self.voltage_list) / len(self.voltage_list))

    def get_clock_avg(self) -> Clock:
        return Clock(sum(self.clock_list) // len(self.clock_list))

    def handle_temp(self) -> None:
        if self.temp > self.temp_max:
            self.temp_max = self.temp
        if self.temp < self.temp_min:
            self.temp_min = self.temp
        self.temp_list.append(self.temp)

    def handle_voltage(self) -> None:
        if self.voltage > self.voltage_max:
            self.voltage_max = self.voltage
        if self.voltage < self.voltage_min:
            self.voltage_min = self.voltage
        self.voltage_list.append(self.voltage)

    def handle_clock(self) -> None:
        if self.clock > self.clock_max:
            self.clock_max = self.clock
        if self.clock < self.clock_min:
            self.clock_min = self.clock
        self.clock_list.append(self.clock)

    def update(self) -> None:
        self.time = datetime.now()
        self.temp = self.get_temp()
        self.voltage = self.get_voltage()
        self.clock = self.get_clock()
        self.throttled = self.get_throttled()

        self.handle_temp()
        self.handle_voltage()
        self.handle_clock()

    def gen_output(self) -> str:
        output = [
            utils.format_time(self.time),
            f"t = {self.temp}{DEGREE_SIGN}C",
            f"v = {self.voltage:.2f}V",
            f"clk = {self.clock} MHz\t",
            self.throttled,
        ]
        return " | ".join(output)

    def gen_summary(self) -> str:
        return (
            "\n--- Raspberry Pi diagnostic statistics ---"
            f"\nTemperature min/avg/max = {self.temp_min}/{self.get_temp_avg():.1f}/{self.temp_max}"
            f"\n    Voltage min/avg/max = {self.voltage_min:.2f}/{self.get_voltage_avg():.2f}/{self.voltage_max:.2f}"
            f"\n      Clock min/avg/max = {self.clock_min}/{self.get_clock_avg()}/{self.clock_max}"
        )

    def gen_log(self, logfile: str) -> None:
        with open(logfile, "a+") as file:
            file.write(self.gen_output() + "\n")

    def __str__(self) -> str:
        print(self.gen_output())
        return super().__str__()
