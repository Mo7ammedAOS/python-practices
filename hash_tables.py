# this is contains Hashtables implemintation.


 # First implement Hash function

def get_hash (key):
    h = 0
    for r in key:
        h += ord(r)
    print(h % 100)

get_hash('march 6')

# 




