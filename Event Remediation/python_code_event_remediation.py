#Automated Testing with Selenium
def automated_testing(url):
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0')
    browser = webdriver.Chrome(options = options)
    browser.set_page_load_timeout(30)
    browser.get(url)
    ps = browser.page_source
    browser.close()
    return ps

#Trigger Actions from own Site
import requests, ujson
response = requests.get('mysite-tutorials.herokuapp.com/api/rebuild')
print(response.json())

#Trigger Actions from Other APIs
import requests, ujson

headers = { 'authorization': "Basic REPLACE_BASIC_AUTH" }
response = requests.post('circleci.com/api/v2/workflow/%7Bid%7D/approve/%7Bapproval_request_id%7D', headers=headers)
data = response.json()
variables['circleci_output'] = data.get('message')
