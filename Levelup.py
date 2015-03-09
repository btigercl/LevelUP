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

@app.route("/skill_sets", methods=["GET"])
def skill_sets():
	"""This should render the jinja insert for the graphical representation of skill clusters"""
	skills = slimmodel.get_skills_list() 
	return render_template("clusters.html", skills=skills)

@app.route("/skill_angelList_call", methods=["GET"])
def skill_angelList_call():
	"""This makes a dynamic call to AngleList for related skills to the user selected skill"""
	skill_name = request.args.get("selected_skill")
	skills = slimmodel.get_skills_list()
	skill_obj = slimmodel.get_skill_by_name(skill_name)
	skill_id = skill_obj.id
	AL_skills_dict = ALskillcall.ALskillcall(skill_id, skill_name)
	jsoned = jsonify(AL_skills_dict) 
	return jsoned

@app.route("/trends")
def trends():
	"""This should render the jinja insert for the trends. This should hold the alorythm 
	for line graphs"""
	trend_skill_list = slimmodel.get_trend_skill_name()	
	# skill_list = [(skill.skill, skill.skill_id) for skill in trend_skill_list if skill.skill != "question"]
	# skill_set = set(skill_list)
	# skills_list_dd = list(skill_set)
	# skills_list_dd.sort()

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
	number_crunch = trend.creating_multi_trend_dict(trend1, trend2, trend3)
	print number_crunch
	# number_crunch2 = trend.cal_trend_precent_by_year(trend2)
	# number_crunch3 = trend.cal_trend_precent_by_year(trend3)
	# trends_dict = {"trend": number_crunch, "trendData2": number_crunch2, "trendData3": number_crunch3
	trends_dict= {"trends": number_crunch}
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

@app.route("/search", methods=["GET"])
def search():
	skills = slimmodel.get_skill_display_name() 
	return jsonify(skills)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
