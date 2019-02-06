import requests
from urllib.parse import urlencode
import json
from random import randint

search_term = 'game of thrones'

url = 'https://api.giphy.com/v1/gifs/search?'
params = { 'api_key' : '<YOUR_API_KEY>', 
		   'q'       : search_term, 
		   'lang'    : 'en' }

url += urlencode( params )
r = requests.get( url )
result = r.json()

i = randint( 0, len( result[ 'data' ] ) - 1 )

rand_result = result[ 'data' ][ i ]
url = rand_result[ 'images' ][ 'original' ][ 'url' ]

print( url )

#on WayScript
#outputs[ 'url' ] = url