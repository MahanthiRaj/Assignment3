operation = input("Enter operation: ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))


add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Cannot divide by zero"


if operation == '+':
    print(add(x, y))
elif operation == '-':
    print(subtract(x, y))
elif operation == '*':
    print(multiply(x, y))
elif operation == '/':
    print(divide(x, y))
else:
    print("Invalid operation!")