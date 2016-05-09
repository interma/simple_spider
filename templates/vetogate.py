# -*- coding: utf-8 -*-
"""
site template define
"""

import sys
sys.path.append(".")
sys.path.append("./templates/")

from functor import *


#field:
#	title channel url thumbnail author language description text_detail 
#	site img_url publish_time state(INA) url_md5

vetogate_72_list = {\
'thumbnail':	('html body div.container2 div.area div.right div.def-list a.ar-EG span.img img','append_domain(GA(item,"src"),"http://www.vetogate.com")'),\
'publish_time':	('html body div.container2 div.area div.right div.def-list a.ar-EG span.date','GT(item)'),\
'description':	('html body div.container2 div.area div.right div.def-list a.ar-EG span.desc', None),\
'url':	('html body div.container2 div.area div.right div.def-list a', 'append_domain(GA(item,"href"),"http://www.vetogate.com")'),\
'title':	('html body div.container2 div div.right div.def-list a', 'get_util_newline(item)'),\
}
vetogate_72_detail = {\
'text_detail':('#start div', None),\
}

if __name__ == "__main__":
	print "i am ok"
	sys.exit(0)
