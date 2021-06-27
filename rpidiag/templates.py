from typing import Dict, Union

HEADER = """
┌──────────┬─────────┬────────┬──────────┬───────────┐
│   TIME   │  TEMP   │ VOLTS  │  CLOCK   │ THROTTLED │
├──────────┼─────────┼────────┼──────────┼───────────┤
    """.strip()


def build_output(output_dict: Dict[str, str]) -> str:
    return "│" + "│".join([f" {val} " for val in output_dict.values()]) + "│"


def build_summary(summary: Dict[str, Union[Dict[str, int], Dict[str, float]]]) -> str:
    temp = summary["temp"]
    voltage = summary["voltage"]
    clock = summary["clock"]

    return f"""
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = {temp["min"]:.1f}/{temp["avg"]:.1f}/{temp["max"]:.1f}
    Voltage min/avg/max = {voltage["min"]:.2f}/{voltage["avg"]:.2f}/{voltage["max"]:.2f}
    Clock min/avg/max = {clock["min"]:.0f}/{clock["avg"]:.0f}/{clock["max"]:.0f}
"""
