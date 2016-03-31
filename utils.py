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

    def get_now(self):
        # Sample Return
        # ['type', 'arg', time]
        current = time.localtime()
        assert isinstance(current, time.struct_time)
        week_day = current.tm_wday
        if self.timeline[week_day] != {}:
            today = self.timeline[week_day]
            assert isinstance(today, dict)
            keys = list(today.keys())
            now = time.strftime("%H:%M", time.localtime())
            keys.append(now)
            keys.sort(key=lambda a: int(a.split(':')[0]) * 60 + int(a.split(':')[1]))
            now_index = keys.index(now)
            if now_index == 0:
                return self.timeline[week_day][keys[1]]
            else:
                return self.timeline[week_day][keys[now_index - 1]]

        else:
            tmp = []
            for i in range(7):
                if self.timeline[i] != {}:
                    tmp.append(i)
            if tmp.__len__() != 0:
                tmp.append(week_day)
            else:
                raise ValueError
            tmp.sort()
            now_index = tmp.index(week_day)
            if now_index == tmp.__len__() - 1:
                return self.timeline[tmp[0]][0]
            else:
                keys = list(self.timeline[tmp[now_index + 1]].keys())
                keys.sort(key=lambda a: int(a.split(':')[0]) * 60 + int(a.split(':')[1]))
                return self.timeline[tmp[now_index + 1]][keys[0]]


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
        cp.read('timeline.conf', encoding="utf-8")
    except FileNotFoundError:
        sys.stderr.write("timeline.conf not found!")
    except configparser.Error:
        sys.stderr.write("timeline.conf is invalid!")
    except:
        sys.stderr.write("Unknown error occurred!")
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    timeline = []
    for i in days:
        try:
            tmp = dict(cp[i])
            for j in tmp:
                tmp[j] = json.loads(tmp[j])
            timeline.append(tmp)
        except:
            timeline.append(dict())
    return timeline


def load_news(path='news'):
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


def load_pic(path='pic'):
    a = os.listdir(path)
    picSuffix = ['png', 'jpg', 'bmp']
    picList = []
    for i in a:
        assert isinstance(i, str)
        for j in picSuffix:
            if i.lower().endswith(j):
                picList.append(path + '/' + i)
    return picList


def load_notification():
    if not os.path.exists('notification.txt'):
        return []
    try:
        with open("notification.txt", 'r') as fp:
            buffer = fp.read()
    except UnicodeDecodeError:
        with codecs.open("notification.txt", 'r', 'utf-8') as fp:
            buffer = fp.read()

    return str(buffer).split('---\n')
