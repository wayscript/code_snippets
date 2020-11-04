names = variables.get('Column_1')
scores = variables.get('Column_2')

from prettytable import PrettyTable
x = PrettyTable()

x.field_names = ['Name', 'Score']

i = zip(names, scores)

for name, score in i:
  x.add_row([name, score])

variables['html_string'] = x.get_html_string()
