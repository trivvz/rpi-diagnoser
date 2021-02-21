import time

from rpidiag import diag_info
from rpidiag.config import IS_LOGGING_ENABLED, REFRESH_TIME
from rpidiag.templates import HEADER


def cli():
    diag = diag_info.DiagInfo()
    print(HEADER)
    try:
        while True:
            diag.update()
            print(diag.get_output())

            if IS_LOGGING_ENABLED:
                diag.log()

            time.sleep(REFRESH_TIME)

    except KeyboardInterrupt:
        print(diag.get_summary())
