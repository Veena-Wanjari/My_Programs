#count number of vowels in a string , that user enters

"""
we will take input from user
take length of the string
here every letter is checked against a, e, i, o and u
and then count is increased by 1
every time it matches, i value is increased
"""

user_string = input("Enter a word: ") 
length = len(user_string)

i = 0 
count = 0

while count < length:
    if user_string[count] == 'a' or  user_string[count] == 'e' or user_string[count] == 'i' or user_string[count] == 'o' or user_string[count] == 'u':
        i = i + 1
    count = count + 1
    
print("Number of vowels are: ", i)  
  
