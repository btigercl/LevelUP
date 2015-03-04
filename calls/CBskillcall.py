from careerbuilder import CareerBuilder 
import os 
from unicodedata import normalize 

DEV_KEY = os.environ.get("CareerBuilder") 

cb =CareerBuilder(DEV_KEY)

def cbskill(skill):
	location_dict_list = []
	results = cb.job_search(Category="JN008" "JN004", Skills= skill)
	drilldown = results["ResponseJobSearch"]["Results"]["JobSearchResult"]
	for sub_dict in drilldown:
		latitude = sub_dict["LocationLatitude"]
		longitude = sub_dict["LocationLongitude"]
		location = sub_dict["Location"]
		latitude_clean = float(normalize('NFKD', latitude).encode('ascii', 'ignore'))
		longitude_clean = float(normalize('NFKD', longitude).encode('ascii', 'ignore'))
		location_clean =  (normalize('NFKD', location).encode('ascii', 'ignore'))
		# jobtitle = sub_dict['JobTitle']
		location_dict_list.append({"type":"Feature", "geometry":{"type": "Point", "coordinates":[latitude_clean, longitude_clean]}, "properties":{"name": location_clean}})
	final_dict = {"type": "FeatureCollection", "features": location_dict_list}
	print final_dict
	return final_dict