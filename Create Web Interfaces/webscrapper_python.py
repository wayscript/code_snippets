website = variables['websiteAnalyze']



import requests

r = requests.get(website)

variables['status_code'] = r.status_code
variables['is_redirect'] = r.is_redirect

cookies = str(r.cookies)
for i in ['<','[',']','>','/']:
  cookies = cookies.replace(i, '')

variables['cookies']     = cookies
