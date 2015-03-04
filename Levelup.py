from flask import Flask, render_template, redirect, request, session, flash, g, url_for, jsonify
from careerbuilder import CareerBuilder 
import jinja2
import os
from db import slimmodel
from calls import ALskillcall, ALjobtitlecall, CBskillcall
import json
import pprint
from unicodedata import normalize  
import trend

app = Flask(__name__)
app.secret_key = 'kittens'
app.jinja_env.undefined = jinja2.StrictUndefined


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
	pp = pprint.PrettyPrinter(indent = 4)
	pp.pprint(AL_skills_dict)
	jsoned = jsonify(AL_skills_dict) 
	return jsoned
	# return render_template("skill_response.html", skill_dict =AL_skills_dict, skills=skills)

@app.route("/trends")
def trends():
	"""This should render the jinja insert for the trends. This should hold the alorythm 
	for line graphs"""
	trend_skill_list = slimmodel.get_trend_skill_name() 
	skill_list = []
	for skill in trend_skill_list:
		if skill[0] not in skill_list and skill[0] != "question":
			skill_list.append(skill[0])
	return render_template("trends.html", trends=skill_list)

@app.route("/db_call_trend", methods=["GET"])
def db_call_trend_lanuage():
	trend1 = request.args.get("selected_trend1")
	trend2 = request.args.get("selected_trend2")
	trend3 = request.args.get("selected_trend3")
	print trend1, trend2, trend3
	number_crunch = trend.cal_trend_precent_by_year(trend1)
	number_crunch2 = trend.cal_trend_precent_by_year(trend2)
	number_crunch3 = trend.cal_trend_precent_by_year(trend3)
	# print number_crunch3, number_crunch2, number_crunch
	trends_dict = {"trendData1": number_crunch, "trendData2": number_crunch2, "trendData3": number_crunch3}
	print trends_dict
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
	skill = request.args.get("selected_skill")
	geoJSON_dict = CBskillcall.cbskill(skill)
	print geoJSON_dict
	return jsonify(geoJSON_dict)
	#pass to D3
	# return render_template("geo_response.html", geo_tups=lat_long_tups, skills = skills)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
