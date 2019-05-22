#!/bin/ python3

filename = input('Filename: ')#typ the file name in the cmd or terminal

startline = input('Startline: ')#typ the start line in the cmd or terminal

endline = input('Endline: ')#typ the end line in the cmd or terminal

f = open(filename, 'r')
lines = f.readlines()
f.close

a = int(startline)
b = int(endline)

data = []
for i in lines[a-1:b]:
    newstr = i[15:27] + i[31:]
    newstr = newstr.replace(' 1 ','H')
    newstr = newstr.replace(' 6 ','C')
    newstr = newstr.replace(' 16 ','S')
    newstr = newstr.replace(' 14 ','Si')#here can be extended with other type of atom
    data.append(newstr)

f = open(filename[:-4] + '.xyz', 'w')
f.write('    '+ str(len(data))+ '\n' + 'FINAL     HEAT OF FORMATION     =     0.000000' + '\n')
for i in data:
    f.write(i)
f.close()

