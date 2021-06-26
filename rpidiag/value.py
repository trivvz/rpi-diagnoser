from typing import Any, Callable, Dict

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
        self.all = [self.value]

    @property
    def value(self):
        return self.getter()

    def update(self) -> None:
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
        super().__init__(self.get)

    def get(self) -> float:
        return float(utils.call_cmd(MEASURE_TEMP).split(MEASURE_TEMP_SPLIT)[0])

    def get_summary(self) -> Dict[str, str]:
        return {f"temp_{k}": f"{v:.1f}" for k, v in self._get_summary().items()}


class Voltage(Value):
    """Class for handling voltage."""

    def __init__(self) -> None:
        super().__init__(self.get)

    def get(self) -> float:
        return float(utils.call_cmd(MEASURE_VOLTS).split(MEASURE_VOLTS_SPLIT)[0])

    def get_summary(self) -> Dict[str, str]:
        return {f"voltage_{k}": f"{v:.2f}" for k, v in self._get_summary().items()}


class Clock(Value):
    """Class for handling clock speed."""

    def __init__(self) -> None:
        super().__init__(self.get)

    def get(self) -> int:
        return int(utils.call_cmd(MEASURE_CLOCK)) // CLOCK_DIVISOR

    def get_summary(self) -> Dict[str, str]:
        return {f"clock_{k}": str(int(v)) for k, v in self._get_summary().items()}
