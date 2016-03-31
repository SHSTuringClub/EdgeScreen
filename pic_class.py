# -*- coding: utf-8 -*-

#    Edge Screen - The Next Generation LED Player of SHS
#    Copyright (C) 2016  Genesis Di
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random
import time

from PyQt5 import QtCore, QtGui, QtWidgets

import ui_ver
import utils


class pic_screen(ui_ver.Ui_MainWindow):
    def update_ui(self):
        credits_index = random.randint(0, self.credits.__len__() - 1)
        self.aqi.setText("AQI: " + str(self.aqi_value))
        self.date.setText(time.strftime(self.DATEFORMAT, time.localtime()))
        self.time.setText(time.strftime(self.TIMEFORMAT, time.localtime()))
        currentPic = self.picList[self.picIndex]
        currentNoti = self.notiList[self.notiIndex]
        Pic = QtGui.QPixmap(currentPic)
        self.Pic = Pic.scaled(1350, 900, 1, 1)
        # Qt::KeepAspectRadio, Qt::SmoothTransformation (bilinear)
        self.picLabel.setPixmap(self.Pic)
        if not currentNoti == "":
            self.notice.setText(currentNoti)
        else:
            self.notice.setText("暂无通知")
        self.picIndex = self.picIndex + 1 if self.picIndex < self.picList.__len__() - 1 else 0
        self.notiIndex = self.notiIndex + 1 if self.notiIndex < self.notiList.__len__() - 1 else 0
        self.credit.setText(self.credits[credits_index])

    def init_ui(self, aqi, refreshTime, path='pic'):
        self.aqi_value = aqi
        self.picList = utils.load_pic(path)
        self.picIndex = 0
        self.notiList = utils.load_notification()
        self.notiIndex = 0
        self.TIMEFORMAT = '%H:%M'
        self.DATEFORMAT = '%Y.%m.%d'
        self.credits = [r'Crafted by SHS Turing Club with ❤',
                        r'Design: Viola Lin',
                        r'Code: Genesis Di & Peter Zheng',
                        r'Edge Screen is OSS Licensed under GPLv3']
        self.exit_hotkey = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape), self.centralwidget)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(refreshTime)
        self.centralwidget.setCursor(QtCore.Qt.BlankCursor)
        self.update_ui()
