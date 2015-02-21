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
	num_pages = req['last_page']

	for page in range(2, num_pages + 1):
		req = requests.get("https://api.angel.co/1/jobs?access_token=" + token, params={'page' : page}).json()		
		
		# roletag_dict = {}
		skill_dict = {}
		intial_dict = req["jobs"]
		subdict in intial_dict:
		job_title = subdict["title"]	
		for tag in subdict["tags"]:
			tag_tups.append((tag["id"], tag["display_name"], tag["name"], tag["tag_type"]))
		for tup in tag_tups:
			if "SkillTag" in tup:
				skill_dict[(skill_cleanse(tup))] = skill_dict.get(skill_cleanse(tup), 0) + 1
			# if "RoleTag" in tup:
			# 	roletag_dict[roletag_cleanse(tup)] = roletag_dict(roletag_cleanse(tup), 0) + 1	
		return skill_dict

def skill_cleanse(tup):
	skill_list = []
	for item in tup:
		if item != "SkillTag":
			if type(item) != int:
				skill_list.append(normalize('NFKD', item).encode('ascii', 'ignore'))
			else:
				skill_list.append(item)
	return skill_tagdisplayname = skill_list[1]



# def roletag_cleanse(tup, job_title):
# 	roletag_list = []
# 	for item in tup:
# 		if item != "RoleTag":
# 			if type(item) != int:
# 				roletag_list.append(normalize('NFKD', item).encode('ascii', 'ignore'))
# 			else:
# 				roletag_list.append(item)					
# 	return job_tagdisplayname = roletag_list[1]

if __name__ == "__main__":
	main()

