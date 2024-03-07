import re

class BwHandler:
    # plot type: histogram
    # plot msgs: list of messages
    def __init__(self, plot_type, plot_msgs):
        self.plot_type = plot_type
        self.plot_msgs = plot_msgs

    def get_plot_data(self):
        plot_type = self.plot_type
        plot_msgs = self.plot_msgs

        # TODO: only support bw handler for now
        pattern = r'@(\d+) get pkt cnt: (\d+) (\S+)'
        raw_data = {"plot_unit": "", "plot_data": []}
        plot_data = []
        for plot_msg in plot_msgs:
            matches = re.search(pattern, plot_msg)
            if matches:
                raw_data["plot_unit"] = matches[3]
                data_point = [float(matches[1]), float(matches[2])]
                raw_data["plot_data"].append(data_point)
            else:
                print("Error: msg {} is not of format {}".format(plot_msg, pattern))

        if len(raw_data["plot_data"]) != 0:
            raw_data["plot_data"].sort(key = lambda x:x[0])

            #TODO: add window config
            if plot_type == "histogram":
                #print("calculating histogram")
                window = 1000
                cur_time = int(raw_data["plot_data"][0][0] / window) * window
                accum_data = 0
                for data_point in raw_data["plot_data"]:
                    if data_point[0] >= (cur_time + window):
                        # dram a triangle
                        plot_data.append([cur_time, 0])
                        plot_data.append([cur_time, accum_data])
                        plot_data.append([cur_time+window, accum_data])
                        plot_data.append([cur_time+window, 0])
                        cur_time = int(data_point[0] / window) * window
                        accum_data = data_point[1]
                    else:
                        accum_data += data_point[1]

                if accum_data != 0:
                    plot_data.append([cur_time, 0])
                    plot_data.append([cur_time, accum_data])
                    plot_data.append([cur_time + window, accum_data])
                    plot_data.append([cur_time + window, 0])

            elif plot_type == "line":
                #print("calculating line")
                # moving window
                window = 100000000
                step   = 1000000
                cur_window_start = int((raw_data["plot_data"][0][0]-window)/step) * step + step
                #print(cur_window_start)
                cur_window_stop  = cur_window_start + window
                #print(cur_window_stop)
                cur_window_list = []
                accum_data = 0
                raw_data_idx = 0
                # add starting point
                plot_data.append([cur_window_start + window/2 - step, 0])

                #print(raw_data["plot_data"])

                while cur_window_start <= raw_data["plot_data"][-1][0] or len(cur_window_list) > 0:
                    #print("calculating line for window [{}, {}]".format(cur_window_start, cur_window_stop))
                    # push raw data into window
                    while raw_data_idx < len(raw_data["plot_data"]) and raw_data["plot_data"][raw_data_idx][0] < cur_window_stop:
                        cur_window_list.append(raw_data["plot_data"][raw_data_idx])
                        accum_data += raw_data["plot_data"][raw_data_idx][1]
                        raw_data_idx += 1
                        #print("appending raw_data, accum_data is: {}".format(accum_data))
                        #print(cur_window_list)
                    # pop raw data from window
                    while len(cur_window_list) > 0 and cur_window_list[0][0] < cur_window_start:
                        accum_data -= cur_window_list[0][1]
                        cur_window_list.pop(0)
                        #print("popping raw_data, accum_data is: {}".format(accum_data))
                        #print(cur_window_list)

                    plot_data.append([cur_window_start+window/2, accum_data/window])
                    # if no data to plot, plot 0 and progress to next node
                    if accum_data == 0 and len(cur_window_list) == 0 and cur_window_start <= raw_data["plot_data"][-1][0]:
                        cur_window_start = int((raw_data["plot_data"][raw_data_idx][0]-window)/step) * step + step
                        cur_window_stop  = cur_window_start + window
                        plot_data.append([cur_window_start + window/2 - step, 0])
                    else:
                        cur_window_start += step
                        cur_window_stop  += step
            else:
                print("Unsupported type passed, should be either histogram or line")
        print(plot_data)
        return plot_data


# class LtHandler:
#     def __init__(self):
#         pass
#
#
# class UtHandler:
#     def __init__(self):
#         pass
#
#
# class BpHandler:
#     def __init__(self):
#         pass

# Controller, interacts between View and Model
class PerfReportCtrl:
    def __init__(self):
        self.cur_rpt_file = ""
        self.model_timescale = []
        self.view_timescale = []
        self.view = None
        self.model = None

    def set_model(self, model):
        self.model = model

    def set_view(self, view):
        self.view = view

    # parse report file, called by view
    def set_report_file(self, rpt_path):
        self.model.set_report_file(rpt_path)
        self.cur_rpt_file = rpt_path
        self.model_timescale = self.cal_timescale(self.model.get_timescale())
        self.view_timescale = self.model_timescale

    def get_report_file(self):
        return self.cur_rpt_file

    def set_view_timescale(self, timescale):
        self.view_timescale = timescale

    def get_view_timescale(self):
        return self.view_timescale

    def get_probe_list(self, probe_idx_type):
        return self.model.get_probe_list(probe_idx_type)

    def get_plot_data(self, probes):
        plot_data = {}
        # filter msgs and covert to plot types:
        # "plot_type": "histogram"/"line",
        # "plot_data": [[x1,x2, x3, ...],[y1, y2, y3 ...]]
        for probe in probes:
            msgs = self.model.retrieve_probe_msgs(probe)
            tn = probe["type"]
            hr = probe["hier"]
            nm = probe["name"]
            plot_type = probe["plot_type"]

            # histogram:
            plot_name = "{}::{}::{}_{}".format(hr, nm, tn, plot_type)
            plot_data[plot_name] = {}
            plot_data[plot_name]["plot_type"] = plot_type
            plot_data[plot_name]["plot_unit"] = ""
            bw_handler = BwHandler(plot_type, msgs)
            plot_data[plot_name]["plot_data"] = bw_handler.get_plot_data()

        return plot_data

    def cal_timescale(self, num_1ms):
        num_of_zero = str(num_1ms).count('0')
        num_of_3zero = int(num_of_zero / 3)
        number = int(num_1ms / pow(10, num_of_3zero * 3))
        if num_of_3zero == 0:
            unit = "ms"
        elif num_of_3zero == 1:
            unit = "us"
        elif num_of_3zero == 2:
            unit = "ns"
        elif num_of_3zero == 3:
            unit = "ps"
        elif num_of_3zero == 4:
            unit = "fs"
        else:
            unit = "na"
        return [number, unit]