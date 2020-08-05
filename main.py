import subprocess
import time
from datetime import datetime


MEASURE_TEMP = "vcgencmd measure_temp"
MEASURE_CLOCK = "vcgencmd measure_clock arm"
MEASURE_VOLTS = "vcgencmd measure_volts"
GET_THROTTLED = "vcgencmd get_throttled"


def call_cmd(cmd: str) -> str:
    return subprocess.check_output(cmd, shell=True).decode().split("=")[1].strip()


def get_temp() -> float:
    temp_str = call_cmd(MEASURE_TEMP)
    return float(temp_str.split("'")[0])
    

def get_clock() -> int:
    clock_str = call_cmd(MEASURE_CLOCK)
    return int(clock_str) // 1_000_000


def get_volts() -> float:
    volts_str = call_cmd(MEASURE_VOLTS)
    return float(volts_str.split("V")[0])


def get_throttled() -> bin:
    throttled_str = call_cmd(GET_THROTTLED)
    return bin(int(throttled_str, 0))


def get_time() -> str:
    return datetime.now().strftime("%H:%M:%S")


def main() -> None:
    output = f"{get_time()} | t = {get_temp()} 'C | v = {get_volts():.2f} V | clk = {get_clock()} MHz\t| {get_throttled()}"
    print(output)


if __name__ == "__main__":
    while True:
        main()
        time.sleep(2)

