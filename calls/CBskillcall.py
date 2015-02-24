from careerbuilder import CareerBuilder 
import os 
from unicodedata import normalize 

DEV_KEY = os.environ.get("CareerBuilder") 

cb =CareerBuilder(DEV_KEY)

def cbskill(skill):
	lat_lon_tups = []
	results = cb.job_search(Category="JN008" "JN004", Skills= skill)
	drilldown = results["ResponseJobSearch"]["Results"]["JobSearchResult"]
	for sub_dict in drilldown:
		latitude = sub_dict["LocationLatitude"]
		longitude = sub_dict["LocationLongitude"]
		location = sub_dict["Location"]
		# jobtitle = sub_dict['JobTitle']
		lat_lon_tups.append((normalize('NFKD', location).encode('ascii', 'ignore'), normalize('NFKD', latitude).encode('ascii', 'ignore'), normalize('NFKD', longitude).encode('ascii', 'ignore')))
	return lat_lon_tups 