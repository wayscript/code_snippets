import requests
from datetime import date
import pandas as pd

response = requests.get('https://www.wayscript.com')
print(response.status_code)
today = date.today()

data = {'date': today, 'response':response}

df = pd.DataFrame(data=data)
df.to_excel('logs.xlsx')

variables['status_code'] = response.status_code
