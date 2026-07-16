# the calculator
n1 = int(input("enter the first number"))

operator = input("enter the operator ( '+', '-', 'x', '/' ) only")

n2 = int(input("enter the second number"))

if operator == '+':
    print(f"the addition of {n1} + {n2} = {n1+n2}")

elif operator == '-':
    print(f"the subtraction of {n1} - {n2} = {n1-n2}")

elif operator == 'x':
    print(f"the multiplication of {n1} * {n2} = {n1*n2}")

elif operator == '/':
    print(f"the division of {n1} / {n2} = {n1/n2}")
else:
    print("invalid operator")