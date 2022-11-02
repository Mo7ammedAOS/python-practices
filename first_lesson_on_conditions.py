User_age = int(input("Enter your age : "))
User_Licensed = input("Have you driving licence ? : ")

# if User_age >= 18 and User_Licensed == 'Yes' :
#     print('ok!\nYou are permitted to drive.')
# else :
#     print('Sorry!\nYou can\'t')

# There is another way to do the same code upove
#Its called Ternary operator

# x = 'allowed' if User_age >= 18  and User_Licensed == 'Yes' else 'not allowed'  
# print(x)  

if User_age >= 18 :
    print('allowed')
elif User_Licensed == 'Yes' :
    print('not allowed')
else :
    print('not allowed')