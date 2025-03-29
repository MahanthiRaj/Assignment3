

x = input("enter your word")
word = ""
for i in x:
    if i not in word:
        word = word +i
print(word)
