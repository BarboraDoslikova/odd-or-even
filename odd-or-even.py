# -*- coding: utf-8 -*-
"""
Ask the user for a number.
Depending on whether the number is even or odd,
print out an appropriate message to the user. 

Even number is an integer (i.e. not a fraction or decimal)
divisible by 2 without a remainder,
including a 0.

By Barbora Doslikova.
"""

userNumber = int(input("Give any whole number: "))

"""
while userNumber <= 0:
    userNumber = float(input("Please, give any positive whole number bigger than 0: "))
else:
    userNumber = userNumber
 """   
    
workingNumber = userNumber/2 - userNumber//2
    
if workingNumber == 0:
    output = "is an EVEN number"
else:
    output = "is is an ODD number"


print(userNumber, output)
