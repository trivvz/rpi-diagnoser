import time

from rpidiag import diag_info
from rpidiag.config import IS_LOGGING_ENABLED, REFRESH_TIME
from rpidiag.output_handler import OutputHandler


def cli():
    if IS_LOGGING_ENABLED:
        OutputHandler.check_save_permissions()
    OutputHandler.print_header()
    diag = diag_info.DiagInfo()
    try:
        while True:
            diag.update()
            print(diag.get_output())

            if IS_LOGGING_ENABLED:
                diag.log()

            time.sleep(REFRESH_TIME)

    except KeyboardInterrupt:
        print(diag.get_summary())
