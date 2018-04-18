import plotly.plotly as py
import plotly.graph_objs as go
import random
import numpy as np

x = np.arange(100) 
y = np.arange(50)
z = [[random.randint(0,20) for i in range(len(x))] for ii in range(len(y))]

file_names = np.arange(5000)
count = 0

hovertext = list()
for yi, yy in enumerate(y):
    hovertext.append(list())
    for xi, xx in enumerate(x):
        hovertext[-1].append('File name: naturalhistoryof00mill_{}<br />Count: {}'.format(file_names[count], z[yi][xi]))
        count += 1
        
trace = go.Heatmap(z = z, x = x, y = y, hoverinfo='text',
                                  text=hovertext)
data = [trace]
py.iplot(data, filename = 'labelled-heatmap')