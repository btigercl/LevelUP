from db import slimmodel
from datetime import date

def cal_trend_by_precent(name):
	tup_list = []
	trend_obj_list = slimmodel.get_trend_by_name(name)
	question_list = slimmodel.get_trend_by_name("question")
	for day in trend_obj_list:
		count = day.question_count 
		returned_date = str(day.date_epoc) 
		date_slice = returned_date[0:9]
		for question in question_list:
			q_date = str(question.date_epoc)
			if date_slice in q_date:
				precent = float(count)/float(question.question_count) * 100
				tup_list.append((date_slice, int(precent))) 
	return tup_list


# cal_trend_by_precent("python")