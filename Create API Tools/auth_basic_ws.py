import requests
import json

url = 'https://21891.wayscript.io/'
headers = {
            "Authorization" : "Basic dXNlcjE6cGFzcw==",
            "Content-Type" : "application/json; charset=utf-8"}

response = requests.get(url, headers=headers)
response = response.text.replace("\'", "\"")
json_response = json.loads(response)

print(json_response.get('users')[0])
