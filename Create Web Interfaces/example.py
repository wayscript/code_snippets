import sys
import requests

n = len(sys.argv)

for i in range(1, n):
    url = sys.argv[i]
    status = requests.get(url).status_code

    if status != 200:
        print( url + ' DOWN! ' + status )
    
    else:
        print( url + ':' + str(status))


