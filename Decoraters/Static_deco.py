class MyClass:
    @staticmethod
    def greet():
        return "Hello, World!"

print(MyClass.greet())


#2

class Calculator:
    @staticmethod
    def multiply(a, b):
        return a * b

print(Calculator.multiply(3, 4))  # Output: 12
