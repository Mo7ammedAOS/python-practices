# expenses = {
#     'January': 2200 ,
#     'February': 2350 ,
#     'March': 2600 

# }

expenses = [ 2200, 2350 , 2600 , 2130 , 2190]

# 1- Comparing between jan an feb

comparetion = expenses[1]-expenses[0]
print(comparetion)  # the answer is 150

# 2- Totall in first three months

total = expenses[2] + expenses[1] + expenses[0]
print(total) # the answer is 7150.

# 3- Totall in the each month expensis is 2000

nov = 0
for i in range(len(expenses)):
    i = 2000
    nov+=i
print(nov) 

# 4- Adding June expenses

june_exp = expenses.insert(5,1980)
print(expenses)

# Taking back 200 and add it to April income

volvo = expenses[3] + 200
noro = expenses.remove(2130)
holo = expenses.insert(3,volvo)
print(expenses)
