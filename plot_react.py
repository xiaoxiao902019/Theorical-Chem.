# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 11:00:31 2019

@author: xiaox
"""
import matplotlib.pyplot as plt
import numpy as np

offset = 0
def reactstate(x,y,c):
    plt.plot((x-0.1,x+0.1),(y,y),color = c)
    return

def plotreact(x):
    xaxis = []
    yaxis = []
    if x[0] == 'a':
        c = 'red'
        label = 'α-attack'
    if x[0] == 'b':
        c = 'blue'
        label = 'β-attack'
    for i in x[1:]:
        reactstate(i[0],i[1]*627.5095,'k')
        xaxis.append(i[0])
        yaxis.append(i[1]*627.5095)
    plt.plot(xaxis,yaxis,'--',color = c, label = label)
    return 

a_Ph = ['a',(1,-1796.689960),(2,-1796.684157),(5,-1796.790072)]
b_Ph = ['b',(1,-629.535251-1166.994112),(3,-1796.727380)]
fig,ax = plt.subplots()
plt.title('Ph;Nu:PhS')
plotreact(a_Ph)
plotreact(b_Ph)
plt.legend()
plt.ylabel('Energy/ kcal mol$^{-1}$')
#ax.tick_params(axis='x',which='both', bottom=False, top=False, labelbottom=False)
plt.xlabel('Reaction coordination')
plt.text(1,-0.1,'Reaction coordination')
plt.show()

a_TIPS = ['a',(1,-2209.865341),(2,-2209.863253),(6,-2209.961762)]
b_TIPS = ['b',(1,-2209.865473),(3,-2209.888213),(4,-2209.886597),(6,-2209.966062)]
fig,ax = plt.subplots()
plt.title('TIPS;Nu:PhS')
plotreact(a_TIPS)
plotreact(b_TIPS)
plt.legend()
plt.ylabel('Energy/ kcal mol$^{-1}$')
#ax.tick_params(axis='x',which='both', bottom=False, top=False, labelbottom=False)
plt.xlabel('Reaction coordination')
plt.text(1,-0.1,'Reaction coordination')
plt.show()    
    