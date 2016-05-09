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

tahrirnews_list = {\
'url':	('#grid_news div.sectionNewContent h3 a', 'GA(item,"href")'),\
'title':	('#grid_news div.sectionNewContent h3 a', None),\
'thumbnail':	('#grid_news div.sectionNewImage.relative a img','GA(item,"src")'),\
#'description':	('#MainContent_CatListingCtrl_ulItemListing li p', None),\
'publish_time':	('#grid_news div.sectionNewContent > div', None),\
}
tahrirnews_detail = {\
'text_detail':('#cpd_con > p', None),\
}


if __name__ == "__main__":
	print "i am ok"
	sys.exit(0)
