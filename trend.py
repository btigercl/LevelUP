from db import slimmodel
from datetime import date

def cal_trend_precent_by_day(name):
	trend_dict_list = []
	trend_obj_list = slimmodel.get_trend_by_name(name)
	question_list = slimmodel.get_trend_by_name("question")
	question_dict = {}
	
	for question in question_list:
		q_date = str(question.date_epoc)
		q_date_slice = q_date[8:10] + '-' + q_date[5:7] + "-" + q_date[0:4]
		question_dict[q_date_slice]= question.question_count

	for day in trend_obj_list:
		count = day.question_count 
		returned_date = str(day.date_epoc) 
		date_slice = returned_date[8:10] + '-' + returned_date[5:7] + "-" + returned_date[0:4]
		if question_dict.get(date_slice):
			precent = float(count)/float(question_dict.get(date_slice)) * 100
			trend_dict_list.append(({"date": date_slice, "percent": precent})) 
	final_dict = {"trend":name, "dataPoints":trend_dict_list}
	return final_dict
# cal_trend_precent_by_day("python")
# q_date_slice = q_date[8:10] + '-' + q_date[5:7] + "-" + q_date[0:4]
# date_slice = returned_date[8:10] + '-' + returned_date[5:7] + "-" + returned_date[0:4]

def cal_trend_precent_by_year(name):
	trend_year_info = []
	year_list = ["2008", "2009", "2010", "2011", "2012", "2013", "2014"]
	trend_obj_list = slimmodel.get_trend_by_name(name)
	question_list = slimmodel.get_trend_by_name("question")
	question_count_dict = {}
	trend_count_dict = {}
	
	for question in question_list:

		q_date = str(question.date_epoc)
		qyear = q_date[0:4]
		question_count_dict[qyear] = question_count_dict.get(qyear, 0) + question.question_count

	
	for day in trend_obj_list:
		count = day.question_count 
		returned_date = str(day.date_epoc) 
		tyear = returned_date[0:4]
		trend_count_dict[tyear] = trend_count_dict.get(tyear, 0) + day.question_count

	
	for year in year_list:
		num = trend_count_dict.get(year)
		den = question_count_dict.get(year)
		percent = float(num)/float(den) * 100
		trend_year_info.append(({"trendName": name, "date": year, "percent": percent})) 
  

	# print trend_year_info
	final_dict = {"trend":name, "dataPoints":trend_year_info}
	return final_dict
# cal_trend_precent_by_year("css")
