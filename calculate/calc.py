


import math

while (True):
    print("Select calculation type\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")

    choice = int(input("\nEnter Choice:"))

    if choice == 0:
        print("Good Bye")
        exit()

    intNum1 = int(input("Enter FIRST number: "))
    intNum2 = int(input("Enter SECOND number: "))

    if choice == 1:
        outcome = intNum1 + intNum2
        print(f"{intNum1} + {intNum2} = {outcome}")
    elif choice == 2:
        outcome = intNum1 - intNum2
        print(f"{intNum1} - {intNum2} = {outcome}")
    elif choice == 3:
        outcome = intNum1 * intNum2
        print(f"{intNum1} * {intNum2} = {outcome}")
    elif choice == 4:
            if intNum2 != 0:
                 outcome = intNum1 / intNum2
                 print(f"{intNum1} / {intNum2} = {outcome}")
            else:
                 print("Divide By Zero Error!!!")