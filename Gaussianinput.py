# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:58:05 2020

@author: tliu
"""
import os

work_path = 'P:\\Downloads\\Calculation\\structure'
print('Working path: ' + work_path)

filelist = os.listdir(work_path)
for file in filelist:
    if '.xyz' in file:
        print(file)
print('==========================================================')
print('All availiable files')


filename = input('Filename: ')
string = input('Type of calculation:')

f = open(filename, 'r')
lines = f.readlines()
f.close()

print('Size of systerm:')
print(len(lines))

save_path ='P:\\Downloads\\Calculation\\Input'
print('Saveing path: ' + save_path)

completeName = os.path.join(save_path, filename[:-4]+ '_' + string + '.inp')

inpfile = open(completeName, 'w')
inpfile.write('%NProcShared=8'+ '\n')
inpfile.write('%chk='+ filename[:-4]+'_'+ string + '.chk'+ '\n')

memo = input('Mermory: \n 1:1000MB \n 2:10000MB \n 3:Others'+ '\n')
if memo == '1':
    memo == '1000MB'
if memo == '2':
    memo = '10000MB'
if memo == '3':
    memo = input('Mermory:')
else:
    print('Wrong mermory requirement!')



inpfile.write('%mem=' + memo + '\n' + '\n')

option = input('Option \n' + 
               '1:ModRedundant Opt=(ModRedundant) \n' +
               '2:Calculate all Opt=(ModRedundant,Calcall) \n' + 
               '3:Frequency frq \n' +
               '4:Other \n')

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

modredun = input('ModRedundant command:' + '\n')
inpfile.write(modredun + '\n')
inpfile.close()

target_path = 'P:\\Downloads\\Calculation\\structure\\xyzstructure'
newfilename = os.path.join(target_path,filename)
os.rename(filename,newfilename)
os.remove(filename)
print('\n' + filename + ' moved to ' + target_path)

input()