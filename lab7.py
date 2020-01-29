"""Let's play 'Guess the Number', the computer will choose a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.

ADVANCED VERSION 1: Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.

ADVANCED VERSION 2: Let them keep guessing in a while loop. Keep track of how many guesses the user has made, and tell them at the end.
"""

import random

user_guess = int(input("Guess the number: "))
num = list(range(1,11))
computer_choice = random.choice(num)
count = 0

while True:
    count += 1
    if user_guess == computer_choice:
        print("Correct!")
        break
    if user_guess < computer_choice:
        print("Wrong! You are too low! Let's play again.")
        user_guess = int(input("Guess the number: "))
        continue
    else:
        print("Wrong! You are too high! Let's play again.")
        user_guess = int(input("Guess the number: "))
        continue

print(f'You guessed {count} times')




    