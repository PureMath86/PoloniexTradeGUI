# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(871, 690)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1.png.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: orange;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"   /* border-color: #1e1e1e;*/\n"
"    border-color: orange;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d30, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252530)\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"   color: #b1b1b1;\n"
"\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lblMonero = QtWidgets.QLabel(self.centralWidget)
        self.lblMonero.setGeometry(QtCore.QRect(40, 622, 53, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblMonero.setFont(font)
        self.lblMonero.setObjectName("lblMonero")
        self.lblMoneroinclO = QtWidgets.QLabel(self.centralWidget)
        self.lblMoneroinclO.setGeometry(QtCore.QRect(200, 622, 164, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblMoneroinclO.setFont(font)
        self.lblMoneroinclO.setObjectName("lblMoneroinclO")
        self.lblBitcoin = QtWidgets.QLabel(self.centralWidget)
        self.lblBitcoin.setGeometry(QtCore.QRect(710, 622, 47, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblBitcoin.setFont(font)
        self.lblBitcoin.setObjectName("lblBitcoin")
        #self.lblEthereum = QtWidgets.QLabel(self.centralWidget)
        #self.lblEthereum.setGeometry(QtCore.QRect(360, 622, 65, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        #self.lblEthereum.setFont(font)
        #self.lblEthereum.setObjectName("lblEthereum")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 239, 791, 371))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 51, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 118, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(156, 143, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 51, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 118, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(156, 143, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 51, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 118, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(156, 143, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.OpenOrders = QtWidgets.QWidget()
        self.OpenOrders.setMinimumSize(QtCore.QSize(858, 0))
        self.OpenOrders.setMaximumSize(QtCore.QSize(600, 16777215))
        self.OpenOrders.setBaseSize(QtCore.QSize(0, 0))
        self.OpenOrders.setObjectName("OpenOrders")
        self.tabOO = QtWidgets.QTabWidget(self.OpenOrders)
        self.tabOO.setGeometry(QtCore.QRect(-1, -2, 801, 361))
        self.tabOO.setStyleSheet("")
        self.tabOO.setTabBarAutoHide(False)
        self.tabOO.setObjectName("tabOO")
        self.tabXMR = QtWidgets.QWidget()
        self.tabXMR.setObjectName("tabXMR")
        self.OpenOrdersWidgetXMR = QtWidgets.QTableWidget(self.tabXMR)
        self.OpenOrdersWidgetXMR.setEnabled(True)
        self.OpenOrdersWidgetXMR.setGeometry(QtCore.QRect(-2, 0, 791, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenOrdersWidgetXMR.sizePolicy().hasHeightForWidth())
        self.OpenOrdersWidgetXMR.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(77, 77, 77))
        gradient.setColorAt(0.1, QtGui.QColor(100, 100, 100))
        gradient.setColorAt(1.0, QtGui.QColor(93, 93, 93))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 101, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(77, 77, 77))
        gradient.setColorAt(0.1, QtGui.QColor(100, 100, 100))
        gradient.setColorAt(1.0, QtGui.QColor(93, 93, 93))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(77, 77, 77))
        gradient.setColorAt(0.1, QtGui.QColor(100, 100, 100))
        gradient.setColorAt(1.0, QtGui.QColor(93, 93, 93))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(77, 77, 77))
        gradient.setColorAt(0.1, QtGui.QColor(100, 100, 100))
        gradient.setColorAt(1.0, QtGui.QColor(93, 93, 93))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 101, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(77, 77, 77))
        gradient.setColorAt(0.1, QtGui.QColor(100, 100, 100))
        gradient.setColorAt(1.0, QtGui.QColor(93, 93, 93))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(77, 77, 77))
        gradient.setColorAt(0.1, QtGui.QColor(100, 100, 100))
        gradient.setColorAt(1.0, QtGui.QColor(93, 93, 93))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 101, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.OpenOrdersWidgetXMR.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.OpenOrdersWidgetXMR.setFont(font)
        self.OpenOrdersWidgetXMR.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.OpenOrdersWidgetXMR.setAutoFillBackground(True)
        self.OpenOrdersWidgetXMR.setStyleSheet("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 0px;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border-left-width:1 px;\n"
"     border-right-width: 1px ;\n"
"    border-bottom-width: 1px;\n"
"}")
        self.OpenOrdersWidgetXMR.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.OpenOrdersWidgetXMR.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.OpenOrdersWidgetXMR.setLineWidth(1)
        self.OpenOrdersWidgetXMR.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.OpenOrdersWidgetXMR.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.OpenOrdersWidgetXMR.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.OpenOrdersWidgetXMR.setAlternatingRowColors(False)
        self.OpenOrdersWidgetXMR.setTextElideMode(QtCore.Qt.ElideLeft)
        self.OpenOrdersWidgetXMR.setShowGrid(True)
        self.OpenOrdersWidgetXMR.setGridStyle(QtCore.Qt.DashLine)
        self.OpenOrdersWidgetXMR.setCornerButtonEnabled(False)
        self.OpenOrdersWidgetXMR.setRowCount(0)
        self.OpenOrdersWidgetXMR.setObjectName("OpenOrdersWidgetXMR")
        self.OpenOrdersWidgetXMR.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetXMR.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetXMR.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetXMR.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetXMR.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetXMR.setHorizontalHeaderItem(4, item)
        self.OpenOrdersWidgetXMR.horizontalHeader().setDefaultSectionSize(151)
        self.OpenOrdersWidgetXMR.horizontalHeader().setStretchLastSection(True)
        self.OpenOrdersWidgetXMR.verticalHeader().setVisible(False)
        self.OpenOrdersWidgetXMR.verticalHeader().setCascadingSectionResizes(False)
        self.OpenOrdersWidgetXMR.verticalHeader().setHighlightSections(True)
        self.OpenOrdersWidgetXMR.verticalHeader().setMinimumSectionSize(39)
        self.OpenOrdersWidgetXMR.verticalHeader().setStretchLastSection(False)
        self.tabOO.addTab(self.tabXMR, "")
        self.tabWidget.addTab(self.OpenOrders, "")
        self.History = QtWidgets.QWidget()
        self.History.setObjectName("History")
        self.tabHistory = QtWidgets.QTabWidget(self.History)
        self.tabHistory.setGeometry(QtCore.QRect(-1, -2, 790, 361))
        self.tabHistory.setStyleSheet("")
        self.tabHistory.setObjectName("tabHistory")
        self.tabXMR1 = QtWidgets.QWidget()
        self.tabXMR1.setObjectName("tabXMR1")
        self.HistoryWidgetXMR = QtWidgets.QTableWidget(self.tabXMR1)
        self.HistoryWidgetXMR.setGeometry(QtCore.QRect(-3, 0, 791, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HistoryWidgetXMR.sizePolicy().hasHeightForWidth())
        self.HistoryWidgetXMR.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.HistoryWidgetXMR.setFont(font)
        self.HistoryWidgetXMR.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.HistoryWidgetXMR.setAutoFillBackground(False)
        self.HistoryWidgetXMR.setStyleSheet("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 0px;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border-left-width:1 px;\n"
"     border-right-width: 1px ;\n"
"    border-bottom-width: 1px;\n"
"}")
        self.HistoryWidgetXMR.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HistoryWidgetXMR.setLineWidth(1)
        self.HistoryWidgetXMR.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.HistoryWidgetXMR.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.HistoryWidgetXMR.setShowGrid(True)
        self.HistoryWidgetXMR.setGridStyle(QtCore.Qt.DashLine)
        self.HistoryWidgetXMR.setCornerButtonEnabled(True)
        self.HistoryWidgetXMR.setRowCount(0)
        self.HistoryWidgetXMR.setObjectName("HistoryWidgetXMR")
        self.HistoryWidgetXMR.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetXMR.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetXMR.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetXMR.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetXMR.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetXMR.setHorizontalHeaderItem(4, item)
        self.HistoryWidgetXMR.horizontalHeader().setDefaultSectionSize(151)
        self.HistoryWidgetXMR.horizontalHeader().setSortIndicatorShown(True)
        self.HistoryWidgetXMR.horizontalHeader().setStretchLastSection(True)
        self.HistoryWidgetXMR.verticalHeader().setVisible(False)
        self.tabHistory.addTab(self.tabXMR1, "")
        self.tabWidget.addTab(self.History, "")
        self.Trading = QtWidgets.QWidget()
        self.Trading.setObjectName("Trading")
        self.tabTrading = QtWidgets.QTabWidget(self.Trading)
        self.tabTrading.setGeometry(QtCore.QRect(-1, -2, 791, 361))
        self.tabTrading.setStyleSheet("")
        self.tabTrading.setObjectName("tabTrading")
        self.tabXMR2 = QtWidgets.QWidget()
        self.tabXMR2.setObjectName("tabXMR2")
        self.sellButton = QtWidgets.QPushButton(self.tabXMR2)
        self.sellButton.setGeometry(QtCore.QRect(540, 260, 93, 28))
        self.sellButton.setStyleSheet("")
        self.sellButton.setObjectName("sellButton")
        self.layoutWidget = QtWidgets.QWidget(self.tabXMR2)
        self.layoutWidget.setGeometry(QtCore.QRect(32, 30, 101, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblBuy = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblBuy.setFont(font)
        self.lblBuy.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblBuy.setObjectName("lblBuy")
        self.verticalLayout_3.addWidget(self.lblBuy)
        self.lblBuyPrice = QtWidgets.QLabel(self.layoutWidget)
        self.lblBuyPrice.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblBuyPrice.setObjectName("lblBuyPrice")
        self.verticalLayout_3.addWidget(self.lblBuyPrice)
        self.lblBuyAmount = QtWidgets.QLabel(self.layoutWidget)
        self.lblBuyAmount.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblBuyAmount.setObjectName("lblBuyAmount")
        self.verticalLayout_3.addWidget(self.lblBuyAmount)
        self.lblBuyTotal = QtWidgets.QLabel(self.layoutWidget)
        self.lblBuyTotal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblBuyTotal.setObjectName("lblBuyTotal")
        self.verticalLayout_3.addWidget(self.lblBuyTotal)
        self.layoutWidget1 = QtWidgets.QWidget(self.tabXMR2)
        self.layoutWidget1.setGeometry(QtCore.QRect(142, 52, 139, 85))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lnBuyPrice = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lnBuyPrice.setClearButtonEnabled(False)
        self.lnBuyPrice.setObjectName("lnBuyPrice")
        self.verticalLayout_6.addWidget(self.lnBuyPrice)
        self.lnBuyAmount = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lnBuyAmount.setObjectName("lnBuyAmount")
        self.verticalLayout_6.addWidget(self.lnBuyAmount)
        self.lnBuyTotal = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lnBuyTotal.setObjectName("lnBuyTotal")
        self.verticalLayout_6.addWidget(self.lnBuyTotal)
        self.layoutWidget2 = QtWidgets.QWidget(self.tabXMR2)
        self.layoutWidget2.setGeometry(QtCore.QRect(382, 30, 101, 101))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lblSell = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblSell.setFont(font)
        self.lblSell.setObjectName("lblSell")
        self.verticalLayout_5.addWidget(self.lblSell)
        self.lblSellPrice = QtWidgets.QLabel(self.layoutWidget2)
        self.lblSellPrice.setObjectName("lblSellPrice")
        self.verticalLayout_5.addWidget(self.lblSellPrice)
        self.lblSellAmount = QtWidgets.QLabel(self.layoutWidget2)
        self.lblSellAmount.setObjectName("lblSellAmount")
        self.verticalLayout_5.addWidget(self.lblSellAmount)
        self.lblSellTotal = QtWidgets.QLabel(self.layoutWidget2)
        self.lblSellTotal.setObjectName("lblSellTotal")
        self.verticalLayout_5.addWidget(self.lblSellTotal)
        self.layoutWidget3 = QtWidgets.QWidget(self.tabXMR2)
        self.layoutWidget3.setGeometry(QtCore.QRect(492, 52, 139, 85))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lnSellPrice = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lnSellPrice.setObjectName("lnSellPrice")
        self.verticalLayout_7.addWidget(self.lnSellPrice)
        self.lnSellAmount = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lnSellAmount.setObjectName("lnSellAmount")
        self.verticalLayout_7.addWidget(self.lnSellAmount)
        self.lnSellTotal = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lnSellTotal.setObjectName("lnSellTotal")
        self.verticalLayout_7.addWidget(self.lnSellTotal)
        self.btnSellGetBTCPrice = QtWidgets.QPushButton(self.tabXMR2)
        self.btnSellGetBTCPrice.setGeometry(QtCore.QRect(642, 55, 21, 21))
        self.btnSellGetBTCPrice.setStyleSheet("")
        self.btnSellGetBTCPrice.setFlat(False)
        self.btnSellGetBTCPrice.setObjectName("btnSellGetBTCPrice")
        self.btnBuyGetBTCTotal = QtWidgets.QPushButton(self.tabXMR2)
        self.btnBuyGetBTCTotal.setGeometry(QtCore.QRect(292, 115, 21, 21))
        self.btnBuyGetBTCTotal.setStyleSheet("")
        self.btnBuyGetBTCTotal.setObjectName("btnBuyGetBTCTotal")
        self.buyButton = QtWidgets.QPushButton(self.tabXMR2)
        self.buyButton.setGeometry(QtCore.QRect(190, 260, 93, 28))
        self.buyButton.setStyleSheet("")
        self.buyButton.setObjectName("buyButton")
        self.tabTrading.addTab(self.tabXMR2, "")
        self.tabWidget.addTab(self.Trading, "")
        self.tabConfiguration = QtWidgets.QWidget()
        self.tabConfiguration.setObjectName("tabConfiguration")
        self.saveButton = QtWidgets.QPushButton(self.tabConfiguration)
        self.saveButton.setGeometry(QtCore.QRect(590, 139, 93, 28))
        self.saveButton.setStyleSheet("")
        self.saveButton.setDefault(False)
        self.saveButton.setFlat(False)
        self.saveButton.setObjectName("saveButton")
        self.layoutWidget4 = QtWidgets.QWidget(self.tabConfiguration)
        self.layoutWidget4.setGeometry(QtCore.QRect(30, 49, 91, 66))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lblPoloniex = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPoloniex.setFont(font)
        self.lblPoloniex.setObjectName("lblPoloniex")
        self.verticalLayout_8.addWidget(self.lblPoloniex)
        self.lblPublicKey = QtWidgets.QLabel(self.layoutWidget4)
        self.lblPublicKey.setObjectName("lblPublicKey")
        self.verticalLayout_8.addWidget(self.lblPublicKey)
        self.lblSecretKey = QtWidgets.QLabel(self.layoutWidget4)
        self.lblSecretKey.setObjectName("lblSecretKey")
        self.verticalLayout_8.addWidget(self.lblSecretKey)
        self.layoutWidget5 = QtWidgets.QWidget(self.tabConfiguration)
        self.layoutWidget5.setGeometry(QtCore.QRect(150, 69, 531, 55))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lnPublicKey = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lnPublicKey.setObjectName("lnPublicKey")
        self.verticalLayout_9.addWidget(self.lnPublicKey)
        self.lnSecretKey = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lnSecretKey.setObjectName("lnSecretKey")
        self.verticalLayout_9.addWidget(self.lnSecretKey)
        self.lblrestartkey = QtWidgets.QLabel(self.tabConfiguration)
        self.lblrestartkey.setGeometry(QtCore.QRect(30, 179, 501, 16))
        self.lblrestartkey.setObjectName("lblrestartkey")
        self.tabWidget.addTab(self.tabConfiguration, "")
        self.layoutWidget6 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(40, 60, 95, 141))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.layoutWidget6.setFont(font)
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblPriceBTC = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblPriceBTC.setFont(font)
        self.lblPriceBTC.setObjectName("lblPriceBTC")
        self.verticalLayout.addWidget(self.lblPriceBTC)
        self.lblPriceUSD = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblPriceUSD.setFont(font)
        self.lblPriceUSD.setObjectName("lblPriceUSD")
        self.verticalLayout.addWidget(self.lblPriceUSD)
        self.lblHigh = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblHigh.setFont(font)
        self.lblHigh.setObjectName("lblHigh")
        self.verticalLayout.addWidget(self.lblHigh)
        self.lblLow = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblLow.setFont(font)
        self.lblLow.setObjectName("lblLow")
        self.verticalLayout.addWidget(self.lblLow)
        self.lblChange = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblChange.setFont(font)
        self.lblChange.setScaledContents(True)
        self.lblChange.setObjectName("lblChange")
        self.verticalLayout.addWidget(self.lblChange)
        #self.lblEthereuminclO = QtWidgets.QLabel(self.centralWidget)
        #self.lblEthereuminclO.setGeometry(QtCore.QRect(520, 622, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        #self.lblEthereuminclO.setFont(font)
        #self.lblEthereuminclO.setObjectName("lblEthereuminclO")
        self.lblMonerox = QtWidgets.QLabel(self.centralWidget)
        self.lblMonerox.setGeometry(QtCore.QRect(140, 38, 91, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lblMonerox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.lblMonerox.setFont(font)
        self.lblMonerox.setAutoFillBackground(False)
        self.lblMonerox.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: rgb(239, 132, 45);\n"
"}")
        self.lblMonerox.setTextFormat(QtCore.Qt.AutoText)
        self.lblMonerox.setScaledContents(False)
        self.lblMonerox.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMonerox.setObjectName("lblMonerox")
        self.layoutWidget7 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget7.setGeometry(QtCore.QRect(140, 61, 91, 140))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lnPriceXMR = QtWidgets.QLineEdit(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lnPriceXMR.setFont(font)
        self.lnPriceXMR.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"")
        self.lnPriceXMR.setFrame(False)
        self.lnPriceXMR.setClearButtonEnabled(False)
        self.lnPriceXMR.setObjectName("lnPriceXMR")
        self.verticalLayout_2.addWidget(self.lnPriceXMR)
        self.lnPriceUSD = QtWidgets.QLineEdit(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.lnPriceUSD.setFont(font)
        self.lnPriceUSD.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"")
        self.lnPriceUSD.setFrame(False)
        self.lnPriceUSD.setObjectName("lnPriceUSD")
        self.verticalLayout_2.addWidget(self.lnPriceUSD)
        self.lnHigh = QtWidgets.QLineEdit(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.lnHigh.setFont(font)
        self.lnHigh.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgrey;\n"
"    color: rgb(136, 136, 136);\n"
"}")
        self.lnHigh.setFrame(False)
        self.lnHigh.setObjectName("lnHigh")
        self.verticalLayout_2.addWidget(self.lnHigh)
        self.lnLow = QtWidgets.QLineEdit(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.lnLow.setFont(font)
        self.lnLow.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgrey;\n"
"    color: rgb(136, 136, 136);\n"
"}")
        self.lnLow.setFrame(False)
        self.lnLow.setObjectName("lnLow")
        self.verticalLayout_2.addWidget(self.lnLow)
        self.lnChange = QtWidgets.QLineEdit(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.lnChange.setFont(font)
        self.lnChange.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgrey;\n"
"    color: rgb(136, 136, 136);\n"
"}")
        self.lnChange.setFrame(False)
        self.lnChange.setObjectName("lnChange")
        self.verticalLayout_2.addWidget(self.lnChange)
        #self.lcdEthereum = QtWidgets.QLCDNumber(self.centralWidget)
        #self.lcdEthereum.setGeometry(QtCore.QRect(310, 639, 141, 21))
        #self.lcdEthereum.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        #self.lcdEthereum.setPalette(palette)
        #self.lcdEthereum.setAutoFillBackground(False)
        #self.lcdEthereum.setStyleSheet("QLCDNumber {\n"
#"    color: rgb(216, 32, 32);\n"
#"}")
 #       self.lcdEthereum.setFrameShape(QtWidgets.QFrame.NoFrame)
  #      self.lcdEthereum.setDigitCount(15)
   #     self.lcdEthereum.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
    #    self.lcdEthereum.setObjectName("lcdEthereum")
        self.lcdMonero = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdMonero.setGeometry(QtCore.QRect(13, 639, 141, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMonero.sizePolicy().hasHeightForWidth())
        self.lcdMonero.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 27, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 27, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 27, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lcdMonero.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.lcdMonero.setFont(font)
        self.lcdMonero.setAutoFillBackground(False)
        self.lcdMonero.setStyleSheet("QLCDNumber {\n"
"    color: rgb(216, 32, 32);\n"
"}")
        self.lcdMonero.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdMonero.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdMonero.setLineWidth(1)
        self.lcdMonero.setSmallDecimalPoint(False)
        self.lcdMonero.setDigitCount(15)
        self.lcdMonero.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdMonero.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdMonero.setObjectName("lcdMonero")
        #self.lcdEthereuminclO = QtWidgets.QLCDNumber(self.centralWidget)
        #self.lcdEthereuminclO.setGeometry(QtCore.QRect(470, 639, 141, 21))
        #self.lcdEthereuminclO.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        #self.lcdEthereuminclO.setPalette(palette)
        #self.lcdEthereuminclO.setAutoFillBackground(False)
        #self.lcdEthereuminclO.setStyleSheet("QLCDNumber {\n"
#"    color: rgb(216, 32, 32);\n"
#"}")
#        self.lcdEthereuminclO.setFrameShape(QtWidgets.QFrame.NoFrame)
#        self.lcdEthereuminclO.setDigitCount(15)
 #       self.lcdEthereuminclO.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
 #       self.lcdEthereuminclO.setObjectName("lcdEthereuminclO")
        self.lcdBitcoin = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdBitcoin.setGeometry(QtCore.QRect(660, 639, 141, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lcdBitcoin.setPalette(palette)
        self.lcdBitcoin.setAutoFillBackground(False)
        self.lcdBitcoin.setStyleSheet("QLCDNumber {\n"
"    color: rgb(216, 32, 32);\n"
"}")
        self.lcdBitcoin.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdBitcoin.setDigitCount(15)
        self.lcdBitcoin.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdBitcoin.setObjectName("lcdBitcoin")
        self.lcdMoneroinclO = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdMoneroinclO.setGeometry(QtCore.QRect(174, 639, 141, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lcdMoneroinclO.setPalette(palette)
        self.lcdMoneroinclO.setAutoFillBackground(False)
        self.lcdMoneroinclO.setStyleSheet("QLCDNumber {\n"
"    color: rgb(216, 32, 32);\n"
"}")
        self.lcdMoneroinclO.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdMoneroinclO.setDigitCount(15)
        self.lcdMoneroinclO.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdMoneroinclO.setObjectName("lcdMoneroinclO")
        self.lblBitcoinx = QtWidgets.QLabel(self.centralWidget)
        self.lblBitcoinx.setGeometry(QtCore.QRect(250, 40, 91, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lblBitcoinx.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.lblBitcoinx.setFont(font)
        self.lblBitcoinx.setAutoFillBackground(False)
        self.lblBitcoinx.setStyleSheet("QLabel{\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: gold;\n"
"}")
        self.lblBitcoinx.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBitcoinx.setWordWrap(False)
        self.lblBitcoinx.setContentsMargins(0, 0, 0, 0)
        self.lblBitcoinx.setObjectName("lblBitcoinx")
        self.layoutWidget8 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget8.setGeometry(QtCore.QRect(250, 92, 91, 22))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.lnBTCPriceUSD = QtWidgets.QLineEdit(self.layoutWidget8)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.lnBTCPriceUSD.setFont(font)
        self.lnBTCPriceUSD.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"")
        self.lnBTCPriceUSD.setFrame(False)
        self.lnBTCPriceUSD.setObjectName("lnBTCPriceUSD")
        self.verticalLayout_16.addWidget(self.lnBTCPriceUSD)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(662, 180, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lnMyAssets = QtWidgets.QLineEdit(self.centralWidget)
        self.lnMyAssets.setGeometry(QtCore.QRect(662, 202, 89, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lnMyAssets.setFont(font)
        self.lnMyAssets.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"")
        self.lnMyAssets.setText("")
        self.lnMyAssets.setFrame(False)
        self.lnMyAssets.setAlignment(QtCore.Qt.AlignCenter)
        self.lnMyAssets.setClearButtonEnabled(False)
        self.lnMyAssets.setObjectName("lnMyAssets")
        self.lbldescAssets = QtWidgets.QLabel(self.centralWidget)
        self.lbldescAssets.setGeometry(QtCore.QRect(660, 230, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(7)
        font.setItalic(True)
        self.lbldescAssets.setFont(font)
        self.lbldescAssets.setObjectName("lbldescAssets")
        self.lblPoloniexStatus = QtWidgets.QLabel(self.centralWidget)
        self.lblPoloniexStatus.setGeometry(QtCore.QRect(660, 30, 69, 29))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lblPoloniexStatus.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblPoloniexStatus.setFont(font)
        self.lblPoloniexStatus.setAutoFillBackground(False)
        self.lblPoloniexStatus.setObjectName("lblPoloniexStatus")
        self.lblPoloniexStatusResult = QtWidgets.QLabel(self.centralWidget)
        self.lblPoloniexStatusResult.setGeometry(QtCore.QRect(730, 30, 89, 29))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.lblPoloniexStatusResult.setFont(font)
        self.lblPoloniexStatusResult.setObjectName("lblPoloniexStatusResult")
        self.buttonChart = QtWidgets.QPushButton(self.centralWidget)
        self.buttonChart.setGeometry(QtCore.QRect(660, 90, 101, 23))
        self.buttonChart.setObjectName("buttonChart")
        self.btnRefresh = QtWidgets.QPushButton(self.centralWidget)
        self.btnRefresh.setGeometry(QtCore.QRect(380, 180, 61, 31))
        self.btnRefresh.setShortcut("")
        self.btnRefresh.setObjectName("btnRefresh")
        self.GprogressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.GprogressBar.setGeometry(QtCore.QRect(450, 180, 131, 31))
        self.GprogressBar.setProperty("value", 0)
        self.GprogressBar.setInvertedAppearance(False)
        self.GprogressBar.setObjectName("GprogressBar")
        MainWindow.setCentralWidget(self.centralWidget)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionSettings.setObjectName("actionSettings")
        self.actionLog = QtWidgets.QAction(MainWindow)
        self.actionLog.setObjectName("actionLog")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabOO.setCurrentIndex(0)
        self.tabHistory.setCurrentIndex(0)
        self.tabTrading.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblMonero.setText(_translate("MainWindow", "Monero"))
        self.lblMoneroinclO.setText(_translate("MainWindow", "Monero incl. OO"))
        self.lblBitcoin.setText(_translate("MainWindow", "Bitcoin"))
        #self.lblEthereum.setText(_translate("MainWindow", "Ethereum"))
        item = self.OpenOrdersWidgetXMR.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Order Number"))
        item = self.OpenOrdersWidgetXMR.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.OpenOrdersWidgetXMR.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price (BTC)"))
        item = self.OpenOrdersWidgetXMR.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SAmount (XMR)"))
        item = self.OpenOrdersWidgetXMR.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Amount (XMR)"))
        self.tabOO.setTabText(self.tabOO.indexOf(self.tabXMR), _translate("MainWindow", "XMR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OpenOrders), _translate("MainWindow", "Open Orders"))
        item = self.HistoryWidgetXMR.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Currency"))
        item = self.HistoryWidgetXMR.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.HistoryWidgetXMR.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.HistoryWidgetXMR.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.HistoryWidgetXMR.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date"))
        self.tabHistory.setTabText(self.tabHistory.indexOf(self.tabXMR1), _translate("MainWindow", "XMR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.History), _translate("MainWindow", "History"))
        self.sellButton.setText(_translate("MainWindow", "Sell"))
        self.lblBuy.setText(_translate("MainWindow", "Buy"))
        self.lblBuyPrice.setText(_translate("MainWindow", "Price (BTC):"))
        self.lblBuyAmount.setText(_translate("MainWindow", "Amount (XMR):"))
        self.lblBuyTotal.setText(_translate("MainWindow", "Total (BTC)"))
        self.lblSell.setText(_translate("MainWindow", "Sell"))
        self.lblSellPrice.setText(_translate("MainWindow", "Price (BTC):"))
        self.lblSellAmount.setText(_translate("MainWindow", "Amount (XMR):"))
        self.lblSellTotal.setText(_translate("MainWindow", "Total (BTC):"))
        self.btnSellGetBTCPrice.setText(_translate("MainWindow", "A"))
        self.btnBuyGetBTCTotal.setText(_translate("MainWindow", "A"))
        self.buyButton.setText(_translate("MainWindow", "Buy"))
        self.tabTrading.setTabText(self.tabTrading.indexOf(self.tabXMR2), _translate("MainWindow", "XMR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Trading), _translate("MainWindow", "Trading"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.lblPoloniex.setText(_translate("MainWindow", "Poloniex"))
        self.lblPublicKey.setText(_translate("MainWindow", "Public Key:"))
        self.lblSecretKey.setText(_translate("MainWindow", "Secret Key:"))
        self.lblrestartkey.setText(_translate("MainWindow", "Restart the application to activate the saved keys."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfiguration), _translate("MainWindow", "Configuration"))
        self.lblPriceBTC.setText(_translate("MainWindow", "Price (BTC):"))
        self.lblPriceUSD.setText(_translate("MainWindow", "Price (USD):"))
        self.lblHigh.setText(_translate("MainWindow", "24h High:"))
        self.lblLow.setText(_translate("MainWindow", "24h Low:"))
        self.lblChange.setText(_translate("MainWindow", "24h Change:"))
        #self.lblEthereuminclO.setText(_translate("MainWindow", "Ethereum incl. OO"))
        self.lblMonerox.setText(_translate("MainWindow", "Monero"))
        self.lblBitcoinx.setText(_translate("MainWindow", "Bitcoin"))
        self.label_2.setText(_translate("MainWindow", "My Assets (USD):"))
        self.lbldescAssets.setText(_translate("MainWindow", "Monero+Bitcoin"))
        self.lblPoloniexStatus.setText(_translate("MainWindow", "Poloniex:"))
        self.lblPoloniexStatusResult.setText(_translate("MainWindow", "checking.."))
        self.buttonChart.setText(_translate("MainWindow", "XMR/BTC Chart"))
        self.btnRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionLog.setText(_translate("MainWindow", "Log"))

