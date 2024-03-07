# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'perf_tool.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(980, 686)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionLoad_Report_File = QAction(MainWindow)
        self.actionLoad_Report_File.setObjectName(u"actionLoad_Report_File")
        self.actionLoad_Cfg_File = QAction(MainWindow)
        self.actionLoad_Cfg_File.setObjectName(u"actionLoad_Cfg_File")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSave_Cfg_File = QAction(MainWindow)
        self.actionSave_Cfg_File.setObjectName(u"actionSave_Cfg_File")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(10)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setIconSize(QSize(40, 40))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.probes = QWidget()
        self.probes.setObjectName(u"probes")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.probes.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.probes)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.plot_button = QPushButton(self.probes)
        self.plot_button.setObjectName(u"plot_button")

        self.gridLayout_3.addWidget(self.plot_button, 1, 3, 1, 1)

        self.frame = QFrame(self.probes)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.tableWidget_probes = QTableWidget(self.frame)
        if (self.tableWidget_probes.columnCount() < 4):
            self.tableWidget_probes.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_probes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_probes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_probes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_probes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_probes.setObjectName(u"tableWidget_probes")
        self.tableWidget_probes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_probes.setSortingEnabled(True)

        self.gridLayout.addWidget(self.tableWidget_probes, 0, 0, 1, 4)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 2, 0, 1, 3)

        self.groupBox = QGroupBox(self.probes)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_typeView = QRadioButton(self.groupBox)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_typeView)
        self.radioButton_typeView.setObjectName(u"radioButton_typeView")
        self.radioButton_typeView.setChecked(True)
        self.radioButton_typeView.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.radioButton_typeView)

        self.radioButton_hierView = QRadioButton(self.groupBox)
        self.buttonGroup.addButton(self.radioButton_hierView)
        self.radioButton_hierView.setObjectName(u"radioButton_hierView")

        self.horizontalLayout.addWidget(self.radioButton_hierView)

        self.radioButton_nameView = QRadioButton(self.groupBox)
        self.buttonGroup.addButton(self.radioButton_nameView)
        self.radioButton_nameView.setObjectName(u"radioButton_nameView")

        self.horizontalLayout.addWidget(self.radioButton_nameView)


        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 3)

        self.groupBox_2 = QGroupBox(self.probes)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_timescale = QLineEdit(self.groupBox_2)
        self.lineEdit_timescale.setObjectName(u"lineEdit_timescale")
        sizePolicy1.setHeightForWidth(self.lineEdit_timescale.sizePolicy().hasHeightForWidth())
        self.lineEdit_timescale.setSizePolicy(sizePolicy1)
        self.lineEdit_timescale.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_timescale.setInputMask(u"")
        self.lineEdit_timescale.setMaxLength(32767)
        self.lineEdit_timescale.setFrame(True)
        self.lineEdit_timescale.setEchoMode(QLineEdit.Normal)
        self.lineEdit_timescale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_timescale.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.lineEdit_timescale)

        self.comboBox_timescale = QComboBox(self.groupBox_2)
        self.comboBox_timescale.addItem("")
        self.comboBox_timescale.addItem("")
        self.comboBox_timescale.addItem("")
        self.comboBox_timescale.addItem("")
        self.comboBox_timescale.addItem("")
        self.comboBox_timescale.setObjectName(u"comboBox_timescale")
        sizePolicy1.setHeightForWidth(self.comboBox_timescale.sizePolicy().hasHeightForWidth())
        self.comboBox_timescale.setSizePolicy(sizePolicy1)
        self.comboBox_timescale.setEditable(False)
        self.comboBox_timescale.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_timescale.setDuplicatesEnabled(True)
        self.comboBox_timescale.setFrame(True)
        self.comboBox_timescale.setModelColumn(0)

        self.horizontalLayout_2.addWidget(self.comboBox_timescale)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.probes, "")
        self.plot = QWidget()
        self.plot.setObjectName(u"plot")
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(9)
        font2.setBold(False)
        self.plot.setFont(font2)
        self.gridLayout_2 = QGridLayout(self.plot)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.plot)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.plot)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.comboBox = QComboBox(self.plot)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 0, 2, 1, 1)

        self.label_3 = QLabel(self.plot)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.plot)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.plot)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_2.addWidget(self.comboBox_2, 1, 2, 1, 1)

        self.tabWidget.addTab(self.plot, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 980, 21))
        self.menubar.setNativeMenuBar(True)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.lineEdit)
        self.label_3.setBuddy(self.lineEdit_2)
#endif // QT_CONFIG(shortcut)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionLoad_Report_File)
        self.menuFile.addAction(self.actionLoad_Cfg_File)
        self.menuFile.addAction(self.actionSave_Cfg_File)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.comboBox_timescale.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Perf Report Tool", None))
        self.actionLoad_Report_File.setText(QCoreApplication.translate("MainWindow", u"Open Report File", None))
        self.actionLoad_Cfg_File.setText(QCoreApplication.translate("MainWindow", u"Open Cfg File", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSave_Cfg_File.setText(QCoreApplication.translate("MainWindow", u"Save Cfg File", None))
        self.plot_button.setText(QCoreApplication.translate("MainWindow", u"Plot !", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem = self.tableWidget_probes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem1 = self.tableWidget_probes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hier", None));
        ___qtablewidgetitem2 = self.tableWidget_probes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem3 = self.tableWidget_probes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Plot type", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sort by:", None))
        self.radioButton_typeView.setText(QCoreApplication.translate("MainWindow", u"Perf Type", None))
        self.radioButton_hierView.setText(QCoreApplication.translate("MainWindow", u"Hierarchy", None))
        self.radioButton_nameView.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Timescale", None))
        self.lineEdit_timescale.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1-1000", None))
        self.comboBox_timescale.setItemText(0, QCoreApplication.translate("MainWindow", u"fs", None))
        self.comboBox_timescale.setItemText(1, QCoreApplication.translate("MainWindow", u"ps", None))
        self.comboBox_timescale.setItemText(2, QCoreApplication.translate("MainWindow", u"ns", None))
        self.comboBox_timescale.setItemText(3, QCoreApplication.translate("MainWindow", u"us", None))
        self.comboBox_timescale.setItemText(4, QCoreApplication.translate("MainWindow", u"ms", None))

        self.comboBox_timescale.setCurrentText("")
        self.comboBox_timescale.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.probes), QCoreApplication.translate("MainWindow", u"Probes", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Time Starts:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Time Stops:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plot), QCoreApplication.translate("MainWindow", u"Plot", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

