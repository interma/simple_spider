# -*- coding: utf-8 -*-
# copy code form xielei

import sys, os, time
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(".")

import re
import socket
import hashlib
import time, random
import base64, zlib, json
import threading, traceback
import urllib2, cookielib
import HTMLParser
from Queue import Queue
from httplib2 import ServerNotFoundError

user_agent_list=[
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'),
    ('User-Agent', 'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1'),
    ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3'),
    ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3'),
    ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24')]


def make_opener(headers=None):
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie), urllib2.HTTPHandler)
    if headers:
        opener.addheaders = headers 
    else:
        ua = random.choice(user_agent_list)
        opener.addheaders = [ua]
    return opener

def download(url, param=None, times=0):
    if times > 2:return 999, '', False
    opener = make_opener()
    try:
        if param:
            return opener.open(url, param, timeout=60).read(), True
        response = opener.open(url, timeout=60)
        data = response.read()
        return response.getcode(), data, True
    except:
        t, v, tb = sys.exc_info()
        #log.error("HTTPError: %s,%s,%s,%s" % (url, t, v, traceback.format_tb(tb)))
        return download(url, times=times + 1)


def get_url_sign(data):
	md5 = hashlib.md5()
	md5.update(data)
	md5_digest = md5.hexdigest()
	return md5_digest


if __name__ == "__main__":
	print "i am ok"
	sys.exit(0)

