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
THROTTLED_VAL_0 = 2  # beginning of first section
THROTTLED_VAL_3 = 6  # end of first section
THROTTLED_VAL_16 = -4  # beginning of second section
THROTTLED_SEP = "::"

DEGREE_SIGN = "\N{DEGREE SIGN}"
VERTICAL_SPLIT = "\u2502"

SUMMARY_STR_TEMPLATE = Template(
    """
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = ${temp_min}/${temp_avg}/${temp_max}
    Voltage min/avg/max = ${voltage_min}/${voltage_avg}/${voltage_max}
      Clock min/avg/max = ${clock_min}/${clock_avg}/${clock_max}
"""
)
