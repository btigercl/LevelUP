import requests
import os
import json 
from unicodedata import normalize  
import slimmodel
import csv


"""This file is designed to make seeding the NexusTable, JobListing Table, JobTitle Table, and the Skill table easily without dups"""
def angellist(session):
	#The main function seeds the job listing table. It needs to check the job ID against id's in the job listing table to avoid dups
	token = os.environ.get("AngelList_Token")
	req = requests.get("https://api.angel.co/1/jobs?access_token=" + token).json()
	num_pages = req['last_page']

	for page in range(2, num_pages + 1):
		req = requests.get("https://api.angel.co/1/jobs?access_token=" + token, params={'page' : page}).json()		
		
		intial_dict = req["jobs"]

		for subdict in intial_dict:
			tag_tups = []
			job_title = subdict["title"]	
			for tag in subdict["tags"]:
				tag_tups.append((tag["id"], tag["display_name"], tag["name"], tag["tag_type"]))
			for tup in tag_tups:
				if "SkillTag" in tup:
					skill_list = []
					for item in tup:
						if item != "SkillTag":
							if type(item) != int:
								skill_list.append(normalize('NFKD', item).encode('ascii', 'ignore'))
							else:
								skill_list.append(item)
					skilltag = slimmodel.Skills(id = skill_list[0], tagdisplayname = skill_list[1], tagname = skill_list[2])
					session.merge(skilltag) 
					session.commit()

				if "RoleTag" in tup:
					roletag_list = []
					for item in tup:
						if item != "RoleTag":
							if type(item) != int:
								roletag_list.append(normalize('NFKD', item).encode('ascii', 'ignore'))
							else:
								roletag_list.append(item)					
					job = slimmodel.JobTitle(id = roletag_list[0], tagdisplay = roletag_list[1], tagname = roletag_list[2], jobtitle = job_title) 
					session.merge(job) 
					session.commit()


# def skill_cleanse(tup,):
# 	skill_list = []
# 	for item in tup:
# 		if item != "SkillTag":
# 			if type(item) != int:
# 				skill_list.append(normalize('NFKD', item).encode('ascii', 'ignore'))
# 			else:
# 				skill_list.append(item)
# 	skill = slimmodel.Skills 
# 	skill.id = skill_list[0]
# 	skill.tagdisplayname = skill_list[1]
# 	skill.tagname = skill_list[2]
# 	session.merge(skill) 
# 	session.commit()


# def roletag_cleanse(tup, job_title):
# 	roletag_list = []
# 	for item in tup:
# 		if item != "RoleTag":
# 			if type(item) != int:
# 				roletag_list.append(normalize('NFKD', item).encode('ascii', 'ignore'))
# 			else:
# 				roletag_list.append(item)					
# 	job = slimmodel.JobTitle 
# 	job.id = roletag_list[0]
# 	job.tagdisplayname = roletag_list[1]
# 	job.tagname = roletag_list[2]
# 	job.jobtitle = job_title
# 	session.merge(job) 
# 	session.commit()

def main(session):
	# You'll call each of the load_* functions with the session as an argument
	angellist(session)

if __name__ == "__main__":
	s= slimmodel.connect()
	main(s)

# if __name__ == "__main__":
# 	main()