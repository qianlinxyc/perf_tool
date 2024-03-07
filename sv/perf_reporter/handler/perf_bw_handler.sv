class perf_bw_handler extends perf_base_handler;
    `perf_hdlr_utils(perf_bw_handler)

    function new(string hier, string name);
        super.new(hier, name);
        this.unit = "pkt";
    endfunction : new

    function void set_packet(int unsigned cnt);
        perf_report_server svr = perf_report_server::get();
        string             message;

        message = $sformatf("get pkt cnt: %0d %0s", cnt, unit);
        svr.print_to_file(message, this);
    endfunction : set_packet

    virtual function string cfg2str(int indent = 0);
        string ind_str = {indent{"\t"}};

        cfg2str = "";
        cfg2str = {cfg2str, ind_str, $sformatf("\"enabled\": %0d,\n", this.enabled)};
        cfg2str = {cfg2str, ind_str, $sformatf("\"unit\": \"%0s\"\n", this.unit   )};
    endfunction : cfg2str

endclass : perf_bw_handler