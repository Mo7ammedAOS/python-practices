# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to20 , print Weird
# If  is even and greater than , print Not Weird
# n = int(input('Enter number please: '))

#  constrain the number between (1 < n < 100) 

# if (1 < n < 100):
#     if  n % 2 != 0:
#         print('weird')
#     elif (n % 2 == 0) and (2 < n < 5):
#         print("Not weird")
#     elif (n % 2 == 0) and (6 < n < 20):
#         print('weird')
#     elif (n % 2 == 0) and  (n > 20) :
#         print('Not weird')
# else:
#     print('WTF')

import math
import os
import random
import re
import sys



# if __name__ == '__main__':
#     n = int(raw_input().strip())

#  constrain the number between (1 < n < 100) 

# x = random(0,100)
while True:
    n = int(input("Enter number from 1 to 100:"))
    if n <= 100:
        if n%2 != 0 :
            print('Weird')
        if n%2 ==0 :
            if n>=2 and n <=5 :
                print('Not Weird')
        if n%2 ==0 :
            if n>=6 and n <=20 :
                print('Weird')
        if n%2 ==0 :
            if n>20:
                print('Not Weird')
            
    elif n>100:
        x = input('Are fucking idiot? Y or N: ')
        
        if x == "Y" or x == "y" :
            print("fuck you")
        if x == "N" or x == "n":
            print("I have said a fuckin number beteween 1 to 100..as hole!!!")
    
