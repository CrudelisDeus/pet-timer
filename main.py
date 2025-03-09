from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtGui import QIcon

'''
import ui
'''

import gui_main

'''
import dev function
'''

#

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

    def _add_time_to_timer(self, minutes=0, seconds=0):
        current_time = self.timeEdit.time()
        new_time = current_time.addSecs(
            minutes * 60 + seconds
        )
        self.timeEdit.setTime(new_time)

    # timer

    def _start_timer(self):
        total_seconds = self.timeEdit.time().hour() * 3600 + \
                        self.timeEdit.time().minute() * 60 + \
                        self.timeEdit.time().second()
        if total_seconds > 0:
            self.countdown_timer.start(1000)

    def _update_time(self):
        current_time = self.timeEdit.time()
        remaining_seconds = current_time.hour() * 3600 + \
                            current_time.minute() * 60 + \
                            current_time.second() - 1

        if remaining_seconds <= 0:
            self.countdown_timer.stop()
            self.timeEdit.setTime(QtCore.QTime(0, 0, 0))
        else:
            new_time = QtCore.QTime(remaining_seconds // 3600,
                                    (remaining_seconds % 3600) // 60,
                                    remaining_seconds % 60)
            self.timeEdit.setTime(new_time)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()