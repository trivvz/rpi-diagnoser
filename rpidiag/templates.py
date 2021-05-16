from string import Template


VER_FRAME = "\u2502"  # ─
HOR_FRAME = "\u2500"  # │
TOP_T = "\u252C"      # ┬
LEFT_T = "\u251C"     # ├
RIGHT_T = "\u2524"    # ┤
CROSS = "\u253C"      # ┼
TL_CORNER = "\u250C"  # ┌
TR_CORNER = "\u2510"  # ┐

HEADER_TEXT = ["   TIME   ", "  TEMP   ", " VOLTS  ", "  CLOCK   ", " THROTTLED "]

HEADER_TOP = (
    TL_CORNER
    + TOP_T.join([len(text) * HOR_FRAME for text in HEADER_TEXT])
    + TR_CORNER
    + "\n"
)

HEADER_MID = "".join([VER_FRAME + text for text in HEADER_TEXT]) + VER_FRAME + "\n"

HEADER_BTM = (
    LEFT_T + CROSS.join([len(text) * HOR_FRAME for text in HEADER_TEXT]) + RIGHT_T
)

HEADER = HEADER_TOP + HEADER_MID + HEADER_BTM

OUTPUT_TEMPLATE = Template(
    f"{VER_FRAME} $time "
    f"{VER_FRAME} $temperature "
    f"{VER_FRAME} $voltage "
    f"{VER_FRAME} $clock "
    f"{VER_FRAME} $throttled "
    f"{VER_FRAME}"
)


SUMMARY_TEMPLATE = Template(
    """
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = ${temp_min}/${temp_avg}/${temp_max}
    Voltage min/avg/max = ${voltage_min}/${voltage_avg}/${voltage_max}
      Clock min/avg/max = ${clock_min}/${clock_avg}/${clock_max}
"""
)
