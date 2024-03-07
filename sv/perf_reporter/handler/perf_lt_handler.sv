class perf_lt_handler extends perf_base_handler;
    `perf_hdlr_utils(perf_lt_handler)

    function new(string hier, string name);
        super.new(hier, name);
        this.unit = "ns";
    endfunction : new

    virtual function string cfg2str(int indent = 0);
    endfunction : cfg2str

endclass : perf_lt_handler