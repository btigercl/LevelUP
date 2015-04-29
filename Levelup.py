from flask import Flask, render_template, redirect, request, session, flash, g, url_for, jsonify 
import jinja2
import os
from database import slimmodel, jsonmodel
from calls import ALskillcall, ALlocation, CBskillcall
import json
import pprint
from unicodedata import normalize  
import trend
import time
import datetime
import urllib
import urlparse
# from werkzeugs.contrib.profiler import ProfilerMiddleware

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.jinja_env.undefined = jinja2.StrictUndefined

# app.config['PROFILE'] = True

# app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])

@app.route("/")
def landing():
	"""Leads into site where user picks throughline skill"""
	skills = slimmodel.get_trend_skill_name()
	session['skill'] = None
	skill_list = []
	for skill in skills:
			skill_list.append(skill[0]) 
	return render_template("landing.html", skills=skill_list)

@app.route("/skill_sets", methods=["GET"])
def skill_sets():
	"""This should render the jinja insert for the graphical representation of skill clusters"""
	if session.get('skill') == None:
		session['skill'] = request.args.get("selected_landing_skill")
	print session 
	skills = slimmodel.get_trend_skill_name()
	skill_list = []
	for skill in skills:
			skill_list.append(skill[0]) 
	return render_template("clusters.html", skills=skill_list)

@app.route("/skill_angelList_call", methods=["GET"])
def skill_angelList_call():
	"""This makes a dynamic call to AngleList for related skills to the user selected skill"""
	skill_name = request.args.get("selected_skill")
	skill_normalize = normalize('NFKD', skill_name).encode('ascii', 'ignore') 
	skill = skill_normalize.lower()
	skill_obj = slimmodel.get_skill_by_tagname(skill_name.lower())
	skill_id_to_send = skill_obj.id
	json_db_oject = jsonmodel.get_object_by_skill_id(skill_id_to_send)
	current_time_epoch = time.time()
	current_time = datetime.date.today()
	expiration_date = current_time_epoch - 259200
	if json_db_oject == None:	
		AL_skills_dict = ALskillcall.ALskillcall(skill_id_to_send, skill_name)
		json_translated = json.dumps(AL_skills_dict) 
		jsonmodel.add_skill_object(skill_id_to_send, skill, json_translated, current_time)
		jsoned = jsonify(AL_skills_dict) 
		return jsoned 
	elif date_converstion(json_db_oject.date_stored) < expiration_date:
		AL_skills_dict = ALskillcall.ALskillcall(skill_id_to_send, skill_name)
		json_translated = json.dumps(AL_skills_dict) 
		jsonmodel.updating_skill_object(skill_id_to_send, json_translated, current_time)
		jsoned = jsonify(AL_skills_dict) 
		return jsoned
	else:
		json_dict = json.loads(json_db_oject.skill_obj)
		json_to_send = jsonify(json_dict)
		return json_to_send

@app.route("/trends")
def trends():
	"""This should render the jinja insert for the trends. This should hold the alorythm 
	for line graphs"""
	trend_skill_list = slimmodel.get_trend_skill_name()	
	skill_list = []
	for skill in trend_skill_list:
			skill_list.append(skill[0])
	return render_template("trends.html", trends=skill_list)

@app.route("/db_call_trend", methods=["GET"])
def db_call_trend_lanuage():
	trend1 = request.args.get("selected_trend1")
	trend2 = request.args.get("selected_trend2")
	trend3 = request.args.get("selected_trend3")
	print trend1, trend2, trend3
	if trend2 == None and trend3 == None:
		number_crunch = trend.creating_trend_dict(trend1)
		trends_dict= {"trends": number_crunch}
		jsoned_trends = jsonify(trends_dict)
	else:	
		number_crunch = trend.creating_multi_trend_dict(trend1, trend2, trend3)
		trends_dict= {"trends": number_crunch}
		jsoned_trends = jsonify(trends_dict)
	return jsoned_trends

@app.route("/geographic_demand")
def geographic_demand():
	"""Render jinja insert for geographic_demands. Map of geographic demand for skill set""" 
	skills = slimmodel.get_trend_skill_name()
	skill_list = []
	for skill in skills:
			skill_list.append(skill[0]) 
	return render_template("geo.html", skills = skill_list)

@app.route("/geographic_demand_skill", methods=["GET"])
def geographic_demand_skill():
	"""This makes a dynamic call to CareerBuilder to return lat/long/location of demand for a skill set"""
	skill_name = request.args.get("selected_geo_skill")
	skill = normalize('NFKD', skill_name).encode('ascii', 'ignore') 
	geoskill = "geo" + normalize('NFKD', skill_name).encode('ascii', 'ignore') 
	skill_obj = slimmodel.get_skill_by_tagname(skill)
	skill_id_to_send = skill_obj.id
	json_db_oject = jsonmodel.get_object_by_skill_id(2 + skill_id_to_send)
	current_time_epoch = time.time()
	current_time = datetime.date.today()
	expiration_date = current_time_epoch - 259200
	if json_db_oject == None:
		AL_location_dict = ALlocation.ALlocationcall(skill_id_to_send, skill_name)
		json_translated = json.dumps(AL_location_dict) 
		jsonmodel.add_skill_object(2 + skill_id_to_send, "geo" + skill, json_translated, current_time)
		jsoned = jsonify(AL_location_dict) 
		return jsoned
	elif date_converstion(json_db_oject.date_stored) < expiration_date:
		AL_location_dict= ALlocation.ALlocationcall(skill_id_to_send, skill_name)
		json_translated = json.dumps(AL_location_dict) 
		jsonmodel.updating_skill_object("geo" + skill, json_translated, current_time)
		jsoned = jsonify(AL_location_dict) 
		return jsoned
	else:
		json_dict = json.loads(json_db_oject.skill_obj)
		print json_dict
		json_to_send = jsonify(json_dict)
		return json_to_send

@app.route("/emerging_tech")
def emerging_tech():
	"""Render jinja insert for emerging_tech.""" 
	return render_template("emerging_tech.html")

@app.route("/cookies")
def cookies_storage():
	"""om-nom-nom"""
	skill = session.get('skill')
	print str(skill)
	skill_to_send = json.dumps({"skill": skill})
	return skill_to_send

def date_converstion(date):
	"""changes reable dates to unix time"""
	date_string = str(date)
	date_time = date_string[0:10]
	cleandate = datetime.datetime.strptime(date_time, '%Y-%m-%d')
	converted_date = time.mktime(cleandate.timetuple())
	return int(converted_date)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # print "port: " + str(port)
    app.run(debug="No_DEBUG", host="0.0.0.0", port=port)
