"""Script specific constants."""

# RPi diagnostic commands
MEASURE_TEMP = "vcgencmd measure_temp"
MEASURE_VOLTS = "vcgencmd measure_volts"
MEASURE_CLOCK = "vcgencmd measure_clock arm"
GET_THROTTLED = "vcgencmd get_throttled"

CLOCK_DIVISOR = 1_000_000
MEASURE_TEMP_SPLIT = "'"
MEASURE_VOLTS_SPLIT = "V"
THROTTLED_SEP = ":"

# Throttled is a 20-bit little-endian
# Reference:
# https://www.raspberrypi.org/documentation/raspbian/applications/vcgencmd.md
#
# Output string looks like this and we need the indices of 3 bits
# (counting starts from 0):
#  "0b111100000000001111"
# 19th^  ^16th      ^3rd
THROTTLED_BIT_19 = 2
THROTTLED_BIT_16 = THROTTLED_BIT_19 + 3
THROTTLED_BIT_3 = -4

OCCURRED_EVENTS = "\nOccurred events: "
EVENTS_MAPPING = {
    0: "soft temperature limit",
    1: "throttling",
    2: "arm frequency capped",
    3: "under-voltage",
}

DEGREE_SIGN = "\N{DEGREE SIGN}"

HOUR_MIN_SEC = "%H:%M:%S"
FULL_DATETIME = f"%Y-%m-%d {HOUR_MIN_SEC}"


OUTPUTS = ["time", "temperature", "voltage", "clock", "throttled"]
