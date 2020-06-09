#here, loop will continue untill the secret is typed

password = ""

while password != 'secret':
    password  = input("Enter the passsword: ")
    if password == 'secret':
        print("You are right")
    else:
        print("Sorry, you are wrong")
        

        