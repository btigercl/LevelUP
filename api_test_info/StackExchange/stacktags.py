import os
import json
import requests
import time
import datetime
import gzip
import urllib2
from StringIO import StringIO
from relativedelta import relativedelta
# import slimmodel 


DEV_KEY = os.environ.get("StackExchange_Key")

def date_converstion(date):
    #changes reable dates to unix
    cleandate = datetime.datetime.strptime(date, '%Y-%m-%d')
    converted_date = time.mktime(cleandate.timetuple())
    return int(converted_date)

def tag_count_by_day(tag, fromyearmonthday, toyearmonthday, DEV_KEY):
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
        name = sub["name"]
        count = sub["count"]
        total = total + count 
        print   name, count
    #     session.add(temp_movie)
    # session.commit()

def main():
    start_date_from = date_converstion("2008-09-01")
    start_date_to = date_converstion("2008-09-02") 
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


#df = datetime.datetime.strptime('2012-02-09', '%Y-%m-%d')
# test = requests.get("https://api.stackexchange.com/2.2/info?site=stackoverflow&key=" + DEV_KEY)
# for item in test:
    # print item 

    # 16+zlib.MAX_WBITS