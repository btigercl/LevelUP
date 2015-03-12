import requests
import os
import json 
from unicodedata import normalize  
import csv

def urlmaker(id, token):
	return "https://api.angel.co/1/tags/" + id  + "/jobs?access_token=" + token


def ALskillcall(id, skill_name):
	token = os.environ.get("AngelList_Token2")
	req = requests.get(urlmaker(str(id), token)).json()
	num_pages = req['last_page']
	
	skill_dict = {}
	skills_tups = []
	roletag_dict = {}
	total = 0

	for page in range(1, 2):
		req = requests.get(urlmaker(str(id), token), params={'page' : page}).json()		 
		
		intial_dict = req["jobs"]
		for subdict in intial_dict:
			tag_tups = []
			skill_tup = []
			total = total + 1 	
			for tag in subdict["tags"]:
				tag_tups.append((tag["id"], tag["display_name"], tag["name"], tag["tag_type"]))
				# skill_tup = []
				# roletag_dict = []
				for tup in tag_tups:
					if "SkillTag" in tup and skill_name not in tup:
						skill_dict[normalize('NFKD', tup[1]).encode('ascii', 'ignore')] = skill_dict.get(normalize('NFKD', tup[1]).encode('ascii', 'ignore'), 0) + 1
						skill_tup.append(normalize('NFKD', tup[1]).encode('ascii', 'ignore'))
					if "RoleTag" in tup:
						roletag_dict[normalize('NFKD', tup[1]).encode('ascii', 'ignore')] = roletag_dict.get(normalize('NFKD', tup[1]).encode('ascii', 'ignore'), 0) + 1			
			skills_tups.append((skill_tup))



	sorted_role_list = sort_dicts_by_value(roletag_dict)
	# sub_groups = creating_sub_groups(sorted_dict, skill_dict, skills_tups, skill_name)
	# final_dict = format_dicts(sub_groups)


	dict_list = []                                                                                                                      
	for skill in skill_dict:
		if skill_dict.get(skill) >= 20:
			dict_list.append({"name": skill, "count": skill_dict.get(skill)})
	final = {"name": skill_name, total: total, "roletag_list": sorted_role_list, "children": dict_list} 
	return final   	 				
	# print final

def sort_dicts_by_value(roletag_dict):
	#sort to see what skills are most closely associated with python 
	ordered_roletag_list = []
	values = sorted(roletag_dict.values(), reverse = True) 
	for value in values:
		for role in roletag_dict:
			if roletag_dict.get(role) == value:
				if role not in ordered_roletag_list:
					ordered_roletag_list.append(role)
	return ordered_roletag_list 

# def creating_sub_groups(sorted_dict, skill_dict, skills_tups, skill_name):

# 	sub_dicts = []
# 	passed_through = [skill_name]
# 	mid_range = len(sorted_dict)/4
# 	for i in range(1, mid_range - 1):
# 		skill_sub_dict = {}
# 		for tup in skills_tups:
# 			if sorted_dict[i] in tup:
# 				for item in tup:
# 					if item != sorted_dict[i] and item != skill_name.lower():
# 						skill_sub_dict[item] = skill_sub_dict.get(item, 0) + 1
		
# 		sub_dicts.append({"name": sorted_dict[i], "children": skill_sub_dict})
		# passed_through.append(sorted_dict[i])


	# return sub_dicts

# def format_dicts(sub_groups):
# 	for skill in skill_dict:
# 		dict_list.append({"source": skill_name, "name": skill, "count": skill_dict.get(skill)})
# 	final = {"main_skill": skill_name, "children": dict_list} 
# 	return final

# ALskillcall(14775, "python")