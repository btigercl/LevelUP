import requests
import os
import json 
from unicodedata import normalize  
import csv

def urlmaker(id, token):
	return "https://api.angel.co/1/tags/" + id  + "/jobs?access_token=" + token


def ALskillcall(id, skill_name):
	#The main function seeds the job listing table. It needs to check the job ID against id's in the job listing table to avoid dups
	token = os.environ.get("AngelList_Token")
	req = requests.get(urlmaker(str(id), token)).json()
	num_pages = req['last_page']
	
	skill_dict = {}
	total = 0

	for page in range(2, 3):
		req = requests.get(urlmaker(str(id), token), params={'page' : page}).json()		 
		
		intial_dict = req["jobs"]

		for subdict in intial_dict:
			tag_tups = []
			total = total + 1 	
			for tag in subdict["tags"]:
				tag_tups.append((tag["id"], tag["display_name"], tag["name"], tag["tag_type"]))
				for tup in tag_tups:
					if "SkillTag" in tup:
						skill_dict[normalize('NFKD', tup[1]).encode('ascii', 'ignore')] = skill_dict.get(normalize('NFKD', tup[1]).encode('ascii', 'ignore'), 0) + 1
	
	dict_list = []                                                                                                                      
	for skill in skill_dict:
		dict_list.append({"source": skill_name, "name": skill, "count": skill_dict.get(skill)})
	final = {"main_skill": skill_name, "children": dict_list}   	 				
	return final

# ALskillcall(14775, "python")

# if __name__ == "__main__":
#     main()
