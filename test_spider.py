# -*- coding: utf-8 -*-

import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")
src_path = os.path.dirname(__file__)
sys.path.append(src_path)
sys.path.append(src_path+"/templates/")

import logging
import re
import socket
import hashlib
import time, random
import base64, zlib, json
import threading, traceback
import urllib2, cookielib
import HTMLParser
import bs4 #BeautifulSoup4
from utils import download
from config import select_value
from test_config import config

#====util function====
def simple_download(url):
	response = urllib2.urlopen(url)
	data = response.read()
	soup = bs4.BeautifulSoup(data, from_encoding="utf-8")
	return soup

def write_file(fname, data):
	file_object = open(fname, 'w')
	file_object.write(data)
	file_object.close()

#====main====
if __name__ == "__main__":

	for target in config:
		name = target['name']
		list_url = target['list_url']
		list_template = target['list_template']
		detail_template = target['detail_template']

		#soup = download(list_url)
		httpcode, data, status = download(list_url)
		if not status:
			print "down fail:"+httpcode
			sys.exit(-1)
		soup = bs4.BeautifulSoup(data, from_encoding="utf-8")
		rows = []
		#parse list page
		for key,conf in list_template.items():
			print key
			values = select_value(soup,conf)
			rn = len(values)
			if not rows:
				for i in range(rn):
					rows.append({})
			else:
				if len(rows) != rn:
					print len(rows),rn
					print key+" not match"
					sys.exit(-1)
			for i in range(rn):
				rows[i][key] = values[i]
				print "\t"+values[i]

		#parse detail page
		for row in rows:
			url = row['url']
			httpcode, data, status = download(url)
			if not status:
				print "down fail:"+httpcode
				sys.exit(-1)
			soup = bs4.BeautifulSoup(data, from_encoding="utf-8")
			for key,conf in detail_template.items():
				print key
				values = select_value(soup,conf)
				if key == "text_detail":
					#combine detail
					row[key] = "\r\n".join(values)
				else:
					row[key] = values[0]
				print "\t"+row[key]

	sys.exit(0)

