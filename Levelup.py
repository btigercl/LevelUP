from flask import Flask, render_template, redirect, request, session, flash, g, url_for
from careerbuilder import CareerBuilder 
# import model
import jinja2
import os

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
	return render_template("clusters.html")

@app.route("/trends")
def trends():
	"""This should render the jinja insert for the trends. This should hold the alorythm 
	for line graphs"""
	return render_template("trends.html")

@app.route("/geographic_demand")
def geographic_demand():
	"""Render jinja insert for geographic_demands. Map of geographic demand for skill set""" 
	return render_template("geo.html")

# @app.route("/new_data_requests")
# def new_data_requests():
# 	"""this is where users can request representation of new data sets. Should be a 
# 	alogrithm that can process this request with APIs and return new data automatically"""
# 	pass

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
