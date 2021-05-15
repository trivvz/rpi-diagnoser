from typing import Dict, List

from rpidiag import utils
from rpidiag.constants import (
    GET_THROTTLED,
    THROTTLED_BIT_3,
    THROTTLED_BIT_16,
    THROTTLED_BIT_19,
    THROTTLED_SEP,
)


def get() -> str:
    throttled_str = _get_binary()
    return (
        _get_occurred_part(throttled_str)
        + f"{THROTTLED_SEP}"
        + _get_active_part(throttled_str)
    )


def get_summary_list() -> List[int]:
    output = []
    for key, val in get_summary().items():
        if val:
            output.append(key)
    return output


def get_summary() -> Dict[int, int]:
    output = {}
    for idx, val in enumerate(_get_occurred_part(_get_binary())):
        output[idx] = int(val)
    return output


def _get_occurred_part(throttled_bin: str) -> str:
    return f"{throttled_bin[THROTTLED_BIT_19:THROTTLED_BIT_16 + 1]}"


def _get_active_part(throttled_bin: str) -> str:
    return f"{throttled_bin[THROTTLED_BIT_3:]}"


def _get_binary() -> str:
    return f"{_get_raw_value():#020b}"


def _get_raw_value() -> int:
    return int(utils.call_cmd(GET_THROTTLED), 0)
