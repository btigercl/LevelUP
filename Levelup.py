from flask import Flask, render_template, redirect, request, session, flash, g, url_for, jsonify
from careerbuilder import CareerBuilder 
import jinja2
import os
from db import slimmodel
from calls import ALskillcall, ALlocation, CBskillcall
import json
import pprint
from unicodedata import normalize  
import trend
from werkzeug.contrib.profiler import ProfilerMiddleware

app = Flask(__name__)
app.secret_key = 'kittens'
app.jinja_env.undefined = jinja2.StrictUndefined

app.config['PROFILE'] = True

app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])

@app.route("/")
def landing():
	"""Home page and lead into site. Basic html/css/bootstrap with a kind of overview of the site"""
	return render_template("landing.html")

@app.route("/skill_sets")
def skill_sets():
	"""This should render the jinja insert for the graphical representation of skill clusters"""
	skills = slimmodel.get_skills_list() 
	return render_template("clusters.html", skills=skills)

@app.route("/skill_angelList_call", methods=["GET"])
def skill_angelList_call():
	"""This makes a dynamic call to AngleList for related skills to the user selected skill"""
	skill_id = request.args.get("selected_skill")
	skills = slimmodel.get_skills_list()
	skill_obj = slimmodel.get_skill_by_id(int(skill_id))
	skill_name = skill_obj.tagdisplayname
	AL_skills_dict = ALskillcall.ALskillcall(skill_id, skill_name)
	# pp = pprint.PrettyPrinter(indent = 4)
	# pp.pprint(AL_skills_dict)
	jsoned = jsonify(AL_skills_dict) 
	return jsoned

@app.route("/trends")
def trends():
	"""This should render the jinja insert for the trends. This should hold the alorythm 
	for line graphs"""
	trend_skill_list = slimmodel.get_trend_list()	
	skill_list = [(skill.skill, skill.skill_id) for skill in trend_skill_list if skill.skill != "question"]
	skill_set = set(skill_list)
	skills_list_dd = list(skill_set)
	skills_list_dd.sort()

	# skill_list = []
	# for skill in trend_skill_list:
	# 	if skill.skill not in skill_list and skill.skill != "question":
	# 		skill_list.append(skill)
	return render_template("trends.html", trends=skills_list_dd)

@app.route("/db_call_trend", methods=["GET"])
def db_call_trend_lanuage():
	trend_1_id = request.args.get("selected_trend1")
	trend_2_id = request.args.get("selected_trend2")
	trend_3_id = request.args.get("selected_trend3")
	print trend_1_id, trend_2_id, trend_3_id
	skill_1_name = slimmodel.get_trend_by_skill_id(int(trend_1_id))
	skill_2_name = slimmodel.get_trend_by_skill_id(int(trend_2_id))
	skill_3_name = slimmodel.get_trend_by_skill_id(int(trend_3_id))
	print skill_1_name, skill_2_name, skill_3_name
	number_crunch = trend.cal_trend_precent_by_year(skill_1_name)
	number_crunch2 = trend.cal_trend_precent_by_year(skill_2_name)
	number_crunch3 = trend.cal_trend_precent_by_year(skill_3_name)
	trends_dict = {"trendData1": number_crunch, "trendData2": number_crunch2, "trendData3": number_crunch3}
	jsoned_trends = jsonify(trends_dict)
	return jsoned_trends

@app.route("/geographic_demand")
def geographic_demand():
	"""Render jinja insert for geographic_demands. Map of geographic demand for skill set""" 
	skills = slimmodel.get_skills_list()
	return render_template("geo.html", skills = skills)

@app.route("/geographic_demand_skill", methods=["GET"])
def geographic_demand_skill():
	"""This makes a dynamic call to CareerBuilder to return lat/long/location of demand for a skill set"""
	skill_id = request.args.get("selected_geo_skill")
	skill_obj = slimmodel.get_skill_by_id(int(skill_id))
	skill_name = skill_obj.tagdisplayname
	geoJSON_dict = ALlocation.ALlocationcall(skill_id, skill_name)
	return jsonify(geoJSON_dict)
	#pass to D3
	# return render_template("geo_response.html", geo_tups=lat_long_tups, skills = skills)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
