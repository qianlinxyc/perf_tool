# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'perf_tool_probe_sel.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QDialog, QDialogButtonBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QRadioButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_PerfToolProbeSelDialog(object):
    def setupUi(self, PerfToolProbeSelDialog):
        if not PerfToolProbeSelDialog.objectName():
            PerfToolProbeSelDialog.setObjectName(u"PerfToolProbeSelDialog")
        PerfToolProbeSelDialog.resize(790, 530)
        self.gridLayout = QGridLayout(PerfToolProbeSelDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_probes = QTableWidget(PerfToolProbeSelDialog)
        if (self.tableWidget_probes.columnCount() < 5):
            self.tableWidget_probes.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_probes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_probes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_probes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_probes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_probes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_probes.setObjectName(u"tableWidget_probes")
        self.tableWidget_probes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_probes.setSortingEnabled(True)

        self.gridLayout.addWidget(self.tableWidget_probes, 3, 0, 1, 3)

        self.buttonBox = QDialogButtonBox(PerfToolProbeSelDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 2, 1, 1)

        self.groupBox = QGroupBox(PerfToolProbeSelDialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.groupBox.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_typeView = QRadioButton(self.groupBox)
        self.radioButton_typeView.setObjectName(u"radioButton_typeView")
        self.radioButton_typeView.setChecked(True)
        self.radioButton_typeView.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.radioButton_typeView)

        self.radioButton_hierView = QRadioButton(self.groupBox)
        self.radioButton_hierView.setObjectName(u"radioButton_hierView")

        self.verticalLayout.addWidget(self.radioButton_hierView)

        self.radioButton_nameView = QRadioButton(self.groupBox)
        self.radioButton_nameView.setObjectName(u"radioButton_nameView")

        self.verticalLayout.addWidget(self.radioButton_nameView)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(PerfToolProbeSelDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout.addWidget(self.lineEdit_3)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout.addWidget(self.lineEdit_2)


        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 3)

        self.groupBox_3 = QGroupBox(PerfToolProbeSelDialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QSize(240, 100))
        self.groupBox_3.setMaximumSize(QSize(240, 100))
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_2 = QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_3, 0, 1, 1, 1)

        self.checkBox_4 = QCheckBox(self.groupBox_3)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_4, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(PerfToolProbeSelDialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_5 = QCheckBox(self.groupBox_4)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_3.addWidget(self.checkBox_5, 0, 0, 1, 1)

        self.checkBox_6 = QCheckBox(self.groupBox_4)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_3.addWidget(self.checkBox_6, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 0, 2, 1, 1)


        self.retranslateUi(PerfToolProbeSelDialog)
        self.buttonBox.accepted.connect(PerfToolProbeSelDialog.accept)
        self.buttonBox.rejected.connect(PerfToolProbeSelDialog.reject)

        QMetaObject.connectSlotsByName(PerfToolProbeSelDialog)
    # setupUi

    def retranslateUi(self, PerfToolProbeSelDialog):
        PerfToolProbeSelDialog.setWindowTitle(QCoreApplication.translate("PerfToolProbeSelDialog", u"Dialog", None))
        ___qtablewidgetitem = self.tableWidget_probes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"Type", None));
        ___qtablewidgetitem1 = self.tableWidget_probes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"Hier", None));
        ___qtablewidgetitem2 = self.tableWidget_probes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"Name", None));
        ___qtablewidgetitem3 = self.tableWidget_probes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"Enabled", None));
        ___qtablewidgetitem4 = self.tableWidget_probes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"Unit", None));
        self.groupBox.setTitle(QCoreApplication.translate("PerfToolProbeSelDialog", u"Sort by", None))
        self.radioButton_typeView.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"Perf Type", None))
        self.radioButton_hierView.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"Hierarchy", None))
        self.radioButton_nameView.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"Name", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PerfToolProbeSelDialog", u"Regular Expression", None))
        self.label_2.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"Hierarchy", None))
        self.lineEdit_3.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"*", None))
        self.label_3.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"Name", None))
        self.lineEdit_2.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"*", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("PerfToolProbeSelDialog", u"Type Selection", None))
        self.checkBox_2.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"utilization", None))
        self.checkBox.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"bandwidth", None))
        self.checkBox_3.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"latency", None))
        self.checkBox_4.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"backpressure", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("PerfToolProbeSelDialog", u"Misc", None))
        self.checkBox_5.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"display disabled probes", None))
        self.checkBox_6.setText(QCoreApplication.translate("PerfToolProbeSelDialog", u"display probes without messages", None))
    # retranslateUi

