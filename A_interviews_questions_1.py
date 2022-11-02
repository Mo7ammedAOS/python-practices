def  is_it_valid(array , subsequence):
    cont = []
    for i in array:
        for y in subsequence:
            if y == i:
                cont.append(y)
    cont
    if len(cont) == len(subsequence):
       print(True)
    else:
        print(False)




items = [1,2,15,20,22,30,7,6,88,60]
volg  = [15,30,7,88]

is_it_valid(items,volg)

# cont = []
# for i in items:
#     for y in volg:
#         if y == i:
#             cont.append(y)
# cont
# if len(cont) == len(volg):
#     print(True)
# else:
#     print(False)
