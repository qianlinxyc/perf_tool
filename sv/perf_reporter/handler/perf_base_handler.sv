//@macro:
//  defines utils needed for hdlr, may add more later
`define perf_hdlr_utils(T)  \
    `m_uvm_get_type_name_func(T)

typedef perf_report_server;

virtual class perf_base_handler extends uvm_object;
    `perf_hdlr_utils(perf_base_handler)

    string hier;
    string name;

    bit    enabled = 1;

    string unit;

    function new(string hier, string name);
        this.hier = hier;
        this.name = name;
        this.register_to_svr();
    endfunction : new

    virtual function void set_unit(string unit);
        this.unit = unit;
    endfunction : set_unit

    //@function:
    //pure virtual function to print cfg of the handler
    pure virtual function string cfg2str(int indent = 0);

    //@function:
    //register perf_handler to perf_server, cannot be overriden
    function void register_to_svr();
        perf_report_server svr;
        svr = perf_report_server::get();
        svr.register_handler(this);
    endfunction : register_to_svr

endclass : perf_base_handler