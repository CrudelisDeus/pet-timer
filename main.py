from PyQt6 import QtCore, QtGui, QtWidgets
import sys

from PyQt6.QtCore import QTime

'''
import ui
'''

import gui_timer

class App(QtWidgets.QMainWindow, gui_timer.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # btn added time
        self.btn_30sec.clicked.connect(
            lambda: self._add_time(seconds=30))
        self.btn_1m.clicked.connect(
            lambda: self._add_time(minutes=1))
        self.btn_5m.clicked.connect(
            lambda: self._add_time(minutes=5))

        # btn timer
        self.btn_run.clicked.connect(self._start_timer)

        # timer
        self.countdown_timer = QtCore.QTimer(self)
        self.countdown_timer.timeout.connect(
            self._update_time
        )

        # checkbox
        self.chkb_mute.setStyleSheet("""
            QCheckBox {
                spacing: 0px;
                padding: 0px;
                border: none;
                background: transparent;
            }
            QCheckBox::indicator {
                width: 40px;
                height: 40px;
                background: none;
                border: none;
            }
            QCheckBox::indicator:unchecked {
                image: url("assets/icon/unmute.svg");
                background: #9E99BF;
                border-radius: 10px;
            }
            QCheckBox::indicator:checked {
                image: url("assets/icon/mute.svg");
                background: #9E99BF;
                border-radius: 10px;
            }
        """)
        self.chkb_mute.setIconSize(QtCore.QSize(20, 20))

    def _add_time(self, minutes=0, seconds=0):
        current_time = self.timer.time()
        new_time = current_time.addSecs(
            minutes * 60 + seconds
        )
        self.timer.setTime(new_time)

    def _start_timer(self):
        total_seconds = self.timer.time().hour() * 3600 + \
                        self.timer.time().minute() * 60 + \
                        self.timer.time().second()

        #
        if self.chkb_mute.isChecked():
            print("Чекбокс включен при старте")
        else:
            print("Чекбокс выключен при старте")

        if total_seconds > 0:
            self._btn_disable_or_enable(False)
            self.countdown_timer.start(1000)

    def _update_time(self):
        current_time = self.timer.time()
        remaining_seconds = current_time.hour() * 3600 + \
                            current_time.minute() * 60 + \
                            current_time.second() - 1
        if remaining_seconds <= 0:
            self.countdown_timer.stop()
            self.timer.setTime(QtCore.QTime(0,0,0))
            self._btn_disable_or_enable(True)
        else:
            self.timer.setTime(
                QtCore.QTime(0, 0, 0).addSecs(
                    remaining_seconds)
            )

    def _btn_disable_or_enable(self, enable=True):
        self.btn_30sec.setEnabled(enable)
        self.btn_1m.setEnabled(enable)
        self.btn_5m.setEnabled(enable)
        self.chkb_mute.setEnabled(enable)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()