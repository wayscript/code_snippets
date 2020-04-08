import pandas as pd

serial_number = variables['Serial_Number']
products = variables['Products']
movement = variables['Movement']

d = {"Products": products, "Movement": movement}


df = pd.DataFrame(d)
print(df)


a_product_df = df[df['Products'] == "Product A"]
product_a_sum = a_product_df['Movement'].astype(float).sum()

b_product_df = df[df['Products'] == "Product B"]
product_b_sum = b_product_df['Movement'].astype(float).sum()

c_product_df = df[df['Products'] == "Product C"]
product_c_sum = c_product_df['Movement'].astype(float).sum()

variables['product_a_sum'] = product_a_sum
variables['product_b_sum'] = product_b_sum
variables['product_c_sum'] = product_c_sum
