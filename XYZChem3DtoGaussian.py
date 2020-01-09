# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:18:34 2019

@author: tliu
"""
import os

open_path = 'P:\\Downloads\\Calculation\\structure\\Chem3Dstructure' #variable
save_path ='P:\\Downloads\\Calculation\\structure' #variable

print('Working path:' + open_path)
for i in os.listdir(open_path):
    if '.xyz' in i:
        print(i)
    
print('==========================================================')
print('All availiable files')


filename = input('Filename: ') 

if filename != '':
    completeName = os.path.join(save_path, filename)
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    f = open(completeName,'w+')
    for i in lines:
        upper = i.index('(')
        bottom = i.index(')')
        i = i.replace(i[upper:bottom+1],'')
        f.write(i)
    f.close()
    fullname = os.path.join(open_path,filename)
    os.remove(fullname)
    print(filename + '  done!')
else:
    for filename in os.listdir(open_path):
        if '.xyz' in filename:
            f = open(filename, 'r')
            lines = f.readlines()
            f.close()
            completeName = os.path.join(save_path, filename)
            f = open(completeName,'w+')
            for i in lines:
                upper = i.index('(')
                bottom = i.index(')')
                i = i.replace(i[upper:bottom+1],'')
                f.write(i)
            f.close()
            fullname = os.path.join(open_path,filename)
            os.remove(fullname)
            print(filename + '   done!')
            
input()
    
