def factorial(n):
    f = 1
    while n>0:
        f = f*n
        n-=1
    return f
    
n = int(input("enter number of fat"))
print("factorial is factorial(n)")




n = int(input("enter number of fat"))
f = 1

while n>0:
    f = f*n
    n-=1
print(f"factorial is {f}")