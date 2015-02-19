import model
import csv 
from datetime import datetime
import requests
import os
import json 
from unicodedata import normalize  
from careerbuilder import CareerBuilder 



#These functions are for seeding the AngelList tables  
def main_angellist(session):
    """Creates the Nexus Table and calls the other functions. Should seed the unique id assigned by computer, ID from Skill table,
	ID from Job Title table, ID from Job Listing table,   """
    pass

def load_job_listing(session):
	"""Called from the main to make use of single api call. Should load AngelList """
	pass

def load_skills(session):
	"""Called from within the main to make use of single api call.Should load AngelList Tags IDs as the table id,
	skill name, skill display names."""
	pass

def load_job_title(session):
	"""Called from within the main to makes use of the singl """


#These functions are for seeding the CareerBuilder Table
def main_careerbuilder(session):
	"""Creates the """



if __name__ == "__main__":
    s= model.connect()
    main(s)