from rpidiag import utils
from rpidiag.constants import (
    GET_THROTTLED,
    THROTTLED_BIT_19,
    THROTTLED_BIT_16,
    THROTTLED_BIT_3,
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
            f"{throttled_str[THROTTLED_BIT_19:THROTTLED_BIT_16]}"
            f"{THROTTLED_SEP}"
            f"{throttled_str[THROTTLED_BIT_3:]}"
        )
