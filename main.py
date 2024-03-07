# Only needed for access to command line arguments
import sys
from PySide6.QtWidgets import QApplication

# MVC
from perf_tool_model import PerfReportModel
from perf_tool_view import PerfReportView
from perf_tool_ctrl import PerfReportCtrl

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Model
    perf_report_model = PerfReportModel()
    perf_report_controller = PerfReportCtrl()
    perf_report_view = PerfReportView(perf_report_controller)

    perf_report_controller.set_model(perf_report_model)
    perf_report_controller.set_view(perf_report_view)

    perf_report_view.show()
    sys.exit(app.exec())
