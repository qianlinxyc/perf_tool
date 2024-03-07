import json


# clean up the raw data from JSON file
# - index:
#       iteration of type name, then hier, then name
#       iteration of hier, then name, then type name
# - raw cfgs:
#       type_name::hier::name
# - raw msgs:
#       type_name::hier::name
class PerfReportModel:
    def __init__(self):
        self.report_file = ""
        self.type_idx = []
        self.hier_idx = []
        self.name_idx = []
        self.data = {}
        self.msgs = {}

    # set report file, and do the data clean up
    def set_report_file(self, report_file):
        self.report_file = report_file
        with open(self.report_file, 'r', encoding='utf-8') as fp:
            self.data = json.load(fp)
        self.type_idx = []
        self.hier_idx = []
        self.name_idx = []
        self.__set_idx__()
        self.msgs = {}
        self.__set_msg__()

    def __set_idx__(self):
        idx = []
        cfg = self.get_cfg()
        for each_type in cfg:
            for each_hier in cfg[each_type]:
                for each_name in cfg[each_type][each_hier]:
                    idx.append({"type": self.__convert_type_name__(each_type), "hier": each_hier, "name": each_name})
        self.type_idx = sorted(idx, key=lambda hdlr: (hdlr["type"], hdlr["hier"], hdlr["name"]))
        self.hier_idx = sorted(idx, key=lambda hdlr: (hdlr["hier"], hdlr["name"], hdlr["type"]))
        self.name_idx = sorted(idx, key=lambda hdlr: (hdlr["name"], hdlr["hier"], hdlr["type"]))

    def get_cfg(self):
        return self.data["cfg"]

    # 0 is type view
    # 1 is hier view
    # 2 is name view
    def get_probe_list(self, probe_idx_type):
        if probe_idx_type == 0:
            return self.type_idx
        elif probe_idx_type == 1:
            return self.hier_idx
        elif probe_idx_type == 2:
            return self.name_idx
        else:
            return []

    def get_timescale(self):
        return self.data["timescale_1ms"]

    def __set_msg__(self):
        msgs = self.data["msgs"]
        cfg = self.get_cfg()
        for each_type in cfg:
            cov_type = self.__convert_type_name__(each_type)
            if cov_type not in self.msgs:
                self.msgs[cov_type] = {}
            for each_hier in cfg[each_type]:
                if each_hier not in self.msgs[cov_type]:
                    self.msgs[cov_type][each_hier] = {}
                for each_name in cfg[each_type][each_hier]:
                    self.msgs[cov_type][each_hier][each_name] = []
        for msg in msgs:
            tn = msg["tn"]
            hr = msg["hr"]
            nm = msg["nm"]
            # TODO: add check if tn/hr/nm doesn't exist
            self.msgs[self.__convert_type_name__(tn)][hr][nm].append(msg["msg"])

    @staticmethod
    def __convert_type_name__(type_name):
        if type_name == "perf_bw_handler":
            new_type_name = "bandwidth"
        elif type_name == "perf_lt_handler":
            new_type_name = "latency"
        elif type_name == "perf_ut_handler":
            new_type_name = "utilization"
        elif type_name == "perf_bp_handler":
            new_type_name = "backpressure"
        else:
            new_type_name = type_name
        return new_type_name

    def retrieve_probe_msgs(self, probe):
        return self.msgs[probe["type"]][probe["hier"]][probe["name"]]

    def get_probe_cfg(self, probe):
        cfg = self.get_cfg()
        return cfg[probe["type"]][probe["hier"]][probe["name"]]
