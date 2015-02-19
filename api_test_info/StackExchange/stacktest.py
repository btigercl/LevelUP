import os
import stackexchange
from unicodedata import normalize 
import json
import requests


DEV_KEY = os.environ.get("StackExchange_Key")

# data = requests.get("http://api.joelfanclub.stackexchange.com/jobs").json()
so = stackexchange.Site(stackexchange.StackOverflow, DEV_KEY)

def top_tags():
	for tag in so.toptag(pagesize=10):
		print tag.tag_name()

def tags(name):
	t =  so.tag(name) 
	print t.name() 
	print t.count()

def questions(tag):
	for question in so.questions(tagged=[tag], pagesize=10):
		print question
		assert 'python' in question.tags	


top_tags()


so.impose_throttling = True
so.throttle_stop = False

#when aelse failsll 
#'api.joelfanclub.stackexchange.com'