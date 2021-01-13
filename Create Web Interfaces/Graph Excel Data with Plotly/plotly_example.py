import pandas as pd
import plotly.express as px

df = pd.read_excel('IRIS.xlsx')
print(df.head(5))

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
                 
fig.write_html("graph.html")