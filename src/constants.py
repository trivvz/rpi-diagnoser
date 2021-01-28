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

