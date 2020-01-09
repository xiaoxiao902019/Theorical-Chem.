# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:47:38 2019

@author: tliu
"""
import os

work_path = 'P:\\Downloads\\Calculation\\Output\\'
print('Working path: ' + work_path)

folder = input('Folder:')
path =work_path + folder #root path

if not os.path.exists(path):
    print('Folder does not exist!')
else:
    for i in os.listdir(path):
        print(i)
    print('===============================')
    print('All availiable files')
    
    filename = input('Filename: ')#typ the file name in the cmd or terminal
    string = input('Key words:')

    if filename != '':
        file = os.path.join(path,filename)
        f = open(file, 'r')
        lines = f.readlines()
        f.close()

        print('Result of '+ filename +':')
        for i in lines:
            if string in i:
                print(i)
    else:
        for filename in os.listdir(path):
            file = os.path.join(path,filename)
            f = open(file, 'r')
            lines = f.readlines()
            f.close()

            print('Result of '+ filename +':')
            for i in lines:
                if string in i:
                    print(i)
            print('===============================')

input()


        
