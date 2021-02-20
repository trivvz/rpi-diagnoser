import os
import sys

if not __package__:
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from rpidiag.main import cli

if __name__ == "__main__":
    sys.exit(cli())
