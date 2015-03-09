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
def cal_trend_precent_by_month(name):
	trend_month_info = []
	month_list = ["2009-01", "2009-02", "2009-03", "2009-04", "2009-05", "2009-06", "2009-07", "2009-08", "2009-09", "2009-10", "2009-11", "2009-12", "2010-01", "2010-02", "2010-03", "2010-04", "2010-05", "2010-06", "2010-07", "2010-08", "2010-09", "2010-10", "2010-11", "2010-12", "2011-01", "2011-02", "2011-03", "2011-04", "2011-05", "2011-06", "2011-07", "2011-08", "2011-09", "2011-10", "2011-11", "2011-12", "2012-01", "2012-02", "2012-03", "2012-04", "2012-05", "2012-06", "2012-07", "2012-08", "2012-09", "2012-10", "2012-11", "2012-12", "2013-01", "2013-02", "2013-03", "2013-04", "2013-05", "2013-06", "2013-07", "2013-08", "2013-09", "2013-10", "2013-11", "2013-12", "2014-01", "2014-02", "2014-03", "2014-04", "2014-05", "2014-06", "2014-07", "2014-08", "2014-09", "2014-10", "2014-11", "2014-12", "2015-01","2015-02"]
	trend_obj_list = slimmodel.get_trend_by_name(name)
	question_list = slimmodel.get_trend_by_name("question")
	question_count_dict = {}
	trend_count_dict = {}

# "2008-09", "2008-10", "2008-11", "2008-12"	

	for question in question_list:
		question_date = str(question.date_epoc)
		question_month = question_date[0:7]
		question_count_dict[question_month] = question_count_dict.get(question_month, 0) + question.question_count
	
	for day in trend_obj_list:
		count = day.question_count 
		returned_date = str(day.date_epoc) 
		trend_month = returned_date[0:7]
		trend_count_dict[trend_month] = trend_count_dict.get(trend_month, 0) + count



	for month in month_list:
		num = trend_count_dict.get(month)
		den = question_count_dict.get(month)
		percent_long = float(num)/float(den) * 100
		percent_round = round(percent_long, 2)
		trend_month_info.append(({"trendName": name, "date": month, "percent": percent_round})) 
  	
  	return trend_month_info



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
		print num	
		den = question_count_dict.get(year)
		print den
		percent_long = float(num)/float(den) * 100
		percent_round = round(percent_long, 2)
		trend_year_info.append(({"trendName": name, "date": year, "percent": percent_round})) 
  
	print trend_year_info
	# final_dict = {"trend":name, "dataPoints":trend_year_info}
	return trend_year_info

def creating_multi_trend_dict(name1, name2, name3):
	
	input_list = [name1, name2, name3]
	trends_dict_list = []

	for name in input_list:
		returned_dict = cal_trend_precent_by_month(name)
		for i in range(len(returned_dict)):
			trends_dict_list.append(returned_dict[i])

	# print trends_dict_list
	return trends_dict_list

# creating_multi_trend_dict("css", "html", "javascript")
