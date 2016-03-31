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


import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

import news_class
import pic_class
import ui_ent
import utils

VERSION = r'Edge Screen - 上中图灵社'


def news_stop():
    global newsWindow
    assert isinstance(newsWindow, QMainWindow)
    newsWindow.close()


def news_start(path='news'):
    global newsWindow, newsUI, entUI
    newsWindow = QMainWindow()
    newsUI = news_class.news_screen()
    newsUI.setupUi(newsWindow)
    try:
        aqi = int(entUI.aqi_input.text())
        refreshTime = 1000 * int(entUI.Refresh_input.text())
        if aqi < 0 or refreshTime <= 0:
            raise ValueError
    except ValueError:
        global d
        d = QMessageBox()
        d.setText("请输入有效 AQI/刷新时间(正整数)!")
        d.show()
        return
    newsUI.init_ui(aqi, refreshTime, path)
    newsWindow.showFullScreen()
    newsUI.exit_hotkey.activated.connect(news_stop)


def pic_stop():
    global picWindow
    picWindow.close()


def pic_start(path='pic'):
    global picWindow, picUI, entUI
    picWindow = QMainWindow()
    picUI = pic_class.pic_screen()
    picUI.setupUi(picWindow)
    try:
        aqi = int(entUI.aqi_input.text())
        refreshTime = 1000 * int(entUI.Refresh_input.text())
        if aqi < 0 or refreshTime <= 0:
            raise ValueError
    except ValueError as e:
        global d
        d = QMessageBox()
        d.setText("请输入有效 AQI/刷新时间(正整数)!")
        d.show()
        return
    picUI.init_ui(aqi, refreshTime, path)
    picWindow.showFullScreen()
    picUI.exit_hotkey.activated.connect(pic_stop)


def link_start():
    global picWindow, newsWindow, timer
    try:
        picWindow.close()
    except NameError:
        pass

    try:
        newsWindow.close()
    except NameError:
        pass

    try:
        timer.stop()
    except NameError:
        pass

    tl = utils.Timeline(utils.load_timeline())
    now = tl.get_now()
    type = 0 if now[0] == '时政' or now[0] == 'news' else 1
    start = [news_start, pic_start]
    time = now[2]
    assert isinstance(time, int)
    start[type](now[1])
    timer = QtCore.QTimer()
    timer.timeout.connect(link_start)
    timer.start(time * 60000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    entWindow = QMainWindow()
    entUI = ui_ent.Ui_Entrance()
    entUI.setupUi(entWindow)
    entUI.newsButton.clicked.connect(news_start)
    entUI.picsButton.clicked.connect(pic_start)
    entUI.linkStartButton.clicked.connect(link_start)
    entUI.versionLabel.setText(VERSION)
    entWindow.show()
    sys.exit(app.exec_())
