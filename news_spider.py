# -*- coding: utf-8 -*-
"""
crawler egypt news into i18n_news_final
use css selector template adopt multi site
"""

import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")
src_path = os.path.dirname(".")
sys.path.append(src_path)
sys.path.append(src_path+"/templates/")

import logging
import re
import socket
import time, random
import json
import threading, traceback
import bs4 #BeautifulSoup4
import MySQLdb
from utils import download
from utils import get_url_sign
from config import config
from config import select_value

#====conf====
DATA_PATH = "./data/"
DB_HOST = "10.50.42.75"
DB_PORT = 3306
DB_USER = "work"
DB_PASS = "npswork627"
DB_NAME = "db_interma"
DB_TABLE = "i18n_news_final"
#field:
#	title channel url thumbnail author language text_detail 
#	site img_url publish_time state(INA) url_md5
DB_TABLE_FIELD = ["works_id","title","channel","sub_channel","url","thumbnail","author","language","description","text_detail","site","img_url","publish_time","state","url_md5"]

logger = logging.getLogger('video_news_crawler')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("./log/news_spider.log")
fh.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(thread)d - %(name)s[%(filename)s:%(lineno)d] - %(message)s')
console.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(console)
logger.addHandler(fh)

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
	
def get_db():
	try:
		conn = MySQLdb.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, passwd=DB_PASS, db=DB_NAME, charset="utf8")
		conn.autocommit(True)
	except:
		return None
	return conn

def complete_rows(rows, target):
	#field:
	#	title channel url thumbnail author language text_detail 
	#	site img_url publish_time state(INA) url_md5
	for row in rows:
		if row['url'] == "" or row['title'] == "":
			return False
		row['language'] = 'arabic'
		row['state'] = 'INA'
		row['site'] = target['site']
		row['channel'] = target['channel']
		row['url_md5'] = get_url_sign(row['url'])
		#skip main_md5

	return True

def mk_insert_sql(row):
	fields = ""
	holds = ""
	param = []
	for field in DB_TABLE_FIELD:
		fields += ","+field
		holds += ",%s"
		val = row.get(field,"") 
		param.append(val)
	sql = "insert into %s (insert_time,update_time,last_crawler_time %s) values( now(),now(),now() %s)" % (DB_TABLE, fields, holds)

	#sql = 'insert into i18n_news_final (title, channel, url, thumbnail, author, language, text_detail, site, img_url, insert_time, update_time, last_crawler_time,publish_time, state, sub_channel, url_md5, main_md5) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, now(),now(), now(), %s, %s, %s ,%s, \''+ main_md5 +'\')'

	return sql,param


#====main====
if __name__ == "__main__":
	logger.info("Start")
	db = get_db()
	if not db:
		logger.fatal("get db fail")
		sys.exit(-1)

	for target in config:
		name = target['name']
		list_url = target['list_url']
		list_template = target['list_template']
		detail_template = target['detail_template']
		logger.info("begin craw: %s" % (list_url))

		httpcode, data, status = download(list_url)
		if not status:
			logger.warning("download %s fail, retcode:%d" % (list_url,httpcode))
			continue

		try:
			soup = bs4.BeautifulSoup(data, from_encoding="utf-8")
		except:
			logger.warning("create soup fail, url:%s" % (list_url))
			continue

		rows = []
		#parse list page
		for key,conf in list_template.items():
			values = select_value(soup,conf)
			rn = len(values)
			if not rows:
				for i in range(rn):
					rows.append({})
			if len(rows) != rn:
				logger.warning("key:%s val num not match, url:%s" % (key, list_url))
				continue
			for i in range(rn):
				rows[i][key] = values[i]

		#parse detail page
		if detail_template:
			for row in rows:
				url = row['url']
				httpcode, data, status = download(url)
				if not status:
					logger.warning("download %s fail, retcode:%d" % (url,httpcode))
					continue

				try:
					soup = bs4.BeautifulSoup(data, from_encoding="utf-8")
				except:
					logger.warning("create soup fail, url:%s" % (list_url))
					continue

				for key,conf in detail_template.items():
					values = select_value(soup,conf)
					if not values:
						logger.warning("select detail key:%s fail, url:%s" % (key, list_url))
						continue

					if key == "text_detail":
						#combine detail
						row[key] = "\r\n".join(values)
					else:
						row[key] = values[0]
		
		logger.info("end craw: %s" % (list_url))

		#write data for debug	
		ts = int(time.time())
		output_json = json.dumps(rows)
		fname = "%s%s-%d.json" % (DATA_PATH,name,ts)
		write_file(fname, output_json)

		#write db
		#db field:
		#	title channel url thumbnail author language text_detail 
		#	site img_url publish_time state(INA) url_md5
		ret = complete_rows(rows, target)
		if not ret:
			logger.warning("complete_rows fail, url:%s, file:%s" % (list_url, fname))
			continue
		
		rows.reverse() # make the newer item's id biger
		cursor = db.cursor()
		for row in rows:
			sql = 'select id from '+DB_TABLE+' where url_md5=%s'  
			param = (row['url_md5'])    
			try:
				n = cursor.execute(sql,param) 
			except:
				logger.warning("select db fail, sql:%s" % (cursor._last_executed))
				continue
			#already have
			if n >= 1:
				continue
			
			sql,param = mk_insert_sql(row)
			try:
				n = cursor.execute(sql,param) 
			except:
				logger.warning("insert db fail, url:%s, sql:%s" % (row['url'],cursor._last_executed))
				continue

		logger.info("end write db: %s" % (list_url))
	
	db.close()
	logger.info("End")
	sys.exit(0)

