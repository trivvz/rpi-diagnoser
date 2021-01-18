#!/usr/bin/python3
import time

import diag_info
from config import REFRESH_TIME


if __name__ == "__main__":
    diag = diag_info.DiagInfo()
    try:
        while True:
            diag.update()
            str(diag)
            # gen_log("log.txt")
            time.sleep(REFRESH_TIME)
    except KeyboardInterrupt:
        print(diag.gen_summary())
