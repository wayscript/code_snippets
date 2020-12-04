import requests
from bs4 import BeautifulSoup

ticker = 'AAPL'
url = 'https://finance.yahoo.com/quote/' + ticker

res = requests.get( url )
html = res.text

soup = BeautifulSoup( html, 'html.parser' )
market_cap_elem = soup.find( 'td', { 'data-test' : 'MARKET_CAP-value' } )
market_cap = market_cap_elem.text

market_cap = int(float(str(market_cap).split('T')[0]) * 1000000000 )

variables[ 'MarketCap' ] = market_cap
