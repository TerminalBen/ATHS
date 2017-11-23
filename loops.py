import random

secretNumber = random.randint(1,10)
print ("i am thinking of a number between 1 and 10.")

for guesses in range (1,7):
    print ("take a guess.")
    guess = int(input())

    if guess>secretNumber:
        print ("too high, try again")

    if guess<secretNumber:
        print("too low, try again")

    if guess ==secretNumber:
         break


if guess == secretNumber:
    print ("congrats, you guessed the number in" +str(guesses)+"guesses")
else:
    print("burro, my number was "+str(secretNumber)+".")

