#plate_name is identical to a plate file name, without the .txt
plate_name = 'BS'










import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin, cos, radians

input_file = open('plate_coordinates.txt', 'r')
lines = input_file.readlines()

line_no = 1
plate_name_list = []
asteriks_index = []
coords_only = []
var = []
x_coordinates = []
y_coordinates = []

#only to use scatterplot; points are on the same level
z_coordinates = []

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

lines = Convert(lines)
for i in lines:     
    i = Convert(i)
    if i[0] == '*':
        asteriks_index.append(line_no)   
    elif i[0] == ' ' or i[0] == '\n':
        pass
    else:
        del i[2]
        plate_name_list.append(["".join(i), line_no]) 
    line_no += 1
line_no = 1


#i have for every two elements of plate_name_list;
#[  [name_plate, line no], [line no]                            ]
for i in plate_name_list:
    if i[0] == plate_name:
        for r in range (i[1], asteriks_index[plate_name_list.index(i)] -1):
            #line of plate name should be = first plate coord, because lines are 1 ahead of index of lines
            #the line with ** has a line no two greater than index of the ** line, so -1
            #the last pair is one below the ** line, so another -1: total -2.
            #however, range excludes the last integer, where -2 maps to the last line. +1 makes a total change of -1.
            lines[r] = Convert(lines[r])
            del lines[r][0]
            for m in range (0, lines[r].index(",")):
            # working on the x coordinate
                var.append(lines[r][m])
            # here, pray that the sci notation works. i could try to join differently, do math myself, or check whether removing 
            # the 0 right after E does anything
            var = float("".join(var))
            x_coordinates.append(var)
            var = []
            for t in range(lines[r].index(",") + 1, len(lines[r])):
                var.append(lines[r][t])
            var = float("".join(var))
            y_coordinates.append(var)
            var = []

for i in range (0, len(x_coordinates)):
    z_coordinates.append(0)

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')


ax.plot(x_coordinates, y_coordinates, z_coordinates, '-o')
plt.show()
