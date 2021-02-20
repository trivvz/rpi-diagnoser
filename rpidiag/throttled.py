from rpidiag import utils
from rpidiag.constants import (
    GET_THROTTLED,
    THROTTLED_BIT_3,
    THROTTLED_BIT_16,
    THROTTLED_BIT_19,
    THROTTLED_SEP,
)


class Throttled:
    def get(self) -> str:
        throttled_str = self._convert_to_binary()
        return (
            self._get_occurred_part(throttled_str)
            + f"{THROTTLED_SEP}"
            + self._get_active_part(throttled_str)
        )

    @staticmethod
    def _get_occurred_part(throttled_bin: str) -> str:
        return f"{throttled_bin[THROTTLED_BIT_19:THROTTLED_BIT_16 + 1]}"

    @staticmethod
    def _get_active_part(throttled_bin: str) -> str:
        return f"{throttled_bin[THROTTLED_BIT_3:]}"

    def _convert_to_binary(self) -> str:
        return f"{self._get_raw_value():#020b}"

    @staticmethod
    def _get_raw_value() -> int:
        return int(utils.call_cmd(GET_THROTTLED), 0)
