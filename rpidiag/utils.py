from datetime import datetime
import subprocess


def call_cmd(cmd: str) -> str:
    """Calls any command and returns its output."""
    raw_output = subprocess.check_output(cmd, shell=True)
    return raw_output.decode().split("=")[1].strip()


def get_formatted_datetime(time: datetime, format: str) -> str:
    return time.strftime(format)
