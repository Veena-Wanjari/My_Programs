

secret_number = 4
count = 0

while count <= 10:
    number = int(input("You are welcome to Winning Game World \n Please guess a number between 1 to 10: "))
    if number > secret_number:
        print("Number is too high")
    
    elif number < secret_number:
        print("Number is too low")
    
    else:
        print("You won!! The winning number is 4 ")
        break
    count = count + 1
    
print('You won in number of attempt:', count)

