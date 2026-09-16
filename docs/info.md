## How it works

This project implements an 8-bit up counter. On every rising edge of `clk`,
if `rst_n` is low, the counter resets to 0. Otherwise, the counter increments
by 1 each clock cycle. The current count value is continuously output on `uo_out`.

## How to test

Provide a clock signal on `clk` and hold `rst_n` low briefly to reset the
counter to 0. Then release `rst_n` (set it high) and observe `uo_out`
incrementing by 1 every clock cycle, wrapping from 255 back to 0.

## External hardware

None.
