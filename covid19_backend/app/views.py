from app import app
import pandas as pd
import json

@app.route('/covid19', methods = ['POST', 'GET'])
def retrieve_chatdata():
	"""
	Retrieve all contries covid-19 data and apply filter for Post request
	"""
	# if request.method == 'GET':
	global_data = pd.read_csv(app.config["CASES_URL"])
	recovered_data = pd.read_csv(app.config["RECOVERED_URL"])
	death_data = pd.read_csv(app.config["DEATH_URL"])
	countries = global_data["Country/Region"].values.tolist()
	available_dates = global_data.columns.values.tolist()[4:]
	# sum of last column's data for total cases
	total_cases = int(global_data.iloc[:, -1].values.sum())
	# sum of last column's data for total death
	total_death = int(death_data.iloc[:, -1].values.sum())
	# sum of total cases date wise
	date_vs_case = global_data.iloc[:, 4:].sum().to_dict()
	# sum of total death date wise
	date_vs_death = death_data.iloc[:, 4:].sum().to_dict()
	# show all data
	data = {
		"countries": countries,
		"date": available_dates,
		"total_cases": total_cases,
		"total_death": total_death,
		"date_vs_case": date_vs_case,
		"date_vs_death": date_vs_death,
	}
	response = json.dumps(data)
	return response

	# elif request.method == 'POST':
		# filter data as per user's selection	
	
	# if request.data.get("country"):
	# selected_country = request.data.get("country")
	
	# if request.data.get("date"):
	# selected_date = request.data.get("date")

	# if selected_country:
	# 	selected_country = "India"
	# if selected_date:
	# 	selected_date = "1/26/20"

	"""
	Filter data according to selected country and date
	"""
	# find index of selected date to get data accordingly
	# index = global_data.columns.get_loc(selected_date)
	# sum of last column's data for total cases
	# total_cases = int(global_data.loc[global_data["Country/Region"] == selected_country].iloc[:, 4:index+1].values.sum())
	# sum of last column's data for total death
	# total_death = int(death_data.loc[global_data["Country/Region"] == selected_country].iloc[:, 4:index+1].values.sum())
	# sum of total cases date wise
	# date_vs_case = global_data.loc[global_data["Country/Region"] == selected_country].iloc[:, 4:index+1].sum().to_dict()
	# sum of total death date wise
	# date_vs_death = death_data.loc[global_data["Country/Region"] == selected_country].iloc[:, 4:index+1].sum().to_dict()
	# data = {
	# 	"country": countries,
	# 	"date": available_dates,
	# 	"total_cases": total_cases,
	# 	"total_death": total_death,
	# 	"date_vs_case": date_vs_case,
	# 	"date_vs_death": date_vs_death,
	# }
	# response = json.dumps(data)
	# return response