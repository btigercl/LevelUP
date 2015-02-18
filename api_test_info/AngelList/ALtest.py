import requests
import os
import json 
from unicodedata import normalize  

token = os.environ.get("AngelList_Token")

req = requests.get("https://api.angel.co/1/jobs?access_token=" + token).json()

intial_dict = req["jobs"]

for subdict in intial_dict:
	skills = []
	skill_list = []
	job_id = subdict["id"]
	date_job_posted = subdict["created_at"]
	company = subdict["startup"]["name"]
	job_description = subdict['description']
	job_title = subdict["title"]
	for tag in subdict["tags"]:
		skills.append((tag["name"], tag["id"], tag["display_name"], tag["tag_type"]))
	for rtup
	# print ("Job ID: %r \
	# 	Date Posted: %r\
	# 	Company: %s \
	# 	Job Description: %s \
	# 	Job Title: %s \
	# 	Skills: %s"
	# 	 % (job_id, date_job_posted, company, job_description, job_title, skills)	
		


	# for skill in skills:
	# 	skill_list.append(normalize('NFKD', skill).encode('ascii', 'ignore'))

	# print skills 
	# 	)

	# # print job_id, date_job_posted, company, job_description, job_title, skills

# print "Skill Tag: %s \
# 				Skill Tag ID: %s \
# 				Skill Display Name: %s" % (tag_name, tag_id, display_name)

# num_pages = req['last_page']

# for page in range(2, num_pages + 1):
#     req = requests.get("https://api.angel.co/1/jobs?access_token" + token, params={'page': page).json()
#     print req['page']


# json.load(req)