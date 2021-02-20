# -*- coding: utf-8 -*-
"""
Ask the user for a number.
Depending on whether the number is even or odd,
print out an appropriate message to the user. 

This is a temporary script file.
"""
import math


userNumber = float(input("Give any positive number: "))


while userNumber <= 0:
    userNumber = float(input("Give any *positive* number: "))
else:
    userNumber = userNumber
    
    
workingNumber = userNumber / 2 - math.floor(userNumber / 2)
    
if workingNumber == 0.0:
    output = " is an EVEN number"
else:
    output = " is is not an even number"


print(userNumber, output)
