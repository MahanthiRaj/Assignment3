#Check if two strings are anagrams
# eq: input: 'mississippi'(main_word), sub_word(sippi), sub_word(miss)

main_word = input("enter your word ")
firstword = input("please enter your word ")

if sorted(main_word)==sorted(firstword):
    print("strings are anagrams")
else:
    print("strings are not anagrams")
        
    
    
    


