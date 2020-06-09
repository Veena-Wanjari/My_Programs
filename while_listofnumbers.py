"""
ask user to choose numbers between 1 to 100 and give range of numbers between selected two numbers
"""
num_1 = int(input("Please enter first number: "))
num_2 = int(input("Please enter second number: "))

while num_1 < 1 or num_1 >100 or num_2 <1 or num_2 >100:
    print("Please give range from 1 to 100 only")
    num_1 = int(input("Please enter first number: "))
    num_2 = int(input("Please enter second number: "))

if num_1 < num_2:
    for i in range(num_1, num_2 + 1):
        print(i, end = ' ')
        
else:
    for i in range(num_2, num_1 + 1):
        print(i, end = " ")