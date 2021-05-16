import argparse
import time

from rpidiag import diag_info
from rpidiag.config import IS_LOGGING_ENABLED, REFRESH_TIME
from rpidiag import output_handler as oh


def cli() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("-q", "--quiet", action="store_true", help="quiet mode")

    args = parser.parse_args()

    if IS_LOGGING_ENABLED:
        oh.check_save_permissions()

    if not args.quiet:
        oh.print_header()

    diag = diag_info.DiagInfo()

    try:
        while True:
            diag.update()

            if not args.quiet:
                print(diag.get_output())

            if IS_LOGGING_ENABLED:
                diag.log()

            time.sleep(REFRESH_TIME)

    except KeyboardInterrupt:
        if not args.quiet:
            print(diag.get_summary())
        else:  # after ^C prompt should go to the next line
            print()
