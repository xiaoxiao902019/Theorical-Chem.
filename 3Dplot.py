#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:02:49 2019

@author: tianshu
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

filename = input('Filename: ') #typ in the file name in the cmd or terminal
f = open(filename, 'r')
lines = f.readlines()
f.close()
line = [i.replace('\t',',') for i in lines]
line = [i.replace('\n','') for i in line]
line = [i.replace(' ','') for i in line]
line = [i.split(',') for i in line]
#data = [list(map(float, i)) for i in data]
data1 = []
data2 = []
label = []
for i in line:
    if i[0] != '':
        if i[0] == 'S-Ca' or i[0] == 'Nu-Ca':
            file = label
        if i[0] == 'S-Ca_PES':
            file = data1
        if i[0] == 'Nu-Ca_PES' or i[0] == 'TIPS-Ca_PES' or i[0] == 'Ph-Ca_PES':
            file = data2
        try:
            num = float(i[0])
            i = list(map(float,i))
        except ValueError:
            print('NO')
        file.append(i)

def takeSecond(elem):
    return elem[1]

def datasort(data):
    data_1 = data[1:]
    data_1.sort(key=takeSecond)
    xaxis = []
    yaxis = []
    z = []
    for n in range(len(data_1)):
            x = float(data_1[n][0])
            y = float(data_1[n][1])
            z_1 = float(data_1[n][2])
            xaxis.append(x)
            yaxis.append(y)
            z.append(z_1)
    z = np.array(z)
    offset = max(z)*627.5095//1000*1000
    zaxis = z*627.5095 - offset
    return data[0][0],np.array(xaxis),np.array(yaxis),zaxis,offset


plot_data1 = datasort(data1)
plot_data2 = datasort(data2)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(plot_data1[1], plot_data1[2], plot_data1[3], zdir='z', label= plot_data1[0])
ax.scatter(plot_data2[1], plot_data2[2], plot_data2[3], zdir='z', label= plot_data2[0])
plt.legend()
plt.xlabel(label[0][0]+'/Å')
plt.ylabel(label[0][1]+'/Å')
ax.set_zlabel('Energy/ kcal mol$^{-1}$')
plt.savefig(filename[:-5],fmt = 'png', dpi = 600)
plt.show()

fig,ax=plt.subplots()
plt.plot(plot_data1[1],  plot_data1[3],'-x',  label= plot_data1[0])
plt.plot(plot_data2[1],  plot_data2[3],'-x',   label= plot_data2[0])
plt.annotate(format(plot_data1[4],'e'),(0,1.02),xycoords = 'axes fraction')
plt.xlabel(label[0][0]+'/Å')
ax.yaxis.set_minor_locator(MultipleLocator(20))
plt.grid(which = 'major',axis='y',ls ='-')
plt.grid(which = 'minor',axis='y',ls ='--',lw=0.5)
plt.ylabel('Energy/kcal mol$^{-1}$')
plt.legend()
plt.savefig(filename[:-5]+'-'+label[0][0],fmt = 'png', dpi = 600)
plt.show()

fig,ax=plt.subplots()
plt.plot(plot_data1[2],  plot_data1[3],'-x',   label= plot_data1[0])
plt.plot(plot_data2[2],  plot_data2[3],'-x',   label= plot_data2[0])
plt.annotate(format(plot_data1[4],'e'),(0,1.02),xycoords = 'axes fraction')
plt.xlabel(label[0][1]+'/Å')
ax.yaxis.set_minor_locator(MultipleLocator(20))
plt.grid(which = 'major',axis='y',ls ='-')
plt.grid(which = 'minor',axis='y',ls ='--',lw=0.5)
plt.ylabel('Energy/kcal mol$^{-1}$')
plt.legend()
plt.savefig(filename[:-5]+'-'+label[0][1],fmt = 'png', dpi = 600)
plt.show()

