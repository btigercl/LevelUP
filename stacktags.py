import os
import json
import requests
import time
import datetime
import gzip
import urllib2
from StringIO import StringIO
from relativedelta import relativedelta
import slimmodel 


DEV_KEY = os.environ.get("StackExchange_Key")

def date_converstion(date):
    #changes reable dates to unix
    cleandate = datetime.datetime.strptime(date, '%Y-%m-%d')
    converted_date = time.mktime(cleandate.timetuple())
    return int(converted_date)

def tag_count_by_day(tag, tag_id, fromyearmonthday, toyearmonthday, DEV_KEY):
    #this adds number of questions per day about a specific tag to the database 

    list = []
    addy = ("http://api.stackexchange.com/2.2/tags?fromdate=" + str(fromyearmonthday) + "&todate=" + str(toyearmonthday) + "&order=desc&sort=popular&inname=" + tag + "&site=stackoverflow&key=" + DEV_KEY)
    req = urllib2.Request(addy)
    req.add_header('Accept-encoding', 'gzip')
    response = urllib2.urlopen(req)
    buf = StringIO( response.read())
    f = gzip.GzipFile(fileobj=buf)
    data = f.read()
    total = 0
    parse = json.loads(data)["items"]
    for sub in parse:
        count = sub["count"]
        total = total + count
    trend_id = fromyearmonthday + tag_id
    trends = Slimmodle.Stack_Overflow_Trends(id=trend_id, skill_id = tag_id, skill = tag, date_epoc =fromyearmonthday, question_count = total)
    session.add(trends)
    session.commit()

# def question_county_by_day(fromyearmonthday, toyearmonthday, DEV_KEY):
#     #this adds number of questions per day to database 

#     addy = ("http://api.stackexchange.com//2.2/questions?fromdate=" + str(fromyearmonthday) + "&todate=" + str(toyearmonthday) + "&order=desc&sort=activity&site=stackoverflow" + DEV_KEY)
#     req = urllib2.Request(addy)
#     req.add_header('Accept-encoding', 'gzip')
#     response = urllib2.urlopen(req)
#     buf = StringIO( response.read())
#     f = gzip.GzipFile(fileobj=buf)
#     data = f.read()
#     total = 0
#     parse = json.loads(data)["items"]
#     for sub in parse:
#         count = sub["count"]
#         total = total + count 
#         session.add(temp_movie)
#     questions_id = 1 + fromyearmonthday 
#     questions = Slimmodle.Stack_Overflow_Trends(id = questions_id, skill_id = 1, skill = question, date_epoc = fromyearmonthday, question_count = total)
#     session.add(questionse)
#     session.commit()


def main():
    """this should make calls to stackexchange every .1 to retreive the number of questions per day since stack
    overflow's founding until present"""  

    start_date_from = date_converstion("2008-09-15")
    start_date_to = date_converstion("2008-09-16") 
    current = (time.time())
    while start_date_to <= current:
        tag_count_by_day("python", start_date_from, start_date_to, DEV_KEY)    
        start_date_from = start_date_from + 86400
        start_date_to = start_date_to + 86400 
        time.sleep(0.1)
        print start_date_from
        print start_date_to

if __name__ == "__main__":
    main()


    # 16+zlib.MAX_WBITS