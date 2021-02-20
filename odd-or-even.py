# -*- coding: utf-8 -*-
"""
Ask the user for a number.
Depending on whether the number is even or odd,
print out an appropriate message to the user. 

This is a temporary script file.
"""

userNumber = int(input("Give a number (integer): "))

if (userNumber / 2) == 1.0:
    output = "even"
else:
    output = "odd"

print(output)
1234567890