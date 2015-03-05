import requests
import os
import json 
from unicodedata import normalize
import geocoder 


def urlmaker(id, token):
	return "https://api.angel.co/1/tags/" + id  + "/jobs?access_token=" + token 

def ALlocationcall(id, skill_name):
	token = os.environ.get("AngelList_Token")
	req = requests.get(urlmaker(str(id), token)).json()
	num_pages = req['last_page']

	for page in range(2, 3):
		req = requests.get(urlmaker(str(id), token), params={'page' : page}).json()
		

	intial_dict = req["jobs"]
	location = []
	tag_tup = []
	geo_dict = []
	for subdict in intial_dict:
		# job_id = subdict["id"]
		# date_job_posted = subdict["created_at"]
		# company = subdict["startup"]["name"]
		# job_description = subdict['description']
		# job_title = subdict["title"]
		for tag in subdict["tags"]:
			tag_tup.append((tag["id"], tag["display_name"], tag["name"], tag["tag_type"]))
	
	for tup in tag_tup:
		if "LocationTag" in tup:
			location.append(normalize('NFKD', tup[1]).encode('ascii', 'ignore'))
	
	for city in location:
		if city != "Anywhere" or city != "None":
			g = geocoder.google(city)
			geo_dict.append(g.geojson)
			# geo_dict.append({"type":"Feature", "geometry":{"type": "Point", "coordinates": lat_long}, "properties":{"name": city}})

	final_dict = {"type": "FeatureCollection", "features": geo_dict}
	return final_dict




# ALlocationcall(16309, "mysql")