import os
import json
import requests
import time
import datetime
import gzip
import urllib2
from StringIO import StringIO
from relativedelta import relativedelta
from db import slimmodel 


DEV_KEY = os.environ.get("StackExchange_Key")

def date_converstion(date):
	#changes reable dates to unix
	cleandate = datetime.datetime.strptime(date, '%Y-%m-%d')
	converted_date = time.mktime(cleandate.timetuple())
	return int(converted_date)

def tag_count_by_day(tag, tagurl, tag_id, fromyearmonthday, toyearmonthday, DEV_KEY):
	#this adds number of questions per day about a specific tag to the database 

	list = []
	backoff = 1
	response = requests.get("http://api.stackexchange.com/2.2/questions?fromdate=" + str(fromyearmonthday) + "&todate=" + str(toyearmonthday) + "&order=desc&sort=activity&tagged=" + tagurl + "&site=stackoverflow&filter=!9YdnSQVoS&key=" + DEV_KEY) 
	if "backoff" in response.headers:
		backoff = int(response.headers["backoff"])
	count = response.json()["total"]
	date = datetime.datetime.fromtimestamp(fromyearmonthday)
	trend_id = fromyearmonthday + tag_id
	trends = slimmodel.Stack_Overflow_Trends(id=trend_id, skill_id = tag_id, skill = tag, date_epoc = date, question_count = count)
	slimmodel.Session.merge(trends)
	slimmodel.Session.commit()
	return backoff

# def question_count_by_day(fromyearmonthday, toyearmonthday, DEV_KEY):
# 	#this adds number of questions per day to database 

# 	backoff = 5
# 	response = requests.get("http://api.stackexchange.com//2.2/questions?filter=total&fromdate=" + str(fromyearmonthday) + "&todate=" + str(toyearmonthday) + "&order=desc&sort=activity&site=stackoverflow&key=" + DEV_KEY)
# 	print response
# 	if "backoff" in response.headers:
# 		backoff = int(response.headers["backoff"])

# 	count = response.json()["total"]
# 	questions_id = 1 + fromyearmonthday 
# 	date = datetime.datetime.fromtimestamp(fromyearmonthday)
# 	questions = slimmodel.Stack_Overflow_Trends(id = questions_id, skill_id = 1, skill = "question", date_epoc = date, question_count = count)
# 	slimmodel.Session.merge(questions)
# 	slimmodel.Session.commit()
# 	return backoff

# def stackexchange_call():
def stackexchange_call(name, tagurl, skill_id):
	"""this should make calls to stackexchange every .1 to retreive the number of questions per day since stack
	overflow's founding until present"""  

	start_date_from = date_converstion("2009-05-02")
	start_date_to = date_converstion("2009-05-03")
	current = (time.time())
	while start_date_to <= current:
		# time.sleep(tag_count_by_day(start_date_from, start_date_to, DEV_KEY))
		time.sleep(tag_count_by_day(name, tagurl, skill_id, start_date_from, start_date_to, DEV_KEY))    
		start_date_from = start_date_from + 86400
		start_date_to = start_date_to + 86400 


def main():
	seeds =	[("jsp", "jsp", 21249)]

	for seed in seeds:
		name = seed[0]
		tagurl = seed[1]
		skill_id = seed[2] 
		stackexchange_call(name, tagurl, skill_id)
		print "done" 


if __name__ == "__main__":
	main()

#To Seed 
#("jsp", "jsp", 21249), ("extjs", "extjs", 30785), ("jsf", "jsf", 36726), ("backbone.js", "backbone", 33096)
#("osx", "osx", 70730), ("hibernate", "hibernate", 35292), ("postgresql", "postgresql", 22286),("vba", "vba", 50304)

#("python", "python", 14775), ("qt", "qt", 34130), ("matlab", "matlab", 28665), ("linq", "linq", 76132)
#("r", "r", 21803), ("eclipse", "eclipse", 39991 12-9-29), ("vb.net", "vb.net", 16023), ("mongodb", "mongodb",16999)
#'python', '2014-01-16
# 
#Seeded
# "java", 14780), ("ruby", 17184), ("perl", 25893), (javascript, ), ("html", 15592),("iphone", 21253),
#("angularjs", 87663), ("django", 16135), ("android", 16680) ('jquery', 15594), ("css", 15593), ('ajax', 16022), 
#('json', 44410), ("c++", "c%2B%2B", 14779), (".net", "text=.net", 14782), ("php", "php", 14776), ("c", "c", 23388)
#("ruby-on-rails", "ruby-on-rails", 169726), ("c#", "c%23", 16020) ("linux", "linux", 31586), ("sql server", "sql-server", 17241)
# 16+zlib.MAX_WBITS ("mysql", "mysql", 16309), ("bash", "bash", 32749), ("asp.net", "asp.net", 17240), ("xml", "xml", 21232)
#("node.js", "node.js", 17000), ("wordpress", "wordpress", 19006), ("spring", "spring", 45160), ("xml", "xml", 21232)
#("wpf", "wpf", 30552)xcode, 
# r, eclipse, vb.net, , wordpress, facebook, 
 #(mysql, mysql, 16309) ("regex", "regex", 76488), ("oracle", "oracle", 59776), ("git", "git", 21135), ("apache", "apache", 24754)]

#("sqlite", "sqlite", 72469), ("bootstrap", "twitter-bootstrap", 84038), ("scala", "scala", 37332), ("codeigniter", "codeigniter", 16749)

#["java", "ruby", "perl", "javascript", "python", "html", "iphone", "angularjs", "django", "android", "jquery", "css""ajax", "json", "c++", ".net", "php", "c", "c#", "linux", "ruby-on-rails", "sql server", "mysql", "bash", "asp.net", "xml", "node.js", "wordpress", "sring", "xml", "wpf", "r", "ecplice", "vb.net", "regex", "oracle", "git", "apache"]

