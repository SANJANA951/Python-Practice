# CALCULATOR

import math

Operator = input("Enter the Operator you want ( + - * /): ")

digits = int(input("Enter how many digits you want( 2 , 3): "))


if digits==2:
    Num1 = float(input("Enter the Num1: "))
    Num2 = float(input("Enter the Num2: "))

    if Operator=="+":
        result = Num1 + Num2
        print(round(result,3))

    elif Operator=="-":
        result = Num1 - Num2
        print(round(result,3))

    elif Operator=="*":
        result = Num1 * Num2
        print(round(result,3))

    elif Operator=="/":
        result = Num1 / Num2
        print(round(result,3))

    else:
       print("You have to chose operator between ( +  *  -  /)")


elif digits==3:
    Num1 = float(input("Enter the Num1: "))
    Num2 = float(input("Enter the Num2: "))
    Num3 = float(input("Enter the Num3: "))

    if Operator=="+":
        result = Num1 + Num2 + Num3
        print(round(result,3))

    elif Operator=="-":
        result = Num1 - Num2 - Num3
        print(round(result,3))

    elif Operator=="*":
        result = Num1 * Num2 * Num3
        print(round(result,3))

    elif Operator=="/":
        result = Num1 / Num2 / Num3
        print(round(result,3))

    else:
       print("You have to chose operator between ( +  *  -  /)")



