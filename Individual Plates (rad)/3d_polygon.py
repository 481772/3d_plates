#Reads a file's radian coordinates from the directory
input_file = open('WL.txt', 'r')





import matplotlib.pyplot as plt

#some have only 15 or so points but look ok 
#AF, AU has outliers, BH,
#CL has outliers and is bunched up, IN outliers
#MS = ?, NB = possible overlap, ND = outliers, NZ = outleirs
#PA = overlapping and outliers, SA = outlier,
#SO = overlap and outliers, SU = overlap and outlier, TO = hard curves,
#WL maybe

lines = input_file.readlines()


sequence_containing_x_vals = []
sequence_containing_y_vals = []
sequence_containing_z_vals = []
num = 0 

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def append_to_n_vals():
    global sequence_containing_x_vals 
    global sequence_containing_y_vals
    global sequence_containing_z_vals
    global num
    var = [] 

    for i in range(0, coord_list.index(" ")): 
        var.append(coord_list[0])
        del coord_list[0]
    del coord_list[0]
    #delete up to/including the space but append everything before that (var) as an x coord 
    sequence_containing_x_vals.append(float("".join(var)))
    
    var = []
    for i in range(0, coord_list.index(" ")): 
        var.append(coord_list[0])
        del coord_list[0]
    del coord_list[0]
    sequence_containing_y_vals.append(float("".join(var)))
    #code for y is identical to that of x, since it's the same case ()

    var = []
    for i in range(0, coord_list.index("\n")-1): 
        var.append(coord_list[i])
    sequence_containing_z_vals.append(float("".join(var)))


for i in lines: 
    coord_list = Convert(i)
    append_to_n_vals()




fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')


ax.plot(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, '-o')
plt.show()
