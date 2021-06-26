from datetime import datetime
from pathlib import Path
from typing import Dict, Union

from rpidiag import output_handler as oh
from rpidiag import templates as t
from rpidiag import throttled, utils, value
from rpidiag.constants import DEGREE_SIGN, FULL_DATETIME, HOUR_MIN_SEC


class DiagInfo:
    """Contains and processes the basic RPi diagnostic info."""

    def __init__(self) -> None:
        self.temperature = value.Temperature()
        self.voltage = value.Voltage()
        self.clock = value.Clock()
        self.time = datetime.now()

    def update(self) -> None:
        self.time = datetime.now()
        self.temperature.update()
        self.voltage.update()
        self.clock.update()

    def get_summary(self) -> str:
        return oh.get_summary(self._get_summary_dict(), throttled.get_summary())

    def _get_summary_dict(self) -> Dict[str, Union[Dict[str, int], Dict[str, float]]]:
        return {
            "temp": self.temperature.get_summary(),
            "voltage": self.voltage.get_summary(),
            "clock": self.clock.get_summary(),
        }

    def get_output(self) -> str:
        return t.build_output(self._get_output_dict())

    def log(self, logfile: Path) -> None:
        oh.save_log(self._format_log_output(), logfile)

    def _format_log_output(self) -> str:
        output = [val for val in self._get_output_dict(FULL_DATETIME).values()]
        return ", ".join(output).replace(DEGREE_SIGN, "deg")

    def _get_output_dict(self, time_format: str = HOUR_MIN_SEC) -> Dict[str, str]:
        return {
            "time": utils.get_formatted_datetime(self.time, time_format),
            "temperature": f"{self.temperature.all[-1]} {DEGREE_SIGN}C",
            "voltage": f"{self.voltage.all[-1]:.2f} V",
            "clock": f"{self._handle_clock_align()}{self.clock.all[-1]} MHz",
            "throttled": throttled.get(),
        }

    def _handle_clock_align(self) -> str:
        return " " if self.clock.all[-1] < 1000 else ""
