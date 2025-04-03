#def main():
 # Logic 
#1)making a uppercase for starting word -> captalize
# input: " Python  is    cool "
# output:" Python  Is    Cool "
# 2) remove space 
# output:"PythonIsCool"
# 3) make a word
      

def cap(a):
    #First we will capitalize the first letter of the string
    return a.capitalize()

def remove_spaces(a):
    res = ""  # this will store the result
    space_added = False  # this will help us add only one space between words

    for i in a:  # it will check each character in the string
        if ord(i) == 32:  # and it will Check if the character is having a space
            if not space_added:  # if the space is not there
                res += " "  # it will add one space
                space_added = True  # it will confirm that the space is added
        else:
            res += i  # it will add the characters with no space to result
            space_added = False  # it will reset to the and check another word

    return res.strip()  # it will remove extra spaces at the end

def word(s):
    t = ""  # This will store the final lowercase string

    for i in s:  # This will check each character in the string
        if 65 <= ord(i) <= 90:  # if the  character is an uppercase letter
            t += chr(ord(i) + 32)  # Then it will convert it to lowercase and add it to the result
        else:
            t += i
  # If it's already lowercase it will just add it to the result

    return t  # it will return the string in lowercase

#Here we will get user input
input_string = input("Enter a string: ")

# this is for remove extra spaces and keep only one space between words
input_string = remove_spaces(input_string)

# Capitalizes the first letter
input_string = cap(input_string)

output = word(input_string)

# it will converts everything to lowercase
print(output)
