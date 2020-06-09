
count = 0

names_list = []

user_input = input("Enter your name and type stop to exit: ")

while user_input!= 'stop':
    names_list.append(user_input)
    count = count + 1
    user_input = input("Enter other names: ")
    
    

print("The names in the list are: ", names_list)

print("Number of names added to the group are:", count)
