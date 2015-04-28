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
	location = []
	roletag = []
	job_id = subdict["id"]
	date_job_posted = subdict["created_at"]
	company = subdict["startup"]["name"]
	job_description = subdict['description']
	job_title = subdict["title"]
	for tag in subdict["tags"]:
		skills.append((tag["id"], tag["display_name"], tag["name"], tag["tag_type"]))
	for tup in skills:
		if "SkillTag" in tup:
			for item in tup:
				if item != "SkillTag":
					if type(item) != int:
						skill_list.append(normalize('NFKD', item).encode('ascii', 'ignore'))
					else:
						skill_list.append(item)
		if "LocationTag" in tup:
			for item in tup:
				if item != "LocationTag":
					if type(item) != int:
						location.append(normalize('NFKD', item).encode('ascii', 'ignore'))
					else:
						location.append(item)

		if "RoleTag" in tup:
			for item in tup:
				if item != "RoleTag":
					if type(item) != int:
						roletag.append(normalize('NFKD', item).encode('ascii', 'ignore'))
					else:
						roletag.append(item)					
	print ("Job ID: %r \
		Date Posted: %r\
		Company: %s \
		Location: %r \
		Job Description: %s \
		Job Title: %s \
		RoleTag: %r \
		Skills: %s") % (job_id, date_job_posted, company, location, job_description, job_title, roletag, skill_list)	
		


	# for skill in skills:
	# 	skill_list.append(normalize('NFKD', skill).encode('ascii', 'ignore'))



# num_pages = req['last_page']

# for page in range(2, num_pages + 1):
#     req = requests.get("https://api.angel.co/1/jobs?access_token" + token, params={'page': page).json()
#     print req['page']


# json.load(req)