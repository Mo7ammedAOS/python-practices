# while True:
#     x = input ('what is your name: ')
#     if x == 'temo':
#         print('Hello Temo')
#         break
    
# name = None
# while not name:
#     name = input('Enter name please : ')
# print('Hello {name}'.format(name=name))

# import time

# for x in range(10, 0, -1):
#     print(x)
#     time.sleep(3)
# print('I will expert in this year')

rows = int(input('How many rows: '))
columns = int(input('How many colums: '))
symbol = input('Which symbol that you waana use: ')
for i in range(rows):
    for j in range(columns):
        print(symbol, end=' ')
   
    
