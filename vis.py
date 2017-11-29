import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go

# df = pd.read_csv(infile, parse_dates={'datetime': ['date', 'time']}, date_parser=dateparse)
df = pd.read_csv('result.csv', parse_dates=['dateTime'], index_col='dateTime') 
df = df.sort_index()
print(df.head())

traces = []

for col in df.columns:
	traces.append(go.Scatter(
		x = df.index,
		y = df[col],
		name = col,
		connectgaps = True
	))

layout = go.Layout(
    title='Twitter Users Happiness Line Chart',
    yaxis=dict(title='Happiness Index'),
    xaxis=dict(title='Date Time')
)

fig = go.Figure(data=traces, layout=layout)

py.plot(fig, filename='result.html')
