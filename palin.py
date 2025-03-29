n = input("Enter a string or a number: ")

r = ""
for char in n:
    r = char + r

if n == r:
    print("Is a Palindrome")
else:
    print("Not a Palindrome")