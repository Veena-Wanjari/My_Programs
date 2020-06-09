user_input = int(input("From a classroom, you have been selected, please enter your age "))

ages = []

while user_input < 5:
    ages.append(user_input)
    user_input = int(input("Print other member's age of your class :"))

print("the ages are: ", ages)
