from src import utils
from src.constants import (
    GET_THROTTLED,
    THROTTLED_VAL_0,
    THROTTLED_VAL_3,
    THROTTLED_VAL_16,
    THROTTLED_SEP,
)


class Throttled:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get() -> str:
        throttled_val = int(utils.call_cmd(GET_THROTTLED), 0)
        throttled_str = f"{throttled_val:#020b}"
        return (
            f"{throttled_str[THROTTLED_VAL_0:THROTTLED_VAL_3]}"
            f"{THROTTLED_SEP}"
            f"{throttled_str[THROTTLED_VAL_16:]}"
        )
