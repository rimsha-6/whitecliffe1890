"""
 Addition Calculator
 Ask user for 2 numbers
 Add numbers
 Display outcome
"""

import math


intNum1 = int(input("Enter FIRST number: "))
intNum2 = int(input("Enter SECOND number: "))

intAns = intNum1 + intNum2

print(intNum1, "+" , intNum2, "=" , intAns)
print(f"{intNum1} + {intNum2} = {intAns}")