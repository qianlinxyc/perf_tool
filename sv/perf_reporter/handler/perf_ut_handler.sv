class perf_ut_handler extends perf_base_handler;
    `perf_hdlr_utils(perf_ut_handler)

    function new(string hier, string name);
        super.new(hier, name);
        this.unit = "\%";
    endfunction : new

    virtual function string perf_info2str();
    endfunction : perf_info2str

    virtual function string cfg2str(int indent = 0);
        cfg2str = "";
    endfunction : cfg2str
endclass : perf_ut_handler