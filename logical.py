num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 >15 and num2 >15:
    print('Then their product is :' , num1 * num2)
    
elif num1 >15 or num2 >15:
    print('Then their sum is: ', num1 + num2)
    
else:
    print("The answer is: ", 0)
    
