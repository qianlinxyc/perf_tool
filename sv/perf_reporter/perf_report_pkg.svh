package perf_report_pkg;
    import uvm_pkg::*;

    `include "handler/perf_base_handler.sv"
    `include "handler/perf_lt_handler.sv"
    `include "handler/perf_bw_handler.sv"
    `include "handler/perf_ut_handler.sv"
    `include "handler/perf_bp_handler.sv"

    `include "perf_report_server.sv"

endpackage : perf_report_pkg
