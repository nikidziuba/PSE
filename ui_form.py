# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(273, 333)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(273, 260))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setWindowTitle(u"PSE")
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/*\n"
"Material Dark Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Inspired on https://github.com/jxfwinter/qt-material-stylesheet\n"
"Company: GTRONICK\n"
"Last updated: 04/12/2018, 15:00.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/MaterialDark.qss\n"
"*/\n"
"QMainWindow {\n"
"	background-color:#1e1d23;\n"
"}\n"
"QDialog {\n"
"	background-color:#1e1d23;\n"
"}\n"
"QColorDialog {\n"
"	background-color:#1e1d23;\n"
"}\n"
"QTextEdit {\n"
"	background-color:#1e1d23;\n"
"	color: #a9b7c6;\n"
"}\n"
"QPlainTextEdit {\n"
"	selection-background-color:#007b50;\n"
"	background-color:#1e1d23;\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-width: 1px;\n"
"	color: #a9b7c6;\n"
"}\n"
"QPushButton{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-botto"
                        "m-color: transparent;\n"
"	border-width: 2px;\n"
"	border-style: solid;\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QPushButton::default{\n"
"	border-style: inset;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #04b97f;\n"
"	border-width: 1px;\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolButton {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #04b97f;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #37efba;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid"
                        ";\n"
"	color: #FFFFFF;\n"
"	padding-bottom: 1px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #37efba;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-bottom: 2px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QPushButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #37efba;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #37efba;\n"
"	padding-bottom: 1px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #808086;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	co"
                        "lor: #808086;\n"
"	padding-bottom: 1px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QLineEdit {\n"
"	border-width: 1px; border-radius: 4px;\n"
"	border-color: rgb(58, 58, 58);\n"
"	border-style: inset;\n"
"	padding: 0 8px;\n"
"	color: #a9b7c6;\n"
"	background:#1e1d23;\n"
"	selection-background-color:#007b50;\n"
"	selection-color: #FFFFFF;\n"
"}\n"
"QLabel {\n"
"	color: #a9b7c6;\n"
"}\n"
"QLCDNumber {\n"
"	color: #37e6b4;\n"
"}\n"
"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(240, 240, 240);\n"
"	border-width: 1px; \n"
"	border-radius: 10px;\n"
"	border-color: rgb(58, 58, 58);\n"
"	border-style: inset;\n"
"	background-color:#1e1d23;\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: #04b97f;\n"
"	border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"	background-color: #1e1d23;\n"
"}\n"
"QMenuBar::item {\n"
"	color: #a9b7c6;\n"
"  	spacing: 3px;\n"
"  	padding: 1px 4px;\n"
"  	background: #1e1d23;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  	background:#1e1d23;\n"
"	color: #FFFFFF;\n"
"}\n"
"QMenu::item:s"
                        "elected {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: #04b97f;\n"
"	border-bottom-color: transparent;\n"
"	border-left-width: 2px;\n"
"	color: #FFFFFF;\n"
"	padding-left:15px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QMenu::item {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #a9b7c6;\n"
"	padding-left:17px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QMenu{\n"
"	background-color:#1e1d23;\n"
"}\n"
"QTabWidget {\n"
"	color:rgb(0,0,0);\n"
"	background-color:#1e1d23;\n"
"}\n"
"QTabWidget::pane {\n"
"		border-color: rgb(77,77,77);\n"
"		background-color:#1e1d23;\n"
"		border-style: solid;\n"
"		border-"
                        "width: 1px;\n"
"    	border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #808086;\n"
"	padding: 3px;\n"
"	margin-left:3px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #04b97f;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-left: 3px;\n"
"	padding-bottom: 2px;\n"
"	margin-left:3px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border-radius:4px;"
                        "\n"
"	border-style:solid;\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-top: 1px;\n"
"	border-width:1px;\n"
"	border-color: rgb(87, 97, 106);\n"
"	background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: #04b97f;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"	color: #a9b7c6;\n"
"	background-color: #1e1d23;\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: #04b97f;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
""
                        "	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"	color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QDoubleSpinBox {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QTimeEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QDateTimeEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QDateEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QComboBox {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"	background: #1e1d23;\n"
"	color: #a9b7c6;\n"
"	selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"	selection-color: #FFFFFF;\n"
"	selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-do"
                        "wn:editable:on {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolBox {\n"
"	color: #a9b7c6;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab {\n"
"	color: #a9b7c6;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	color: #FFFFFF;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QScrollArea {\n"
"	color: #FFFFFF;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	background: #04b97f;\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	background: #04b97f;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"	border: 1px solid #5c5c5c;\n"
"	width: 14px;\n"
"	margin: -5px 0;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"	border: 1px solid #5c5c5c;\n"
"	height: 14"
                        "px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #04b97f;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bt_path = QToolButton(self.centralwidget)
        self.bt_path.setObjectName(u"bt_path")
        self.bt_path.setGeometry(QRect(10, 50, 251, 24))
        self.bt_path.setStyleSheet(u"border-bottom-color: rgb(83, 83, 83);")
        self.bt_exit = QToolButton(self.centralwidget)
        self.bt_exit.setObjectName(u"bt_exit")
        self.bt_exit.setGeometry(QRect(232, 0, 41, 31))
        self.bt_exit.setStyleSheet(u"border-bottom-color: rgb(152, 0, 3);")
        self.bt_min = QToolButton(self.centralwidget)
        self.bt_min.setObjectName(u"bt_min")
        self.bt_min.setGeometry(QRect(190, 0, 41, 31))
        self.bt_min.setStyleSheet(u"border-bottom-color: rgb(43, 115, 159)")
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(8, 5, 51, 21))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 15, 281, 31))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.bt_save = QPushButton(self.centralwidget)
        self.bt_save.setObjectName(u"bt_save")
        self.bt_save.setEnabled(False)
        self.bt_save.setGeometry(QRect(10, 300, 251, 23))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 80, 251, 211))
        self.tabWidget.setUsesScrollButtons(False)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.label_money = QLabel(self.tab_1)
        self.label_money.setObjectName(u"label_money")
        self.label_money.setGeometry(QRect(10, 10, 52, 16))
        sizePolicy.setHeightForWidth(self.label_money.sizePolicy().hasHeightForWidth())
        self.label_money.setSizePolicy(sizePolicy)
        self.label_money.setTextFormat(Qt.PlainText)
        self.label_money.setScaledContents(False)
        self.box_money = QSpinBox(self.tab_1)
        self.box_money.setObjectName(u"box_money")
        self.box_money.setEnabled(False)
        self.box_money.setGeometry(QRect(10, 30, 231, 24))
        self.box_money.setMaximum(999999999)
        self.label_level = QLabel(self.tab_1)
        self.label_level.setObjectName(u"label_level")
        self.label_level.setGeometry(QRect(10, 60, 42, 16))
        sizePolicy.setHeightForWidth(self.label_level.sizePolicy().hasHeightForWidth())
        self.label_level.setSizePolicy(sizePolicy)
        self.box_level = QSpinBox(self.tab_1)
        self.box_level.setObjectName(u"box_level")
        self.box_level.setEnabled(False)
        self.box_level.setGeometry(QRect(10, 80, 231, 24))
        self.box_level.setMinimum(1)
        self.box_level.setMaximum(15000)
        self.bt_save_main = QToolButton(self.tab_1)
        self.bt_save_main.setObjectName(u"bt_save_main")
        self.bt_save_main.setEnabled(False)
        self.bt_save_main.setGeometry(QRect(10, 150, 231, 23))
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.combo_key = QComboBox(self.tab_2)
        self.combo_key.setObjectName(u"combo_key")
        self.combo_key.setEnabled(False)
        self.combo_key.setGeometry(QRect(10, 30, 231, 24))
        self.label_key = QLabel(self.tab_2)
        self.label_key.setObjectName(u"label_key")
        self.label_key.setGeometry(QRect(10, 10, 49, 16))
        self.label_value = QLabel(self.tab_2)
        self.label_value.setObjectName(u"label_value")
        self.label_value.setGeometry(QRect(10, 60, 49, 16))
        self.te_value = QPlainTextEdit(self.tab_2)
        self.te_value.setObjectName(u"te_value")
        self.te_value.setEnabled(False)
        self.te_value.setGeometry(QRect(10, 80, 231, 70))
        self.label_risk1 = QLabel(self.tab_2)
        self.label_risk1.setObjectName(u"label_risk1")
        self.label_risk1.setGeometry(QRect(110, 0, 131, 41))
        self.bt_value_save = QToolButton(self.tab_2)
        self.bt_value_save.setObjectName(u"bt_value_save")
        self.bt_value_save.setEnabled(False)
        self.bt_value_save.setGeometry(QRect(12, 160, 231, 23))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.bt_editor = QToolButton(self.tab_3)
        self.bt_editor.setObjectName(u"bt_editor")
        self.bt_editor.setEnabled(False)
        self.bt_editor.setGeometry(QRect(20, 70, 211, 23))
        self.bt_load = QToolButton(self.tab_3)
        self.bt_load.setObjectName(u"bt_load")
        self.bt_load.setEnabled(False)
        self.bt_load.setGeometry(QRect(22, 140, 211, 23))
        self.label_risk2 = QLabel(self.tab_3)
        self.label_risk2.setObjectName(u"label_risk2")
        self.label_risk2.setGeometry(QRect(10, 10, 221, 51))
        self.label_risk2.setScaledContents(False)
        self.label_risk2.setAlignment(Qt.AlignCenter)
        self.label_risk2.setWordWrap(True)
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.line.raise_()
        self.bt_path.raise_()
        self.bt_exit.raise_()
        self.bt_min.raise_()
        self.label_title.raise_()
        self.bt_save.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(MainWindow)
        self.bt_min.clicked.connect(MainWindow.min_button_clicked)
        self.bt_exit.clicked.connect(MainWindow.exit_button_clicked)
        self.bt_path.clicked.connect(MainWindow.path_button_clicked)
        self.bt_save.clicked.connect(MainWindow.save_button_clicked)
        self.combo_key.currentTextChanged.connect(MainWindow.key_combo_changed)
        self.bt_value_save.clicked.connect(MainWindow.save_value_button_clicked)
        self.bt_editor.clicked.connect(MainWindow.edit_button_clicked)
        self.bt_load.clicked.connect(MainWindow.load_editor_button_clicked)
        self.bt_save_main.clicked.connect(MainWindow.save_main_button_clicked)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.bt_path.setText(QCoreApplication.translate("MainWindow", u"Choose Path", None))
        self.bt_exit.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.bt_min.setText(QCoreApplication.translate("MainWindow", u"\u2014", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"PSE", None))
        self.bt_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_money.setText(QCoreApplication.translate("MainWindow", u"Money:    ", None))
        self.label_level.setText(QCoreApplication.translate("MainWindow", u"Level:    ", None))
        self.bt_save_main.setText(QCoreApplication.translate("MainWindow", u"Save Values", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Main", None))
        self.label_key.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_value.setText(QCoreApplication.translate("MainWindow", u"Value:", None))
        self.label_risk1.setText(QCoreApplication.translate("MainWindow", u"Change at your own risk!", None))
        self.bt_value_save.setText(QCoreApplication.translate("MainWindow", u"Save Value", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"All", None))
        self.bt_editor.setText(QCoreApplication.translate("MainWindow", u"Open Decrypted File In Editor", None))
        self.bt_load.setText(QCoreApplication.translate("MainWindow", u"Load Data From Edited File", None))
        self.label_risk2.setText(QCoreApplication.translate("MainWindow", u"Warning!                                                            Has to be valid or will break your save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Editor", None))
        pass
    # retranslateUi

