import os
from unicodedata import normalize 
import json
import requests
import time
import datetime
from StringIO import StringIO
import gzip
import urllib2


DEV_KEY = os.environ.get("StackExchange_Key")


def tag_count_by_month(tag, fromyearmonthday, toyearmonthday, DEV_KEY):
    df = datetime.datetime.strptime(fromyearmonthday, '%Y-%m-%d')
    dt = datetime.datetime.strptime(toyearmonthday, '%Y-%m-%d')
    fd = time.mktime(df.timetuple())
    td = time.mktime(dt.timetuple())
    addy = ("http://api.stackexchange.com/2.2/tags?fromdate=" + str(int(fd)) + "&todate=" + str(int(td)) + "&order=desc&sort=popular&inname=" + tag + "&site=stackoverflow&key=" + DEV_KEY)
    req = urllib2.Request(addy)
    req.add_header('Accept-encoding', 'gzip')
    response = urllib2.urlopen(req)
    buf = StringIO( response.read())
    f = gzip.GzipFile(fileobj=buf)
    data = f.read()
    print json.loads(data)["items"]

    
    # print req.read()
    # print io
    # for item in req:
    #   print item
    # pobject= json.loads(req)
    # print pobject["items"]


tag_count_by_month("python","2008-09-01", "2008-09-30", DEV_KEY)

#df = datetime.datetime.strptime('2012-02-09', '%Y-%m-%d')
# test = requests.get("https://api.stackexchange.com/2.2/info?site=stackoverflow&key=" + DEV_KEY)
# for item in test:
    # print item 

    # 16+zlib.MAX_WBITS