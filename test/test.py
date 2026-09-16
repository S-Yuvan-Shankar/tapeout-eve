# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Start clock: 10 us period = 100 KHz
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # -------------------------
    # Reset the counter
    # -------------------------
    dut._log.info("Reset")

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    # Hold reset for 2 clock cycles
    await ClockCycles(dut.clk, 2)

    # Counter should be 0 after reset
    assert dut.uo_out.value == 0

    # Release reset
    dut.rst_n.value = 1

    # -------------------------
    # Test counting
    # -------------------------
    dut._log.info("Testing counter")

    # After 1 clock cycle, counter = 1
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 1

    # After another clock cycle, counter = 2
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 2

    # Count up to 10
    for expected_count in range(3, 11):
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == expected_count

    dut._log.info("Counter test passed!")

    # -------------------------
    # Test reset again
    # -------------------------
    dut._log.info("Testing reset")

    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 1)

    # Counter should return to 0
    assert dut.uo_out.value == 0

    dut.rst_n.value = 1

    # Counter should start again from 1
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 1

    dut._log.info("All tests passed!")
