from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtGui import QIcon

from PyQt6.QtCore import QTime

'''
import ui
'''

import gui_timer

'''
import dev function
'''

import fun_volume

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
                background: transparent;
            }
            QCheckBox::indicator:checked {
                background: transparent;
            }
        """)
        self.chkb_mute.stateChanged.connect(self._chkb_icon_change)
        self.chkb_mute.setIconSize(QtCore.QSize(20, 20))
        self._chkb_icon_change()

    def _add_time(self, minutes=0, seconds=0):
        current_time = self.timer.time()
        new_time = current_time.addSecs(
            minutes * 60 + seconds
        )
        self.timer.setTime(new_time)

    def _start_timer(self):
        if self.countdown_timer.isActive():
            self.timer.setTime(QtCore.QTime(0, 0, 0))
            self.countdown_timer.stop()
            self._btn_disable_or_enable(True)
            self.btn_run.setIcon(QIcon('assets/icon/btn_run.svg'))
        else:
            total_seconds = self.timer.time().hour() * 3600 + \
                            self.timer.time().minute() * 60 + \
                            self.timer.time().second()

            if total_seconds > 0:
                self._btn_disable_or_enable(False)
                self.btn_run.setIcon(QIcon('assets/icon/btn_run_stop.svg'))
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
            if self.chkb_mute.isChecked():
                fun_volume.mute()

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
        if enable:
            self._change_color_label_mute('#262626')
        else:
            self._change_color_label_mute('#0D0D0D')

    def _chkb_icon_change(self):
        if self.chkb_mute.isChecked():
            self.label_mute.setPixmap(QtGui.QPixmap("assets/icon/mute.svg"))
            self._change_color_label_mute('#262626')
        else:
            self.label_mute.setPixmap(QtGui.QPixmap("assets/icon/unmute.svg"))
            self._change_color_label_mute('#262626')

    def _change_color_label_mute(self, color=''):
        self.label_mute_bkg.setStyleSheet(f"background-color: {color};"
                                          "\nborder-radius: 10px;")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()