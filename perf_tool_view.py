import os
import re

from PySide6.QtWidgets import (QTableWidgetItem,
                               QMainWindow,
                               QDialog,
                               QFileDialog,
                               QToolTip,
                               )
from PySide6.QtCore import Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCharts import (QLineSeries,
                              QValueAxis,
                              QChartView,
                              QChart,
                              )
from PySide6.QtGui import (QPainter,
                           QCursor,
                           )

# Pyecharts
#from pyecharts import options as opts
#from pyecharts.charts import Line, Bar
#from pyecharts.faker import Faker

# UI
from ui.perf_tool_ui import Ui_MainWindow
from ui.perf_tool_probe_sel_ui import Ui_PerfToolProbeSelDialog

# List sort by
# sort by = 0: type-hier-name
# sort by = 1: hier-name-type
# sort by = 2: name-hier-type
def probe_list_sort(probe_list, sort_by):
    if sort_by == 0:
        probe_list.sort(key=lambda hdlr: (hdlr["type"], hdlr["hier"], hdlr["name"]))
    elif sort_by == 1:
        probe_list.sort(key=lambda hdlr: (hdlr["hier"], hdlr["name"], hdlr["type"]))
    else:
        probe_list.sort(key=lambda hdlr: (hdlr["name"], hdlr["hier"], hdlr["type"]))

class PerfReportProbeSelDialog(QDialog, Ui_PerfToolProbeSelDialog):
    def __init__(self, ctrl):
        super().__init__()
        self.setupUi(self)
        self.ctrl = ctrl
        self.__display_probe_list__()
        #Sort by
        self.radioButton_typeView.clicked.connect(self.__display_probe_list__)
        self.radioButton_hierView.clicked.connect(self.__display_probe_list__)
        self.radioButton_nameView.clicked.connect(self.__display_probe_list__)
        #Type Selection Check Box
        self.checkBox.toggled.connect(self.__display_probe_list__)
        self.checkBox_2.toggled.connect(self.__display_probe_list__)
        self.checkBox_3.toggled.connect(self.__display_probe_list__)
        self.checkBox_4.toggled.connect(self.__display_probe_list__)
        #Regex
        self.lineEdit_2.textChanged.connect(self.__display_probe_list__)
        self.lineEdit_3.textChanged.connect(self.__display_probe_list__)

    def get_selected_probes(self):
        selected_probes = []
        # first find selected items
        selected_indexes = self.tableWidget_probes.selectedIndexes()
        selected_rows = []
        for index in selected_indexes:
            if index.column() == 0:
                selected_rows.append(index.row())
        selected_rows.sort()
        for selected_row in selected_rows:
            index = {}
            row_type = self.tableWidget_probes.item(selected_row, 0).text()
            row_hier = self.tableWidget_probes.item(selected_row, 1).text()
            row_name = self.tableWidget_probes.item(selected_row, 2).text()
            index["type"] = row_type
            index["hier"] = row_hier
            index["name"] = row_name
            selected_probes.append(index)
        return selected_probes

    def __display_probe_list__(self):
        # TODO: support hide disabled probes
        # TODO: support hide probes with no messages
        # Refresh the probes table
        self.tableWidget_probes.clearContents()
        probes_list = self.ctrl.get_probe_list(0)
        sort_by = self.get_sorting_selection()
        probe_list_sort(probes_list, sort_by)
        probes_list = self.__apply_name_filter__(probes_list)
        self.tableWidget_probes.setRowCount(len(probes_list))
        incr = 0
        for probes in probes_list:
            item_type = QTableWidgetItem(probes["type"])
            item_type.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item_hier = QTableWidgetItem(probes["hier"])
            item_hier.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item_name = QTableWidgetItem(probes["name"])
            item_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            # item_enable = QTableWidgetItem(probe_cfg[each_type][each_hier][each_name]["enabled"])
            # item_unit = QTableWidgetItem(probe_cfg[each_type][each_hier][each_name]["unit"])
            self.tableWidget_probes.setItem(incr, 0, item_type)
            self.tableWidget_probes.setItem(incr, 1, item_hier)
            self.tableWidget_probes.setItem(incr, 2, item_name)
            # self.tableWidget_probes.setItem(incr, 3, item_enable)
            # self.tableWidget_probes.setItem(incr, 4, item_unit)
            incr += 1

    def get_sorting_selection(self):
        if self.radioButton_typeView.isChecked():
            return 0
        if self.radioButton_hierView.isChecked():
            return 1
        if self.radioButton_nameView.isChecked():
            return 2

    def __apply_name_filter__(self, probes_list):
        #print("__apply_name_filter__ called")
        filtered_probes_list = probes_list
        #print(filtered_probes_list)

        # type selection
        bw_select = self.checkBox.isChecked()
        lt_select = self.checkBox_3.isChecked()
        ut_select = self.checkBox_2.isChecked()
        bp_select = self.checkBox_4.isChecked()
        #print("bw: {}, lt: {}, ut: {}, bp: {}".format(bw_select, lt_select, ut_select, bp_select))

        if not bw_select:
            filtered_probes_list = [item for item in filtered_probes_list if item["type"] != "bandwidth"]
        if not lt_select:
            filtered_probes_list = [item for item in filtered_probes_list if item["type"] != "latency"]
        if not ut_select:
            filtered_probes_list = [item for item in filtered_probes_list if item["type"] != "utilization"]
        if not bp_select:
            filtered_probes_list = [item for item in filtered_probes_list if item["type"] != "backpressure"]

        # regex
        hier_str = self.lineEdit_3.text()
        name_str = self.lineEdit_2.text()

        if not hier_str == "*":
            hier_str = "^{}$".format(hier_str.replace("*", ".*"))
            hier_regex = re.compile(hier_str)
            filtered_probes_list = [item for item in filtered_probes_list if re.match(hier_regex, item["hier"])]
        if not name_str == "*":
            name_str = "^{}$".format(name_str.replace("*", ".*"))
            name_regex = re.compile(name_str)
            filtered_probes_list = [item for item in filtered_probes_list if re.match(name_regex, item["name"])]

        #print(filtered_probes_list)
        return filtered_probes_list

class PerfReportView(QMainWindow, Ui_MainWindow):
    def __init__(self, ctrl):
        super().__init__()
        self.setupUi(self)
        self.ctrl = ctrl
        self.actionLoad_Report_File.triggered.connect(self.open_rpt_dialog)
        self.actionExit.triggered.connect(self.close)

        #self.plot_button.clicked.connect(self.plot_figures_test)
        self.plot_button.clicked.connect(self.plot_figures)

        self.pushButton.clicked.connect(self.dialog_add_probe)
        self.pushButton_2.clicked.connect(self.delete_probe)
        self.plot_probes = []

        self.radioButton_typeView.clicked.connect(self.__display_plot_probes__)
        self.radioButton_hierView.clicked.connect(self.__display_plot_probes__)
        self.radioButton_nameView.clicked.connect(self.__display_plot_probes__)

    def __display_plot_probes__(self):
        sort_by = self.get_sorting_selection()
        probe_list_sort(self.plot_probes, sort_by)
        self.tableWidget_probes.clearContents()
        self.tableWidget_probes.setSortingEnabled(False)
        self.tableWidget_probes.setRowCount(len(self.plot_probes))
        incr = 0
        for probes in self.plot_probes:
            item_type = QTableWidgetItem(probes["type"])
            item_type.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item_hier = QTableWidgetItem(probes["hier"])
            item_hier.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item_name = QTableWidgetItem(probes["name"])
            item_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            #print("{}::{}::{}".format(item_type.text(), item_hier.text(), item_name.text()))
            # item_enable = QTableWidgetItem(probe_cfg[each_type][each_hier][each_name]["enabled"])
            # item_unit = QTableWidgetItem(probe_cfg[each_type][each_hier][each_name]["unit"])
            self.tableWidget_probes.setItem(incr, 0, item_type)
            self.tableWidget_probes.setItem(incr, 1, item_hier)
            self.tableWidget_probes.setItem(incr, 2, item_name)
            # self.tableWidget_probes.setItem(incr, 3, item_enable)
            # self.tableWidget_probes.setItem(incr, 4, item_unit)
            incr += 1

    # open report load dialog
    def open_rpt_dialog(self):
        #Open rpt dialog
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Perf Report Files (*.rpt);;Log files (*.log);;Any files (*)")
        dialog.setViewMode(QFileDialog.Detail)
        perf_report_file = self.ctrl.get_report_file()
        if perf_report_file != "":
            dialog.setDirectory(os.path.dirname(perf_report_file))
        if dialog.exec():
            filename = dialog.selectedFiles()
            self.ctrl.set_report_file(filename[0])
            self.statusbar.showMessage("File {} loaded successfully".format(filename[0]))
            # Refresh the timescale info
            timescale = self.ctrl.get_view_timescale()
            self.lineEdit_timescale.setText(str(timescale[0]))
            self.comboBox_timescale.setCurrentText(str(timescale[1]))
            # Refresh the probes table

    def plot_figures_test(self):
        self.pyecharts_window = QWebEngineView()
        self.pyecharts_window.setFixedWidth(1024)
        self.pyecharts_window.setFixedHeight(758)

        # 准备数据集
        x1_data = list(range(10))
        dataset1_data = [i ** 2 for i in x1_data]
        x2_data = list(range(5, 15))
        dataset2_data = [i ** 3 for i in x2_data]

        # 创建Line图表对象
        line1 = Line()
        line2 = Line()

        # 添加数据集到Line对象1
        line1.add_dataset("数据集1", dataset1_data)
        line1.set_series_opts(label_opts=opts.LabelOpts(position="inside"))

        # 添加数据集到Line对象2
        line2.add_dataset("数据集2", dataset2_data)
        line2.set_series_opts(label_opts=opts.LabelOpts(position="inside"))

        # 组合两个Line对象
        line = (line1 + line2).set_global_opts(title_opts=opts.TitleOpts(title="两个x轴数据点不同的折线图示例"))

        self.pyecharts_window.setHtml(line.render_embed())
        self.pyecharts_window.show()


    def plot_figures(self):
        # first find selected items
        selected_indexes = self.tableWidget_probes.selectedIndexes()
        selected_rows = []
        for index in selected_indexes:
            if index.column() == 0:
                selected_rows.append(index.row())
        selected_rows.sort()
        selected_probes = []
        for selected_row in selected_rows:
            index = {"type": self.tableWidget_probes.item(selected_row, 0).text(),
                     "hier": self.tableWidget_probes.item(selected_row, 1).text(),
                     "name": self.tableWidget_probes.item(selected_row, 2).text(),
                     "plot_type": self.tableWidget_probes.item(selected_row, 3).text()}
            selected_probes.append(index)
        plot_data = self.ctrl.get_plot_data(selected_probes)

        # plot data
        chart = QChart()
        #chart.setTitle("Simple Bar Chart Example")
        chart.setAnimationOptions(QChart.AllAnimations)

        axisX = QValueAxis()
        #axisX.setRange(780000000, 1500000000)  # 设置X轴范围
        timescale = self.ctrl.get_view_timescale()
        axisX.setTitleText("time({}{})".format(timescale[0], timescale[1]))
        chart.addAxis(axisX, Qt.AlignBottom)

        for data_name in plot_data:
            lineseries = QLineSeries()
            lineseries.setName(data_name)
            for data_point in plot_data[data_name]["plot_data"]:
                lineseries.append(data_point[0], data_point[1])

            axisY = QValueAxis()
            # axisY.setRange(0, 10)  # 设置Y轴范围
            # axisY.setLabelFormat("y1")
            axisY.setTitleText(data_name)

            # Note the order here!
            # First add axis to a chart, then specify the axis to the lineseries!!!
            chart.addAxis(axisY, Qt.AlignLeft)
            chart.addSeries(lineseries)
            lineseries.attachAxis(axisX)
            lineseries.attachAxis(axisY)

            lineseries.hovered.connect(lambda point, series=lineseries:
                QToolTip.showText(QCursor.pos(), "%s\nx:%f\ny: %f" % (lineseries.name(), point.x(), point.y())))

        # 创建图表视图
        self.chartView = QChartView(chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartView.setRubberBand(QChartView.HorizontalRubberBand)
        self.chartView.show()

    def dialog_add_probe(self):
        psel_dialog = PerfReportProbeSelDialog(self.ctrl)
        if psel_dialog.exec():
            selected_probes = psel_dialog.get_selected_probes()
            self.plot_probes += selected_probes
            self.__display_plot_probes__()

    def delete_probe(self):
        selected_indexes = self.tableWidget_probes.selectedIndexes()
        selected_rows = []
        for index in selected_indexes:
            if index.column() == 0:
                selected_rows.append(index.row())
        selected_rows.sort(reverse=True)
        for selected_row in selected_rows:
            self.plot_probes.pop(selected_row)
        self.__display_plot_probes__()

    def get_sorting_selection(self):
        if self.radioButton_typeView.isChecked():
            return 0
        if self.radioButton_hierView.isChecked():
            return 1
        if self.radioButton_nameView.isChecked():
            return 2


