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

aljazeera_list = {\
'url':	('#main-content article > h1 a', 'append_domain(GA(item,"href"),"http://www.aljazeera.net")'),\
'title':	('#main-content article > h1 a', None),\
'description':	('#main-content article > p', None),\
#'publish_time':	('#main-content article div.share_container_element.doneCounter',None),\ #js render
}
aljazeera_detail = {\
'img_url':('#main-player > img', 'append_domain(GA(item,"data-original"),"http://www.aljazeera.net")'),\
'text_detail':('#DynamicContentContainer > p', None),\
}

if __name__ == "__main__":
	print "i am ok"
	sys.exit(0)
