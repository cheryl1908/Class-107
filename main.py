import pandas as pd
import csv
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
mean_level=df.groupby("level")["attempt"].mean()
print(mean_level)
fig=go.Figure(
    go.Bar(x=mean_level,y=['Level 1','Level 2','Level 3','Level 4'],orientation='h')
)
fig.show()