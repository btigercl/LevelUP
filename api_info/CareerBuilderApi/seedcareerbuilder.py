from careerbuilder import CareerBuilder 
import os
from unicodedata import normalize  
import request

DEV_KEY = os.environ.get("CareerBuilder") 
cb =CareerBuilder(DEV_KEY)

def careerbuilder(searched_skill, searched_skills_id):
	results = cb.job_search(Category="JN008" "JN004" Skills=searched_skill)
		print results
	drilldown = results["ResponseJobSearch"]["Results"]["JobSearchResult"]
	for sub_dict in drilldown:
		templist = model.Skill_Demand_Location()
		templist.date_posted =
		templist.jobtitle = sub_dict['JobTitle']
		templist.skill = searched_skill
		templist.AL_skill_id = searched_skills_id
		templist.company = sub_dict["Company"]
		templist.ONetjobtitle = sub_dict["ONetFriendlyTitle"]
		templist.tease = sub_dict["DescriptionTeaser"]
		templist.location = sub_dict["Location"]s
		templist.latitude = sub_dict["LocationLatitude"]
		templist.longitude = sub_dict["LocationLongitude"]
		session.add(templist)
    session.commit()





#Keyword=