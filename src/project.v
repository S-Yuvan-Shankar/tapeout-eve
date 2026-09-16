/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_counter (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IO Enable: 1=output, 0=input
    input  wire       ena,      // Enable
    input  wire       clk,      // Clock
    input  wire       rst_n     // Active-low reset
);

    // 8-bit counter register
    reg [7:0] count;

    // Counter logic
    always @(posedge clk) begin
        if (!rst_n)
            count <= 8'b00000000;
        else
            count <= count + 8'b00000001;
    end

    // Send counter value to output pins
    assign uo_out = count;

    // Bidirectional pins are unused
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Unused inputs
    wire _unused = &{ena, ui_in, uio_in, 1'b0};

endmodule
