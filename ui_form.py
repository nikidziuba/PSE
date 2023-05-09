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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(273, 260)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(273, 260))
        MainWindow.setMaximumSize(QSize(273, 260))
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
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 99, 251, 161))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_money = QLabel(self.verticalLayoutWidget)
        self.label_money.setObjectName(u"label_money")
        sizePolicy.setHeightForWidth(self.label_money.sizePolicy().hasHeightForWidth())
        self.label_money.setSizePolicy(sizePolicy)
        self.label_money.setTextFormat(Qt.PlainText)
        self.label_money.setScaledContents(False)

        self.verticalLayout.addWidget(self.label_money)

        self.box_money = QSpinBox(self.verticalLayoutWidget)
        self.box_money.setObjectName(u"box_money")
        self.box_money.setEnabled(False)
        self.box_money.setMaximum(999999999)

        self.verticalLayout.addWidget(self.box_money)

        self.label_level = QLabel(self.verticalLayoutWidget)
        self.label_level.setObjectName(u"label_level")
        sizePolicy.setHeightForWidth(self.label_level.sizePolicy().hasHeightForWidth())
        self.label_level.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_level)

        self.box_level = QSpinBox(self.verticalLayoutWidget)
        self.box_level.setObjectName(u"box_level")
        self.box_level.setEnabled(False)
        self.box_level.setMinimum(1)
        self.box_level.setMaximum(15000)

        self.verticalLayout.addWidget(self.box_level)

        self.bt_save = QPushButton(self.verticalLayoutWidget)
        self.bt_save.setObjectName(u"bt_save")
        self.bt_save.setEnabled(False)

        self.verticalLayout.addWidget(self.bt_save)

        self.label_filename = QLabel(self.centralwidget)
        self.label_filename.setObjectName(u"label_filename")
        self.label_filename.setEnabled(True)
        self.label_filename.setGeometry(QRect(0, 80, 271, 16))
        self.label_filename.setAlignment(Qt.AlignCenter)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.line.raise_()
        self.bt_path.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_filename.raise_()
        self.bt_exit.raise_()
        self.bt_min.raise_()
        self.label_title.raise_()

        self.retranslateUi(MainWindow)
        self.bt_save.clicked.connect(MainWindow.save_button_clicked)
        self.bt_min.clicked.connect(MainWindow.min_button_clicked)
        self.bt_exit.clicked.connect(MainWindow.exit_button_clicked)
        self.bt_path.clicked.connect(MainWindow.path_button_clicked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.bt_path.setText(QCoreApplication.translate("MainWindow", u"Choose Path", None))
        self.label_money.setText(QCoreApplication.translate("MainWindow", u"Money:    ", None))
        self.label_level.setText(QCoreApplication.translate("MainWindow", u"Level:    ", None))
        self.bt_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_filename.setText("")
        self.bt_exit.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.bt_min.setText(QCoreApplication.translate("MainWindow", u"\u2014", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"PSE", None))
        pass
    # retranslateUi

