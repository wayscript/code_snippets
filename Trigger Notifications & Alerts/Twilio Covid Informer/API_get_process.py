import requests
from datetime import datetime

today_date = str(datetime.today().strftime('%Y%m%d'))

data = requests.get('http://covidtracking.com/api/states/daily')
json_data = data.json()
# print(json_data)
data = {}
for item in json_data[0:56:1]:
  state = item.get('state')
  date = item.get('date')
  death = item.get('death')
  hospitalized = item.get('hospitalized')
  total = item.get('total')
  dict = {"date":date, "death":death, "hospitalized":hospitalized, "total":total}
  data[state] = dict

output_data = data

variables['data_to_pass'] = output_data
