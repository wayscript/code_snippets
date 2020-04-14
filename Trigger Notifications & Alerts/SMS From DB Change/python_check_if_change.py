#import our desired modules
import pandas as pd

#import the variables from SQL
products = variables[ 'Products' ]
quantities = variables[ 'Quantities' ]
a_sum_list = variables[ 'a_sum_list' ]

#Change type of variables to integer type
quantities = [int(s) for s in quantities]

#Creating our dataframe for easy spreadsheet operations
dict = {'products': products, 'quantities': quantities}
df = pd.DataFrame(dict)

#Finding important values to us
a_products = df[df['products'] == 'A']
print(a_products)

#Total order quantities
current_a_sum = a_products['quantities'].sum()

#Finding Previous Order Quantity
last_a_sum = int(a_sum_list[-1])
print(last_a_sum)

# Change Check
sum_has_changed = last_a_sum != current_a_sum
print(sum_has_changed)

# Passing our variable to our workflow
variables['sum_has_changed'] = sum_has_changed
variables['current_a_sum'] = current_a_sum
