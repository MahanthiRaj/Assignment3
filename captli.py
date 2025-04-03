#find all words starting with capital letter(captalize, ascii)
#input: "Today is oGod Day"
#output:'Today', 'Good', 'Day'
#1) split using comma( output (Today, is, Good , Day))
#2) for loop len(split())
#3)if search,

def capitalized_words(x):  # first we define a function with name print_int and input as x
        
    result = ""  # it will store the result if the first letter of the  word is captial
    
    # first we Split the input string into words and loop to each word
    for word in x.split():
        #  It will check if the first letter of the word is a capital letter
        if word[0].isupper():  # If the first letter is uppercase it will go to if 
            # If the result has words it will add the current word with a comma beforethe word
            if result:
                result += ", " + word  # here it will add a comma and add the word to the result
            else:
                result = word  # If the  result is empty it will start with the first capitalized word
                
    return result  # finally it will return the captilized words in the string with commas to result

x = "Today is Good Day" # this is input
print(capitalized_words(x))  # here we call function with the input x