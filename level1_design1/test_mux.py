# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

class DisconnectedPortsError(Exception):

    def __init__(self):
        super().__init__("There are Disconnected Ports to DUT, kindly refer to module Definition")


@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    inp_val = 0b10
    num_sel_bits = 5

    for i in range(31):
        getattr(dut, f"inp{i}").value = inp_val
        dut.sel.value = i
        await Timer(2, "ns")
        dut._log.info(dut.out.value)
        assert dut.out.value == inp_val, f"Values {inp_val} != {dut.out.value} didn't match"

