some_list = ['a', 'b', 'c', 'b', 'd', 'n', 'n']
du =[]
for x in some_list:
    if some_list.count(x) > 1 :
        if x not in du :
            du.append(x)
print(du)

