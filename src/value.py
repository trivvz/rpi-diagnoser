from typing import Callable

from src import utils
from src.constants import (
    MEASURE_CLOCK,
    CLOCK_DIVISOR,
    MEASURE_TEMP,
    MEASURE_TEMP_SPLIT,
    MEASURE_VOLTS,
    MEASURE_VOLTS_SPLIT,
)
from src.my_types import TypeClock, TypeTemperature, TypeVoltage, AnyValue


class Value:
    """Base class for different measured values."""

    def __init__(self, getter: Callable[[], AnyValue]) -> None:
        self.getter = getter
        self.value = self.getter()
        self.min = self.value
        self.max = self.value
        self.all = [self.value]

    def update(self) -> None:
        self.value = self.getter()
        if self.value > self.max:
            self.max = self.value
        if self.value < self.min:
            self.min = self.value
        self.all.append(self.value)

    def get_avg(self) -> AnyValue:
        return sum(self.all) / len(self.all)


class Temperature(Value):
    """Class for handling temperature."""

    def __init__(self) -> None:
        super().__init__(self.get)
        # self.get()

    @staticmethod
    def get() -> TypeTemperature:
        val = float(utils.call_cmd(MEASURE_TEMP).split(MEASURE_TEMP_SPLIT)[0])
        return TypeTemperature(val)


class Voltage(Value):
    """Class for handling voltage."""

    def __init__(self) -> None:
        super().__init__(self.get)

    @staticmethod
    def get() -> TypeVoltage:
        val = float(utils.call_cmd(MEASURE_VOLTS).split(MEASURE_VOLTS_SPLIT)[0])
        return TypeVoltage(val)


class Clock(Value):
    """Class for handling clock speed."""

    def __init__(self) -> None:
        super().__init__(self.get)

    @staticmethod
    def get() -> TypeClock:
        val = int(utils.call_cmd(MEASURE_CLOCK))
        return TypeClock(val // CLOCK_DIVISOR)

    def get_avg(self) -> TypeClock:
        return sum(self.all) // len(self.all)
