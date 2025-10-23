a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    result = a + b
    print(f"{a} + {b} = {result}")
elif operation == '-':
    result = a - b
    print(f"{a} - {b} = {result}")
elif operation == '*':
    result = a * b
    print(f"{a} * {b} = {result}")
elif operation == '/':
    if b == 0:
        print("Cannot divide by 0")
    else:
        result = a / b
        print(f"{a} / {b} = {result}")
else:
    print("Invalid operation. Please use one of: + - * /")
