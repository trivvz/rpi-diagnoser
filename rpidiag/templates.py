from string import Template


VER_FRAME = "\u2502"  # ─
HOR_FRAME = "\u2500"  # │
TOP_T = "\u252C"      # ┬
LEFT_T = "\u251C"     # ├
RIGHT_T = "\u2524"    # ┤
CROSS = "\u253C"      # ┼
TL_CORNER = "\u250C"  # ┌
TR_CORNER = "\u2510"  # ┐

outputs = ["time", "temperature", "voltage", "clock", "throttled"]

OUTPUT_TEMPLATE = Template(
    "".join([f"{VER_FRAME} ${var} " for var in outputs]) + VER_FRAME
)

SUMMARY_TEMPLATE = Template(
    """
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = ${temp_min}/${temp_avg}/${temp_max}
    Voltage min/avg/max = ${voltage_min}/${voltage_avg}/${voltage_max}
      Clock min/avg/max = ${clock_min}/${clock_avg}/${clock_max}
"""
)


def build_header() -> str:
    text = ["   TIME   ", "  TEMP   ", " VOLTS  ", "  CLOCK   ", " THROTTLED "]

    top = (
        TL_CORNER
        + TOP_T.join([len(text) * HOR_FRAME for text in text])
        + TR_CORNER
        + "\n"
    )

    mid = "".join([VER_FRAME + text for text in text]) + VER_FRAME + "\n"

    btm = LEFT_T + CROSS.join([len(text) * HOR_FRAME for text in text]) + RIGHT_T

    return top + mid + btm

