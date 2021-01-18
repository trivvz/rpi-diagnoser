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
22:38:25 | t = 59.7°C | v = 0.85V | clk = 1500 MHz       | 0b0
22:38:27 | t = 60.4°C | v = 0.85V | clk = 1500 MHz        | 0b10000000000000001000
22:38:29 | t = 59.2°C | v = 0.85V | clk = 1000 MHz       | 0b10000000000000000000
^C
--- Raspberry Pi diagnostic statistics ---
Temperature min/avg/max = 59.2/59.8/60.4
    Voltage min/avg/max = 0.85/0.85/0.85
      Clock min/avg/max = 1500/1500/1500
```

## How to read throttled message?
```
01110000000000000010
||||            ||||_ Under-voltage detected
||||            |||_ Arm frequency capped
||||            ||_ Currently throttled
||||            |_ Soft temperature limit active
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
