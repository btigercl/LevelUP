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