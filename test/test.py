import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):

    dut._log.info("Starting 8-bit counter test")

    # 100 kHz clock
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Initial values
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Reset
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)

    assert dut.uo_out.value == 0, "Counter did not reset to 0"

    # Release reset
    dut.rst_n.value = 1

    # Check counting
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 1, "Expected 1"

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 2, "Expected 2"

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 3, "Expected 3"

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 4, "Expected 4"

    dut._log.info("Counter test passed!")
