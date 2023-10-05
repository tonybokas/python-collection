'''This is a number-guessing game.'''

import random

secretNumber = random.randint(1, 20)

print('I am thinking of a number bewteen 1 and 20.')

# Ask the player to make a guess (6 times).
for guessesMade in range(1, 7):
    print('Make a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # because the player guessed the correct number.

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesMade) + ' guesses!')
else:
    print('You failed to guess my number. It was ' + str(secretNumber) + '.')