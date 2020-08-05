# RPi Diagnoser

## Small Python script which can be used to diagnose current status of your Raspberry Pi

### Output includes:
- time
- temperature
- voltage
- CPU clock
- throttled status code in binary

Example output:
`22:14:53 | t = 52.1 'C | v = 1.20 V | clk = 599 MHz     | 0b1010000000000000000`

### How to read throttled message?
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
Adopted from this [comment](https://github.com/raspberrypi/firmware/commit/404dfef3b364b4533f70659eafdcefa3b68cd7ae#commitcomment-31620480).

#### Script was checked to be working with RPi 3B+.
