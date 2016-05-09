# -*- coding: utf-8 -*-
"""
list_url => template config
"""

import sys, os
sys.path.append(".")
sys.path.append("./templates/")
from functor import *
from vetogate import *
from masrawy import *
from arabic import *
from aljazeera import *
from tahrirnews import *

def select_value(soup, conf):
	path,functor = conf
	if not functor:
		functor = 'GT(item)'
	items = soup.select(path)
	#print items
	values = []
	for item in items:
		val = eval(functor)
		values.append(val)
	return values

config = [\
		{"name":"tahrirnews","list_url":"http://www.tahrirnews.com/category/299","list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
		#{"name":"masrawy_35","list_url":"http://www.masrawy.com/News/News_Egypt/section/35/%D8%A3%D8%AE%D8%A8%D8%A7%D8%B1-%D9%85%D8%B5%D8%B1#hpnav","list_template":masrawy_35_list,"detail_template":masrawy_35_detail},\
		#{"name":"masrawy_35","list_url":"http://www.masrawy.com/News/News_Regions/section/204/%D8%A3%D8%AE%D8%A8%D8%A7%D8%B1-%D8%A7%D9%84%D9%85%D8%AD%D8%A7%D9%81%D8%B8%D8%A7%D8%AA#hpnav","list_template":masrawy_35_list,"detail_template":masrawy_35_detail},\
]

if __name__ == "__main__":
	print "i am ok"
	sys.exit(0)

