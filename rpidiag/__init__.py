from sys import version_info, exit

if version_info < (3, 6, 0):
    exit("Python 3.6 or later is required.")
