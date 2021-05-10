# Create an html document from your sql frame to pass on to an endpoint or email
import pandas as pd

info_dictionary = {}
for i in range( 1, 8 ):
    variable_string = 'Column_' + str(i)
    info_dictionary[i] = variables[variable_string]

df = pd.DataFrame(data=info_dictionary)
variables['html_sql_processes'] = df.to_html()
