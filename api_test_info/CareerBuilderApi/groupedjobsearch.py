from careerbuilder import CareerBuilder 
import SecretKeys
from unicodedata import normalize  

DEV_KEY = SecretKeys.Dev_Key

cb =CareerBuilder(DEV_KEY)

results = cb.job_search(AdvancedGroupingMode=True, EnableCompanyJobTitleCollapse=True, Keyword="python" "django", Category="JN008" "JN004")
print results

drilldown = results["ResponseJobSearch"]["SearchResults"]["GroupedSearchResults"]["JobSearchResult"]

for sub_dict in drilldown:
	company = sub_dict["Company"]
	ONetjobtitle = sub_dict["ONetFriendlyTitle"]
	tease = sub_dict["DescriptionTeaser"]
	detailsURL = sub_dict["JobDetailsURL"]
	latitude = sub_dict["LocationLatitude"]
	longitude = sub_dict["LocationLongitude"]
	location = sub_dict["Location"]
	jobtitle = sub_dict['JobTitle']
	if sub_dict["Skills"] == None:
		skills = sub_dict["Skills"]
	else:
		skills = [] 
		for skill in sub_dict["Skills"]["Skill"]:
			skills.append(normalize('NFKD', skill).encode('ascii', 'ignore'))   
	print "Company %s: JobTitle: %s DescriptionTeaser: %s URL: %s Latitude: %r Longitude: %r Location: %s JobTitle: %s Skills: %r" \
	 %(company, ONetjobtitle, tease, detailsURL, latitude, longitude, location, jobtitle, skills) 