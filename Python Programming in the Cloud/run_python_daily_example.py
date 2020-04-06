import requests

info = requests.get('https://www.wayscript.com')
website_status = info.status_code

print(website_status)
