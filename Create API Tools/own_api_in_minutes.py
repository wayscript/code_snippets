### Quick API sample Code ###

import json
import random

value_from_url = variables['value']
random.seed(value_from_url)
number = random.randint(0,100000000000)

dict_x = {"number":number}

return_json = json.dumps(dict_x)

variables['return_json'] = return_json

​
