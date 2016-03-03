# -*- coding: utf-8 -*-

import codecs
import configparser
import os
import sys


class news(object):
    def __init__(self, title, pic):
        self.title = title
        self.pic = pic


class timeline(object):
    pass


def load_timeline():
    cp = configparser.ConfigParser(delimiters='=')  # To support time like 6:00
    try:
        cp.read('timeline.conf')
    except FileNotFoundError:
        sys.stderr.write("timeline.conf not found!")


def load_news(path):
    a = os.listdir(path)
    newsList = []
    for i in a:
        assert isinstance(i, str)
        if i.endswith("txt"):
            pic_src = i[:i.rfind(".")]
            if os.path.exists(path + '/' + pic_src):
                with codecs.open(path + '/' + i, 'r', 'utf-8') as fp:
                    title = fp.read()
                newsList.append(news(title, path + '/' + pic_src))
    return newsList


def load_pic():
    a = os.listdir("pic")
    picSuffix = ['png', 'jpg', 'bmp']
    picList = []
    for i in a:
        assert isinstance(i, str)
        for j in picSuffix:
            if i.lower().endswith(j):
                picList.append(i)
    return picList


def load_notification():
    try:
        with open("notification.txt", 'r') as fp:
            buffer = fp.read()
        return str(buffer).split('\n')
    except FileNotFoundError:
        return []
