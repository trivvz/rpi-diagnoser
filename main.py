#!/usr/bin/python3
import time
from datetime import datetime
from typing import List

import utils
from config import (
    DEGREE_SIGN,
    GET_THROTTLED,
    MEASURE_CLOCK,
    MEASURE_TEMP,
    MEASURE_VOLTS,
)
from my_types import Clock, Temperature, Voltage


class DiagInfo:
    def __init__(self) -> None:

        self.temp: Temperature = Temperature(0.0)
        self.min_temp: Temperature = Temperature(0.0)
        self.max_temp: Temperature = Temperature(0.0)
        self.temp_list: List[Temperature] = []

        self.voltage: Voltage = Voltage(0.0)
        self.min_voltage: Voltage = Voltage(0.0)
        self.max_voltage: Voltage = Voltage(0.0)
        self.voltage_list: List[Voltage] = []

        self.clock: Clock = Clock(0)
        self.min_clock: Clock = Clock(0)
        self.max_clock: Clock = Clock(0)
        self.clock_list: List[Clock] = []

        self.throttled: str
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
        return bin(throttled_val)

    def update(self) -> None:
        self.time = datetime.now()
        self.temp = self.get_temp()
        self.voltage = self.get_voltage()
        self.clock = self.get_clock()
        self.throttled = self.get_throttled()

    def gen_output(self) -> str:
        return f"{utils.format_time(self.time)} | t = {self.temp}{DEGREE_SIGN}C | v = {self.voltage:.2f}V | clk = {self.clock} MHz\t| {self.throttled}"

    def gen_log(self, logfile: str) -> None:
        with open(logfile, "a+") as file:
            file.write(self.gen_output() + "\n")

    def __str__(self) -> str:
        print(self.gen_output())
        return super().__str__()


if __name__ == "__main__":
    try:
        while True:
            diag_info = DiagInfo()
            diag_info.update()
            str(diag_info)
            # gen_log("log.txt")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n--- Raspberry Pi diagnostic statistics ---")
