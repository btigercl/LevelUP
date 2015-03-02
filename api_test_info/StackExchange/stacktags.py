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

def stackexchange_call(name, tagurl, skill_id):
	"""this should make calls to stackexchange every .1 to retreive the number of questions per day since stack
	overflow's founding until present"""  

	start_date_from = date_converstion("2008-08-15")
	start_date_to = date_converstion("2008-08-16") 
	current = (time.time())
	while start_date_to <= current:
		time.sleep(tag_count_by_day(name, tagurl, skill_id, start_date_from, start_date_to, DEV_KEY))    
		start_date_from = start_date_from + 86400
		start_date_to = start_date_to + 86400 

def main():
	seeds =	[("ruby-on-rails", "ruby-on-rails", 169726), ("c#", "c%23", 16020)]

	for seed in seeds:
		name = seed[0]
		tagurl = seed[1]
		skill_id = seed[2] 
		stackexchange_call(name, tagurl, skill_id)
		print "done" 


if __name__ == "__main__":
	main()

#To Seed ("ruby-on-rails", "ruby-on-rails", 169726), ("c#", "c%23", 16020), 

# ("ruby-on-rails", 169726s), ("c#", 16020), ("sql", 15850), (objectivec, objective-c, 82326)
 #mysql, asp.net, arrays, bash, node.js


# 
#Seeded
# "java", 14780), ("ruby", 17184), ("perl", 25893), (javascript, ), (python, )("html", 15592),("iphone", 21253),
#("angularjs", 87663), ("django", 16135), ("android", 16680) ('jquery', 15594), ("css", 15593), ('ajax', 16022), 
#('json', 44410), ("c++", "c%2B%2B", 14779), (".net", "text=.net", 14782), ("php", "php", 14776), ("c", "c", 23388)
	# 16+zlib.MAX_WBITS 