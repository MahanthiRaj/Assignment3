
#input:"test@example.com" - 1check- .com, 2nd check- @
#output:check if it is an email or not

def gmail(n): # This is the  function named gmail that takes an input n

    if ".com" in n and "@" in n: #it will check if the input contains "@" and ".com"
        print(n) # if it is valid then it will print the gmail
    else:
        print("enter valid  input") # If it's not valid it will ask for valid input
        
n = input("enter your gmail: ") # Ask the user to enter their Gmail address
gmail(n) # it will Call the gmail' function with the input n



#second method using ends with

def gmail(n):  # This is the  function named gmail that takes an input n
    
    #it will check if the input contains "@" and ends with ".com"
    if "@" in n and n.endswith(".com"):  
        print(n)  # if it is valid then it will print the gmail
    else:
        print("enter valid input")  # If it's not valid it will ask for valid input
        
n = input("enter your gmail: ")  # Ask the user to enter their Gmail address
gmail(n)  # it will Call the gmail' function with the input n
