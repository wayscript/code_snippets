CREATE TABLE purchase_orders(
   id serial PRIMARY KEY,
   po_number INT NOT NULL,
   buyer VARCHAR (50) NOT NULL,
   product VARCHAR (50) NOT NULL,
   quantity INT NOT NULL
);




INSERT INTO purchase_orders (po_number, buyer, product, quantity)
    VALUES (1000, 'Derrick', 'Straws', 50000),
            (1001, 'Derrick', 'Cups', 50000),
            (1002, 'Derrick', 'Napkins', 200000),
            (1003, 'Derrick', 'Dish Soap', 30),
            (1004, 'Derrick', 'French Fries (50 lb)', 10),
            (1005, 'Derrick', 'Orange Syrup', 2),
            (1006, 'Derrick', 'Grape Syrup', 2);

SELECT * FROM purchase_orders




'''
### Python Code Used Here ###
#Imports
import json

# Reading in Variables from Previous WayScript Modules
po_number = variables['PO_Number']
name = variables['Name']
product = variables['Product']
quantity = variables['Quantity']

# Creating Dict objects to store values to
data = {}
order = {}

# Beginning index
i = 0

#Iterate over potentially many products on a single PO
for p in product:
  order['product'] = p
  order['quantity'] = quantity[i]
  order['buyer'] = name[i]
  i += 1

# write data to our dict
data['order'] = order

# create json format to pass to API
return_data = json.dumps(data)

variables['return_data'] = return_data
'''
