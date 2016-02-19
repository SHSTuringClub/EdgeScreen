# -*- coding: utf-8 -*-

import httplib2
import json
import codecs

def get_AQI():
    h = httplib2.Http("tmp")
    (resp_headers, content) = h.request("http://www.pm25.in/api/querys/only_aqi.json?city=shanghai"
                                        "&token=5j1znBVAsnSf5xQyNQyq&stations=no", "GET")
    try:
        return json.loads(str(content.decode("unicode-escape")))[0]["aqi"]
    except Exception as e:
        return -1

def getNewsList():
    with codecs.open("data.json", 'r', 'utf-8') as fp:
        newsList = json.loads(str(fp.read()))
    return newsList