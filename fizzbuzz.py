
n = 100
FIZZ = []
BUZZ = []
FIZZBUZZ = []
number = []
for i in range(1,n):

    if (i % 3 == 0) and (i % 5 == 0):
        FIZZBUZZ.append(i)
        
    elif (i % 3 == 0):
        FIZZ.append(i)

    elif (i % 5 == 0):
        BUZZ.append(i)
    
    else:
        number.append(i)
        
print(f" FIZZ : {FIZZ} \n BUZZ: {BUZZ} \n FIZZBUZZ: {FIZZBUZZ} \n number: {number}")

      
      