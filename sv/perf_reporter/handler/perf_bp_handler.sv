class perf_bp_handler extends perf_base_handler;
    `perf_hdlr_utils(perf_bp_handler)

    function new(string hier, string name);
        super.new(hier, name);
        this.unit = "NA";
    endfunction : new

    virtual function string perf_info2str();
    endfunction : perf_info2str

    virtual function string cfg2str(int indent = 0);
    endfunction : cfg2str

endclass : perf_bp_handler
