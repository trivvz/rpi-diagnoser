import functools
from string import Template
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
    return Template(
        "".join([f"{c.VER_FRM} ${var} " for var in c.OUTPUTS]) + c.VER_FRM
    ).substitute(output_dict)


def build_summary(summary: Dict[str, str]) -> str:
    return Template(
        """
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = ${temp_min}/${temp_avg}/${temp_max}
    Voltage min/avg/max = ${voltage_min}/${voltage_avg}/${voltage_max}
    Clock min/avg/max = ${clock_min}/${clock_avg}/${clock_max}
    """
    ).substitute(summary)
