from PyQt6 import QtCore, QtWidgets
import sys

'''
import ui
'''

import gui_main

'''
import dev function
'''

import fun_volume
import fun_lock
import fun_power

class App(QtWidgets.QMainWindow, gui_main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # btn added time to timer
        self.btn_30sec.clicked.connect(
            lambda: self._add_time_to_timer(seconds=30))
        self.btn_1min.clicked.connect(
            lambda: self._add_time_to_timer(minutes=1))
        self.btn_5min.clicked.connect(
            lambda: self._add_time_to_timer(minutes=5))

        # btn timer start
        self.btn_run.clicked.connect(self._start_timer)
        self.countdown_timer = QtCore.QTimer(self)
        self.countdown_timer.timeout.connect(
            self._update_time
        )

        # btn function
        self.btn_fun_volume.setCheckable(True)
        self.btn_fun_volume.setChecked(True)
        self.btn_fun_volume.clicked.connect(
            lambda: self._set_state_fun_btn(
                self.btn_fun_volume, 'volume'
            )
        )

        self.btn_fun_lock.setCheckable(True)
        self.btn_fun_lock.setChecked(True)
        self.btn_fun_lock.clicked.connect(
            lambda: self._set_state_fun_btn(
                self.btn_fun_lock, 'lock screen'
            )
        )

        self.btn_fun_power.setCheckable(True)
        self.btn_fun_power.setChecked(True)
        self.btn_fun_power.clicked.connect(
            lambda: self._set_state_fun_btn(
                self.btn_fun_power, 'power'
            )
        )

    # function
    # --------

    def _set_state_fun_btn(self, button, button_name):
        if button.isChecked():
            state = 'on'
        else:
            state = 'off'

        button.setText(f'{button_name}: {state}')

    # timer
    # -----

    def _add_time_to_timer(self, minutes=0, seconds=0):
        current_time = self.timeEdit.time()
        new_time = current_time.addSecs(
            minutes * 60 + seconds
        )
        self.timeEdit.setTime(new_time)

    def _start_timer(self):
        if self.countdown_timer.isActive():
            self._reset_timer()
        else:
            total_seconds = self.timeEdit.time().hour() * 3600 + \
                            self.timeEdit.time().minute() * 60 + \
                            self.timeEdit.time().second()
            if total_seconds > 0:
                self.btn_run.setText('stop')
                self._btn_enable_or_disable(False)
                self.countdown_timer.start(1000)

    def _update_time(self):
        current_time = self.timeEdit.time()
        remaining_seconds = current_time.hour() * 3600 + \
                            current_time.minute() * 60 + \
                            current_time.second() - 1

        if remaining_seconds <= 0:
            if not self.btn_fun_volume.isChecked():
                fun_volume.mute()
            if not self.btn_fun_lock.isChecked():
                fun_lock.lock_screen()
            if not self.btn_fun_power.isChecked():
                fun_power.power()
            self._reset_timer()
        else:
            new_time = QtCore.QTime(remaining_seconds // 3600,
                                    (remaining_seconds % 3600) // 60,
                                    remaining_seconds % 60)
            self.timeEdit.setTime(new_time)

    def _reset_timer(self):
        self.countdown_timer.stop()
        self.timeEdit.setTime(QtCore.QTime(0, 0, 0))
        self._btn_enable_or_disable(True)
        self.btn_run.setText('start')
        self.btn_fun_volume.setChecked(True)
        self.btn_fun_volume.setText('volume: on')
        self.btn_fun_lock.setChecked(True)
        self.btn_fun_lock.setText('lock screen: on')
        self.btn_fun_power.setChecked(True)
        self.btn_fun_power.setText('power: on')

    # other
    # -----

    def _btn_enable_or_disable(self, enable=True):
        """button disable or enable"""
        self.btn_30sec.setEnabled(enable)
        self.btn_1min.setEnabled(enable)
        self.btn_5min.setEnabled(enable)
        self.btn_fun_volume.setEnabled(enable)
        self.btn_fun_lock.setEnabled(enable)
        self.btn_fun_power.setEnabled(enable)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()