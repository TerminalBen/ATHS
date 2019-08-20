import random

secretNumber = random.randint(1,20)

for guesstaken in range (1,7):
	guess = int(input("take a guess between 1 and 20"))
	if guess > 20:
		print('Fuck off.')

	if guess > secretNumber:
		print("too high")
	if guess < secretNumber:	 
		print ("too low")
	else:
		break

if guess == secretNumber:
	print ('good job you got it in '+str(guesstaken)+'guesses \n')
else:
	print ("it was " +str(secretNumber)+ ". Sorry \n")	
