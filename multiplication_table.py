user_number = input("Enter a number: ")

while (not user_number.isdigit()) or (int(user_number) < 1) or (int(user_number) > 12):
    print("Must be an integer between 1 to 12")
    user_number = input("Enter a number:  \n")
    
user_number = int(user_number)

print("====================")
print(f"This is the multiplication table for {user_number}")
print()
for i in range(1,13):
    print(f" {user_number} x {i} = {user_number * i} ")

print()


