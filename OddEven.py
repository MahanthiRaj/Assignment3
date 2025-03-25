#Write a 1 to 10 even number? Write a 1 to 10 odd number?
#for n in range(0,11):
    #if n % 2==0:
        #print("Even",n)
    #else:
        #print("odd",n)
        
def even(x,y):
    for i in range (x,y):
        if i % 2==0:
            print("even",i)
            
x = int(input("enter stsrting point"))
y = int(input("enter stsrting point"))

print(even(x,y))
