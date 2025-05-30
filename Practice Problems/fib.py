
n = int(input("How many Fibonacci terms do you want? "))
a, b = 0, 1
for i in range(n):
    a, b = b, a + b
    print(b)