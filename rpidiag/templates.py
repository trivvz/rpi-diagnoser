import functools
from typing import Dict

from rpidiag import constants as c


@functools.lru_cache(maxsize=1)
def build_header() -> str:
    text = ["   TIME   ", "  TEMP   ", " VOLTS  ", "  CLOCK   ", " THROTTLED "]

    top = (
        c.TL_CORNER
        + c.TOP_T.join([len(text) * c.HOR_FRM for text in text])
        + c.TR_CORNER
        + "\n"
    )

    mid = "".join([c.VER_FRM + text for text in text]) + c.VER_FRM + "\n"

    btm = c.LEFT_T + c.CROSS.join([len(text) * c.HOR_FRM for text in text]) + c.RIGHT_T

    return top + mid + btm


def build_output(output_dict: Dict[str, str]) -> str:
    return "".join([f"{c.VER_FRM} {val} " for val in output_dict.values()]) + c.VER_FRM


def build_summary(summary: Dict[str, str]) -> str:
    return f"""
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = {summary["temp_min"]}/{summary["temp_avg"]}/{summary["temp_max"]}
    Voltage min/avg/max = {summary["voltage_min"]}/{summary["voltage_avg"]}/{summary["voltage_max"]}
    Clock min/avg/max = {summary["clock_min"]}/{summary["clock_avg"]}/{summary["clock_max"]}
    """
