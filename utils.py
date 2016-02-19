# -*- coding: utf-8 -*-

import os
import codecs

class news(object):
    def __init__(self, title, pic):
        self.title = title
        self.pic = pic

def load_news():
    a = os.listdir("news")
    newsList = []
    for i in a:
        assert isinstance(i, str)
        if i.endswith("txt"):
            pic_src = i[:i.rfind(".")]
            if os.path.exists("news/" + pic_src):
                with codecs.open("news/" + i, 'r', 'utf-8') as fp:
                    title = fp.read()
                newsList.append(news(title, pic_src))
    return newsList
