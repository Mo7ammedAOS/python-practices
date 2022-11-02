picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]

]

for row in picture:
    for pixel in row :
        if pixel == 0 :
            print(' ',end=' ')   # The use of end = '' is to put the items of rows in on  line
        else:
            print('*',end=' ')
    print() # this is just mean a new line .