from careerbuilder import CareerBuilder 
from xml.etree import ElementTree as ET 



DEV_KEY = 

cb =CareerBuilder(DEV_KEY)

results = cb.categories()


drilldown = results["ResponseCategories"]["Categories"]["Category"]

for sub_dicts in drilldown:
	code = sub_dicts["Code"]
	text = sub_dicts["Name"]["#text"]
	print code, text 