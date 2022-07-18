# is sorting needed?

import numpy as np
from math import pi, sin, cos, radians

input_file = open('plate_coordinates.txt', 'r')
lines = input_file.readlines()
#lines is now a string but ill make it an array 

# the code will try to handle it all in chunks, like this:
#abbreviation/plate name\n
#long,lat coords\n
#...
#...
#*** end of line segment ***\n
#next abbreviation/plate name\n


longitude = []
latitude = []
colatitude = 0.0

names_and_coords = []
only_coords = []

blank_lines = []

plate_name = ""
plate_name_list = []
line_no = 1
num_plates = 1


def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
    


lines = Convert(lines)
for i in lines:     
    i = Convert(i)
    if i[0] == '*' or i[0] == ' ' or i[0] == '\n':
        pass
    else:
        del i[2]
        plate_name_list.append(["".join(i), line_no]) 
    line_no += 1
line_no = 1

for i in plate_name_list:
    file_name = i[0] + ".txt"
    #print for debug
    f = open(file_name, 'w')
    f.write("".join(only_coords))
    f.close()

for i in lines:        
    if i[0] == ' ':
        coord_pair_list = Convert(i)
        coord_pair_list.pop(0)
        coord_pair_list.pop(-1)
        #removed a space and turned the numbers into a list
        #print("coord_pair_list")
        #print(coord_pair_list)

        for i in range (0, coord_pair_list.index(',')):
            longitude.append(coord_pair_list[i])
        #takes from comma to front to make a list of long
        #print("longitude as sign + list")
        #print(longitude)
        
    
        for i in range (coord_pair_list.index(',') + 1, len(coord_pair_list)):
            latitude.append(coord_pair_list[i])
        #print("latitude as sign + list")
        #print(latitude)
        #list of lat coord

        longitude = float("".join(longitude))
        latitude = float("".join(latitude))

        if longitude < 0:
            longitude = 360 + longitude 
        if latitude > 0:
            colatitude = 90 - latitude
        if latitude < 0:
            colatitude = 180 + latitude
        

        x = 10 * sin(radians(colatitude)) * cos(radians(longitude))
        y = 10 * sin(radians(colatitude)) * sin(radians(longitude))
        z = 10 * cos(radians(colatitude))

        #the last coord in each plate repeats
        if str(x)+' '+str(y)+' '+str(z)+'\n' == names_and_coords[-1]:
            del names_and_coords[-1]
        
        #to get around out of list index error
        only_coords.insert(0, " ")
        if str(x)+' '+str(y)+' '+str(z)+'\n' == only_coords[-1]:
            del only_coords[-1]
        del only_coords[0]
        
        names_and_coords.append(str(x)+' '+str(y)+' '+str(z)+'\n')
        only_coords.append(str(x)+' '+str(y)+' '+str(z)+'\n')
        

        longitude = []
        latitude = []
        colatitude = 0.0
        # print (names_and_coords[-1])
        # print(only_coords[-1])
        # print("-----------------------------------------------")
    else:
        i = "".join(i)
        names_and_coords.append(i)
        if num_plates < len(plate_name_list):
            #to get around list index out of range in the following
            if line_no == plate_name_list[num_plates][1]:
                file_name = plate_name_list[num_plates-1][0] + ".txt"
                text_file = open(file_name, "w")
                n = text_file. write(str("".join(only_coords)))
                text_file. close()
                #print list with [num_plates-1][0] file name
                only_coords = []
                #dump onlycoords
                num_plates += 1
    line_no += 1
#the cycle right above to print only_coords to a file with a specific name
#fails on the last plate, because num_plates in [num_plates][1] will 
#not be able to trigger, as there are no more plate names to read
#so the plate gets printed, without conditions, after lines runs out of elements

file_name = plate_name_list[num_plates-1][0] + ".txt"
text_file = open(file_name, "w")
n = text_file. write(str("".join(only_coords)))
text_file. close()
        
        
text_file = open("cartesian_plate_coords", "w")
n = text_file. write(str("".join(names_and_coords)))
text_file. close()
#how to output files
