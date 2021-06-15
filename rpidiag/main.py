import argparse
import time
from argparse import Namespace
from pathlib import Path

from rpidiag import diag_info
from rpidiag import output_handler as oh
from rpidiag.config import LOGPATH, REFRESH_TIME
from rpidiag.templates import HEADER


def cli():
    args = _parse_cli()

    if args.log:
        oh.check_save_permissions(args.log)

    if not args.quiet:
        print(HEADER)

    diag = diag_info.DiagInfo()

    try:
        while True:
            diag.update()

            if not args.quiet:
                print(diag.get_output())

            if args.log:
                diag.log(Path(args.log))

            time.sleep(args.refresh / 1000)

    except KeyboardInterrupt:
        if not args.quiet:
            print(diag.get_summary())
        else:  # after ^C prompt should go to the next line
            print()


def _parse_cli() -> Namespace:
    parser = argparse.ArgumentParser(prog="rpidiag")

    parser.add_argument(
        "-l",
        "--log",
        nargs="?",
        const=LOGPATH,
        help=f"log output, defaults to {LOGPATH}",
    )
    parser.add_argument(
        "-r",
        "--refresh",
        type=int,
        default=REFRESH_TIME,
        help="set refresh time, defaults to 2000 ms",
    )
    parser.add_argument("-q", "--quiet", action="store_true", help="quiet mode")

    return parser.parse_args()
