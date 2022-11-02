# from functools import reduce
my_List = [20,55,90]
a = [(0,2),(4,3),(9,9),(10,-1)]
# def accumilator (acc, item):
#     print(acc, item)
#     return acc + item
# print(reduce(accumilator, my_List, 3))

print(list(map(lambda it: it + 1 , my_List)))
a.sort(key= lambda x:x[1])
print(a)
