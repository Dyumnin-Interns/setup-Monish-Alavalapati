module dut_xor(input wire a,
	input wire b,
	output wire y
);

dut uut(
    .a(a),
    .b(b),
    .y(y)
);

initial begin
   $dumpfile("waves.vcd");
   $dumpvars; 
end
endmodule
