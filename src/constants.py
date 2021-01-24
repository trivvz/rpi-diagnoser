"""Script specific constants."""

# RPi diagnostic commands
MEASURE_TEMP = "vcgencmd measure_temp"
MEASURE_TEMP_SPLIT = "'"

MEASURE_VOLTS = "vcgencmd measure_volts"
MEASURE_VOLTS_SPLIT = "V"

MEASURE_CLOCK = "vcgencmd measure_clock arm"
CLOCK_DIVISOR = 1_000_000

GET_THROTTLED = "vcgencmd get_throttled"
THROTTLED_VAL_0 = 2  # beginning of first section
THROTTLED_VAL_3 = 6  # end of first section
THROTTLED_VAL_16 = -4  # beginning of second section
THROTTLED_SEP = "::"

DEGREE_SIGN = "\N{DEGREE SIGN}"
VERTICAL_SPLIT = "\u2502"
