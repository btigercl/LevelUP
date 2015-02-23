import requests
import os
import json 
from unicodedata import normalize  
import csv


def ALjobtitlecall(id):
	#The main function seeds the job listing table. It needs to check the job ID against id's in the job listing table to avoid dups
	token = os.environ.get("AngelList_Token")
	req = requests.get("https://api.angel.co/1/tags/" + str(id)  + "/jobs?access_token=" + token).json()
	num_pages = req['last_page']
	
	jobtitle_dict = {}
	for page in range(1, num_pages + 1):
		req = requests.get("https://api.angel.co/1/jobs?access_token=" + token, params={'page' : page}).json()		
		
		
		intial_dict = req["jobs"]

		for subdict in intial_dict:
			tag_tups = []	
			for tag in subdict["tags"]:
				tag_tups.append((tag["id"], tag["display_name"], tag["name"], tag["tag_type"]))
				for tup in tag_tups:
					if "RoleTag" in tup:
						jobtitle_dict[normalize('NFKD', tup[1]).encode('ascii', 'ignore')] = jobtitle_dict.get(normalize('NFKD', tup[1]).encode('ascii', 'ignore'), 0) + 1
	print jobtitle_dict
	return jobtitle_dict 


fun = ALjobtitlecall(14775)