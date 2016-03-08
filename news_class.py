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

from PyQt5 import QtCore, QtGui

import ui_hor
import utils


class news_screen(ui_hor.Ui_Horizontal):
    def update_ui(self):
        credits_index = random.randint(0, self.credits.__len__() - 1)
        self.aqi.setText("AQI: " + str(self.aqi_value))
        self.datetime.setText(time.strftime(self.TIMEFORMAT, time.localtime()))
        currentNews = self.newsList[self.newsIndex]
        currentNoti = self.notiList[self.notiIndex]
        assert isinstance(currentNews, utils.News)
        newsP = QtGui.QPixmap(currentNews.pic)
        self.newsP = newsP.scaled(1240, 820, 1, 1)
        # Qt::KeepAspectRadio, Qt::SmoothTransformation (bilinear)
        self.picLabel.setPixmap(self.newsP)
        self.news.setText(currentNews.title)
        if not currentNoti == "":
            self.notice.setText(currentNoti)
        else:
            self.notice.setText("暂无通知")
        self.newsIndex = self.newsIndex + 1 if self.newsIndex < self.newsList.__len__() - 1 else 0
        self.notiIndex = self.notiIndex + 1 if self.notiIndex < self.notiList.__len__() - 1 else 0
        self.credit.setText(self.credits[credits_index])

    def init_ui(self, aqi, refreshTime):
        self.aqi_value = aqi
        self.newsList = utils.load_news()
        self.newsIndex = 0
        self.notiList = utils.load_notification()
        self.notiIndex = 0
        self.TIMEFORMAT = '%Y.%m.%d %H:%M'
        self.credits = [r'Crafted by SHS Turing Club with ❤',
                        r'Design: Viola Lin',
                        r'Code: Genesis Di & Peter Zheng',
                        r'Edge Screen - Milestone 2']
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(refreshTime)
        self.update_ui()
