RPiDiag
=======

[![Tests](https://github.com/trivvz/rpidiag/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/trivvz/rpidiag/actions/workflows/tests.yml)

### RPiDiag is an app that can be used to check the current status of your Raspberry Pi.

Output includes
---------------

- time
- temperature
- voltage
- CPU clock
- throttled status code in binary
- summary printed after exiting with `^C` (similar to the `ping` command)

Example output
--------------

```
┌──────────┬─────────┬────────┬──────────┬───────────┐
│   TIME   │  TEMP   │ VOLTS  │  CLOCK   │ THROTTLED │
├──────────┼─────────┼────────┼──────────┼───────────┤
│ 00:23:30 │ 60.3 °C │ 1.34 V │ 1400 MHz │ 1000:1000 │
│ 00:23:32 │ 59.5 °C │ 1.23 V │  700 MHz │ 1000:0000 │
│ 00:23:34 │ 57.8 °C │ 1.20 V │  600 MHz │ 1000:0000 │
^C
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = 57.8/59.2/60.3
    Voltage min/avg/max = 1.20/1.26/1.34
      Clock min/avg/max = 600/900/1400

Occurred events: soft temperature limit
```

Logging
-------

By default, logging is turned off, but it can be changed by setting `IS_LOGGING_ENABLED` to `True` in [src/config.py](src/config.py).
The default log path is set to `/var/log/rpidiag.log` meaning that `sudo` is needed to save the log file.
Remember that extensive logging may shorten the life of an SD Card.
It is advised to do it with a tool like [log2ram](https://github.com/azlux/log2ram) which mounts `/var/log` directly in RAM.

How to read a throttled message?
--------------------------------

*Note that trailing zeros are removed from the output.*

```
0111|000000000000|0010
||||              ||||_ Under-voltage detected
||||              |||_ Arm frequency capped
||||              ||_ Currently throttled
||||              |_ Soft temperature limit active
||||_ Under-voltage has occurred since last reboot
|||_ Arm frequency capped has occurred
||_ Throttling has occurred
|_ Soft temperature limit has occurred
```
*Adopted from this [comment](https://github.com/raspberrypi/firmware/commit/404dfef3b364b4533f70659eafdcefa3b68cd7ae#commitcomment-31620480).*

Compatibility
-------------

- RPi 3B+
- RPi 4B
- but it should work for every Pi

How to run?
-----------

No external Python packages are needed to run the app at this point.
Python 3.6 or later is needed.

```
git clone https://github.com/trivvz/rpidiag.git
cd rpidiag
python3 rpidiag
```

### For development

Dependencies are managed by
[poetry](https://github.com/python-poetry/poetry).
To build an environment with development dependencies run the
following:

```
git clone https://github.com/trivvz/rpidiag.git
cd rpidiag
pip3 install -U poetry
poetry install
```

TODO
----

- [x] add CLI interface (quiet mode, turn on/off the log, print help)
- [x] add pyproject.toml
- [ ] organize the repo into a Python package
- [ ] change package structure to include `src` folder
- [ ] add more flexible CLI interface, e.g. `-TC` to output only temp and clock values and similar

