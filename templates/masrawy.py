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

masrawy_35_list = {\
'url':	('#MainContent_CatListingCtrl_ulItemListing li p a', 'append_domain(GA(item,"href"),"http://www.masrawy.com")'),\
'title':	('#MainContent_CatListingCtrl_ulItemListing li p a', 'GA(item,"title")'),\
'thumbnail':	('#MainContent_CatListingCtrl_ulItemListing li a img','GA(item,"src")'),\
'description':	('#MainContent_CatListingCtrl_ulItemListing li p', None),\
'publish_time':	('#MainContent_CatListingCtrl_ulItemListing li time','GT(item)'),\
}
masrawy_35_detail = {\
'text_detail':('#content div.articleBody', None),\
}


if __name__ == "__main__":
	print "i am ok"
	sys.exit(0)
