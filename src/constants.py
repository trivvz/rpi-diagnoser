"""Script specific constants."""
from string import Template

# RPi diagnostic commands
MEASURE_TEMP = "vcgencmd measure_temp"
MEASURE_TEMP_SPLIT = "'"

MEASURE_VOLTS = "vcgencmd measure_volts"
MEASURE_VOLTS_SPLIT = "V"

MEASURE_CLOCK = "vcgencmd measure_clock arm"
CLOCK_DIVISOR = 1_000_000

GET_THROTTLED = "vcgencmd get_throttled"

# Throttled is 20-bit little-endian
# Reference: https://www.raspberrypi.org/documentation/raspbian/applications/vcgencmd.md
THROTTLED_BIT_19 = 2  # beginning of first section
THROTTLED_BIT_16 = 6  # end of first section
THROTTLED_BIT_3 = -4  # beginning of second section

THROTTLED_SEP = ":"

# DEGREE_SIGN = "\N{DEGREE SIGN}"
# VER_FRAME = "\u2502"

# SUMMARY_STR_TEMPLATE = Template(
#     """
# --- Raspberry Pi diagnostic statistics ---
# Temperature min/avg/max = ${temp_min}/${temp_avg}/${temp_max}
#     Voltage min/avg/max = ${voltage_min}/${voltage_avg}/${voltage_max}
#       Clock min/avg/max = ${clock_min}/${clock_avg}/${clock_max}
# """
# )

# TOP_T = "\u252C"
# LEFT_T = "\u251C"
# RIGHT_T = "\u2524"
# CROSS = "\u253C"
# TL_CORNER = "\u250C"
# TR_CORNER = "\u2510"
# HOR_FRAME = "\u2500"

# INITIAL_STR = f"""
# {TL_CORNER}{HOR_FRAME*10}{TOP_T}{HOR_FRAME*8}{TOP_T}{HOR_FRAME*7}{TOP_T}{HOR_FRAME*10}{TOP_T}{HOR_FRAME*11}{TR_CORNER}
# {VER_FRAME}   TIME   {VER_FRAME}  TEMP  {VER_FRAME} VOLTS {VER_FRAME}  CLOCK   {VER_FRAME} THROTTLED {VER_FRAME}
# {LEFT_T}{HOR_FRAME*10}{CROSS}{HOR_FRAME*8}{CROSS}{HOR_FRAME*7}{CROSS}{HOR_FRAME*10}{CROSS}{HOR_FRAME*11}{RIGHT_T}
# """

# OUTPUT_TEMPLATE = Template(
#     f"""
# {VER_FRAME} $time {VER_FRAME} $temperature{DEGREE_SIGN}C {VER_FRAME} $voltage {VER_FRAME} $clock MHz {VER_FRAME} $throttled {VER_FRAME}
# """
# )
