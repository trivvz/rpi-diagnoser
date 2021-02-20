#!/usr/bin/python3
import time

from rpidiag import diag_info
from rpidiag.config import IS_LOGGING_ENABLED, REFRESH_TIME, LOGFILE
from rpidiag.templates import HEADER


if __name__ == "__main__":
    diag = diag_info.DiagInfo()
    print(HEADER)
    try:
        while True:
            diag.update()
            str(diag)

            if IS_LOGGING_ENABLED:
                diag.gen_log(LOGFILE)

            time.sleep(REFRESH_TIME)

    except KeyboardInterrupt:
        print(diag.gen_summary())
