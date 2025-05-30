n= int(input("enter number:"))

if  n<2:
    print("not a prime")
elif n == 2:
    print("prime num,ber")
elif n % 2 == 0:
    print ("not a prime number")
else:
    print ("prime number")