#website list
import requests
website_1 = 'https://www.wayscript.com'
website_2 = 'https://www.youtube.com/channel/UCv1JpM-XII0PMnqoCJfZA2g'

website_list = [website_1, website_2]

status_list = []
for w in website_list:
    r = requests.get(w)
    code = r.status_code
    status_list.append(code)

print(status_list)

variables['status_list'] = status_list
