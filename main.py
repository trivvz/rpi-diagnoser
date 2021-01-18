#!/usr/bin/python3
import subprocess
import time
from datetime import datetime

from config import GET_THROTTLED, MEASURE_CLOCK, MEASURE_TEMP, MEASURE_VOLTS


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


def gen_output() -> str:
    return f"{get_time()} | t = {get_temp()} 'C | v = {get_volts():.2f} V | clk = {get_clock()} MHz\t| {get_throttled()}"


def gen_log(logfile: str) -> None:
    with open(logfile, "a+") as file:
        file.write(gen_output() + "\n")


def print_status() -> None:
    print(gen_output())


if __name__ == "__main__":
    try:
        while True:
            print_status()
            # gen_log("log.txt")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n--- Raspberry Pi diagnostic statistics ---")
