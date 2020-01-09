# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:00:11 2020

@author: tliu
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import time
from matplotlib.ticker import MultipleLocator

work_path='P:\\Downloads\\Calculation\\Output\\data'
print('Working path: ' + work_path) 

for i in os.listdir(work_path):
    if '.data' in i:
        filename = os.path.join(work_path,i)
        print(i + '                 ' + time.ctime(os.path.getmtime(filename)))
        
print('==========================================================')
print('All availiable files')
    

filename = input('Filename: ') #typ in the file name in the cmd or terminal
filename = os.path.join(work_path,filename)

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

def takeFirst(elem):
    return elem[0]

data.sort(key=takeFirst)
xaxis = []
y = []
for n in range(len(data)):
    x = float(data[n][0])
    y_1 = float(data[n][1])
    xaxis.append(x)
    y.append(y_1)
y = np.array(y)
yaxis = y*627.5095-max(y)*627.5095//1000*1000

name = str(filename.replace('.',''))

fig,ax =plt.subplots()
ax.plot(xaxis,yaxis,color='black', marker='x',mec ='blue',  markersize=5,lw = 0.5)

if max(y) > 10:
    x_label = 'Angle'
else:
    x_label = 'Distance/Å'    
plt.title(name)
plt.annotate(format(max(y)*627.5095//1000*1000,'e'),(0,1.02),xycoords = 'axes fraction')
plt.xlabel(x_label)
ax.yaxis.set_minor_locator(MultipleLocator(20))
plt.grid(which = 'major',axis='y',ls ='-')
plt.grid(which = 'minor',axis='y',ls ='--',lw=0.5)
plt.ylabel('Energy/kcal mol$^{-1}$')
plt.savefig(name,fmt = 'png', dpi = 600)

input()