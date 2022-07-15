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
long_float = 0.0
lat_float = 0.0
exponent = []
var_1 = 0
var_2 = 0
sign = []

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
    

def trim_coord():
    global longitude 
    global latitude
    global exponent
    global sign
    
    exponent.insert(0, int(longitude[-1]))
    sign.insert(0, longitude[0])
    longitude.pop(0)
    for i in range (0,4):
        longitude.pop(-1)

    exponent.insert(1, int(latitude[-1]))
    sign.insert(0, latitude[0])
    latitude.pop(0)
    for i in range (0,4):
        latitude.pop(-1)
  



def deg_to_rad():
    global longitude 
    global latitude
    global long_float
    global lat_float
    global exponent

    long_float = float("".join(longitude))
    #longitude list joined to get number, float because python is rounding 
    for i in range (0, exponent[0]):
        long_float = long_float * 10
    long_float = radians(long_float)
    #longitude angle should be between 0 and 2pi. if rad value is over ~6.3 (2pi), then the number needs to be changed in accordiance to its sign
    # if long_float < 0: 
        
    # elif long_float > 2 * pi:


    lat_float = float("".join(latitude))
    #lat list joined to get number
    for i in range (0, exponent[1]):
        lat_float = lat_float * 10
    lat_float = radians(lat_float)
    exponent = []
    #longitude angle should be between 0 and 180 (pi rad). if rad value is over [pi], then the number needs to be changed in accordiance to its sign
    #this part might not matter
    
    
    # if lat_float < 0: 
    #     while lat_float < 0:
    #     lat_float
    # elif lat_float > pi:

    
def check_sign():
    global long_float
    global lat_float
    global sign #[long, lat]
    if sign[0] == '-':
        long_float = 2*pi -long_float
    if sign[1] == '-':
        lat_float = pi - lat_float 
    sign = []
    



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


        trim_coord()
        # print("longitude sign + exp and long after removing exp, space, sign")
        # print(sign[0])
        # print(exponent[0])
        # print(longitude)
        # print("latitude sign + exp and long after removing exp, space, sign")
        # print(sign[1])
        # print(exponent[1])
        # print(latitude)


        deg_to_rad()
        # print("longitude and latitude in radians")
        # print(long_float)
        # print(lat_float)

        check_sign()
        # print("after accounting for signs")
        # print(long_float)
        # print(lat_float)

        x = 10 * sin(lat_float) * cos(long_float)
        y = 10 * sin(lat_float) * sin(long_float)
        z = 10 * cos(lat_float)

        #the last coord in each plate repeats
        if str(x)+' '+str(y)+' '+str(z)+'\n' == names_and_coords[-1]:
            del names_and_coords[-1]
        if str(x)+' '+str(y)+' '+str(z)+'\n' == only_coords[-1]:
            del only_coords[-1]
        
        names_and_coords.append(str(x)+' '+str(y)+' '+str(z)+'\n')
        only_coords.append(str(x)+' '+str(y)+' '+str(z)+'\n')
        

        longitude = []
        latitude = []
        long_float = 0.0
        lat_float = 0.0
        exponent = []
        var_1 = 0
        var_2 = 0
        sign = []
        # print (names_and_coords[-1])
        # print(only_coords[-1])
        # print("-----------------------------------------------")
    else:
        i = "".join(i)
        names_and_coords.append(i)
        #need to delete \n in the lines with plate names so that it matches the name element in each sublist
        if line_no == plate_name_list[num_plates][1]:
            text_file = open(plate_name_list[num_plates-1][0], "w")
            n = text_file. write(str("".join(only_coords)))
            text_file. close()
            #print list with [num_plates-1][0] file name
            only_coords = []
            #dump onlycoords
    line_no += 1
#the cycle right above to print only_coords to a file with a specific name
#fails on the last plate, because num_plates in [num_plates][1] will 
#not be able to trigger, as there are no more plate names to read
#so the plate gets printed, without conditions, after lines runs out of elements
text_file = open(plate_name_list[num_plates-1][0], "w")
n = text_file. write(str("".join(only_coords)))
text_file. close()
        

        
text_file = open("radian_plate_coords", "w")
n = text_file. write(str("".join(names_and_coords)))
text_file. close()
#how to output files
