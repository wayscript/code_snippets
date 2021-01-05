# pandas demo 
import pandas as pd
import numpy as np

# reading in excel files
df = pd.read_excel('DummydataWorkbook.xlsx')
print(df.head(10))

# describing excel files
print(df.describe())

#indexing columns
print(df['Test 1'])

df['average'] = (df['Test 1'] + df['Test 2']) / 2

df.to_excel('averages.xlsx')