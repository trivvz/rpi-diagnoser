from typing import Dict

HEADER = """
┌──────────┬─────────┬────────┬──────────┬───────────┐
│   TIME   │  TEMP   │ VOLTS  │  CLOCK   │ THROTTLED │
├──────────┼─────────┼────────┼──────────┼───────────┤
    """.strip()


def build_output(output_dict: Dict[str, str]) -> str:
    return "│" + "│".join([f" {val} " for val in output_dict.values()]) + "│"


def build_summary(summary: Dict[str, str]) -> str:
    s = summary
    return f"""
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = {s["temp_min"]}/{s["temp_avg"]}/{s["temp_max"]}
    Voltage min/avg/max = {s["voltage_min"]}/{s["voltage_avg"]}/{s["voltage_max"]}
    Clock min/avg/max = {s["clock_min"]}/{s["clock_avg"]}/{s["clock_max"]}
    """
