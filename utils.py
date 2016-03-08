# -*- coding: utf-8 -*-

import codecs
import configparser
import json
import os
import sys
import time


class News(object):
    def __init__(self, title, pic):
        self.title = title
        self.pic = pic


class Timeline(object):
    def __init__(self, timeline_list):
        assert isinstance(timeline_list, list)
        self.timeline = timeline_list

    def get_next(self):
        current = time.localtime()


def load_timeline():
    # Sample Return
    # [
    #   {
    #       '6:00': ['type', 'arg'],
    #       '7:00': ['type', 'arg']
    #   },
    #   ...
    # ]
    cp = configparser.ConfigParser(delimiters='=')  # To support time like 6:00
    try:
        cp.read('timeline.conf')
    except FileNotFoundError:
        sys.stderr.write("timeline.conf not found!")
    except configparser.Error:
        sys.stderr.write("timeline.conf is invalid!")
    except Exception as e:
        sys.stderr.write("Unknown error occurred!")
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    timeline = []
    for i in days:
        try:
            tmp = dict(cp[i])
            for j in tmp:
                tmp[j] = json.loads(tmp[j])
            timeline.append(tmp)
        except KeyError:
            timeline.append(dict())
    return timeline

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
                newsList.append(News(title, path + '/' + pic_src))
    return newsList


def load_pic():
    a = os.listdir("pic")
    picSuffix = ['png', 'jpg', 'bmp']
    picList = []
    for i in a:
        assert isinstance(i, str)
        for j in picSuffix:
            if i.lower().endswith(j):
                picList.append("pic/" + i)
    return picList


def load_notification():
    try:
        with open("notification.txt", 'r') as fp:
            buffer = fp.read()
        return str(buffer).split('\n')
    except FileNotFoundError:
        return []
