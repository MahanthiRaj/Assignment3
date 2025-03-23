#create a calultor which is having a = 5, b = 6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

n = input("enter your symbol: ")

if n == '+':
    result = a+b
    print("Addition:",result)
elif n == '-':
    result = a-b
    print("subtraction:",result)
elif n == '*':
    result = a-b
    print("Multiplication:",result)
elif n == '/':
    result = a/b
    print("Division:",result)
elif n == '%':
    result = a%b
    print("Modulus:",result)
else:
    print("enter a valid input")
    


#print("addition:",c,"\nsubtraction:",d,"\nMultiplication: ",e,"\nDivision:",f,"\nModulus:",g)
#print(f"addition:{c}",f"\nsubtraction:{d}",f"\nMultiplication:{e}",f"\nDivision:{f}",f"\nModulus:{g}")




