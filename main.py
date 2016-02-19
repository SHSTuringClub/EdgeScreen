# -*- coding: utf-8 -*-
import sys
import ui_ent
import news
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

VERSION = r'Edge Screen - v0.1 - 上中图灵社'

def news_start():
    global newsWindow, newsUI, entUI
    newsWindow = QMainWindow()
    newsUI = news.news_screen()
    newsUI.setupUi(newsWindow)
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
    newsUI.init_ui(aqi, refreshTime)
    newsWindow.showFullScreen()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    entWindow = QMainWindow()
    entUI = ui_ent.Ui_Entrance()
    entUI.setupUi(entWindow)
    entUI.newsButton.clicked.connect(news_start)
    entUI.versionLabel.setText(VERSION)
    entWindow.show()
    sys.exit(app.exec_())