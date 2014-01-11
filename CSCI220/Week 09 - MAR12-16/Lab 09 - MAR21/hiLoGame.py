# hiLoGame.py
# Number-guessing game
# <Chad Hobbs>

from random import randint

guesses = 1
rand_num = randint(2,99)

while guesses <= 7:
    guess = eval(input("Try to guess the number! Enter a number between 1 and 100: "))

    if guess == rand_num:
        print("You win in",guesses,"guesses!")
        guesses = 9
    elif guess < rand_num:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")
    guesses = guesses + 1

if guesses == 8:
    print("Sorry, you lose. The number was",rand_num)
