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
#start vetogate
{"name":"vetogate_72", "site":"vetogate.com", "channel":"72", "list_url":"http://www.vetogate.com/list/72/ahzab", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_70", "site":"vetogate.com", "channel":"70", "list_url":"http://www.vetogate.com/list/70/eslamyoun", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_75", "site":"vetogate.com", "channel":"75", "list_url":"http://www.vetogate.com/list/75/akbat", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_76", "site":"vetogate.com", "channel":"76", "list_url":"http://www.vetogate.com/list/76/harakat", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_71", "site":"vetogate.com", "channel":"71", "list_url":"http://www.vetogate.com/list/71/madany", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_74", "site":"vetogate.com", "channel":"74", "list_url":"http://www.vetogate.com/list/74/barlman", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_73", "site":"vetogate.com", "channel":"73", "list_url":"http://www.vetogate.com/list/73/nekabat", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_60", "site":"vetogate.com", "channel":"60", "list_url":"http://www.vetogate.com/list/60/benok", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_61", "site":"vetogate.com", "channel":"61", "list_url":"http://www.vetogate.com/list/61/borsa", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_59", "site":"vetogate.com", "channel":"59", "list_url":"http://www.vetogate.com/list/59/business", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_62", "site":"vetogate.com", "channel":"62", "list_url":"http://www.vetogate.com/list/62/akarat", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_57", "site":"vetogate.com", "channel":"57", "list_url":"http://www.vetogate.com/list/57/altras", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_50", "site":"vetogate.com", "channel":"50", "list_url":"http://www.vetogate.com/list/50/momtaz", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_54", "site":"vetogate.com", "channel":"54", "list_url":"http://www.vetogate.com/list/54/negom", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_53", "site":"vetogate.com", "channel":"53", "list_url":"http://www.vetogate.com/list/53/andia", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_52", "site":"vetogate.com", "channel":"52", "list_url":"http://www.vetogate.com/list/52/harafish", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_51", "site":"vetogate.com", "channel":"51", "list_url":"http://www.vetogate.com/list/51/mazalim", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_55", "site":"vetogate.com", "channel":"55", "list_url":"http://www.vetogate.com/list/55/international", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_58", "site":"vetogate.com", "channel":"58", "list_url":"http://www.vetogate.com/list/58/women", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_67", "site":"vetogate.com", "channel":"67", "list_url":"http://www.vetogate.com/list/67/ebdaat", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_68", "site":"vetogate.com", "channel":"68", "list_url":"http://www.vetogate.com/list/68/thakafagamheria", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_69", "site":"vetogate.com", "channel":"69", "list_url":"http://www.vetogate.com/list/69/salonat", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_65", "site":"vetogate.com", "channel":"65", "list_url":"http://www.vetogate.com/list/65/kotob", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_66", "site":"vetogate.com", "channel":"66", "list_url":"http://www.vetogate.com/list/66/maared", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_48", "site":"vetogate.com", "channel":"48", "list_url":"http://www.vetogate.com/list/48/international", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_45", "site":"vetogate.com", "channel":"45", "list_url":"http://www.vetogate.com/list/45/cinema", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_49", "site":"vetogate.com", "channel":"49", "list_url":"http://www.vetogate.com/list/49/masrah", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_162", "site":"vetogate.com", "channel":"162", "list_url":"http://www.vetogate.com/list/162/talkshow", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_78", "site":"vetogate.com", "channel":"78", "list_url":"http://www.vetogate.com/list/78/naeb", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_80", "site":"vetogate.com", "channel":"80", "list_url":"http://www.vetogate.com/list/80/daftar", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_77", "site":"vetogate.com", "channel":"77", "list_url":"http://www.vetogate.com/list/77/mahakem", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_926", "site":"vetogate.com", "channel":"926", "list_url":"http://www.vetogate.com/list/926/cars", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_931", "site":"vetogate.com", "channel":"931", "list_url":"http://www.vetogate.com/list/931/technology", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_126", "site":"vetogate.com", "channel":"126", "list_url":"http://www.vetogate.com/list/126/SocietyandEntertainment", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
{"name":"vetogate_33", "site":"vetogate.com", "channel":"33", "list_url":"http://www.vetogate.com/list/33/govs", "list_template":vetogate_72_list, "detail_template":vetogate_72_detail},\
#start masrawy
{"name":"masrawy_35", "site":"masrawy.com", "channel":"35", "list_url":"http://www.masrawy.com/News/News_Egypt/section/35/أخبار-مصر#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_202", "site":"masrawy.com", "channel":"202", "list_url":"http://www.masrawy.com/News/News_PublicAffairs/section/202/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_206", "site":"masrawy.com", "channel":"206", "list_url":"http://www.masrawy.com/News/News_Economy/section/206/%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_577", "site":"masrawy.com", "channel":"577", "list_url":"http://www.masrawy.com/Sports/Sports_News/section/577/%D8%A3%D8%AE%D8%A8%D8%A7%D8%B1-%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6%D8%A9#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_579", "site":"masrawy.com", "channel":"575", "list_url":"http://www.masrawy.com/Sports/Sports-arab-international/section/579/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_578", "site":"masrawy.com", "channel":"578", "list_url":"http://www.masrawy.com/Sports/Sports-others/section/578/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_227", "site":"masrawy.com", "channel":"227", "list_url":"http://www.masrawy.com/sports/articles/section/227/%d9%85%d9%82%d8%a7%d9%84%d8%a7%d8%aa#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_254", "site":"masrawy.com", "channel":"254", "list_url":"http://www.masrawy.com/arts/cinema/section/254/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_255", "site":"masrawy.com", "channel":"255", "list_url":"http://www.masrawy.com/arts/music/section/255/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_205", "site":"masrawy.com", "channel":"205", "list_url":"http://www.masrawy.com/News/News_Cases/section/205/%D8%AD%D9%88%D8%A7%D8%AF%D8%AB-%D9%88%D9%82%D8%B6%D8%A7%D9%8A%D8%A7#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_375", "site":"masrawy.com", "channel":"375", "list_url":"http://www.masrawy.com/Autos/autos_news/section/375/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_219", "site":"masrawy.com", "channel":"219", "list_url":"http://www.masrawy.com/Howa_w_Hya/Health/section/219/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_222", "site":"masrawy.com", "channel":"222", "list_url":"http://www.masrawy.com/Howa_w_Hya/Pregnancy/section/222/%D8%A7%D9%84%D8%AD%D9%85%D9%84-%D9%88%D8%A7#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_402", "site":"masrawy.com", "channel":"402", "list_url":"http://www.masrawy.com/Howa_w_Hya/Grooming/section/402/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_385", "site":"masrawy.com", "channel":"385", "list_url":"http://www.masrawy.com/News/Tech-reports/section/385/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_220", "site":"masrawy.com", "channel":"220", "list_url":"http://www.masrawy.com/Howa_w_Hya/Fashion/section/220/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_603", "site":"masrawy.com", "channel":"603", "list_url":"http://www.masrawy.com/Howa_w_Hya/Travel/section/603#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_208", "site":"masrawy.com", "channel":"208", "list_url":"http://www.masrawy.com/News/News_Various/section/208/منوعات#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_467", "site":"masrawy.com", "channel":"467", "list_url":"http://www.masrawy.com/sports/sports_galleries/Section/467/%D8%B5%D9%88%D8%B1#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_239", "site":"masrawy.com", "channel":"239", "list_url":"http://www.masrawy.com/Howa_w_Hya/Cooking-Recipes/section/239/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_61", "site":"masrawy.com", "channel":"61", "list_url":"http://www.masrawy.com/Islameyat/Fatawa/section/61/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_50", "site":"masrawy.com", "channel":"50", "list_url":"http://www.masrawy.com/Islameyat/makalat/section/50/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_51", "site":"masrawy.com", "channel":"51", "list_url":"http://www.masrawy.com/Islameyat/Sera/section/51/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_56", "site":"masrawy.com", "channel":"56", "list_url":"http://www.masrawy.com/Islameyat/Quran/section/56/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_445", "site":"masrawy.com", "channel":"445", "list_url":"http://www.masrawy.com/Islameyat/Others/section/445/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_446", "site":"masrawy.com", "channel":"446", "list_url":"http://www.masrawy.com/Islameyat/kesas/section/446/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_215", "site":"masrawy.com", "channel":"215", "list_url":"http://www.masrawy.com/Islameyat/Islameyat-Videos/section/215/#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
		{"name":"masrawy_204", "site":"masrawy.com", "channel":"204", "list_url":"http://www.masrawy.com/News/News_Regions/section/204/%D8%A3%D8%AE%D8%A8%D8%A7%D8%B1-%D8%A7%D9%84%D9%85%D8%AD%D8%A7%D9%81%D8%B8%D8%A7%D8%AA#hpnav", "list_template":masrawy_35_list, "detail_template":masrawy_35_detail},\
#start arabic.cnn.com
{"name":"arabic_1", "site":"arabic.cnn.com", "channel":"1", "list_url":"http://arabic.cnn.com/%D9%85%D8%B5%D8%B1", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_2", "site":"arabic.cnn.com", "channel":"2", "list_url":"http://arabic.cnn.com/%D8%A7%D9%84%D8%A5%D9%85%D8%A7%D8%B1%D8%A7%D8%AA-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9-%D8%A7%D9%84%D9%85%D8%AA%D8%AD%D8%AF%D8%A9", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_3", "site":"arabic.cnn.com", "channel":"3", "list_url":"http://arabic.cnn.com/البحرين", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_4", "site":"arabic.cnn.com", "channel":"4", "list_url":"http://arabic.cnn.com/%D8%A7%D9%84%D9%85%D9%85%D9%84%D9%83%D8%A9-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_5", "site":"arabic.cnn.com", "channel":"5", "list_url":"http://arabic.cnn.com/%D8%A7%D9%84%D9%83%D9%88%D9%8A%D8%AA", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_6", "site":"arabic.cnn.com", "channel":"6", "list_url":"http://arabic.cnn.com/%D8%A7%D9%84%D9%8A%D9%85%D9%86", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_7", "site":"arabic.cnn.com", "channel":"7", "list_url":"http://arabic.cnn.com/%D8%B3%D9%84%D8%B7%D9%86%D8%A9-%D8%B9%D9%85%D8%A7%D9%86", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_8", "site":"arabic.cnn.com", "channel":"8", "list_url":"http://arabic.cnn.com/قطر", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_9", "site":"arabic.cnn.com", "channel":"9", "list_url":"http://arabic.cnn.com/%D8%A7%D9%84%D8%A3%D8%B1%D8%AF%D9%86", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_10", "site":"arabic.cnn.com", "channel":"10", "list_url":"http://arabic.cnn.com/العراق", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_11", "site":"arabic.cnn.com", "channel":"11", "list_url":"http://arabic.cnn.com/%D8%B3%D9%88%D8%B1%D9%8A%D8%A7", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_12", "site":"arabic.cnn.com", "channel":"12", "list_url":"http://arabic.cnn.com/%D9%84%D9%8A%D8%A8%D9%8A%D8%A7", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_13", "site":"arabic.cnn.com", "channel":"13", "list_url":"http://arabic.cnn.com/%D8%A7%D9%84%D8%AC%D8%B2%D8%A7%D8%A6%D8%B1", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_14", "site":"arabic.cnn.com", "channel":"14", "list_url":"http://arabic.cnn.com/المغرب", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_15", "site":"arabic.cnn.com", "channel":"15", "list_url":"http://arabic.cnn.com/%D8%AA%D9%88%D9%86%D8%B3", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_16", "site":"arabic.cnn.com", "channel":"16", "list_url":"http://arabic.cnn.com/%D9%84%D9%8A%D8%A8%D9%8A%D8%A7", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_17", "site":"arabic.cnn.com", "channel":"17", "list_url":"http://arabic.cnn.com/middle_east", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_18", "site":"arabic.cnn.com", "channel":"18", "list_url":"http://arabic.cnn.com/world", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_19", "site":"arabic.cnn.com", "channel":"19", "list_url":"http://arabic.cnn.com/business", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_20", "site":"arabic.cnn.com", "channel":"20", "list_url":"http://arabic.cnn.com/sport", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_21", "site":"arabic.cnn.com", "channel":"21", "list_url":"http://arabic.cnn.com/entertainment", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_22", "site":"arabic.cnn.com", "channel":"22", "list_url":"http://arabic.cnn.com/scitech", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_23", "site":"arabic.cnn.com", "channel":"23", "list_url":"http://arabic.cnn.com/%D8%B3%D9%81%D8%B1", "list_template":arabic_list,"detail_template":arabic_detail},\
		{"name":"arabic_24", "site":"arabic.cnn.com", "channel":"24", "list_url":"http://arabic.cnn.com/gallery", "list_template":arabic_list,"detail_template":arabic_detail},\
#start aljazeera.net
{"name":"aljazeera_1", "site":"aljazeera.net", "channel":"1", "list_url":"http://www.aljazeera.net/news/arabic", "list_template":aljazeera_list,"detail_template":aljazeera_detail},\
		{"name":"aljazeera_2", "site":"aljazeera.net", "channel":"2", "list_url":"http://www.aljazeera.net/news/international", "list_template":aljazeera_list,"detail_template":aljazeera_detail},\
		{"name":"aljazeera_3", "site":"aljazeera.net", "channel":"3", "list_url":"http://www.aljazeera.net/ebusiness", "list_template":aljazeera_list,"detail_template":aljazeera_detail},\
		{"name":"aljazeera_4", "site":"aljazeera.net", "channel":"4", "list_url":"http://www.aljazeera.net/encyclopedia/economy", "list_template":aljazeera_list,"detail_template":aljazeera_detail},\
		{"name":"aljazeera_5", "site":"aljazeera.net", "channel":"5", "list_url":"http://www.aljazeera.net/news/sport", "list_template":aljazeera_list,"detail_template":aljazeera_detail},\
		{"name":"aljazeera_6", "site":"aljazeera.net", "channel":"6", "list_url":"http://www.aljazeera.net/news/cultureandart", "list_template":aljazeera_list,"detail_template":aljazeera_detail},\
		{"name":"aljazeera_7", "site":"aljazeera.net", "channel":"7", "list_url":"http://www.aljazeera.net/news/healthmedicine", "list_template":aljazeera_list,"detail_template":aljazeera_detail},\
		{"name":"aljazeera_8", "site":"aljazeera.net", "channel":"8", "list_url":"http://www.aljazeera.net/encyclopedia/healthmedicine", "list_template":aljazeera_list,"detail_template":aljazeera_detail},\
		{"name":"aljazeera_9", "site":"aljazeera.net", "channel":"9", "list_url":"http://www.aljazeera.net/news/scienceandtechnology", "list_template":aljazeera_list,"detail_template":aljazeera_detail},\
		{"name":"aljazeera_10", "site":"aljazeera.net", "channel":"10", "list_url":"http://www.aljazeera.net/news/miscellaneous", "list_template":aljazeera_list,"detail_template":aljazeera_detail},\
		{"name":"aljazeera_11", "site":"aljazeera.net", "channel":"11", "list_url":"http://www.aljazeera.net/multimedia/caricature", "list_template":aljazeera_list,"detail_template":aljazeera_detail},\
		{"name":"aljazeera_12", "site":"aljazeera.net", "channel":"12", "list_url":"http://www.aljazeera.net/news/presstour", "list_template":aljazeera_list,"detail_template":aljazeera_detail},\
		{"name":"aljazeera_13", "site":"aljazeera.net", "channel":"13", "list_url":"http://www.aljazeera.net/multimedia/photoGallery", "list_template":aljazeera_list,"detail_template":aljazeera_detail},\
		{"name":"aljazeera_14", "site":"aljazeera.net", "channel":"14", "list_url":"http://www.aljazeera.net/news/hijri", "list_template":aljazeera_list,"detail_template":aljazeera_detail},\
#start tahrirnews
{"name":"tahrirnews_299", "site":"tahrirnews.com", "channel":"299", "list_url":"http://www.tahrirnews.com/category/299", "list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
		{"name":"tahrirnews_340", "site":"tahrirnews.com", "channel":"340", "list_url":"http://www.tahrirnews.com/category/340", "list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
		{"name":"tahrirnews_298", "site":"tahrirnews.com", "channel":"298", "list_url":"http://www.tahrirnews.com/category/298", "list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
		{"name":"tahrirnews_300", "site":"tahrirnews.com", "channel":"300", "list_url":"http://www.tahrirnews.com/category/300", "list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
		{"name":"tahrirnews_338", "site":"tahrirnews.com", "channel":"338", "list_url":"http://www.tahrirnews.com/category/338", "list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
		{"name":"tahrirnews_301", "site":"tahrirnews.com", "channel":"301", "list_url":"http://www.tahrirnews.com/category/301", "list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
		{"name":"tahrirnews_342", "site":"tahrirnews.com", "channel":"342", "list_url":"http://www.tahrirnews.com/category/342", "list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
		{"name":"tahrirnews_343", "site":"tahrirnews.com", "channel":"343", "list_url":"http://www.tahrirnews.com/category/343", "list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
		{"name":"tahrirnews_302", "site":"tahrirnews.com", "channel":"302", "list_url":"http://www.tahrirnews.com/category/302", "list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
		{"name":"tahrirnews_100", "site":"tahrirnews.com", "channel":"100", "list_url":"http://www.tahrirnews.com/category/100", "list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
		{"name":"tahrirnews_344", "site":"tahrirnews.com", "channel":"344", "list_url":"http://www.tahrirnews.com/category/344", "list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
		{"name":"tahrirnews_345", "site":"tahrirnews.com", "channel":"345", "list_url":"http://www.tahrirnews.com/category/345", "list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
		{"name":"tahrirnews_307", "site":"tahrirnews.com", "channel":"307", "list_url":"http://www.tahrirnews.com/category/307", "list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
		{"name":"tahrirnews_303", "site":"tahrirnews.com", "channel":"303", "list_url":"http://www.tahrirnews.com/category/303", "list_template":tahrirnews_list,"detail_template":tahrirnews_detail},\
]

if __name__ == "__main__":
	print config
	print "i am ok"
	sys.exit(0)

