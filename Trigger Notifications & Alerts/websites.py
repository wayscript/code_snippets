#website list
import requests
website_1 = 'https://www.wayscript.com'
website_2 = 'https://www.youtube.com/channel/UCv1JpM-XII0PMnqoCJfZA2g'

website_list = [website_1, website_2]


for w in website_list:
    r = requests.get(w)
    r.status
