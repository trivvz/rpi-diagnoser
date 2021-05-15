from typing import Callable, Dict, Any

from rpidiag import utils
from rpidiag.constants import (
    MEASURE_CLOCK,
    CLOCK_DIVISOR,
    MEASURE_TEMP,
    MEASURE_TEMP_SPLIT,
    MEASURE_VOLTS,
    MEASURE_VOLTS_SPLIT,
)
from rpidiag.my_types import TypeClock, TypeTemperature, TypeVoltage


class Value:
    """Base class for different measured values."""

    def __init__(self, getter: Callable[[], Any]) -> None:
        self.getter = getter
        self.value = self.getter()
        self.all = [self.value]

    def update(self) -> None:
        self.value = self.getter()
        self.all.append(self.value)

    def _get_summary(self) -> Dict[str, Any]:
        return {
            "min": min(self.all),
            "avg": sum(self.all) / len(self.all),
            "max": max(self.all),
        }


class Temperature(Value):
    """Class for handling temperature."""

    def __init__(self) -> None:
        super().__init__(self.get_temperature)

    @staticmethod
    def get_temperature() -> TypeTemperature:
        val = float(utils.call_cmd(MEASURE_TEMP).split(MEASURE_TEMP_SPLIT)[0])
        return TypeTemperature(val)

    def get_summary(self) -> Dict[str, str]:
        return {f"temp_{k}": f"{v:.1f}" for k, v in self._get_summary().items()}


class Voltage(Value):
    """Class for handling voltage."""

    def __init__(self) -> None:
        super().__init__(self.get_voltage)

    @staticmethod
    def get_voltage() -> TypeVoltage:
        val = float(utils.call_cmd(MEASURE_VOLTS).split(MEASURE_VOLTS_SPLIT)[0])
        return TypeVoltage(val)

    def get_summary(self) -> Dict[str, str]:
        return {f"voltage_{k}": f"{v:.2f}" for k, v in self._get_summary().items()}


class Clock(Value):
    """Class for handling clock speed."""

    def __init__(self) -> None:
        super().__init__(self.get_clock)

    @staticmethod
    def get_clock() -> TypeClock:
        val = int(utils.call_cmd(MEASURE_CLOCK))
        return TypeClock(val // CLOCK_DIVISOR)

    def get_summary(self) -> Dict[str, str]:
        return {f"clock_{k}": str(int(v)) for k, v in self._get_summary().items()}
