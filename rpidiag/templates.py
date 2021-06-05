from typing import Dict

HEADER = """
┌──────────┬─────────┬────────┬──────────┬───────────┐
│   TIME   │  TEMP   │ VOLTS  │  CLOCK   │ THROTTLED │
├──────────┼─────────┼────────┼──────────┼───────────┤
    """.strip()


def build_output(output_dict: Dict[str, str]) -> str:
    return "│" + "│".join([f" {val} " for val in output_dict.values()]) + "│"


def build_summary(summary: Dict[str, str]) -> str:
    return f"""
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = {summary["temp_min"]}/{summary["temp_avg"]}/{summary["temp_max"]}
    Voltage min/avg/max = {summary["voltage_min"]}/{summary["voltage_avg"]}/{summary["voltage_max"]}
    Clock min/avg/max = {summary["clock_min"]}/{summary["clock_avg"]}/{summary["clock_max"]}
    """
