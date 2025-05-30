#Sum Items in List(Write a Python program to sum all the items in a list.
def sum_list(list1):
    
list1 = [5,6,7,8,9]
result = sum(list1)
print(result)


#Multiply Items in List(Write a Python program to multiply all the items in a list.)

list1 = [5,6.7,8,9]

result = 1

for i in list1:
    result*=i
    
print(result)

#Get Largest Number in List(Write a Python program to get the largest number from a list)

list1 = [5,6.7,8,9]

large = list1[0]


for i in range(1,len(list1)):
    if list1[i] > large:
        large = i
        
print(large)

# second method

list1 = [5,6.7,8,9]


large = min(list1)
        
print(large)

#4. Get Smallest Number in List(Write a Python program to get the smallest number from a list.

list1 = [5,6.7,8,9]


small = list1[0]    

for i in list1:
    if i < small:
        small = i
        
print(small)



list1 = [5,6.7,8,9]


small = min(list1)
        
print(small)

#5. Count Strings with Same Start and End(Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.)
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2


sample_list = ['abc', 'xyz', 'aba', '1221']

count = 0

for string in sample_list:
    if string[0] == string[-1]: 
        count += 1

print(count)



