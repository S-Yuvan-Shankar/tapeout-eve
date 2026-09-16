/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_counter (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    reg [7:0] count;

    always @(posedge clk) begin
        if (!rst_n)
            count <= 8'h00;
        else
            count <= count + 8'h01;
    end

    assign uo_out  = count;
    assign uio_out = 8'h00;
    assign uio_oe  = 8'h00;

    // Unused inputs
    wire _unused = &{ena, ui_in, uio_in, 1'b0};

endmodule
