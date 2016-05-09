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

arabic_list = {\
'url':	('div.news-content.breakpoint div h2.desktop-headline a', 'append_domain(GA(item,"href"),"http://arabic.cnn.com")'),\
'title':	('div.news-content.breakpoint div h2.desktop-headline a', None),\
'thumbnail':	('div.news-content.breakpoint a img','GA(item,"src")'),\
#'description':	('#MainContent_CatListingCtrl_ulItemListing li p', None),\
#'publish_time':	('#MainContent_CatListingCtrl_ulItemListing li time','GT(item)'),\
}
arabic_detail = {\
'text_detail':('div.news-content div.article-content div p', None),\
'publish_time':	('div.news-utilities.clearfix span.news-date',None),\
}


if __name__ == "__main__":
	print "i am ok"
	sys.exit(0)
