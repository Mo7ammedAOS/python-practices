tr = [
    [0,0,1],
    [1,1,0],
    [1,0,0]
]

for row in tr:
    for pixel in row:
        if pixel == 0 :
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print('-')