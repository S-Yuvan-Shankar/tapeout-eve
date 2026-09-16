import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):

    dut._log.info("Start")

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 2)

    assert dut.uo_out.value == 0

    # Release reset
    dut.rst_n.value = 1

    # Counter should increment every clock
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 1

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 2

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 3

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 4

    # Test several more counts
    for expected in range(5, 11):
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == expected

    # Test reset again
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 0

    dut._log.info("Counter test passed!")
