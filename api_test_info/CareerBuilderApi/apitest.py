from careerbuilder import CareerBuilder 
import SecretKeys

DEV_KEY = SecretKeys.Dev_Key

cb =CareerBuilder(DEV_KEY)
countryc= "US"

results = cb.industrycodes()

drilldown = results["ResponseIndustryCodes"]["IndustryCodes"]["IndustryCode"]

for sub_dicts in drilldown:
	code = sub_dicts["Code"]
	text = sub_dicts["Name"]["#text"]
	print code, text 





# print drilldown

# for code_dict in drilldown2:
# 	print code_dict["Name"]["#text"]

# def get_codes(results):

