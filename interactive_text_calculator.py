import math
# Basic text calculator user input
first_num = float(input("Enter first number: \n"))
sec_num = float(input("Enter second number: \n"))
usr_op = input("Select an operation you want to carry out - \n "
               "add \n sub \n mul \n div \n power \n mod \n log \n")


if usr_op == "add":
    print("Addition: ", first_num + sec_num)
elif usr_op == "sub":
    print("Subtraction: ", first_num - sec_num)
elif usr_op == "mul":
    print("Multiplication: ", first_num * sec_num)
elif usr_op == "div":
    print("Division: ", first_num / sec_num)
elif usr_op == "power":
    print("Power output: ", first_num ** sec_num)
elif usr_op == "mod":
    print("Remainder: ", first_num % sec_num)
elif usr_op == "log":
    # using log function from math module
    result = math.log(first_num, sec_num)
    print("Log of ", first_num, " to base ", sec_num, ": ", result)
else:
    print("Incorrect operation selected")