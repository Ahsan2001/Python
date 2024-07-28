
# Scenario 02: Calculating Square Roots of Even Numbers



# Imagine you're tasked with calculating the 
# square roots of even numbers from 1 to 10 using 
# list comprehension and lambda functions.


import math


numbers = (1,2,3,4,5,6,7,8,9,10) 

for num in numbers: 
    if (num % 2) == 0: 
        print(f"The square root of {num} is {round(math.sqrt(num), 2)}") 
