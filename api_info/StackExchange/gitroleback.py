import os
import json
import requests
import time
import datetime
import gzip
import urllib2
from relativedelta import relativedelta


DEV_KEY = os.environ.get("StackExchange_Key")

def date_converstion(date):
    #changes reable dates to unix
    cleandate = datetime.datetime.strptime(date, '%Y-%m-%d')
    converted_date = time.mktime(cleandate.timetuple())
    return str(int(converted_date))

def tag_count_by_month(tag, fromyearmonthday, toyearmonthday, DEV_KEY):
    list = []
    fd = date_converstion(fromyearmonthday)
    td = date_converstion(toyearmonthday)
    addy = ("http://api.stackexchange.com/2.2/tags?fromdate=" + fd + "&todate=" + td + "&order=desc&sort=popular&inname=" + tag + "&site=stackoverflow&key=" + DEV_KEY)
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
    start_date_from = "2008-09-01"
    start_date_to = "2008-09-30"
    tag_count_by_month("python", start_date_from, start_date_to, DEV_KEY)

if __name__ == "__main__":
    main()