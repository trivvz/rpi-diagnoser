# RPi Diagnoser

### Small Python script which can be used to diagnose current status of your Raspberry Pi

## Output includes:
- time
- temperature
- voltage
- CPU clock
- throttled status code in binary
- summary printed after exiting with `^C` (similar to `ping` command)

## Example output:
```
┌──────────┬────────┬───────┬──────────┬───────────┐
│   TIME   │  TEMP  │ VOLTS │  CLOCK   │ THROTTLED │
├──────────┼────────┼───────┼──────────┼───────────┤
│ 00:23:30 │ 58.0°C │ 1.34V │ 1400 MHz │ 1000:0000 │
│ 00:23:32 │ 57.5°C │ 1.23V │  700 MHz │ 1000:0000 │
│ 00:23:34 │ 57.5°C │ 1.20V │  600 MHz │ 1000:0000 │
^C
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = 57.5/57.8/58.0
    Voltage min/avg/max = 1.20/1.28/1.34
      Clock min/avg/max = 600/1025/1400
```

## How to read throttled message?
Note that trailing zeros are removed from the output

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

## Compatibility
- RPi 3B+
- RPi 4B
- above was checked but it should work for every Pi

## How to run?
```
git clone https://github.com/trivvz/rpi-diagnoser.git
python3 rpi-diagnoser/main.py
```

## TODO
- calculate and show standard deviation
- update throttled output
- log to /var/log (for usage with [log2ram](https://github.com/azlux/log2ram))
- add CLI interface
