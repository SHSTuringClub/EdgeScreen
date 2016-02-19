# -*- coding: utf-8 -*-

from PyQt5 import QtCore
import ui_hor
import utils
import random
import time

class news_screen(ui_hor.Ui_Horizontal):
    def update_ui(self):
        credits_index = random.randint(0, self.credits.__len__() - 1)
        self.aqi.setText("AQI: " + str(self.aqi_value))
        self.datetime.setText(time.strftime(self.TIMEFORMAT, time.localtime()))
        current = self.newsList[self.newsIndex]
        assert isinstance(current, utils.news)
        self.newspic.setStyleSheet(r'background-image: url("news/' + current.pic + r'"); background-repeat: no-repeat; background-position: center')
        self.news.setText(current.title)
        self.newsIndex += 1 if self.newsIndex < self.newsList.__len__() - 1 else 0
        self.credit.setText(self.credits[credits_index])

    def init_ui(self, aqi, refreshTime):
        self.aqi_value = aqi
        self.newsList = utils.load_news()
        self.newsIndex = 0
        self.TIMEFORMAT = '%Y.%m.%d %H:%M'
        self.credits = [r'Crafted by SHS Turing Club with ❤️',
                        r'Design: Viola Lin',
                        r'Code: Genesis Di & Peter Zheng']
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(refreshTime)
        self.update_ui()