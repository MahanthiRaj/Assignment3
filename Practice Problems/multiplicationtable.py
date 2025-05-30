n = int(input("enter number:"))

i = 1
while i<11:
    print(f"{n} x {i} = {n*i}")
    i+=1
    
    
def multiplication(n):
    for i in range(1,11):
        
        print(f"{n} x {i} = {n * i}")

n = int(input("Enter a number: "))
multiplication(n)
    