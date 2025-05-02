SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/dut.v
VERILOG_SOURCES += $(PWD)/wrapper/dut_test.v
TOPLEVEL = dut_xor
MODULE = dut_test
include $(shell python3 -m cocotb.config --makefiles)/Makefile.sim