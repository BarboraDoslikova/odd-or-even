# -*- coding: utf-8 -*-
"""
Asks the user for a number.
Depending on whether the number is even or odd,
prints out an appropriate message to the user. 

Even number is an integer (i.e. not a fraction or decimal)
divisible by 2 without a remainder,
including a 0.

Catches ValueError exception,
e.g. when an integer was not entered.32

By Barbora Doslikova.
"""
try:  
    userNumber = int(input("Give any whole number: ")) 
except ValueError:
    print("please re-run the script and try to enter a valid whole number")
except:
    print("something else went wrong, please try again")
else:
    workingNumber = userNumber/2 - userNumber//2
        
    if workingNumber == 0:
        output = "is an EVEN number"
    else:
        output = "is is an ODD number"     
    
    print(userNumber, output)
