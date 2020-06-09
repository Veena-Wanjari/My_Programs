guess = input("Please guess the season : ")

guess.lower()

if guess == 'winter':
    print("Yes .. You are right !!")
    
elif guess == 'summer':
    print("OOPS !! Try again....")

elif guess == 'spring':
    print("OOPS !! Try again....")
    
elif guess == 'autumn':
    print("OOPS !! Try again....")
    
elif guess == 'rainy':
    print("OOPS !! Try again....")
    
else:
    print("This is not the season")

print('You have choosen', guess.capitalize())


        


