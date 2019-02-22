from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

outputs = {} #**comment out on WayScript**
api_key = 'YOUR_API_KEY'

def get_crypto_data( symbol ): 
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters = { 'symbol' : symbol }

    headers = { 'Accepts' : 'application/json',
                'X-CMC_PRO_API_KEY' : api_key  }

    session = Session()
    session.headers.update( headers )

    try:
        response = session.get( url, params = parameters )
        data = json.loads( response.text )
        data_to_return = data.get( 'data', {} ).get( symbol, {} )
        return data_to_return
    except ( ConnectionError, Timeout, TooManyRedirects ) as e:
        print( e )
        return None

def build_outputs( data ): 
    quote = data.get( 'quote' ).get( 'USD' )
    outputs[ 'name' ] = data.get( 'name' )
    outputs[ 'price' ] = quote.get( 'price' )
    return outputs

def main():
    symbol = input( '\nEnter a Symbol: ' )
    data = get_crypto_data( symbol )
    if not data: return
    outputs = build_outputs( data )
    print( '\nThe Price for ' + outputs[ "name" ] + ' is ' + str( outputs[ "price" ] ) )

if __name__ == '__main__':
    main()

