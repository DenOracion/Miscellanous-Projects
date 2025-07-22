# Simple calculator to perform simple arithmetic operations using Python

operator = input("Enter an operator (+ - * /): ") # Asks the user to input one of four operators
num1 = float(input("Enter the first number: ")) # Asks user to input the first number
num2 = float(input("Enter the second number: ")) # Asks user to input the second number

if operator == "+":
    # If the operator selected is '+', a result driven from adding num1 and num2 together will be printed, rounded to the nearest three digits  
    result = num1 + num2
    print(round(result, 3))
elif operator == "-": # The other three operators function the same as the first one, given that the operator was selected
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else: # If none of the four operators were inputted, a message stating that the user has inputted an invalid operator will be printed
    print(f"{operator} is not valid, please input a valid operator")