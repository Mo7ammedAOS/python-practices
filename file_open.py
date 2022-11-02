flie = open('flie.txt', 'r') # The varible name should be identical with file name
Second = flie.readlines()

newlist = []
# for itemes in Second:
#     if itemes[-1] == '\n':
#        newlist.append(itemes[:-1])         manner 1
#     else :
#         newlist.append(itemes)
# print(newlist)

# for itemes in Second:
#     newlist.append(itemes.strip())    manner2
# print(newlist)

# Manner 2 looks cleaner than manner 1