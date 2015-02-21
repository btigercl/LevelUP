import requests
import os
import json 
from unicodedata import normalize  
# import slimmodel
# import csv


"""This file is designed to make seeding the NexusTable, JobListing Table, JobTitle Table, and the Skill table easily without dups"""
def main():
	#The main function seeds the job listing table. It needs to check the job ID against id's in the job listing table to avoid dups
	token = os.environ.get("AngelList_Token")
	req = requests.get("https://api.angel.co/1/jobs?access_token=" + token).json()
	intial_dict = req["jobs"]

	for subdict in intial_dict:
		tag_tups = []
		# job_id = subdict["id"]
		# date_job_posted = subdict["created_at"]
		# company = subdict["startup"]["name"]
		# job_description = subdict['description']
		job_title = subdict["title"]	
		for tag in subdict["tags"]:
			tag_tups.append((tag["id"], tag["display_name"], tag["name"], tag["tag_type"]))
		for tup in tag_tups:
			if "SkillTag" in tup:
				skill_cleanse(tup)
			# if "LocationTag" in tup:
			# 	location = locationtag_cleanse(tup)
			if "RoleTag" in tup:
				roletag_cleanse(tup, job_title)	

def skill_cleanse(tup):
	skill_list = []
	for item in tup:
		if item != "SkillTag":
			if type(item) != int:
				skill_list.append(normalize('NFKD', item).encode('ascii', 'ignore'))
			else:
				skill_list.append(item)
		# skill = model.skill 
	skill_id = skill_list[0]
	skill_tagdisplayname = skill_list[1]
	skill_tagname = skill_list[2]
		# session.add(skill) 
  #   session.commit()
	print skill_id, skill_tagdisplayname, skill_tagname
	print skill_list

# def locationtag_cleanse(tup):
# 	location = []
# 	for item in tup:
# 		if item != "LocationTag":
# 			if type(item) != int:
# 				location.append(normalize('NFKD', item).encode('ascii', 'ignore'))
# 	return location

def roletag_cleanse(tup, job_title):
	roletag_list = []
	for item in tup:
		if item != "RoleTag":
			if type(item) != int:
				roletag_list.append(normalize('NFKD', item).encode('ascii', 'ignore'))
			else:
				roletag_list.append(item)					
		# job = model.jobtitle 
	job_id = roletag_list[0]
	job_tagdisplayname = roletag_list[1]
	job_tagname = roletag_list[2]
	job_jobtitle = job_title
	print job_id, job_tagdisplayname, job_tagname, job_jobtitle
	# session.add(skill) 
 #    session.commit()

if __name__ == "__main__":
	main()

# if __name__ == "__main__":
#     s= model.connect()
#     main(s)

# 	for skill in skills:
# 		skill_list.append(normalize('NFKD', skill).encode('ascii', 'ignore'))



# num_pages = req['last_page']

# for page in range(2, num_pages + 1):
#     req = requests.get("https://api.angel.co/1/jobs?access_token" + token, params={'page': page).json()
#     print req['page']


# json.load(req)