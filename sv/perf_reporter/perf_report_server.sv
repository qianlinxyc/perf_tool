typedef perf_report_server;

class perf_report_server extends uvm_component;

    protected static perf_report_server svr = perf_report_server::get();

    //@variable:
    //  handlers[type][hier][name]
    perf_base_handler handlers[string][string][string];

    //@variable:
    //  file handle(s)
    integer file_handle;

    // global configuration
    // file control

    bit first_msg_flag = 1;

    // dummy new function, never use
    protected function new(string name="base", uvm_component parent);
        super.new(name, parent);
    endfunction : new

    // static get function to get the handle of perf report server
    static function perf_report_server get();
        if(svr == null) begin
            svr = new("perf_report_server", uvm_root::get());
        end
        return svr;
    endfunction : get

    //@function:
    //  cannot be overriden, register handler to perf report server
    function void register_handler(perf_base_handler hdlr);
        string tn = hdlr.get_type_name();
        string hr = hdlr.hier;
        string nm = hdlr.name;

        if(handlers.exists(tn)) begin
            if(handlers[tn].exists(hr)) begin
                if(handlers[tn][hr].exists(nm)) begin
                    `uvm_fatal("perf_report_server", $sformatf("%s %s %s already exists! handler register failed!", tn, hr, nm))
                end
            end
        end
        handlers[tn][hr][nm] = hdlr;
    endfunction : register_handler

    //@function:
    //  convert config info to strings, print static config to file in json
    //  cfg: {
    //      perf_lw_handler: {
    //          hierA: {
    //              nameB: {
    //                  ......
    //              }
    //          }
    //      }
    //  },

    function string cfg2str(int indent = 0);
        string ind_str = {indent{"\t"}};

        cfg2str = "";
        cfg2str = {cfg2str, ind_str, "\"cfg\": {\n"};
        cfg2str = {cfg2str, __cfg2str_type__(indent+1)};
        cfg2str = {cfg2str, ind_str, "},\n"};

        return cfg2str;
    endfunction : cfg2str

    function string __cfg2str_type__(int indent = 0);
        bit    first = 1;
        string ind_str = {indent{"\t"}};

        __cfg2str_type__ = "";
        foreach(handlers[ii]) begin
            // iterate through handler types
            if(!first) begin
                __cfg2str_type__ = {__cfg2str_type__, ",\n"};
            end
            __cfg2str_type__ = {__cfg2str_type__, ind_str, $sformatf("\"%0s\": {\n", ii)};
            __cfg2str_type__ = {__cfg2str_type__, __cfg2str_hier__(ii, indent+1)};
            __cfg2str_type__ = {__cfg2str_type__, ind_str, "}"};
            first = 0;
        end
        __cfg2str_type__ = {__cfg2str_type__, "\n"};
    endfunction : __cfg2str_type__

    function string __cfg2str_hier__(string tn, int indent = 0);
        bit    first = 1;
        string ind_str = {indent{"\t"}};

        __cfg2str_hier__ = "";
        foreach(handlers[tn][jj]) begin
            // iterate through hierarchies
            if(!first) begin
                __cfg2str_hier__ = {__cfg2str_hier__, ",\n"};
            end
            __cfg2str_hier__ = {__cfg2str_hier__, ind_str, $sformatf("\"%0s\": {\n", jj)};
            __cfg2str_hier__ = {__cfg2str_hier__, __cfg2str_hdlr__(tn, jj, indent+1)};
            __cfg2str_hier__ = {__cfg2str_hier__, ind_str, "}"};
            first = 0;
        end
        __cfg2str_hier__ = {__cfg2str_hier__, "\n"};
    endfunction : __cfg2str_hier__

    function string __cfg2str_hdlr__(string tn, string hr, int indent = 0);
        bit    first = 1;
        string ind_str = {indent{"\t"}};

        __cfg2str_hdlr__ = "";
        foreach(handlers[tn][hr][kk]) begin
            // iterate through handlers
            if(!first) begin
                __cfg2str_hdlr__ = {__cfg2str_hdlr__, ",\n"};
            end
            __cfg2str_hdlr__ = {__cfg2str_hdlr__, ind_str, $sformatf("\"%0s\": {\n", kk)};
            __cfg2str_hdlr__ = {__cfg2str_hdlr__, handlers[tn][hr][kk].cfg2str(indent+1)};
            __cfg2str_hdlr__ = {__cfg2str_hdlr__, ind_str, "}"};
            first = 0;
        end
        __cfg2str_hdlr__ = {__cfg2str_hdlr__, "\n"};
    endfunction : __cfg2str_hdlr__

    virtual function void start_of_simulation_phase(uvm_phase phase);
        super.start_of_simulation_phase(phase);
        file_handle = $fopen("performance.rpt", "w");

        $fwrite(file_handle, "{\n");

        // calibrate the timescale:
        $fwrite(file_handle, "\t\"timescale_1ms\": %0t,\n", 1ms);

        $fwrite(file_handle, "%0s", cfg2str(.indent(1)));
        $fwrite(file_handle, "\t\"msgs\":[\n");
    endfunction : start_of_simulation_phase

    virtual function void report_phase(uvm_phase phase);
        super.report_phase(phase);
        $fdisplay(file_handle, "\n\t]");
        $fdisplay(file_handle, "}");
        $fclose(file_handle);
    endfunction : report_phase

    // {"tn": "type_name", "hr": "hierarchy", "nm": "name", "msg": "message"}
    function void print_to_file(string message, perf_base_handler handler);
        string content = "";
        string ind_str = "\t\t";

        if(!first_msg_flag) begin
            content = {content, ",\n"};
        end
        content = {content, ind_str, $sformatf("{\"tn\":\"%0s\",", handler.get_type_name())};
        content = {content, $sformatf("\"hr\":\"%0s\",", handler.hier)};
        content = {content, $sformatf("\"nm\":\"%0s\",", handler.name)};
        content = {content, $sformatf("\"msg\":\"@%0t %0s\"}", $realtime(), message)};
        $fwrite(file_handle, content);
        first_msg_flag = 0;
    endfunction : print_to_file

endclass : perf_report_server