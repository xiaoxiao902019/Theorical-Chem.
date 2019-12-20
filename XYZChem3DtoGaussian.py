# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:18:34 2019

@author: tliu
"""
import os.path

filename = input('Filename: ') #typ in the file name in the cmd or terminal
f = open(filename, 'r')
lines = f.readlines()
f.close()


save_path ='P:\\Downloads\\Calculation\\structure'
completeName = os.path.join(save_path, filename)

f = open(completeName,'w+')
for i in lines:
    upper = i.index('(')
    bottom = i.index(')')
    i = i.replace(i[upper:bottom+1],'')
    f.write(i)
   
f.close()
    
