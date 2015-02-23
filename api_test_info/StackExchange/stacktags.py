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

def tag_count_by_day(tag, tag_id, fromyearmonthday, toyearmonthday, DEV_KEY):
	#this adds number of questions per day about a specific tag to the database 

	list = []
	backoff = 1
	response = requests.get("http://api.stackexchange.com/2.2/tags?fromdate=" + str(fromyearmonthday) + "&todate=" + str(toyearmonthday) + "&order=desc&sort=popular&inname=" + tag + "&site=stackoverflow&key=" + DEV_KEY) 
	if "backoff" in response.headers:
		backoff = int(response.headers["backoff"])
	total = 0
	parse = response.json()["items"]
	for sub in parse:
		count = sub["count"]
		total = total + count
	date = datetime.datetime.fromtimestamp(fromyearmonthday)
	trend_id = fromyearmonthday + tag_id
	trends = slimmodel.Stack_Overflow_Trends(id=trend_id, skill_id = tag_id, skill = tag, date_epoc = date, question_count = total)
	slimmodel.Session.add(trends)
	slimmodel.Session.commit()
	print backoff
	return backoff

# def question_county_by_day(fromyearmonthday, toyearmonthday, DEV_KEY):
# 	#this adds number of questions per day to database 

# 	response = requests.get("http://api.stackexchange.com//2.2/questions?fromdate=" + str(fromyearmonthday) + "&todate=" + str(toyearmonthday) + "&order=desc&sort=activity&site=stackoverflow" + DEV_KEY)
# 	if "backoff" in response.headers:
# 		backoff = int(response.headers["backoff"])
# 		total = 0
# 	parse = response.json()["items"]
# 	for sub in parse:
# 		count = sub["count"]
# 		total = total + count 
# 		session.add(temp_movie)
# 	questions_id = 1 + fromyearmonthday 
# 	questions = slimmodel.Stack_Overflow_Trends(id = questions_id, skill_id = 1, skill = question, date_epoc = fromyearmonthday, question_count = total)
# 	session.add(questionse)
# 	session.commit()


def main():
	"""this should make calls to stackexchange every .1 to retreive the number of questions per day since stack
	overflow's founding until present"""  

	start_date_from = date_converstion("2010-04-19")
	start_date_to = date_converstion("2010-04-20") 
	current = (time.time())
	while start_date_to <= current:
		time.sleep(tag_count_by_day("python", 14775, start_date_from, start_date_to, DEV_KEY))    
		start_date_from = start_date_from + 86400
		start_date_to = start_date_to + 86400 

if __name__ == "__main__":
	main()


	# 16+zlib.MAX_WBITS