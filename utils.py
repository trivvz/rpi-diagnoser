from datetime import datetime
import subprocess

def call_cmd(cmd: str) -> str:
    """Calls any command and returns its output."""
    return subprocess.check_output(cmd, shell=True).decode().split("=")[1].strip()

def format_time(time: datetime) -> str:
    return time.strftime("%H:%M:%S")