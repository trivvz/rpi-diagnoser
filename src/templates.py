from string import Template

DEGREE_SIGN = "\N{DEGREE SIGN}"

VER_FRAME = "\u2502"  # ─
HOR_FRAME = "\u2500"  # │
TOP_T = "\u252C"      # ┬
LEFT_T = "\u251C"     # ├
RIGHT_T = "\u2524"    # ┤
CROSS = "\u253C"      # ┼
TL_CORNER = "\u250C"  # ┌
TR_CORNER = "\u2510"  # ┐

TIME_WIDTH = 10
TEMP_WIDTH = 8
VOLTS_WIDTH = 7
CLOCK_WIDTH = 10
THROTTLED_WIDTH = 11

HEADER = (
    f"{TL_CORNER}{HOR_FRAME*TIME_WIDTH}{TOP_T}"
    f"{HOR_FRAME*TEMP_WIDTH}{TOP_T}"
    f"{HOR_FRAME*VOLTS_WIDTH}{TOP_T}"
    f"{HOR_FRAME*CLOCK_WIDTH}{TOP_T}"
    f"{HOR_FRAME*THROTTLED_WIDTH}{TR_CORNER}\n"
    f"{VER_FRAME}   TIME   "
    f"{VER_FRAME}  TEMP  "
    f"{VER_FRAME} VOLTS "
    f"{VER_FRAME}  CLOCK   "
    f"{VER_FRAME} THROTTLED {VER_FRAME}\n"
    f"{LEFT_T}{HOR_FRAME*TIME_WIDTH}{CROSS}"
    f"{HOR_FRAME*TEMP_WIDTH}{CROSS}"
    f"{HOR_FRAME*VOLTS_WIDTH}{CROSS}"
    f"{HOR_FRAME*CLOCK_WIDTH}{CROSS}"
    f"{HOR_FRAME*THROTTLED_WIDTH}{RIGHT_T}"
)


OUTPUT_TEMPLATE = Template(
    f"""
{VER_FRAME} $time {VER_FRAME} $temperature {VER_FRAME} $voltage {VER_FRAME} $clock {VER_FRAME} $throttled {VER_FRAME}
"""[
        1:-1
    ]
)


SUMMARY_STR_TEMPLATE = Template(
    """
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = ${temp_min}/${temp_avg}/${temp_max}
    Voltage min/avg/max = ${voltage_min}/${voltage_avg}/${voltage_max}
      Clock min/avg/max = ${clock_min}/${clock_avg}/${clock_max}
"""
)
