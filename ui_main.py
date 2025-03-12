# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QTimeEdit, QWidget)
import rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 300)
        MainWindow.setMinimumSize(QSize(600, 300))
        MainWindow.setMaximumSize(QSize(600, 300))
        icon = QIcon()
        icon.addFile(u":/assets/logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background: #5B7065")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(600, 300))
        self.centralwidget.setMaximumSize(QSize(600, 300))
        self.btn_run = QPushButton(self.centralwidget)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setGeometry(QRect(30, 243, 540, 27))
        self.btn_run.setMinimumSize(QSize(540, 27))
        self.btn_run.setMaximumSize(QSize(540, 27))
        self.btn_run.setStyleSheet(u"QPushButton {\n"
"background-color: #304040;\n"
"color: #C9D1C8;\n"
"font-family: Inter;\n"
"font-size: 15px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #374A4A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #04202C;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: #03161F;\n"
"}\n"
"")
        self.timeEdit = QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(213, 126, 173, 48))
        self.timeEdit.setMinimumSize(QSize(173, 48))
        self.timeEdit.setMaximumSize(QSize(173, 48))
        self.timeEdit.setStyleSheet(u"QTimeEdit {\n"
"    font-family: Inter;\n"
"    font-size: 40px;\n"
"    font-weight: normal;\n"
"    color: #C9D1C8;\n"
"    background: transparent; \n"
"    border: none;\n"
"}\n"
"\n"
"QTimeEdit {\n"
"    border-radius: 5px; \n"
"}\n"
"\n"
"QTimeEdit::up-button, QTimeEdit::down-button {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"")
        self.btn_30sec = QPushButton(self.centralwidget)
        self.btn_30sec.setObjectName(u"btn_30sec")
        self.btn_30sec.setGeometry(QRect(140, 174, 100, 27))
        self.btn_30sec.setMinimumSize(QSize(100, 27))
        self.btn_30sec.setMaximumSize(QSize(100, 27))
        self.btn_30sec.setStyleSheet(u"QPushButton {\n"
"background-color: #304040;\n"
"color: #C9D1C8;\n"
"font-family: Inter;\n"
"font-size: 15px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #374A4A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #04202C;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: #03161F;\n"
"}\n"
"")
        self.btn_1min = QPushButton(self.centralwidget)
        self.btn_1min.setObjectName(u"btn_1min")
        self.btn_1min.setGeometry(QRect(250, 174, 100, 27))
        self.btn_1min.setMinimumSize(QSize(100, 27))
        self.btn_1min.setMaximumSize(QSize(100, 27))
        self.btn_1min.setStyleSheet(u"QPushButton {\n"
"background-color: #304040;\n"
"color: #C9D1C8;\n"
"font-family: Inter;\n"
"font-size: 15px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #374A4A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #04202C;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: #03161F;\n"
"}\n"
"")
        self.btn_5min = QPushButton(self.centralwidget)
        self.btn_5min.setObjectName(u"btn_5min")
        self.btn_5min.setGeometry(QRect(360, 174, 100, 27))
        self.btn_5min.setMinimumSize(QSize(100, 27))
        self.btn_5min.setMaximumSize(QSize(100, 27))
        self.btn_5min.setStyleSheet(u"QPushButton {\n"
"background-color: #304040;\n"
"color: #C9D1C8;\n"
"font-family: Inter;\n"
"font-size: 15px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #374A4A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #04202C;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: #03161F;\n"
"}\n"
"")
        self.btn_fun_volume = QPushButton(self.centralwidget)
        self.btn_fun_volume.setObjectName(u"btn_fun_volume")
        self.btn_fun_volume.setGeometry(QRect(30, 30, 100, 27))
        self.btn_fun_volume.setMinimumSize(QSize(100, 27))
        self.btn_fun_volume.setMaximumSize(QSize(100, 27))
        self.btn_fun_volume.setStyleSheet(u"QPushButton {\n"
"background-color: #304040;\n"
"color: #C9D1C8;\n"
"font-family: Inter;\n"
"font-size: 12px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #374A4A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #04202C;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: #03161F;\n"
"}\n"
"")
        self.btn_fun_lock = QPushButton(self.centralwidget)
        self.btn_fun_lock.setObjectName(u"btn_fun_lock")
        self.btn_fun_lock.setGeometry(QRect(250, 30, 100, 27))
        self.btn_fun_lock.setMinimumSize(QSize(100, 27))
        self.btn_fun_lock.setMaximumSize(QSize(100, 27))
        self.btn_fun_lock.setStyleSheet(u"QPushButton {\n"
"background-color: #304040;\n"
"color: #C9D1C8;\n"
"font-family: Inter;\n"
"font-size: 12px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #374A4A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #04202C;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: #03161F;\n"
"}\n"
"")
        self.btn_fun_power = QPushButton(self.centralwidget)
        self.btn_fun_power.setObjectName(u"btn_fun_power")
        self.btn_fun_power.setGeometry(QRect(470, 30, 100, 27))
        self.btn_fun_power.setMinimumSize(QSize(100, 27))
        self.btn_fun_power.setMaximumSize(QSize(100, 27))
        self.btn_fun_power.setStyleSheet(u"QPushButton {\n"
"background-color: #304040;\n"
"color: #C9D1C8;\n"
"font-family: Inter;\n"
"font-size: 12px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #374A4A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #04202C;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: #03161F;\n"
"}\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Smart Sleep Timer", None))
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm:ss", None))
        self.btn_30sec.setText(QCoreApplication.translate("MainWindow", u"+30 sec", None))
        self.btn_1min.setText(QCoreApplication.translate("MainWindow", u"+1 min", None))
        self.btn_5min.setText(QCoreApplication.translate("MainWindow", u"+5 min", None))
        self.btn_fun_volume.setText(QCoreApplication.translate("MainWindow", u"volume: on", None))
        self.btn_fun_lock.setText(QCoreApplication.translate("MainWindow", u"lock screen: on", None))
        self.btn_fun_power.setText(QCoreApplication.translate("MainWindow", u"power: on", None))
    # retranslateUi

