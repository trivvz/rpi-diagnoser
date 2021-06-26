from typing import Any, Callable, Dict, List, Union

from rpidiag import utils
from rpidiag.constants import (
    CLOCK_DIVISOR,
    MEASURE_CLOCK,
    MEASURE_TEMP,
    MEASURE_TEMP_SPLIT,
    MEASURE_VOLTS,
    MEASURE_VOLTS_SPLIT,
)


class Value:
    """Base class for different measured values."""

    def __init__(self, getter: Callable[[], Any]) -> None:
        self.getter = getter
        self.all: List[Union[int, float]] = []

    @property
    def value(self) -> Union[int, float]:
        return self.getter()

    def update(self) -> None:
        self.all.append(self.value)

    def get_summary(self) -> Dict[str, Union[int, float]]:
        return {
            "min": min(self.all),
            "avg": sum(self.all) / len(self.all),
            "max": max(self.all),
        }


class Temperature(Value):
    """Class for handling temperature."""

    def __init__(self) -> None:
        super().__init__(get_temperature)


class Voltage(Value):
    """Class for handling voltage."""

    def __init__(self) -> None:
        super().__init__(get_voltage)


class Clock(Value):
    """Class for handling clock speed."""

    def __init__(self) -> None:
        super().__init__(get_clock)


def get_temperature() -> float:
    return float(utils.call_cmd(MEASURE_TEMP).split(MEASURE_TEMP_SPLIT)[0])


def get_voltage() -> float:
    return float(utils.call_cmd(MEASURE_VOLTS).split(MEASURE_VOLTS_SPLIT)[0])


def get_clock() -> int:
    return int(utils.call_cmd(MEASURE_CLOCK)) // CLOCK_DIVISOR
