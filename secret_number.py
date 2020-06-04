'''
Secret number game

Program generate random number between 1 to 100.
We want user to guess a number between 1-100.
If user has guesses bigger number than the secret number, the program will return >
if less than program will return <
if guess right then guesses the secret number
'''

# random number generator module

import random

secret_number = random.randint(1, 100)

while True:
    usr_number = int(input("Guess a number between 1 to 100: \n"))
    if usr_number > 100 or usr_number < 1:
         print ("Enter the number within 1 to 100")
    elif usr_number > secret_number:
        print("Number is > than secret number")
    elif usr_number < secret_number:
        print("Number is < than secret number")
    else:
        print("You win !!!! ")
        break