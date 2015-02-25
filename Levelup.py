from flask import Flask, render_template, redirect, request, session, flash, g, url_for, jsonify
from careerbuilder import CareerBuilder 
import jinja2
import os
from db import slimmodel
from calls import ALskillcall, ALjobtitlecall, CBskillcall
import json


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
	jobtitles = slimmodel.get_jobtitles_list()
	return render_template("clusters.html", skills=skills, jobtitles=jobtitles)

@app.route("/skill_angelList_call", methods=["POST"])
def skill_angelList_call():
	"""This makes a dynamic call to AngleList for related skills to the user selected skill"""
	skill_id = request.form.get("selected_skill")
	skills = slimmodel.get_skills_list() 
	AL_skills_dict = ALskillcall.ALskillcall(skill_id)
	#jsonify 
	#pass to D3
	return render_template("skill_response.html", skill_dict =AL_skills_dict, skills=skills)
	 	

@app.route("/trends")
def trends():
	"""This should render the jinja insert for the trends. This should hold the alorythm 
	for line graphs"""
	return render_template("trends.html")

@app.route("/db_call_trend_lanuage", methods=["GET"])
def db_call_trend_lanuage():
	#language1 = request.form.get("language1")
	#language2 = request.form.get("language2")
	#language3 = request.form.get("language3")
	#makes database call based on values
	#returns info
	#pass info to D3 file 
	pass

@app.route("/geographic_demand")
def geographic_demand():
	"""Render jinja insert for geographic_demands. Map of geographic demand for skill set""" 
	skills = slimmodel.get_skills_list()
	return render_template("geo.html", skills = skills)

@app.route("/geographic_demand_skill", methods=["POST"])
def geographic_demand_skill():
	"""This makes a dynamic call to CareerBuilder to return lat/long/location of demand for a skill set"""
	skill = request.form.get("selected_skill")
	lat_long_tups = CBskillcall.cbskill(skill)
	print lat_long_tups
	return json.dumps(lat_long_tups)
	# skills = slimmodel.get_skills_list()
	#jsonify 
	#pass to D3
	# return render_template("geo_response.html", geo_tups=lat_long_tups, skills = skills)

# @app.route("/new_data_requests")
# def new_data_requests():
# 	"""this is where users can request representation of new data sets. Should be a 
# 	alogrithm that can process this request with APIs and return new data automatically"""
# 	pass

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
