import argparse
import time

from rpidiag import diag_info
from rpidiag.config import REFRESH_TIME, LOGFILE
from rpidiag import output_handler as oh


def cli() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-l",
        "--log",
        nargs="?",
        const=LOGFILE,
        help=f"log output, defaults to {LOGFILE}",
    )
    parser.add_argument("-q", "--quiet", action="store_true", help="quiet mode")

    args = parser.parse_args()

    if args.log:
        oh.check_save_permissions(args.log)

    if not args.quiet:
        oh.print_header()

    diag = diag_info.DiagInfo()

    try:
        while True:
            diag.update()

            if not args.quiet:
                print(diag.get_output())

            if args.log:
                diag.log(args.log)

            time.sleep(REFRESH_TIME)

    except KeyboardInterrupt:
        if not args.quiet:
            print(diag.get_summary())
        else:  # after ^C prompt should go to the next line
            print()
