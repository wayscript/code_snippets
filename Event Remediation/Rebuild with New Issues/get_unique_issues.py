import requests
import pandas as pd

headers = {'X-Rollbar-Access-Token' : 󰀂v.25-rollbar-read-key󰀂}
response = requests.get('https://api.rollbar.com/api/1/items/?status=active&page=1', headers = headers)
variables['top_items'] = response.json().get('result').get('items')

try:
    df = pd.DataFrame(columns = ['id', 'title'])
    for item in variables['top_items']:
        df = df.append({'id' : item['id'], 'title' : item['title']}, ignore_index = True)

    previous_df = pd.read_excel('previous.xlsx')
    new_values = df[~df['title'].isin(previous_df['title']) ]
    print(new_values)

    new_issues_count = len(new_values['title'])
    print(new_issues_count)
    variables['new_issues_count'] = new_issues_count

    if new_issues_count > 0:
        variables['new_issues'] = new_values['title']
 except:
    pass


df.to_excel('previous.xlsx')
