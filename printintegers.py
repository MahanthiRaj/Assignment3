
#input:"There are 24 apples and 12" ascii value
#output:24,12


def print_int(x):  # first we define a function with name print_int and input as x
    result = " "  # this is a empty tring to store result
    
    # first we Split the input string into words and loop to each word 
    for number in x.split():  
        # here we check if the word is a number
        if number.isdigit():  
            #if it a number i will add to result 
            if result:  
                result += "," + number  # and it will add comma before  number
            else:
                result = number  # if the result is empty it will start with the firdt number
    
    return result  # it will return the ouput to the result


x = "There are 24 apples and 12 apples" # This is the input
print(print_int(x))  # finally we will call the function print_int with input x 
