# -*- coding: utf-8 -*-
"""
common functor
"""

#def get_text(item):
def GT(item):
	return item.text.encode("utf-8", "ignore").strip()
#def get_attr(item, attr):
def GA(item, attr):
	return item[attr].encode("utf-8", "ignore").strip()
def append_domain(item, domain):
	return domain+item
def get_util_newline(item):
	return GT(item).split("\n")[0].strip()	



