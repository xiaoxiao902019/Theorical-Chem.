#!/bin/ python3

import numpy as np
import matplotlib.pyplot as plt

filename = input('Filename: ') #typ in the file name in the cmd or terminal
f = open(filename, 'r')
lines = f.readlines()
f.close()
data = [i.replace('\t',',') for i in lines]
data = [i.replace('\n','') for i in data]
data = [i.replace(' ','') for i in data]
data = [i.split(' ') for i in data]
data = [i[0].split(',') for i in data]
data = [i for i in data if i != ['']]
data = [list(map(float, i)) for i in data]

delta_y = input('Shift of the energy (/Hartree): ') #typ in shift of energy in the cmd or terminal
def takeSecond(elem):
    return elem[1]

data.sort(key=takeSecond)
xaxis = []
yaxis = []
for n in range(len(data)):
    x = float(data[n][1])
    y = float(data[n][0])
    xaxis.append(x)
    yaxis.append(y+float(delta_y))

name = str(filename.replace('.',''))

plt.figure(name)
plt.plot(xaxis,yaxis,color='black', marker='x',mec ='blue',  markersize=5,lw = 0.5)
if max(xaxis) > 10:
    x_label = 'Angle'
else:
    x_label = 'Distance/Å'    
plt.title(name)
plt.xlabel(x_label)
plt.ylabel('Energy/hartree')
plt.savefig(name,fmt = 'png', dpi = 600)
