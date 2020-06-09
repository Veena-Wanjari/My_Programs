

name = input("Enter your name:  ")

print("Hi", name.capitalize(), '!!', 'You are welcome to Guessing Game')



n = 5

while  n>0:
    fruit = input("Please enter your fruit name or type exit, You have only five chances : ")

    if fruit == 'mango':
        print("good ")
        break
        
    elif fruit == 'exit':
        print("Mangoes are your favourite")
        break
    else:
         
        n = n-1
        print("number of chances left: ", n)