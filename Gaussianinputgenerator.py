# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:38:25 2019

@author: tliu
"""
import os.path


filename = input('Filename: ')#typ the file name in the cmd or terminal
string = input('Type of calculation:')

f = open(filename, 'r')
lines = f.readlines()
f.close()

print('Size of systerm:')
print(len(lines))

save_path ='P:\\Downloads\\Calculation\\Input'
completeName = os.path.join(save_path, filename[:-4]+ '_' + string + '.inp')

inpfile = open(completeName, 'w')
inpfile.write('%NProcShared=8'+ '\n')
inpfile.write('%chk='+ filename[:-4]+'_'+ string + '.chk'+ '\n')

memo = input('Mermory(1000MB/10000MB etc.):'+ '\n')
inpfile.write('%mem=' + memo + '\n' + '\n')

option = input('Option \n' + 
               '1:ModRedundant Opt=(ModRedundant) \n' +
               '2:Calculate all Opt=(ModRedundant,Calcall) \n' + 
               '3:Frequency frq \n' +
               '4:Other')

options = ''
if '1' in option:
    options = options + ' Opt=(ModRedundant) '
if '2' in option:
    options = options + ' Opt=(ModRedundant,Calcall) '
if '3' in option:
    options = options + ' frq '
if '4' in option:
    others = input('Other command:')
    options = options + ' ' + others + ' '
    
inpfile.write('#T B3LYP/Def2SVP EmpiricalDispersion=GD3BJ ' + options + '\n'+ '\n')
inpfile.write('g16 ' + filename[:-4]+'_'+ string + '\n' + '\n')

charge = input('Charge:')
multi = input('Multiplcity:')
inpfile.write(charge + ' ' + multi + '\n')

for i in lines:
    inpfile.write(i)
inpfile.write('\n')

modredun = input('ModRedundant command:'
            )
inpfile.write(modredun + '\n')
inpfile.close()