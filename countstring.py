#ind most frequent character in the string
   #input: 'mississippi
   #output:'i', 's'
   
def frequency(word):
    freq = {}
    
    for char in word:
        freq[char] = freq.get(char, 0) + 1
        
    max_freq = max(freq.values())
    
    for char, count in freq.items():
        if count == max_freq:
            print(char)

letter = input("enter a word ")
frequency(letter)

    
    
    
    